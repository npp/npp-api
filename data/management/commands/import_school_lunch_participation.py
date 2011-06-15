from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import SchoolLunchParticipation
import csv

# National Priorities Project Data Repository
# import_school_lunch_participation.py
# Updated 7/27/2010, Joshua Ruihley, Sunlight Foundation

# Imports USDA State Level School Lunch Participation Data
# source info: http://www.fns.usda.gov/pd/01slfypart.htm (accurate as of 7/27/2010)
# npp csv: http://assets.nationalpriorities.org/raw_data/hunger/school_lunch_participation.csv (updated 7/27/2010)
# destination model:  SchoolLunchParticipation

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) change 'amount' column in data_SchoolLunchParticipation table to type 'bigint'
# 5) Run as Django management command from your project path "python manage.py import_school_lunch_participation"
#
# SAFE TO RE-RUN OR RELOAD A YEAR: NO

SOURCE_FILE = '%s/hunger/school_lunch_participation.csv' % (settings.LOCAL_DATA_ROOT)

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
                                #if year & state already exist, update the value in case it's been updated since the last load
                                record = SchoolLunchParticipation.objects.get(state=state, year=int(year_row[j]))
                                record.value = clean_int(col)
                                record.save
                                db.reset_queries()
                                
                            #ideally, we'd first check for the MultipleRecordsExist error before just assuming that the .get failed 
                            #b/c the record doesn't exists yet
                                
                            except:
                                #this year & state isn't in the db yet; insert
                                record = SchoolLunchParticipation()
                                record.year = int(year_row[j])
                                record.state = state
                                record.value = clean_int(col)
                                record.save()
                                db.reset_queries()
                            
                                