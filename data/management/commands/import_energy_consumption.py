from django import db
from django.db import transaction
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import EnergyConsumptionStateRaw
import csv
from npp_api.data.utils import clean_num
from datetime import datetime

# National Priorities Project Data Repository
# import_energy_consumption.py 

# Imports U.S. Department of Energy Annual State Energy Consumption data (from SEDS)
# government source: http://www.eia.doe.gov/state/seds/seds-data-complete.cfm#consumption --> "data files" --> "consumption in btu". filename is use_all_btu.csv(accurate as of 4/10/2013)
# destination model:  EnergyConsumptionStateRaw

# HOWTO:
# 1) Download source file from url listed above
# 2) change SOURCE_FILE variable to the the path of the source file you just downloaded
# 3) Run as Django management command from your project path "python manage.py import_energy_consumption_state_annual"

# Safe to re-run: yes

SOURCE_FILE = '%s/energy/use_all_btu.csv' % settings.LOCAL_DATA_ROOT

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):

        @transaction.commit_on_success
        def import_consumption():
            data_reader = csv.reader(open(SOURCE_FILE))
            insert_count = 0
            cutoff_year = 1990
            for i, row in enumerate(data_reader):
                if i==0:
                    years = row[2:]
                    #if we already have data for the years in the file, delete it
                    for h, header in enumerate(years):
                        if header >= cutoff_year:
                            print 'deleting %s records' % header
                            data = EnergyConsumptionStateRaw.objects.filter(year=header)
                            data.delete()
                else:
                    for j, col in enumerate(row[2:]):
                        year = years[j]
                        if year >= cutoff_year:
                            record = EnergyConsumptionStateRaw(
                                year=year,
                                state=row[0],
                                msn=row[1],
                                value=clean_num(col))
                            record.save()
                            db.reset_queries()
                            insert_count = insert_count + 1             
            
            print '%s import complete. %s records inserted' % (
                        SOURCE_FILE, insert_count)
                        
        start_time = datetime.now()
        import_consumption()
        elapsed_time = datetime.now() - start_time
        print 'elasped time = ' + str(elapsed_time)