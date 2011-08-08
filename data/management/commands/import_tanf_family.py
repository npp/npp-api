from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import TanfFamilyStateRaw
import csv

# National Priorities Project Data Repository
# import_tanf_family.py

# Imports year TANF family participation estimates
# source info: http://www.acf.hhs.gov/programs/ofa/data-reports/index.htm (accurate as of 8/5/2011)
# npp csv: http://assets.nationalpriorities.org/raw_data/hhs.gov/tanf_family.csv (updated )
# destination model:  TanfFamilyStateRaw

# HOWTO:
# 1) Download source file from url listed above
# 2) Convert source file to .csv with same formatting as npp csv 
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) Run as Django management command from your project path "python manage.py import_tanf_family

# Safe to re-run: YES

SOURCE_FILE = '%s/hhs.gov/tanf_family.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        def clean_num(value):
            if value.strip()=='':
                value=None
            else:
                value = value.replace(",","")
                value = int(value)
            return value
            
        data_reader = csv.reader(open(SOURCE_FILE))
        
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
                                record = TanfFamilyStateRaw.objects.get(year=year,state=state)
                            except MultipleObjectsReturned:
                                print 'error: multiple records exist for ' + str(year_row[j]) + ' ' + state
                                continue
                            except:
                                record = TanfFamilyStateRaw()
                                record.year = year
                                record.state = state
                                
                            value = clean_num(col)
                            record.value = value
                            record.save()
                            db.reset_queries()