from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import CffrProgramRaw

# National Priorities Project Data Repository
# import_cffr_annual_pre93_prog.py 
# Updated 3/17/2010, Joshua Ruihley, Sunlight Foundation

# Imports Annual CFFR program identification file
# government source: pre-93 data mailed to Barb Chalfonte from Census, data from 1993 on: http://www.census.gov/govs/cffr/
# source data: 
# pre-93: http://assets.nationalpriorities.org/raw_data/cffr/cffr_pre93.tar.gz
# '93 and later: http://assets.nationalpriorities.org/raw_data/cffr/cffr.tar.gz

# destination model:  CffrProgramRaw

# HOWTO:
# 1) Download .tar.gz from source data below
# 2) decompress source data into a path and enter path into SOURCE_PATH var below
# 3) Run as Django management command from your project path "python manage.py import_cffr_annual_prog"
# AFTER IMPORTING EVERY YEAR:
# 4) Create indexes in database
#   CREATE INDEX idx_year ON data_cffrprogramraw (year)

YEAR = 2010
SOURCE_PATH = '%s/cffr/%s/' % (settings.LOCAL_DATA_ROOT, YEAR)

if YEAR < 1993:
    SOURCE_FILE = '%sPROG%s.DAT' % (SOURCE_PATH, str(YEAR))
else:
    SOURCE_FILE = '%s%sprog.txt' % (SOURCE_PATH, str(YEAR)[2:4])    

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        print SOURCE_FILE
        f = open(SOURCE_FILE, 'r')
        record_count = 0
        error_count = 0

        for line in f:
            program_id_code= line[0:6]
            program_name = line[6:79]
            program_name = program_name.strip().replace('\x96','-') #workaround for some unicode that showed up in the downloaded file
            
            record = CffrProgramRaw(year=YEAR, program_id_code=program_id_code, program_name=program_name)
        
            try:
                record.save()
                db.reset_queries()
                record_count = record_count + 1
            except:
                print 'insert failed for %s %s' % (program_id_code,program_name)
                error_count = error_count + 1
                
        print '%s records loaded from %s. Number of errors was %s' % (record_count, SOURCE_FILE, error_count)
        