from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import WicParticipationStateRaw
from npp_api.data.utils import clean_num
import csv

# National Priorities Project Data Repository
# import_wic_participation_state.py

# Imports USDA SNAP Benefits per Person by State
# source info: http://www.fns.usda.gov/pd/26wifypart.htm (accurate as of 5/17/2012)
# npp csv: http://assets.nationalpriorities.org/raw_data/hunger/wic_participants.csv (updated 7/27/2010)
# destination model:  WicParticipationStateRaw

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) Run as Django management command from your project path "python manage.py import_wic_participation_state"

# Safe to re-run: yes

SOURCE_FILE = '%s/hunger/wic_participants.csv' % (settings.LOCAL_DATA_ROOT)

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
                place = row[0].rstrip()
                #hacky stuff to make 2011 dataset comply with older imports
                place = place.replace('Dept.', 'Department')
                place = place.replace('Dept', 'Department')
                
                if place[0] != ' ':
                    state = row[0]
                    type = 'Total'
                else:
                    place = place.lstrip()
                    type = place
                for j,col in enumerate(row):
                    if j > 0:
                        year = year_row[j]
                        try:
                            record = WicParticipationStateRaw.objects.get(
                                state=state,place=place,year=year)
                            current_value = clean_num(col)
                            if record.value != current_value:
                                record.value = current_value
                                record.save()
                                update_count = update_count + 1
                            else:
                                unchanged_count = unchanged_count + 1
                        except:
                            record = WicParticipationStateRaw()
                            record.state = state
                            record.place = place
                            record.type = type
                            record.year = year
                            record.value = clean_num(col)
                            record.save()
                            insert_count = insert_count + 1
        db.reset_queries()
        print 'wic participation import complete. %s inserted, %s updated, %s unchanged' % (
            insert_count, update_count, unchanged_count)
