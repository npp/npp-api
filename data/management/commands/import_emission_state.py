from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import StateEmissions
import csv

# National Priorities Project Data Repository
# import_emissions_state.py
# Updated 4/21/2010, Joshua Ruihley, Sunlight Foundation

# Imports IRS Data Book Gross Collections, by Type of Tax and State
# source info: http://www.eia.doe.gov/cneaf/electricity/epa/emission_state.xls (accurate as of 6/15/2011)
# npp csv: http://assets.nationalpriorities.org.s3.amazonaws.com/raw_data/doe/emission_state.csv
# destination model:  StateEmissions

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv (rename US-TOTAL to US)
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) convert co2, so2 and nox columns in database to type bigint
# 5) Run as Django management command from your project path "python manage.py import_emissions_state

# Safe to re-run: YES (if year/state record is already
# loaded, program will update the value rather than insert a new record)
# NOTE: since the file always goes back to 1990, you can also delete the currently data and reload from scratch. We did this in June 11 b/c the data had changed so significantly


SOURCE_FILE = '%s/doe.gov/emission_state.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        error_count = 0
        update_count = 0
        insert_count = 0
        for i, row in enumerate(data_reader):
            if i > 0:
                year = row[0]
                if  len(year):
                
                    state = row[1]
                    producer_type = row[2]
                    energy_source = row[3]
                    co2 = row[4]
                    so2 = row[5]
                    nox = row[6]
                    
                    try:
                        record = StateEmissions.objects.get(year=year, state=state, producer_type = producer_type, energy_source = energy_source)
                        update = False
                        if record.co2 != co2:
                            update = True
                            record.co2 = co2
                        if record.so2 != so2:
                            update = True
                            record.so2 = so2
                        if record.nox != nox:
                            update = True
                            record.nox = nox
                        if update:
                            record.save()
                            update_count = update_count + 1
                            
                    except MultipleObjectsReturned:
                        print 'error: multiple records exist for ' + str(year) + ' ' + state + ' ' + producer_type + ' ' + energy_source
                        error_count = error_count + 1
                        continue 
                        
                    except:
                        record = StateEmissions(year=year, state=state, producer_type=producer_type,
                            energy_source=energy_source, co2=co2, so2=so2, nox=nox)
                        record.save()
                        insert_count = insert_count + 1
                        
        db.reset_queries()
        print 'Load complete.'
        print 'Records added = ' + str(insert_count)
        print 'Records updated = ' + str(update_count)
        print 'Errors = ' + str(error_count)
        