from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import FamiliesPoverty
from django.core.exceptions import MultipleObjectsReturned
import csv

# National Priorities Project Data Repository
# import_families_poverty.py
# Updated 7/28/2010, Joshua Ruihley, Sunlight Foundation

# Imports Census Data on Number of Families in poverty
# source info: http://dataferrett.census.gov/TheDataWeb/launchDFA.html (accurate as of 6/15/2011)
# as of 9/2011 for years 2005 & greater, source switches from CPS to ACS 1 year estimates, available via Census Factfinder, e.g. http://factfinder2.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=ACS_10_1YR_S1702&prodType=table
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/ferrett/families_poverty.csv (updated 7/28/2010)
# destination model:  FamiliesPoverty

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) change 'amount' column in data_FamiliesPoverty table to type 'bigint'
# 5) Run as Django management command from your project path "python manage.py import_families_poverty"

# Safe to re-run: yes

SOURCE_FILE = '%s/census.gov/acs/state/families_in_poverty.csv' % (settings.LOCAL_DATA_ROOT)

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
                        record = FamiliesPoverty.objects.get(year=year,state=state)
                        update_count = update_count + 1
                    except MultipleObjectsReturned:
                        print 'error: multiple records exist for %s %s' % (year, state)
                        continue
                    except:
                        record = FamiliesPoverty(year=year,state=state)
                        print 'inserting %s %s' % (year, state)
                        insert_count = insert_count + 1
                        record.families_total = clean_int(row[2])
                        record.families_total_moe = clean_int(row[3])
                        record.families_poverty_percent = row[4]
                        record.families_poverty_percent_moe = row[5]
                        record.save()
                else:
                    continue
                    
        print '%s records updated, %s inserted' % (update_count, insert_count)