from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import CffrRaw

# National Priorities Project Data Repository
# import_cffr_annual.py 
# Updated 3/17/2010, Joshua Ruihley, Sunlight Foundation

# Imports Annual CFFR data file
# government source: http://www.census.gov/govs/cffr/ (accurate as of 11/20/2009)
# source data: http://assets.nationalpriorities.org/raw_data/cffr/cffr.tar.gz
# destination model:  CFFR

# HOWTO:
# 1) Download .tar.gz from source data below
# 2) decompress source data into a path and enter path into SOURCE_PATH var below
# 3) Run as Django management command from your project path "python manage.py import_cffr_annual"
# 4) Make sure your database has amount field set as a bigint (and not a regular int)
# AFTER IMPORTING EVERY YEAR:
# 5) Create indexes in database
#   CREATE INDEX idx_state_postal ON data_cffrraw (state_postal)
#   CREATE INDEX idx_year ON data_cffrraw (year)

YEAR = 2009
SOURCE_PATH = '%s/cffr/%s/' % (settings.LOCAL_DATA_ROOT, YEAR)
if YEAR > 2002:
    SOURCE_FILE = '%s%s%scffcom.txt' % (SOURCE_PATH, str(YEAR)[2], str(YEAR)[3])
else:
    SOURCE_FILE = '%s%s%sCFFCOM.TXT' % (SOURCE_PATH, str(YEAR)[2], str(YEAR)[3])

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        f = open(SOURCE_FILE, 'r')
        error_count = 0
        insert_count = 0
        for line in f:
            state_code= line[0:2]
            county_code = line[2:5]
            place_code = line[5:10]
            state_postal = line[10:12]
            county_name = line[12:36].rstrip()
            place_name = line[36:60].rstrip()
            population = int(line[60:69])
            if population == 0:
                population = None
            congress_district = line[69:103]
            program_code = line[103:109]
            object_type = line[109:111]
            agency_code = line[111:115]
            funding_sign = line[115:116]
            amount = int(line[116:128])
            
            if funding_sign == '-':
                amount_adjusted = amount*-1
            else:
                amount_adjusted = amount

            record = CffrRaw(year=YEAR, state_code=state_code, county_code=county_code, 
                place_code=place_code, state_postal=state_postal, county_name=county_name, 
                place_name=place_name, population=population, congress_district=congress_district, 
                program_code=program_code, object_type=object_type, agency_code=agency_code, 
                funding_sign=funding_sign, amount=amount, amount_adjusted=amount_adjusted)
            try:
                record.save()
                db.reset_queries()
                insert_count = insert_count + 1
            except:
                error_count = error_count + 1
                print 'load failed for record %s %s %s %s %s %s %s' % (year, state_code, county_code, place_code, program_code, object_type, agency_code)
                
        print '%s records loaded. %s errors' % (insert_count, error_count)
                
