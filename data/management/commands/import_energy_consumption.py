from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import EnergyConsumptionStateRaw
import csv
from npp_api.data.utils import clean_num

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
        data_reader = csv.reader(open(SOURCE_FILE))
        update_count = 0
        insert_count = 0
        unchanged_count = 0
        for i, row in enumerate(data_reader):
            if i==0:
                fields = row
            else:
                for j, col in enumerate(row):
                    if fields[j].lower() == 'state':
                        state = col
                    elif fields[j].lower() == 'msn':
                        msn = col
                    else:
                        year = int(fields[j])
                        value = clean_num(col)
                        try:
                            record = EnergyConsumptionStateRaw.objects.get(
                                year=year,
                                state=state,
                                msn=msn)
                            if record.value <> value:
                                record.value = value
                                record.save()
                                db.reset_queries()
                                update_count = update_count + 1
                            else:
                                unchanged_count = unchanged_count + 1
                        except MultipleObjectsReturned:
                            print 'error: multiple records exist for %s %s %s' % (
                                year, state, msn)
                            continue
                        except:
                            record = EnergyConsumptionStateRaw(state=state, 
                                msn=msn, year=year, value=value)
                            record.save()
                            db.reset_queries()
                            insert_count = insert_count + 1
            
        print '%s import complete. %s records updated, %s inserted, %s unchanged' % (
                    SOURCE_FILE, update_count, insert_count, unchanged_count)