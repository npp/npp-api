from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import StateLaborForceParticipation
import csv

# National Priorities Project Data Repository
# import_state_labor_force_participation.py

# Imports BLS State Labor Force Participation
# source info: http://www.bls.gov/lau/#tables (Employment Status of the Civilian Noninstitutional Population by State-->http://www.bls.gov/lau/staadata.txt): accurate as of 6/17/2011)
# npp csv: http://assets.nationalpriorities.org/raw_data/bls.gov/state_labor_force_participation.csv (updated 6/30/2010)
# destination model:  StateLaborForceParticipation

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv. TODO: update program to scrape the text file into required formatting, as there is a significant amt. of manual work
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_state_labor_force_participation"

# Safe to re-run: YES. Numbers for past years are revised, so it's necessary to check them & update if necessary.

SOURCE_FILE = '%s/bls.gov/state_labor_force_participation.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        def clean_num(value):
            if value.strip()=='':
                value=None
            else:
                value = value.replace(",","")
                if value.count('.') == 0:
                    value=int(value)
                else:
                    value=float(value)
            return value
            
        data_reader = csv.reader(open(SOURCE_FILE))
        
        for i, row in enumerate(data_reader):
            if i == 0:
                header_row = row;            
            else:
                if len(row[0]):
                    year = row[0]
                    state = row[1]
                    try:
                        record = StateLaborForceParticipation.objects.get(year = year, state = state)
                    except MultipleObjectsReturned:
                        print 'error: multiple records exist for ' + str(year_row[j]) + ' ' + state
                        continue
                    except:
                        record = StateLaborForceParticipation()
                        record.year = year
                        record.state = state
                        
                    record.civilian_noninstitutional_pop = clean_num(row[2])
                    record.civilian_labor_force = clean_num(row[3])
                    record.labor_force_participation_rate = clean_num(row[4])
                    record.employment_total = clean_num(row[5])
                    record.employment_pop_rate = clean_num(row[6])
                    record.unemployment_total = clean_num(row[7])
                    record.unemployment_rate = clean_num(row[8])
                    record.save()
