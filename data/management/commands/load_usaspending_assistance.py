from django import db
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Sum
from data.models import UsaspendingAssistanceRaw, Cfda, State, UsaspendingAssistanceCounty, UsaspendingAssistanceState
from django.db import connection, transaction

# National Priorities Project Data Repository
# load_usaspending_assistance_county.py 

# Populates UsaspendingAssistance county aggregates
# source model(s): UsaspendingAssistanceRaw
# destination model:  UsaspendingAssistanceCounty

#TODO: log list of invalid programs
#TODO: log list of invalid county codes

class Command(BaseCommand):
    args = '<year>'
    help = 'loads usaspending_assistance county & state aggregates for use by API/data.nationalpriorities'

    def handle(self, *args, **options):
    
        def get_missing_cfda():
            try:
                missing_cfda_id = Cfda.objects.get(program_number = '99.999').id
                return missing_cfda_id
            except:
                print 'Ending run: unable to find Cfda record to represent missing/invalid program.'
                print 'Make sure the Cfda model has a record for program 99.999 and try again.'
                return

        def load_year_county(year_current):

            records_current = UsaspendingAssistanceCounty.objects.filter(year=year_current).count()
            #if we already have records loaded for this year, skip it
            if records_current == 0:
                print 'starting usaspending_assistance county load for year ' + str(year_current) + '...'
                cursor = connection.cursor()
                missing_cfda_id = get_missing_cfda()
                #insert usaspending assistance county/program aggregates
                cursor.execute('''
                INSERT INTO data_usaspendingassistancecounty (year, cfda_id, state_id, 
                    county_id, fed_funding, loan_value, loan_subsidy,
                    fed_funding_per_capita, loan_value_per_capita,
                    loan_subsidy_per_capita, create_date, update_date)
                SELECT
                    u.fiscal_year
                ,   COALESCE(p.id, %s) as cfda_id 
                ,   s.id as state_id
                ,   COALESCE(c.id,
                    (SELECT id from data_county co 
                    where co.state_id = s.id and co.county_ansi = '999'))
                ,   SUM(u.fed_funding_amount)
                ,   SUM(u.face_loan_guran)
                ,   SUM(u.orig_sub_guran)
                ,   ROUND(SUM(u.fed_funding_amount)/population.total,2)
                ,   ROUND(SUM(u.face_loan_guran)/population.total,2)
                ,   ROUND(SUM(u.orig_sub_guran)/population.total,2)
                ,   NOW()
                ,   NOW()
                FROM
                    data_usaspendingassistanceraw u
                    LEFT JOIN data_state s 
                    ON (CASE WHEN u.recipient_state_code = '99' THEN 'UD' ELSE u.recipient_state_code END) = s.state_abbr
                    LEFT JOIN data_county c
                    ON u.recipient_county_code = c.county_ansi
                    AND s.id = c.state_id
                    LEFT JOIN data_cfda p
                    ON u.cfda_program_num = p.program_number
                    LEFT JOIN data_populationgendercounty population
                    ON s.id = population.state_id
                    AND c.id = population.county_id
                    AND u.fiscal_year = population.year
                WHERE 
                    u.recipient_state_code IS NOT NULL
                    AND u.fiscal_year = %s
                GROUP BY
                    u.fiscal_year
                ,   COALESCE(p.id, %s)
                ,   s.id
                ,   COALESCE(c.id,(SELECT id from data_county co where co.state_id = s.id and co.county_ansi = '999'))
                ,   population.total
                ''',[missing_cfda_id,year_current,missing_cfda_id])
                transaction.commit_unless_managed()
            else:
                print str(year_current) + ' skipped: ' + str(records_current) + ' county records already loaded.'

        def load_year_state(year_current):
            records_current = UsaspendingAssistanceState.objects.filter(year=year_current).count()
            #if we already have records loaded for this year, skip it
            if records_current == 0:
                print 'starting usaspending_assistance state load for year ' + str(year_current) + '...'
                missing_cfda_id = get_missing_cfda()
                cursor = connection.cursor()
                #insert usaspending assistance state/program aggregates
                cursor.execute('''
                INSERT INTO data_usaspendingassistancestate (year, cfda_id, state_id, 
                    fed_funding, loan_value, loan_subsidy,
                    fed_funding_per_capita, loan_value_per_capita,
                    loan_subsidy_per_capita, create_date, update_date)
                SELECT
                    u.fiscal_year
                ,   COALESCE(p.id, %s) as cfda_id 
                ,   s.id as state_id
                ,   SUM(u.fed_funding_amount)
                ,   SUM(u.face_loan_guran)
                ,   SUM(u.orig_sub_guran)
                ,   ROUND(SUM(u.fed_funding_amount)/population.total,2)
                ,   ROUND(SUM(u.face_loan_guran)/population.total,2)
                ,   ROUND(SUM(u.orig_sub_guran)/population.total,2)
                ,   NOW()
                ,   NOW()
                FROM
                    data_usaspendingassistanceraw u
                    LEFT JOIN data_state s 
                    ON (CASE WHEN u.recipient_state_code = '99' THEN 'UD' ELSE u.recipient_state_code END) = s.state_abbr
                    LEFT JOIN data_cfda p
                    ON u.cfda_program_num = p.program_number
                    LEFT JOIN data_populationgenderstate population
                    ON s.id = population.state_id
                    AND u.fiscal_year = population.year
                WHERE 
                    u.recipient_state_code IS NOT NULL
                    AND u.fiscal_year = %s
                GROUP BY
                    u.fiscal_year
                ,   COALESCE(p.id, %s)
                ,   s.id
                ,   population.total
                ''',[missing_cfda_id,year_current,missing_cfda_id])
                transaction.commit_unless_managed()
            else:
                print str(year_current) + ' skipped: ' + str(records_current) + ' state records already loaded.'

        if len(args):
            for year in args:
                load_year_county(year)
                print str(year) + ': county done'
                load_year_state(year)
                print str(year) + ': state done'
        else:
            #if no year arguments specified, load everything
            for y in UsaspendingAssistanceRaw.objects.values('fiscal_year').distinct():
                year_current = y['fiscal_year']
                load_year_county(year_current)
                print str(year_current) + ': county done'
                load_year_state(year_current)
                print str(year_current) + ': state done'