from django import db
from django.core.management.base import BaseCommand, CommandError
from django.db import connection, transaction

# National Priorities Project Data Repository
# load_cffr_per_capita.py 
# Created 1/2/2013

# Updates the per-capita fields in the CFFR and Payments to Individuals
# Run when population data has been updated.

class Command(BaseCommand):
    args = '<year>'
    help = 'updates existing per-capita numbers for cffr and pymnts to individuals'
    
    def handle(self, *args, **options):
                
        def load_per_capita_county(year_current):
            cursor = connection.cursor()
            cursor.execute('''
            UPDATE data_cffr c
            LEFT JOIN data_populationgendercounty pop
                ON c.state_id = pop.state_id 
                AND c.county_id = pop.county_id
                AND c.year = pop.year
            SET 
                c.amount_per_capita = ROUND(c.amount/pop.total,2) 
            ,	c.update_date = NOW()
            WHERE c.year = %s''',[year_current])
            transaction.commit_unless_managed()
            return cursor.rowcount
            
        def load_per_capita_state(year_current):
            cursor = connection.cursor()
            cursor.execute('''
            UPDATE data_cffrstate c
            LEFT JOIN data_populationgenderstate pop
                ON c.state_id = pop.state_id 
                AND c.year = pop.year
            SET 
                c.amount_per_capita = ROUND(c.amount/pop.total,2) 
            ,	c.update_date = NOW()
            WHERE c.year = %s''',[year_current])
            transaction.commit_unless_managed()
            return cursor.rowcount
            
        def load_per_capita_individual_county(year_current):
            cursor = connection.cursor()
            cursor.execute('''
            UPDATE data_cffrindividualcounty c
            LEFT JOIN data_populationgendercounty pop
                ON c.state_id = pop.state_id
                AND c.county_id = pop.county_id
                AND c.year = pop.year
            SET 
                c.amount_per_capita = ROUND(c.amount/pop.total,2) 
            ,	c.update_date = NOW()
            WHERE c.year = %s''',[year_current])
            transaction.commit_unless_managed()
            return cursor.rowcount
        
        def load_per_capita_individual_state(year_current):
            cursor = connection.cursor()
            cursor.execute('''
            UPDATE data_cffrindividualstate c
            LEFT JOIN data_populationgenderstate pop
                ON c.state_id = pop.state_id
                AND c.year = pop.year
            SET 
                c.amount_per_capita = ROUND(c.amount/pop.total,2) 
            ,	c.update_date = NOW()
            WHERE c.year = %s''',[year_current])
            transaction.commit_unless_managed()
            return cursor.rowcount
                
        if len(args):
            for year in args:
                rows = load_per_capita_county(year)
                print "%s: %s county per-capita rows updated" % (year, rows)
                rows = load_per_capita_state(year)
                print "%s: %s state per-capita rows updated" % (year, rows)
                rows = load_per_capita_individual_county(year)
                print "%s: %s payments to individuals county per-capita rows" % (year, rows)
                rows = load_per_capita_individual_state(year)
                print "%s: %s payments to individuals state per-capita rows updated" % (year, rows)
        else:
            print "Please specify a year (in YYYY format)."
