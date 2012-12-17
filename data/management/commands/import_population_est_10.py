from django import db
from django.db import transaction
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import PopulationEst10Raw
from datetime import datetime
from npp_api.data.utils import clean_num, pad_state, pad_county, clean_county_name
import csv
import glob

# National Priorities Project Data Repository
# import_population_est_10.py

# Imports 2010-2020 county population estimates
# source info: http://www.census.gov/popest/data/counties/asrh/2011/CC-EST2011-RACE6.html
# npp csv: 
# destination model: PopulationEst10Raw

# Safe to re-run: YES (previous population estimates are often revised)

SOURCE_FOLDER = '%s/census.gov/population_estimates' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    @transaction.commit_on_success  
    def handle_noargs(self, **options):
            
        def import_state(filename):
        
            try:
                with open(filename) as f:
                    #data_reader = csv.reader(f)
                    data_reader = csv.reader(open(file))
            except IOError:
                print 'cannot open file: %s' % filename
                return
            except:
                print 'unknown file issue: %s' % filename
                return
                
            insert_count = 0
            update_count = 0
                
            for i, row in enumerate(data_reader):
                if i == 0:
                    header_row = [x.lower() for x in row]
                else:
                    state = pad_state(row[1])
                    county = pad_county(row[2])
                    gender = row[5]
                    ethnic_origin = row[6]
                    race = row[7]
                    
                    record, created = PopulationEst10Raw.objects.get_or_create(state=state,county=county,gender=gender,ethnic_origin=ethnic_origin,race=race)
                    record.sumlev = row[0]
                    record.stname = row[3]
                    record.ctyname = clean_county_name(row[4])
                    record.census2010pop = clean_num(row[8])
                    record.estimatesbase2010 = clean_num(row[9])
                    record.popestimate2010 = clean_num(row[10])
                    record.popestimate2011 = clean_num(row[11])
                    try:
                        record.popestimate2012 = clean_num(row[12])
                        record.popestimate2013 = clean_num(row[13])
                        record.popestimate2014 = clean_num(row[14])
                        record.popestimate2015 = clean_num(row[15])
                        record.popestimate2016 = clean_num(row[16])
                        record.popestimate2017 = clean_num(row[17])
                        record.popestimate2018 = clean_num(row[18])
                        record.popestimate2019 = clean_num(row[19])
                        record.census2020pop = clean_num(row[20])
                        record.popestimate2020 = clean_num(row[21])
                    except:
                        pass
                    
                    if created:
                        insert_count = insert_count + 1
                    else:
                        update_count = update_count + 1
                            
                    record.save()
                    db.reset_queries()
                    
            f.close()
            print '%s: updates = %s; inserts = %s' % (filename, update_count, insert_count)
        
        start_time = datetime.now()
        source_prefix = '%s/CC-EST2011-6RACE-' % SOURCE_FOLDER
        files = glob.glob('%s*.csv' % source_prefix)
        for file in files:
            import_state(file)

        elapsed_time = datetime.now() - start_time
        print 'elasped time = ' + str(elapsed_time)
        print ' '

                