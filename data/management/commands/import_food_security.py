from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import FoodSecurityStateRaw
import csv

# National Priorities Project Data Repository
# import_food_security_state.py

# Imports food security from the Census' Current Population Food Security Supplement
# source info: Data Ferrett (current population survey-->food security-->GESTCEN (geography variables) & HRFS12MD (food security supplement variables)
# npp csv: 
# destination model:  FoodSecurityStateRaw

# HOWTO:
# 1) Log into the data ferrett and create a table using the above variables
# 2) "Make a table"
# 3) Use states as columns and the HRFS12MD variable contents as the columns
# 4) Select HHSUPWGT as the weighting variable (adjusts for household non-responses)
# 5) Save table as a .csv
# 2) Convert saved .csv to same formatting as npp csv 
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) Run as Django management command from your project path "python manage.py import_food_security

# Safe to re-run: YES

SOURCE_FILE = '%s/hunger/foodsecurity.csv' % (settings.LOCAL_DATA_ROOT)
SOURCE_FILE_OLD = '%s/hunger/foodsecurity-pre2005.csv' % (settings.LOCAL_DATA_ROOT) #this is here for a one-time load of older data

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        def clean_num(value):
            if value.strip()=='':
                value=None
            else:
                value = value.replace(",","")
                value = int(value)
            return value
            
        insert_count = 0
        update_count = 0
        data_reader = csv.reader(open(SOURCE_FILE))
        
        print 'loading food security'
        for i, row in enumerate(data_reader):
            if i == 0:
                header_row = row;            
            else:
                if row[0].strip().lower().find('total') != -1:
                    state = 'US'
                else:
                    state = row[0].strip()
                if len(state):
                    year = row[7]
                    try:
                        record = FoodSecurityStateRaw.objects.get(year=year,state=state)
                        update_count = update_count + 1
                    except MultipleObjectsReturned:
                        print 'error: multiple records exists for %s %s' % (year, state)
                    except:
                        insert_count = insert_count + 1
                        record = FoodSecurityStateRaw()
                        record.year = year
                        record.state = state
                    
                    record.household_total = clean_num(row[1])
                    record.no_response = clean_num(row[2])
                    record.food_secure_high = clean_num(row[3])
                    record.food_secure_marginal = clean_num(row[4])
                    record.food_secure_low = clean_num(row[5])
                    record.food_secure_very_low = clean_num(row[6])
                        
                    #print '%s %s %s' % (record.year, record.state, record.household_total)
                    record.save()
                    db.reset_queries()
                    
        print 'done loading food security. %s records updated and %s records inserted' % (update_count, insert_count)
                    
        #one time load for pre-2005 data, which is formatted a little differently and uses HRFS12M1 instead of HRFS12MD
        try:
            data_reader = csv.reader(open(SOURCE_FILE_OLD))
        except:
            return
        
        insert_count = 0
        update_count = 0
        print 'loading pre-2005 food security data'
        
        for i, row in enumerate(data_reader):
            if i == 0:
                header_row = row;            
            else:
                if row[0].strip().lower().find('total') != -1:
                    state = 'US'
                else:
                    state = row[0].strip()
                if len(state):
                    year = row[7]
                    try:
                        record = FoodSecurityStateRaw.objects.get(year=year,state=state)
                        update_count = update_count + 1
                    except MultipleObjectsReturned:
                        print 'error: multiple records exists for %s %s' % (year, state)
                    except:
                        record = FoodSecurityStateRaw()
                        record.year = year
                        record.state = state
                        insert_count = insert_count + 1
                    
                    record.household_total = clean_num(row[1])
                    record.no_response = clean_num(row[2])
                    record.food_secure = clean_num(row[4])
                    record.food_secure_low = clean_num(row[5])
                    record.food_secure_very_low = clean_num(row[6])
                        
                    record.save()
                    db.reset_queries()
                    
        print 'done loading pre-2005 food security. %s records updated and %s records inserted' % (update_count, insert_count)