from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import HealthInsuranceStateRaw
from npp_api.data.utils import clean_num
import csv
import re
import glob

# National Priorities Project Data Repository
# import_health_insurance.py

# Imports Census ACS Health Insurance Coverage Data
# source info: Census ACS 1 Year Estimates, table C27010 (accurate as of 01/18/2013)
# destination model:  HealthInsuranceStateRaw

# HOWTO:
# 1) Download source files
# 2) change SOURCE_FILE variable to the the path of the source file you just created
# 3) Run as Django management command from your project path "python manage.py import_health_insurance

# Safe to re-run: YES

SOURCE_FOLDER = '%s/census.gov/acs/state/' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        def load_year(file, year):
            data_reader = csv.reader(open(file))
            total_inserts = 0
            total_updates = 0
            for i, row in enumerate(data_reader):
                if i == 0:
                    header_row = row
                elif file.find('ann') <> -1 and i == 1:
                    #if we're working with an annotated version of the 
                    #downloaded ACS file, ignore the 2nd row
                    pass
                else:
                    state = row[2]
                    try:
                        record = HealthInsuranceStateRaw.objects.get(year=year,state=state)
                        total_updates = total_updates + 1
                    except:
                        record = HealthInsuranceStateRaw()
                        record.year = year
                        record.state = state
                        total_inserts = total_inserts + 1

                    record.geoid = row[0]
                    record.pop = clean_num(row[3])
                    record.pop_moe = clean_num(row[4])
                    record.pop_under_18 = clean_num(row[5])
                    record.pop_under_18_moe = clean_num(row[6])
                    record.pop_under_18_private = clean_num(row[7])
                    record.pop_under_18_private_moe = clean_num(row[8])
                    record.pop_under_18_public = clean_num(row[9])
                    record.pop_under_18_public_moe = clean_num(row[10])
                    record.pop_under_18_private_public = clean_num(row[11])
                    record.pop_under_18_private_public_moe = clean_num(row[12])
                    record.pop_under_18_no_ins = clean_num(row[13])
                    record.pop_under_18_no_ins_moe = clean_num(row[14])
                    record.pop_18_34 = clean_num(row[15])
                    record.pop_18_34_moe = clean_num(row[16])
                    record.pop_18_34_private = clean_num(row[17])
                    record.pop_18_34_private_moe = clean_num(row[18])
                    record.pop_18_34_public = clean_num(row[19])
                    record.pop_18_34_public_moe = clean_num(row[20])
                    record.pop_18_34_private_public = clean_num(row[21])
                    record.pop_18_34_private_public_moe = clean_num(row[22])
                    record.pop_18_34_no_ins = clean_num(row[23])
                    record.pop_18_34_no_ins_moe = clean_num(row[24])
                    record.pop_35_64 = clean_num(row[25])
                    record.pop_35_64_moe = clean_num(row[26])
                    record.pop_35_64_private = clean_num(row[27])
                    record.pop_35_64_private_moe = clean_num(row[28])
                    record.pop_35_64_public = clean_num(row[29])
                    record.pop_35_64_public_moe = clean_num(row[30])
                    record.pop_35_64_private_public = clean_num(row[31])
                    record.pop_35_64_private_public_moe = clean_num(row[32])
                    record.pop_35_64_no_ins = clean_num(row[33])
                    record.pop_35_64_no_ins_moe = clean_num(row[34])
                    record.pop_over_64 = clean_num(row[35])
                    record.pop_over_64_moe = clean_num(row[36])
                    record.pop_over_64_private = clean_num(row[37])
                    record.pop_over_64_private_moe = clean_num(row[38])
                    record.pop_over_64_public = clean_num(row[39])
                    record.pop_over_64_public_moe = clean_num(row[40])
                    record.pop_over_64_private_public = clean_num(row[41])
                    record.pop_over_64_private_public_moe = clean_num(row[42])
                    record.pop_over_64_no_ins = clean_num(row[43])
                    record.pop_over_64_no_ins_moe = clean_num(row[44])
                    record.save()

            db.reset_queries()
            print '%s imported. %s updated, %s inserted' % (year, total_updates, total_inserts)

        files = glob.glob('%sACS_*_1YR_C27010_with_ann.csv' % 
            SOURCE_FOLDER)
        files.extend(glob.glob('%sACS_*_1YR_c27010.csv' % 
            SOURCE_FOLDER))
        for file in files:
            y = re.search('_[0-9][0-9]_', file)
            year = '20%s' % file[y.start() + 1:y.end() - 1]
            load_year(file, year)