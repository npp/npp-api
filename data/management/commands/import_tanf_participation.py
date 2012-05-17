from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import TanfParticipationStateRaw
from npp_api.data.utils import clean_num
import csv

# National Priorities Project Data Repository
# import_tanf_participants.py

# Imports year TANF participation estimates
# source info: http://www.acf.hhs.gov/programs/ofa/data-reports/index.htm (accurate as of 5/17/2012)
# npp csv: http://assets.nationalpriorities.org/raw_data/hhs.gov/tanf_participation (updated )
# destination model:  TanfParticipationStateRaw

# HOWTO:
# 1) Download source file from url listed above
# 2) Convert source file to .csv with same formatting as npp csv 
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) Run as Django management command from your project path "python manage.py import_tanf_participation"

# Safe to re-run: YES

SOURCE_FILE = '%s/hhs.gov/tanf_participation.csv' % (settings.LOCAL_DATA_ROOT)

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
                        if len(state):
                            year = year_row[j]
                            try:
                                record = TanfParticipationStateRaw.objects.get(year=year,state=state)
                                current_value = clean_num(col)
                                if record.value != current_value:
                                    record.value = current_value
                                    record.save()
                                    update_count = update_count + 1
                                else:
                                    unchanged_count = unchanged_count + 1
                            except MultipleObjectsReturned:
                                print 'error: multiple records exist for %s %s' % (year_row[j], state)
                                continue
                            except:
                                record = TanfParticipationStateRaw()
                                record.year = year
                                record.state = state
                                record.value = clean_num(col)
                                record.save()
                                insert_count = insert_count + 1
                            
        db.reset_queries()
        print 'tanf individual participation import complete. %s inserted, %s updated, %s unchanged' % (
            insert_count, update_count, unchanged_count)