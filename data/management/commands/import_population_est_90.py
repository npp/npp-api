from django import db
from django.db import transaction
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import PopulationEst90Raw
from datetime import datetime

# National Priorities Project Data Repository
# import_population_est_90.py

# Imports yearly census population estimates from the 1990-1999 decade
# source info: http://www.census.gov/popest/datasets.html#cntyinter (accurate as of 7/6/2011)
# npp csv: 
# destination model: PopulationEst90Raw

# HOWTO:
# 1) Download source files from url listed above to your local data root folder. There is one file per year
# 2) Change SOURCE_FOLDER variable to the folder that contains the files
# 3) Run as Django management command from your project path "python manage.py import_population_est_90

# Safe to re-run: YES (previous population estimates are often revised)

YEARS = ['1999']
SOURCE_FOLDER = '%s/census.gov/population_estimates' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        def clean_int(value):
            value = value.replace(",","")
            try:
                value = int(value)
            except:
                value = None
            return value

        @transaction.commit_on_success
        def import_year(yearid):
        
            source_file = '%s/STCH-icen%s.txt' % (SOURCE_FOLDER, yearid)
            print source_file
            insert_count = 0
            update_count = 0

            with open(source_file) as data_reader:
                
                for row in data_reader:
                    year = row[:2]
                    state = row[4:6]
                    county = row[6:9]
                    agegrp = row[10:12].strip()
                    race_gender = row[13]
                    ethnic_origin = row[15]
                    
                    try:
                        record = PopulationEst90Raw.objects.get(year=year,state=state,county=county,agegrp=agegrp, race_gender=race_gender,ethnic_origin=ethnic_origin)
                        update_count = update_count + 1
                    except:
                        record = PopulationEst90Raw()
                        record.year = year
                        record.state = state
                        record.county = county
                        record.year = year
                        record.agegrp = agegrp
                        record.race_gender = race_gender
                        record.ethnic_origin = ethnic_origin
                        insert_count = insert_count + 1
                        
                    record.population = clean_int(row[17:].strip())
                    record.save()
                    db.reset_queries()
                    
            print 'updates = ' + str(update_count) + '; inserts = ' + str(insert_count)
        
        #for each year, find and import its corresponding file
        start_time = datetime.now()        
        for year in YEARS:
            import_year(year)
        elapsed_time = datetime.now() - start_time
        print 'elasped time = ' + str(elapsed_time)
        print ' '
