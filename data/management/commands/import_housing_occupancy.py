from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import HousingOccupancyStateRaw
from npp_api.data.utils import clean_num, clean_moe
import csv

# National Priorities Project Data Repository
# import_household_occupancy.py

# Imports Household Occupancy
# source info: http://factfinder2.census.gov/bkmk/navigation/1.0/en/d_program:ACS (American Community 1 Year Estimates, Table=DP04 SELECTED HOUSING CHARACTERISTICS, Geography=United States + All States)
# destination model:  HousingOccupancyStateRaw

# HOWTO:
# 1) Use Census Factfinder site (url above) to get ACS 1 year estimates, table DP04. Download the csv version.
# 2) Create a new housing_occupancy csv using data from the DP04 download (info below)
# Mapping for model names to ACS column names
# total units = HC01_VC03
# total units moe = HC02_vc03
# occupied units = HC01_VC04
# occupied units moe HC02_VC04
# occupied units % HC03_VC04
# occumpied units % moe HC04_VC04
# vacant units HC01_VC05
# vacant units moe HC02_VC05
# vacant units percent HC03_VC05
# vacant units percent moe HC04_VC05
# owner vacancy rate HC01_VC07
# owner vacancy rate moe HC02_VC07
# renter vacancy rate HC01_VC08
# renter vacancy rate moe HC02_VC08
# owner occupied HC01_VC63
# owner occupied moe HC02_VC63
# owner occupied % HC03_VC63
# owner occupied % moe HC04_VC63
# renter occupied HC01_VC64
# renter occupied moe HC02_VC64
# renter occupied % HC03_VC64
# renter occupied % moe HC04_VC64

# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) Run as Django management command from your project path "python manage.py import_household_occupancy"

# Safe to re-run: YES.

class Command(NoArgsCommand):

    def handle_noargs(self, **options):
            
        for year in range(2005, 2015):
            source_file = '%s/census.gov/housing/housing_occupancy_%s.csv' % (settings.LOCAL_DATA_ROOT, year)
            insert_count = 0
            update_count = 0
            try:
                data_reader = csv.reader(open(source_file))
            except:
                continue
                
            for i, row in enumerate(data_reader):
                if i == 0:
                    header_row = row
                elif i > 0:
                    if row[0].strip() <> '':
                        state = row[2]
                        try:
                            record = HousingOccupancyStateRaw.objects.get(state=state,year=year)
                            update_count = update_count + 1
                        except:
                            record = HousingOccupancyStateRaw()
                            record.year = year
                            record.state = state
                            insert_count = insert_count + 1
                            
                        if len(row[1]) == 1:
                            record.state_fips = '0%s' % row[1]
                        elif len(row[1]) == 2:
                            record.state_fips = row[1]
                        else:
                            record.state_fips = '00'
                        record.total_units = clean_num(row[3])
                        record.total_units_moe = clean_moe(row[4])
                        record.occupied_units = clean_num(row[5])
                        record.occupied_units_moe = clean_moe(row[6])
                        record.occupied_units_percent = clean_num(row[7])
                        record.occupied_units_percent_moe = clean_moe(row[8])
                        record.vacant_units = clean_num(row[9])
                        record.vacant_units_moe = clean_moe(row[10])
                        record.vacant_units_percent = clean_num(row[11])
                        record.vacant_units_percent_moe = clean_moe(row[12])
                        record.owner_vacancy_rate = clean_num(row[13])
                        record.owner_vacancy_rate_moe = clean_moe(row[14])
                        record.renter_vacancy_rate = clean_num(row[15])
                        record.renter_vacancy_rate_moe = clean_moe(row[16])
                        record.owner_occupied = clean_num(row[17])
                        record.owner_occupied_moe = clean_moe(row[18])
                        record.owner_occupied_percent = clean_num(row[19])
                        record.owner_occupied_percent_moe = clean_moe(row[20])
                        record.renter_occupied = clean_num(row[21])
                        record.renter_occupied_moe = clean_moe(row[22])
                        record.renter_occupied_percent = clean_num(row[23])
                        record.renter_occupied_percent_moe = clean_moe(row[24])
                        record.save()
            print '%s household occupancy raw import complete. %s records updated, %s inserted' % (year, update_count, insert_count)           
        db.reset_queries()
                
           