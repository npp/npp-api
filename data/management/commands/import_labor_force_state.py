from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import LaborForceStateRaw
import csv
from npp_api.data.utils import clean_num

# National Priorities Project Data Repository
# import_labor_force_state.py

# Imports BLS State Labor Force Participation
# source info: http://www.bls.gov/lau/#tables (Employment Status of the Civilian Noninstitutional Population by State-->http://www.bls.gov/lau/staadata.txt): accurate as of 6/17/2011)
# npp csv: http://assets.nationalpriorities.org/raw_data/bls.gov/state_labor_force_participation.csv (updated 6/30/2010)
# destination model:  LaborForceStateRaw

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv.
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_state_labor_force_participation"

# Safe to re-run: YES. 

SOURCE_FILE = '%s/bls.gov/state_labor_force_participation.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        data_reader = csv.reader(open(SOURCE_FILE))
        insert_count = 0
        update_count = 0

        for i, row in enumerate(data_reader):
            if i == 0:
                header_row = row;            
            else:
                if len(row[0]):
                    area_fips = row[0]
                    if len(area_fips) == 1:
                        area_fips = '0' + area_fips
                    year = row[2]
                    try:
                        record = LaborForceStateRaw.objects.get(
                            year = year, area_fips = area_fips)
                        update_count = update_count + 1
                    except MultipleObjectsReturned:
                        print 'error: multiple records exists for year = %s and fips = %s' % (year, area_fips)
                        continue
                    except:
                        insert_count = insert_count + 1
                        record = LaborForceStateRaw()
                        record.year = year
                        record.area_fips = area_fips
                    
                    record.area = row[1]
                    record.civilian_noninstitutional_pop = clean_num(row[3])
                    record.labor_force_total = clean_num(row[4])
                    record.labor_force_participation_rate = clean_num(row[5])
                    record.employment_total = clean_num(row[6])
                    record.employment_pop_rate = clean_num(row[7])
                    record.unemployment_total = clean_num(row[8])
                    record.unemployment_rate = clean_num(row[9])
                    record.save()
 
        db.reset_queries()
        print 'state labor force import complete. %s inserts and %s updates.' % (insert_count,update_count)
