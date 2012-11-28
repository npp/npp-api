from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import PeopleInPoverty
from django.core.exceptions import MultipleObjectsReturned
import csv

# National Priorities Project Data Repository
# import_people_in_poverty.py

# Imports census.gov State People in Poverty
# pre-2005 source info: http://www.census.gov/hhes/www/poverty/data/historical/people.html (accurate as of 6/15/2011)
# as of 9/2011 for years 2005 & greater, source switches from CPS to ACS 1 year estimates table S1701, available via Census Factfinder, e.g. http://factfinder2.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=ACS_10_1YR_S1701&prodType=table
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/income/people_in_poverty.csv (updated 6/29/2010)
# destination model:  PeopleInPoverty

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_people_in_poverty"

# Safe to re-run: yes

SOURCE_FILE = '%s/census.gov/acs/state/people_in_poverty.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
        def clean_int(value):
            if value <> '':
                value = int(value.replace(',', '').replace(' ', ''))
            else:
                value = None
            return value
        
        insert_count = 0
        update_count = 0
        
        for i, row in enumerate(data_reader):
            if i == 0:
                header_row = row;            
            else:
                if len(row[0]):
                    year = row[0]
                    state = row[1].lower()
                    try:
                        record = PeopleInPoverty.objects.get(year=year,state=state)
                        update_count = update_count + 1
                    except MultipleObjectsReturned:
                        print 'error: multiple records exist for %s %s' % (year, state)
                        continue
                    except:
                        record = PeopleInPoverty(year=year,state=state)
                        print 'inserting %s %s' % (year, state)
                        insert_count = insert_count + 1
                    record.total_population = clean_int(row[2])
                    record.value = clean_int(row[4])
                    record.value_standard_error = clean_int(row[5])
                    record.percent = row[6]
                    record.percent_standard_error = row[7]
                    record.save()
                else:
                    continue
                    
        print '%s records updated, %s inserted' % (update_count, insert_count)