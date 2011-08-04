from django import db
#from django.core.management.base import NoArgsCommand
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Sum
from data.models import CffrRaw, CffrProgram, CffrState, State, County, Cffr
from django.db import connection, transaction

# National Priorities Project Data Repository
# load_cffr.py 
# Created 5/11/2011

# Populates the Cffr model and the CffrState summary table used by the API
# source model(s): CffrRaw
# source load command(s): import_cffr
# destination model:  Cffr, CffrState

# HOWTO:
# 1) Ensure that CffrRaw, CffrProgram, State, County is loaded and up to date (especially make sure that any new program codes have been loaded to CffrProgram before running this script)
# 2) Run as Django management command from your project path "python manage.py load_cffr"

#to run the process for all years, set load_this_year to ''
load_this_year = '1993'

#class Command(NoArgsCommand):
class Command(BaseCommand):
    args = '<year>'
    help = 'loads cffr county and state tables from the raw cffr table'
    
    #def handle_noargs(self, **options):
    def handle(self, *args, **options):
            
        def get_state(**lookup):
            state_ref_current = State.objects.get(**lookup)
            return state_ref_current
            
        def get_county(**lookup):
            try:
                county_ref_current = County.objects.get(state=lookup['state'], county_ansi=lookup['county_ansi'])
            except:
                county_ref_current = add_county(**lookup)
            return county_ref_current
            
        def add_county(**lookup):            
            #Sometimes, CFFR records come through with old county codes
            #that aren't in the official ANSI county list. Rather than skip
            #these records, add the missing county record.  
            
            #get the county name from the CFFR raw record
            cffr_county = CffrRaw.objects.filter(state_code = lookup['state'].state_ansi,county_code = lookup['county_ansi'])
            if cffr_county.count() > 0:
                county_name = cffr_county[0].county_name
            else:
                county_name = 'Unknown'
            record = County(state_id=lookup['state'].id, county_ansi=lookup['county_ansi'], county_name=county_name)
            record.save()
            return record
            
        def get_program(**lookup):
            program_ref_current = CffrProgram.objects.get(**lookup)
            return program_ref_current
        
        def load_year_county(year_current):
            
            records_current = Cffr.objects.filter(year=year_current).count()
            #if we already have records loaded for this year, skip it
            if records_current == 0:
            
                print 'starting cffr load for year ' + str(year_current) + '...'
                
                cursor = connection.cursor()
                
                #check for unknown state codes
                cursor.execute('''
                SELECT COUNT(*)
                FROM 
                    data_cffrraw r
                    LEFT JOIN data_state s
                    ON r.state_code = s.state_ansi
                WHERE
                    r.year > 1992 AND
                    s.state_ansi IS NULL''')
                x = cursor.fetchone()
                if x[0] > 0:
                    print '1 or more state codes for ' + str(year_current) + ' were not in the state table. No records will be loaded for ' + str(year_current) + '.'
                    return
                    
                #check for unknown program ids
                cursor.execute('''
                SELECT COUNT(*)
                FROM
                    data_cffrraw r
                    LEFT JOIN data_cffrprogram p
                    ON r.program_code = p.program_code
                    AND p.year = r.year
                WHERE
                    r.year = %s
                    AND p.id IS NULL
                ''',[year_current])
                x = cursor.fetchone()
                if x[0] > 0:
                    print '1 or more program codes for ' + str(year_current) + ' were not in CffrProgram. No records will be loaded for ' + str(year_current) + '.'
                    return
                    
                #insert any missing counties
                cursor.execute('''
                INSERT INTO data_county (state_id, county_ansi, county_abbr, county_name, create_date, update_date)
                SELECT DISTINCT
                    s.id, r.county_code, '', r.county_name, NOW(), NOW()
                FROM 
                    data_cffrraw r
                    JOIN data_state s
                    ON r.state_code = s.state_ansi
                    LEFT JOIN data_county c
                    ON r.county_code = c.county_ansi
                    AND s.id = c.state_id 

                WHERE
                    r.year = %s
                    AND c.id IS NULL
                    AND s.state_abbr <> 'DC'
                ''',[year_current])
                
                #finally, aggregate raw cffr data to the county level & insert it
                cursor.execute('''
                INSERT INTO data_cffr (year, state_id, county_id, cffrprogram_id, amount, create_date, update_date)
                SELECT
                    c.year
                ,   s.id
                ,   co.id
                ,   p.id
                ,   SUM(amount_adjusted)
                ,   NOW()
                ,   NOW()
                FROM
                    data_cffrraw c
                    JOIN data_state s
                    ON c.state_code = s.state_ansi
                    JOIN data_county co
                    ON c.county_code = co.county_ansi
                    AND s.id = co.state_id
                    JOIN data_cffrprogram p
                    ON c.program_code = p.program_code
                    AND c.year = p.year
                WHERE
                    c.year = %s
                GROUP BY
                    c.year, s.id, co.id, p.id
                ''',[year_current])
               
            else:
                print str(year_current) + ' skipped: ' + str(records_current) + ' county records already loaded for that year.'
                
        def load_year_state(year_current):
        
            records_current = CffrState.objects.filter(year=year_current).count()
            #if we already have records loaded for this year, skip it
            if records_current == 0:
            
                cursor = connection.cursor()
                cursor.execute('''
                insert into data_cffrstate (
                    year, state_id, cffrprogram_id, amount, create_date, update_date)
                select 
                    year
                ,   state_id
                ,   cffrprogram_id
                ,   sum(amount)
                ,   now()
                ,   now()
                from
                    data_cffr
                where
                    year= %s
                group by
                    year
                ,   state_id
                ,   cffrprogram_id
                ''',[year_current])
                
                transaction.commit_unless_managed()
                
            else:
                print str(year_current) + ' skipped: ' + str(records_current) + ' state records already loaded for that year.'
                
        if len(args):
            for year in args:
                load_year_county(year)
                print str(year) + ': cffrcounty done'
                load_year_state(year)
                print str(year) + ': cffrstate done'
        else:
            #if no year arguments specified, load everything
            for y in CffrRaw.objects.values('year').distinct():
                year_current = y['year']
                if year_current > 1992:
                    load_year_county(year_current)
                    print str(year_current) + ': cffrcounty done'
                    load_year_state(year_current)
                    print str(year_current) + ': cffrstate done'