from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.db import connection, transaction

# National Priorities Project Data Repository
# load_labor_force_county.py

# Loads Bureau of Labor Statistics Annual State Unemployment Rates
# npp csvs: http://assets.nationalpriorities.org.s3.amazonaws.com/raw_data/bls.gov/county_unemployment/laucnty<year>.csv
# destination model:  LaborForceCounty

# HOWTO:
# 1) Run as Django management command from your project path "python manage.py load_labor_force_county"

# Safe to re-run: no

# To Do: needs validations (e.g., do rows in source table = rows in loaded table); should be preceded by a drop table command

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        cursor = connection.cursor()
        
        cursor.execute('''
        INSERT INTO data_laborforcecounty
        SELECT 
            NULL
        ,    l.year
        ,   s.id
        ,   c.id
        ,   laus_code
        ,   labor_force
        ,   employed
        ,   unemployed
        ,   unemployment_rate
        ,   NOW()
        ,   NOW()
        FROM
            data_laborforcecountyraw l
            JOIN data_state s
            ON l.state_fips = s.state_ansi
            JOIN data_county c
            ON l.county_fips = c.county_ansi 
            AND s.id = c.state_id
        ''')

        transaction.commit_unless_managed()