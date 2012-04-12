from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import NewAidsCases
import csv
import sys
from npp_api.data.utils import clean_num

# National Priorities Project Data Repository
# import_new_aids_cases.py

# Imports HHS State New AIDS Cases Data
# source info: latest years are stored in PDF format.  for the 6/2011 updated, we pulled last several years manually into the old copy of aids.csv :(
#   http://www.cdc.gov/hiv/topics/surveillance/resources/reports/#surveillance-->HIV Surveillance Report (Diagnosis of HIV Infection
#   and AIDS in the United States and Dependent Areas, 2010) --> Table 20 AIDS diagnosis, by area of residence
# npp csv: http://assets.nationalpriorities.org/raw_data/health/aids.csv (updated 6/17/2010)
# destination model:  NewAIDSCases

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_new_aids_cases

# safe to re-run:  NO

SOURCE_FILE = '%s/health/aids.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        insert_count = 0
        update_count = 0
        unchanged_count = 0
        for i, row in enumerate(data_reader):
            if i == 0:
                year_row = row;            
            else:
                for j,col in enumerate(row):
                    if j == 0:
                        state = col.strip()
                    elif j > 0:
                        year = year_row[j]
                        try:
                            record = NewAidsCases.objects.get(state=state,year=year)
                            if record.value <> clean_num(col):
                                record.value = clean_num(col)
                                record.save()
                                db.reset_queries()
                                update_count = update_count + 1
                            else:
                                unchanged_count = unchanged_count + 1
                        except MultipleObjectsReturned:
                            print 'error: multiple records exist for %s %s' % (year, state)
                            continue
                        except:
                            record = NewAidsCases(year = year, state=state, value = clean_num(col))
                            record.save()
                            db.reset_queries()
                            insert_count = insert_count + 1
        print '%s import complete. %s records updated, %s inserted, %s unchanged' % (SOURCE_FILE, update_count, insert_count, unchanged_count)
