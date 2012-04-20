from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import ElectricEmissionsStateRaw
import csv
from npp_api.data.utils import clean_num

# National Priorities Project Data Repository
# import_electric_emissions.py

# Imports Electric Power Estimate Emissions by state
# source info: http://www.eia.gov/electricity/data.cfm#elecenv 
#   (accurate as of 4/20/2012)
# source file: http://www.eia.gov/cneaf/electricity/epa/emission_state.xls
#   (accurate as of 4/20/2012)
# destination model:  ElectricEmissionsStateRaw

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv 
#       rename US-TOTAL to US)
# 3) change SOURCE_FILE variable to the the path of the 
#       source file you just created
# 4) convert co2, so2 and nox columns in database to type bigint
# 5) Run as Django management command from your project path 
#       "python manage.py import_electric_emissions"

# Safe to re-run: YES (if year/state record is already
# loaded, program will update the value rather than insert a new record)
# NOTE: since the file always goes back to 1990, you can also delete the 
#   currently data and reload from scratch.


SOURCE_FILE = '%s/energy/emission_state.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        error_count = 0
        update_count = 0
        insert_count = 0
        unchanged_count = 0
        for i, row in enumerate(data_reader):
            if i > 0:
                year = row[0]
                if  len(year):
                
                    if row[1].lower().find('us') >= 0:
                        state = 'US'
                    else:
                        state = row[1]
                    producer_type = row[2]
                    energy_source = row[3]
                    co2 = clean_num(row[4])
                    so2 = clean_num(row[5])
                    nox = clean_num(row[6])
                    
                    try:
                        record = ElectricEmissionsStateRaw.objects.get(
                            year=year, state=state, 
                            producer_type = producer_type,
                            energy_source = energy_source)
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
                            db.reset_queries()
                            update_count = update_count + 1
                        else:
                            unchanged_count = unchanged_count + 1
  
                    except:
                        record = ElectricEmissionsStateRaw(year=year, state=state, 
                            producer_type=producer_type,
                            energy_source=energy_source, 
                            co2=co2, so2=so2, nox=nox)
                        record.save()
                        db.reset_queries()
                        insert_count = insert_count + 1
                        
        print 'Emissions import complete. %s records inserted, %s updated, and %s unchanged.' % (insert_count, update_count, unchanged_count)
        print '%s errors' % error_count
        