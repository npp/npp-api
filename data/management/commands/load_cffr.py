from django import db
from django.core.management.base import NoArgsCommand
from django.db.models import Sum
from data.models import CffrRaw, CffrProgram, CffrState, State, County, Cffr

# National Priorities Project Data Repository
# load_cffr.py 
# Created 5/11/2011

# Populates the Cffr model and the CffrState summary table used by the API
# source model(s): CffrRaw
# source load command(s): import_cffr
# destination model:  Cffr, CffrState

# HOWTO:
# 1) Ensure that CffrRaw, CffrProgram, State, County is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_cffr"

#to run the process for all years, set load_this_year to ''
load_this_year = '2009'

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
            
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
        
        def load_year(year_current):
            record_count = 0
            error_count = 0
            skip_count = 0
            state_saved = ''
            county_saved = ''
            program_saved = ''
            
            records_current = Cffr.objects.filter(year=year_current).count()
            #if we already have records loaded for this year, skip it
            if records_current == 0:
            
                print 'starting cffr load for year ' + str(year_current) + '...'
            
                log = open("data/management/commands/load_cffr.log", "w")
            
                fields=['year', 'state_code', 'county_code', 'program_code']
                statelookup = {}
                countylookup = {}
                programlookup = {}
                
                for p in CffrRaw.objects.filter(year=year_current).values(*fields).annotate(total=Sum('amount_adjusted')).order_by('state_code', 'county_code', 'program_code'):
                    
                    state_code = p['state_code']
                    county_code = p['county_code']
                    program_code = p['program_code']
              
                    try:
                        if state_saved != state_code:
                            statelookup['state_ansi'] = state_code
                            try:
                                state_ref_current = get_state(**statelookup)
                            except:
                                skip_count = skip_count + 1
                                log.write('Record skipped: state not found. Year = ' + str(year_current) + ' State code = ' + state_code + ' County code = ' + county_code + ' Program code = ' + program_code + '\n')
                                continue
                            state_saved = state_code
                            countylookup['county_ansi'] = county_code
                            countylookup['state'] = state_ref_current
                            county_ref_current = get_county(**countylookup)
                            county_saved = county_code
                        if county_saved != county_code:
                            countylookup['county_ansi'] = county_code
                            countylookup['state'] = state_ref_current
                            county_ref_current = get_county(**countylookup)
                            county_saved = county_code
                        if program_saved != program_code:
                            programlookup['year'] = year_current
                            programlookup['program_code'] = program_code
                            try:
                                program_ref_current = get_program(**programlookup)
                            except:
                                skip_count = skip_count + 1
                                log.write('Record skipped: program not found. Year = ' + str(year_current) + ' State code = ' + state_code + ' County code = ' + county_code + ' Program code = ' + program_code + '\n')
                                continue
                            
                    except:
                        skip_count = skip_count + 1
                        log.write('Record skipped. ' + str(year_current) + ' state=' + state_code + ' county=' + county_code + ' program=' + program_code + '\n' )
                        continue
                        
                    record = Cffr(year=year_current, state=state_ref_current, county=county_ref_current, cffrprogram=program_ref_current, amount=p['total'])
                
                    try:
                        record.save()
                        db.reset_queries()
                        record_count = record_count + 1
                        try:
                            log.write(str(year_current) + ' state=' + state_code + ' county=' + county_code + ' program=' + program_code + ' amount=' + str(p['total']) + '\n')
                        except:
                            log.write('cffr record loaded\n')
                    except:
                        log.write('Failed load for ' + str(year_current) + ' state=' + state_code + ' county=' + county_code + ' program=' + program_code + '\n')
                        error_count = error_count + 1
                        
                print str(year_current) + ': ' + str(record_count) + ' records loaded. ' + str(skip_count) + ' records skipped. Number of errors was ' + str(error_count) + '.'
                log.close()
                
            else:
                print str(records_current) + ' Cffr records already loaded for ' + str(year_current) + '. No ' + str(year_current) + ' will be loaded.'
                
        def load_year_state(year_current):
            record_count = 0
            error_count = 0
            skip_count = 0
            state_saved = ''
            program_saved = ''
            
            records_current = CffrState.objects.filter(year=year_current).count()
            
            #if we already have records loaded for this year, skip it
            if records_current == 0:
            
                print 'starting cffr aggregate state load for ' + str(year_current) + '...'
                
                log = open("data/management/commands/load_cffr.log", "a")
                
                fields = ['year', 'state', 'cffrprogram']
                statelookup = {}
                programlookup = {}
                state_totals = Cffr.objects.filter(year=year_current).values(*fields).annotate(amount=Sum('amount')).order_by('state', 'cffrprogram')
                for s in state_totals:
                    state_id = s['state']
                    program_id = s['cffrprogram']
              
                    try:
                        if state_saved != state_id:
                            statelookup['id'] = state_id
                            state_ref_current = get_state(**statelookup)
                            state_saved = state_id
                        if program_saved != program_id:
                            programlookup['year'] = year_current
                            programlookup['id'] = program_id
                            program_ref_current = get_program(**programlookup)
                            
                    except:
                        skip_count = skip_count + 1
                        log.write('Record skipped. ' + str(year_current) + ' state=' + str(state_id) + ' program=' + str(program_id) + '\n')
                        continue
                
                    record = CffrState(year=year_current, state=state_ref_current, cffrprogram = program_ref_current, amount=s['amount'])
                    
                    try:
                        record.save()
                        db.reset_queries()
                        record_count = record_count + 1
                        try:
                            log.write(str(year_current) + ' state=' + state_ref_current.state_ansi + ' program=' + program_ref_current.program_code + ' amount=' + str(s['amount']) + '\n')
                        except:
                            log.write('cffrstate loaded\n')
                    except:
                        log.write('Failed load for ' + str(year_current) + ' state=' + state_ref_current.state_ansi + ' program=' + program_ref_current.program_code + '\n')
                        error_count = error_count + 1
                        
                log.close()
                    
            else:
                print str(records_current) + ' CffrState records already loaded for ' + str(year_current) + '. No ' + str(year_current) + ' will be loaded.'
                
        if load_this_year:    
            load_year(load_this_year)
            load_year_state(load_this_year)
        else:
            for y in CffrRaw.objects.values('year').distinct():
                year_current = y['year']
                load_year(year_current)
                load_year_state(year_current)
        
        
