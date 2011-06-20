from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import MedicaidParticipation
import csv

# National Priorities Project Data Repository
# import_medicaid_participation.py
# Updated 6/18/2010, Joshua Ruihley, Sunlight Foundation

# Imports HHS State Medicaid Participation
# source info: http://www.census.gov/compendia/statab/cats/health_nutrition/medicare_medicaid.html (table 148) (accurate as of 6/20/2011)
# npp csv: http://assets.nationalpriorities.org/raw_data/health/medicaid_participation.csv (updated 6/18/2010)
# destination model:  MedicaidParticipation

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv.  Make sure numbers are still expressed in thousands (import will handle--just ensure that's still the case)
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_medicaid_participation

# Safe to re-run: YES. Previous years' numbers can be revised.

SOURCE_FILE = '%s/health/medicaid_participation.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
        def clean_int(value):
            if value <> '':
                value = float(value.replace(',','').replace(' ', ''))
                value = int(value * 1000)
            else:
                value = None
            return value
        
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
                                record = MedicaidParticipation.objects.get(state=state, year=year)
                            except MultipleObjectsReturned:
                                print 'error: multiple records exist for ' + str(year_row[j]) + ' ' + state
                                continue
                            except:
                                record = MedicaidParticipation()
                                record.state = state
                                record.year = year
                            value = col
                            record.value = clean_int(value)
                            record.save()