from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import MedianHouseholdIncomeStateRaw
from npp_api.data.utils import clean_num
import csv
import sys
import traceback

# National Priorities Project Data Repository
# import_median_household_income.py

# Imports Median Household Income
# source info: http://factfinder2.census.gov/bkmk/navigation/1.0/en/d_program:ACS (American Community 1 Year Estimates, Table=B19013, Geography=United States + All States)
# npp csv: http://assets.nationalpriorities.org/raw_data/census.gov/income/median_household_[year].csv (updated 3/23/2012)
# destination model:  MedianHouseholdIncomeStateRaw

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) Run as Django management command from your project path "python manage.py import_median_household_income

# Safe to re-run: YES.

class Command(NoArgsCommand):

    def handle_noargs(self, **options):
            
        for year in range(2001, 2015):
            source_file = '%s/census.gov/income/median_household_%s.csv' % (settings.LOCAL_DATA_ROOT, year)
            try:
                data_reader = csv.reader(open(source_file))
                insert_count = 0
                update_count = 0
                error_count = 0
                for i, row in enumerate(data_reader):
                    if i == 0:
                        header_row = row
                    elif i > 0:
                        if row[0].strip() <> '':
                            try:
                                state = row[2]
                                record, created = MedianHouseholdIncomeStateRaw.objects.get_or_create(state=state,year=year)
                                record.year = year
                                record.state = state
                                if len(row[1]) == 1:
                                    record.state_fips = '0%s' % row[1]
                                elif len(row[1]) == 2:
                                    record.state_fips = row[1]
                                else:
                                    record.state_fips = '00'
                                record.median_household_income = clean_num(row[3])
                                record.median_household_income_moe = clean_num(row[4])
                                record.save()
                                db.reset_queries()
                            except:
                                print 'Error inserting/updating record for year %s, state %s' % (year, state)
                                print sys.exc_info()[1]
                                #traceback.print_exc(sys.exc_info()[2])
                                error_count = error_count + 1
                                continue
                            
                            if created:
                                insert_count = insert_count + 1
                            else:
                                update_count = update_count + 1
            
                print '%s median household income raw import complete. %s records updated, %s inserted' % (year, update_count, insert_count)
                
            except:
                    continue