from django import db
from django.db import transaction
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import PopulationEst00Raw, AnsiState
from datetime import datetime
import csv

# National Priorities Project Data Repository
# import_population_est_00.py

# Imports yearly census population estimates from the 2000-2009 decard
# source info: http://www.census.gov/popest/counties/asrh/CC-EST2009-alldata.html (accurate as of 7/6/2011)
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
            
        @transaction.commit_on_success
        def import_state(stateid):
        
            source_file = '%s/cc-est2009-alldata-%s.csv' % (SOURCE_FOLDER, stateid)
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
                if i == 0:
                    header_row = [x.lower() for x in row]
                else:
                    state = row[1]
                    county = row[2]
                    year = row[5]
                    agegrp = row[6]
                    try:
                        record = PopulationEst00Raw.objects.get(state=state,county=county,year=year,agegrp=agegrp)
                        update_count = update_count + 1
                    except:
                        record = PopulationEst00Raw()
                        record.state = state
                        record.county = county
                        record.year = year
                        record.agegrp = agegrp
                        insert_count = insert_count + 1
                    
                    for j,col in enumerate(row):
                        if j > 6:
                            setattr(record, header_row[j], clean_int(col))
                        elif header_row[j] == 'ctyname':
                            setattr(record, header_row[j], unicode(col.strip(),errors='ignore'))
                        else:
                            setattr(record, header_row[j], col.strip())
                            
                    record.save()
                    db.reset_queries()
                    
            f.close()
            print 'updates = ' + str(update_count) + '; inserts = ' + str(insert_count)
            
        #if state_ansi list is empty, set up to process all states
        if not len(STATE_ANSI):
            states = AnsiState.objects.all()
            for state in states:
                STATE_ANSI.append(state.ansi_state)
        
        #for each state, find and import its corresponding file
        start_time = datetime.now()
        for state in STATE_ANSI:
            import_state(state)
        elapsed_time = datetime.now() - start_time
        print 'elasped time = ' + str(elapsed_time)
        print ' '

                