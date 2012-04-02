from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import AlternativeFuelVehicles
from npp_api.data.utils import clean_num
import csv
import sys
import os.path

# National Priorities Project Data Repository
# import_alternative_fuel_vehicles.py
# Updated 5/17/2010, Joshua Ruihley, Sunlight Foundation

# Imports Department of Energy Alternative Fuel Vehicles Total
# source info: http://www.eia.gov/renewable/alternative_transport_vehicles/xls/attf_V2.xls (accurate as of 4/2/2012)
# npp csv: http://assets.nationalpriorities.org/raw_data/energy/attf_v2.csv (updated 5/17/2010)
# destination model:  AlternativeFuelVehicles

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_alternative_fuel_vehicles
#
# SAFE TO RE-RUN OR RELOAD A YEAR: YES

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        for year in range(2001, 2016):
                source_file = '%s/energy/attf_v2_%s.csv' % (settings.LOCAL_DATA_ROOT, year)
                if os.path.isfile(source_file):
                    data_reader = csv.reader(open(source_file))
                    insert_count = 0
                    update_count = 0
                    for i, row in enumerate(data_reader):
                        if i == 0:
                            year_row = row
                        else:
                            for j,col in enumerate(row):
                                if j == 0:
                                    state = col.strip()
                                elif j > 0 and state <> '' and col.strip() <> '':
                                    year = year_row[j]
                                    try:
                                        record = AlternativeFuelVehicles.objects.get(state=state,year=year)
                                        if record.value <> clean_num(col):
                                            record.value = clean_num(col)
                                            record.save()
                                            db.reset_queries()
                                            update_count = update_count + 1
                                    except MultipleObjectsReturned:
                                        print '% error: multiple records exist for %s %s' % (source_file, year, state)
                                        continue
                                    except:
                                        record = AlternativeFuelVehicles(year = year, state=state, value = clean_num(col))
                                        record.save()
                                        db.reset_queries()
                                        insert_count = insert_count + 1
                    print '%s import complete. %s records updated, %s inserted' % (source_file, update_count, insert_count)