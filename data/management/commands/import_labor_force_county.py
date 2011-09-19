from django import db
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import MultipleObjectsReturned
from data.models import LaborForceCountyRaw
import csv

# National Priorities Project Data Repository
# import_unemployment_county.py

# Imports Bureau of Labor Statistics Annual County Labor Force Data
# source info: http://www.bls.gov/lau/#tables (accurate as of 9/15/2011)
# npp csvs: http://assets.nationalpriorities.org.s3.amazonaws.com/raw_data/bls.gov/county_unemployment/laucnty<year>.csv
# destination model:  LaborForceCountyRaw

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FOLDER variable to the the path of the source file you just created
# 4) Run as Django management command from your project path "python manage.py import_labor_force_county [year] (or leave out year to load all files in folder)

# Safe to re-run: yes (and these numbers are restated over time, so load previous 5 years as well as the newest year)

YEARS = [1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
SOURCE_FOLDER = '%s/bls.gov/county_laborforce/' % settings.LOCAL_DATA_ROOT

class Command(BaseCommand):
    args = '<year>'
    help = 'loads county labor force csv for specified year'
    
    def handle(self, *args, **options):

        def clean_int(value):
            value = value.replace(' ', '').replace('N.A.', '')
            if value <> '':
                value = int(value.replace(',', ''))
            else:
                value = None
            return value
            
        def clean_float(value):
            value = value.replace(' ', '').replace('N.A.', '')
            if value <> '':
                value = float(value.replace(',', ''))
            else:
                value = None
            return value
            
        def pad_state_ansi(value):
            if len(value) == 2:
                return value
            elif len(value) == 1:
                return '0' + value
            else:
                print 'invalid state fips %s' % value
                return value
        
        def pad_county_ansi(value):
            if len(value) == 3:
                return value
            elif len(value) == 2:
                return '0' + value
            elif len(value) == 1:
                return '00' + value
            else:
                print 'invalid county fips %s' % value
                return value

        def load_year(year):
            source_file = '%slaucnty%s.csv' % (SOURCE_FOLDER,str(year)[2:4])
            try:
                data_reader = csv.reader(open(source_file))
            except:
                print '%s file not found' % year
                return
            
            insert_count = 0
            update_count = 0
            
            for i, row in enumerate(data_reader):
                if i > 0 and len(row[0]):
                    laus_code = row[0]
                    state_fips = row[1]
                    county_fips = row[2]
                    county_name = row[3]
                    year = row[4]
                    labor_force = clean_int(row[5])
                    employed = clean_int(row[6])
                    unemployed = clean_int(row[7])
                    unemployment_rate = clean_float(row[8])
                    
                    try:
                        record = LaborForceCountyRaw.objects.get(year=year,state_fips=pad_state_ansi(state_fips),county_fips=pad_county_ansi(county_fips))
                        record.labor_force = labor_force
                        record.employed = employed
                        record.unemployed = unemployed
                        record.unemployment_rate = unemployment_rate
                        update_count = update_count + 1
                    except MultipleObjectsReturned:
                        print 'error: multiple records exist for %s %s %s (%s)' % (year, state_fips, county_fips, county_name)
                        continue
                    except:
                        record = LaborForceCountyRaw(laus_code=laus_code, state_fips=pad_state_ansi(state_fips),
                            county_fips=pad_county_ansi(county_fips),county_name=county_name, year=year,
                            labor_force=labor_force, employed=employed, unemployed=unemployed,
                            unemployment_rate=unemployment_rate)
                        insert_count = insert_count + 1
                    record.save()
                    db.reset_queries()
                    
            print '%s county labor force load complete. %s inserts and %s updates.' % (year,insert_count,update_count)
            
        if len(args):
            for year in args:
                load_year(year)
        else:
            #if no args specified, load all files in the directory
            for year in YEARS:
                load_year(year)
                
        
