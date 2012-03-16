from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import HighSchoolDropouts
from npp_api.data.utils import clean_num
import csv

# National Priorities Project Data Repository
# import_hs_dropouts.py
# Updated 7/21/2010, Joshua Ruihley, Sunlight Foundation

# Imports NCES High School Dropout Data
# source info: http://nces.ed.gov/ccd/bat/index.asp (accurate as of 3/16/2012)
# npp csv: http://assets.nationalpriorities.org/raw_data/education/dropouts/hs_dropouts.csv (updated 3/16/2011)
# destination model:  HighSchoolDropouts

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_hs_dropouts"

# Safe to re-run: YES.

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        
        for year in range(2001, 2015):
            source_file = '%s/education/dropouts/hs_dropouts_%s.csv' % (settings.LOCAL_DATA_ROOT, year)
            try:
                data_reader = csv.reader(open(source_file))
                insert_count = 0
                update_count = 0
                for i, row in enumerate(data_reader):
                    if i == 0:
                        year_row = row
                    else:
                        for j,col in enumerate(row):
                            if j == 0:
                                state = col
                            elif j > 0:
                                if row[0].strip() <> '':
                                    try:
                                        year = year_row[j]
                                        record, created = HighSchoolDropouts.objects.get_or_create(state=state,year=year)
                                        record.value = clean_num(col)
                                        record.save()
                                        db.reset_queries()
                                        if created:
                                            insert_count = insert_count + 1
                                        else:
                                            update_count = update_count + 1
                                    except:
                                        print 'Error inserting/updating record for year %s, state %s' % (year, state)
                                        print sys.exc_info()[1]
                                        #traceback.print_exc(sys.exc_info()[2])
                                        continue
                                        
                print '%s hs dropouts complete. %s records updated, %s inserted' % (year, update_count, insert_count)
                
            except:
                    continue
                                
                       