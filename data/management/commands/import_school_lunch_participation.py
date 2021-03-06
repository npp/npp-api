from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import SchoolLunchParticipationStateRaw
from npp_api.data.utils import clean_num
import csv

# National Priorities Project Data Repository
# import_school_lunch_participation.py

# Imports USDA State Level School Lunch Participation Data
# source info: http://www.fns.usda.gov/pd/01slfypart.htm (accurate as of 5/15/2012)
# npp csv: http://assets.nationalpriorities.org/raw_data/hunger/school_lunch_participation.csv (updated 7/27/2010)
# destination model:  SchoolLunchParticipationStateRaw

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv (watch out for various spellings of Dept. of Defense)
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) change 'amount' column in data_SchoolLunchParticipation table to type 'bigint'
# 5) Run as Django management command from your project path "python manage.py import_school_lunch_participation"
#
# SAFE TO RE-RUN OR RELOAD A YEAR: YES (if year/state record is already
# loaded, program will update the value rather than insert a new record)

SOURCE_FILE = '%s/hunger/school_lunch_participation.csv' % (settings.LOCAL_DATA_ROOT)

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
                state = row[0]
                if len(state):
                    for j,col in enumerate(row):
                        if j > 0:
                            try:
                                #if year & state already exist, update the value (previous years' data is often revised)
                                record = SchoolLunchParticipationStateRaw.objects.get(state=state, year=int(year_row[j]))
                                current_value = clean_num(col)
                                if record.value != current_value:
                                    record.value = current_value
                                    record.save()
                                    update_count = update_count + 1
                                else:
                                    unchanged_count = unchanged_count + 1
                                
                            except MultipleObjectsReturned:
                                print 'error: multiple records exist for %s %s' % (str(year_row[j]), state)
                                continue
                                
                            except:
                                #this year & state isn't in the db yet; insert
                                record = SchoolLunchParticipationStateRaw()
                                record.year = int(year_row[j])
                                record.state = state
                                record.value = clean_num(col)
                                record.save()
                                insert_count = insert_count + 1
        
        db.reset_queries()
        print 'school lunch participation import complete. %s inserted, %s updated, %s unchanged' % (
            insert_count, update_count, unchanged_count)
                            
                                