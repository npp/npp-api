from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import SnapParticipationHouseholds
import csv

# National Priorities Project Data Repository
# import_snap_participation_households.py
# Updated 7/27/2010, Joshua Ruihley, Sunlight Foundation

# Imports USDA Number of Households Participating in Foodstamp Program per State
# source info: http://www.fns.usda.gov/pd/16SNAPpartHH.htm (accurate as of 6/15/2011)
# npp csv: http://assets.nationalpriorities.org/raw_data/hunger/snap_participation_households.csv (updated 7/27/2010)
# destination model:  SnapParticipationHouseholds

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) change 'amount' column in data_SNAPParticipationHouseholds table to type 'bigint'
# 5) Run as Django management command from your project path "python manage.py import_snap_participation_households"

# Safe to re-run: YES (if year/state record is already
# loaded, program will update the value rather than insert a new record)

SOURCE_FILE = '%s/hunger/snap_participation_households.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        
        def clean_int(value):
            if value.strip()=='':
                value=None
            else:
                value=int(value)
            return value
            
        data_reader = csv.reader(open(SOURCE_FILE))
        
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
                                record = SnapParticipationHouseholds.objects.get(state=state, year=int(year_row[j]))
                                current_value = clean_int(col)
                                if record.value != current_value:
                                    print str(year_row[j]) + ' ' + state + ' updating from ' + str(record.value) + ' to ' + str(current_value)
                                    record.value = current_value
                                    record.save()
                                
                            except MultipleObjectsReturned:
                                print 'error: multiple records exist for ' + str(year_row[j]) + ' ' + state
                                continue
                                
                            except:
                                #this year & state isn't in the db yet; insert
                                record = SnapParticipationHouseholds()
                                record.year = int(year_row[j])
                                record.state = state
                                record.value = clean_int(col)
                                record.save()
                           
        db.reset_queries()