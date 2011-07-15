from django import db
from django.db import transaction
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import PopulationEst80Raw
from datetime import datetime
import csv

# National Priorities Project Data Repository
# import_population_est_80.py

# Imports yearly census population estimates from the 1980-1989 decade
# source info: http://www.census.gov/popest/archives/1980s/PE-02.html(accurate as of 7/6/2011)
# npp csv: 
# destination model: PopulationEst00Raw

# HOWTO:
# 1) Download source files from url listed above to your local data root folder. There is one file per year
# 2) Change SOURCE_FOLDER variable to the folder that contains the files
# 3) Run as Django management command from your project path "python manage.py import_population_est_80

# Safe to re-run: YES (previous population estimates are often revised)

SOURCE_FOLDER = '%s/census.gov/population_estimates' % (settings.LOCAL_DATA_ROOT)
YEARS = ['1981']

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        def clean_int(value):
            value = value.strip().replace(",","")
            try:
                value = int(value)
            except:
                value = None
            return value
            
        @transaction.commit_on_success
        def import_year(yearid):
        
            source_file = '%s/PE-02-%s.csv' % (SOURCE_FOLDER, yearid)
            print source_file
            
            insert_count = 0
            update_count = 0
            
            try:
                with open(source_file) as f:
                    data_reader = csv.reader(f)
                data_reader = csv.reader(open(source_file))
            except IOError:
                print 'cannot open file'
                return
            except:
                print 'unknown file issue'
                return
                
            for i, row in enumerate(data_reader):
                if len(row) and row[0] == yearid:
                    year = row[0].strip()
                    state_county = row[1].strip()
                    race_gender = row[2].strip()
                    try:
                        record = PopulationEst80Raw.objects.get(year=year, state_county=state_county, race_gender=race_gender)
                        update_count = update_count + 1
                    except:
                        record = PopulationEst80Raw()
                        record.year = year
                        record.state_county = state_county
                        record.race_gender = race_gender
                        insert_count = insert_count + 1
                        
                    record.age_under_5 = clean_int(row[3])
                    record.age_5_9 = clean_int(row[4])
                    record.age_10_14 = clean_int(row[5])
                    record.age_15_19 = clean_int(row[6])
                    record.age_20_24 = clean_int(row[7])
                    record.age_25_29 = clean_int(row[8])
                    record.age_30_34 = clean_int(row[9])
                    record.age_35_39 = clean_int(row[10])
                    record.age_40_44 = clean_int(row[11])
                    record.age_45_49 = clean_int(row[12])
                    record.age_50_54 = clean_int(row[13])
                    record.age_55_59 = clean_int(row[14])
                    record.age_60_64 = clean_int(row[15])
                    record.age_65_69 = clean_int(row[16])
                    record.age_70_74 = clean_int(row[17])
                    record.age_75_79 = clean_int(row[18])
                    record.age_80_84 = clean_int(row[19])
                    record.age_over_84 = clean_int(row[20])
                    
                    record.save()
                    db.reset_queries()
                        
            f.close()
            print 'updates = ' + str(update_count) + '; inserts = ' + str(insert_count)
            
        #for each year, find and import its corresponding file
        start_time = datetime.now()
        for year in YEARS:
            import_year(year)
        elapsed_time = datetime.now() - start_time
        print 'elasped time = ' + str(elapsed_time)
        print ' '

                