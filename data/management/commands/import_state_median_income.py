from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import StateMedianIncome
import csv

# National Priorities Project Data Repository
# import_state_median_income.py
# Updated 5/3/2010, Joshua Ruihley, Sunlight Foundation

# Imports U.S. Census Annual Social and Economic Supplement State Median Income Using 3-Year Average Medians
# source info: http://www.census.gov/hhes/www/income/data/historical/household/H08_2009.xls (accurate as of 6/19/2011)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/income/h08_2009.csv (updated 6/19/2011)
# destination model:  StateMedianIncome

# HOWTO:
# 1) Download source file from url listed above
# 2) Convert source file to .csv with same formatting as npp csv (include only the rows w/ data incurrent dollars)
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) Run as Django management command from your project path "python manage.py import_emissions_state

# Safe to re-run: YES (data from previous years can be revised)

SOURCE_FILE = '%s/census.gov/income/h08_2009.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        def clean_num(value):
            if value.strip()=='':
                value=None
            else:
                value = value.replace(",","")
                value = float(value)
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
                                record = StateMedianIncome.objects.get(year=year,state=state)
                            except MultipleObjectsReturned:
                                print 'error: multiple records exist for ' + str(year_row[j]) + ' ' + state
                                continue
                            except:
                                record = StateMedianIncome()
                                record.year = year
                                record.state = state
                                
                            value = clean_num(col)
                            record = StateMedianIncome(state=state, year=year, median_income=value)
                            record.save()
        
        
        
        
        
        
        
        
        
        
        
        for i, row in enumerate(data_reader):
            if i > 0:
                state = row[0]
                median_income = row[1]
                standard_error = row[2]
                ninety_pct = row[3]
                states_not_different = row[4]
                states_higher = row[5]
                states_lower = row[6]
                start_year = row[7]
                end_year = row[8]
                
                record = StateMedianIncome(state=state, median_income=median_income,
                    standard_error=standard_error, ninety_pct=ninety_pct,
                    states_not_different=states_not_different, states_higher=states_higher,
                    states_lower=states_lower, start_year=start_year, end_year=end_year)
                record.save()