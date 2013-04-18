from django import db
from django.db import transaction
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import ElectricEmissionsStateRaw
import csv
from npp_api.data.utils import clean_num

# National Priorities Project Data Repository
# import_electric_emissions.py

# Imports Electric Power Estimate Emissions by state
# source info: http://www.eia.gov/electricity/data.cfm#elecenv 
#   (accurate as of 4/10/2013)
# source file: http://www.eia.gov/cneaf/electricity/epa/emission_state.xls
#   (accurate as of 4/10/2013)
# destination model:  ElectricEmissionsStateRaw

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv 
# 3) change SOURCE_FILE variable to the the path of the 
#       source file you just created
# 4) Run as Django management command from your project path 
#       "python manage.py import_electric_emissions"

# Safe to re-run: YES
# NOTE: since the file always goes back to 1990, you can also delete the 
#   current data and reload from scratch.


SOURCE_FILE = '%s/energy/emission_state.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    @transaction.commit_on_success
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        update_count = 0
        insert_count = 0
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
                    if row[4].lower().find('-') >= 0:
                        co2 = 0
                    else:
                        co2 = clean_num(row[4])
                    if row[5].lower().find('-') >= 0:
                        so2 = 0
                    else:
                        so2 = clean_num(row[5])
                    if row[6].lower().find('- ') >= 0:
                        nox = 0
                    else:
                        nox = clean_num(row[6])

                    try:
                        record = ElectricEmissionsStateRaw.objects.get(
                            year=year, state=state, 
                            producer_type = producer_type,
                            energy_source = energy_source)
                        record.c02 = co2
                        record.s02 = s02
                        record.nox = nox
                        update_count = update_count + 1  
                    except:
                        record = ElectricEmissionsStateRaw(year=year, state=state, 
                            producer_type=producer_type,
                            energy_source=energy_source, 
                            co2=co2, so2=so2, nox=nox)
                        insert_count = insert_count + 1
                    record.save()
                    db.reset_queries()

        print 'Emissions import complete. %s records inserted, %s updated.' % (insert_count, update_count)
        