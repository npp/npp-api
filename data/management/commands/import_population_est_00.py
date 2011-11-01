from django import db
from django.db import transaction
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import PopulationEst00Raw, AnsiState
from datetime import datetime
import csv

# National Priorities Project Data Repository
# import_population_est_00.py

# Imports 2000-2010 county intercensal estimates
# source info: http://www.census.gov/popest/intercensal/county/CO-EST00INT-SEXRACEHISP.csv (accurate as of 11/2011)
# npp csv: 
# destination model: PopulationEst00Raw

# HOWTO:
# 1) Download source files from url listed above to your local data root folder. There is one file per state :(
# 2) Change SOURCE_FOLDER variable to the folder that contains the files
# 3) Run as Django management command from your project path "python manage.py import_population_est_00

# Safe to re-run: YES (previous population estimates are often revised)

SOURCE_FOLDER = '%s/census.gov/population_estimates' % (settings.LOCAL_DATA_ROOT)
STATE_ANSI = [] #set to [] to process files for all states

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        def clean_int(value):
            value = value.replace(",","")
            try:
                value = int(value)
            except:
                value = None
            return value
            
        def pad_state(value):
            if len(value) == 1:
                value = '%s%s' % ('0',value)
            return value
            
        def pad_county(value):
            if len(value) == 1:
                value = '%s%s' % ('00',value)
            elif len(value) == 2:
                value = '%s%s' % ('0', value)
            return value
            
        def clean_county_name(value):
            value = unicode(value.strip(),errors='ignore')
            return value
        
        start_time = datetime.now()
        source_file = '%s/CO-EST00INT-SEXRACEHISP.csv' % SOURCE_FOLDER
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
            if i == 0:
                header_row = [x.lower() for x in row]
            else:
                state = pad_state(row[1])
                county = pad_county(row[2])
                gender = row[5]
                ethnic_origin = row[6]
                race = row[7]
                
                record, created = PopulationEst00Raw.objects.get_or_create(state=state,county=county,gender=gender,ethnic_origin=ethnic_origin,race=race)
                record.sumlev = row[0]
                record.stname = row[3]
                record.ctyname = clean_county_name(row[4])
                record.estimatesbase2000 = clean_int(row[8])
                record.popestimate2000 = clean_int(row[9])
                record.popestimate2001 = clean_int(row[10])
                record.popestimate2002 = clean_int(row[11])
                record.popestimate2003 = clean_int(row[12])
                record.popestimate2004 = clean_int(row[13])
                record.popestimate2005 = clean_int(row[14])
                record.popestimate2006 = clean_int(row[15])
                record.popestimate2007 = clean_int(row[16])
                record.popestimate2008 = clean_int(row[17])
                record.popestimate2009 = clean_int(row[18])
                record.census2010pop = clean_int(row[19])
                record.popestimate2010 = clean_int(row[20])
                
                if created:
                    insert_count = insert_count + 1
                else:
                    update_count = update_count + 1
                        
                record.save()
                db.reset_queries()
                
        f.close()
        print 'updates = ' + str(update_count) + '; inserts = ' + str(insert_count)
            
        elapsed_time = datetime.now() - start_time
        print 'elasped time = ' + str(elapsed_time)
        print ' '

                