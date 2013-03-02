from django import db
from django.db import transaction
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from data.models import UsaspendingAssistanceRaw
from django.core.exceptions import MultipleObjectsReturned
from npp_api.data.utils import clean_num
from datetime import datetime
import csv, os, glob

# National Priorities Project Data Repository
# import_usaspending_assistance.py

# Imports Assistance Data from USASpending. 
# These files have been created via xxxxx from USASpending monthly archives (http://usaspending.gov/data)
# destination model:  UsaspendingAssistanceRaw

# Safe to re-run: yes

SOURCE_DIR = '%s/usaspending' % (settings.LOCAL_DATA_ROOT)

class Command(BaseCommand):
    args = '<year>'
    help = 'loads aggreagated USASpending assistance files for specified fiscal year'
    
    def handle(self, *args, **options):

        @transaction.commit_on_success
        def load_year(year):
            dir_path = os.path.join('%s/*totals%s.csv' % (SOURCE_DIR, year))
            for file in glob.glob(dir_path):
               print 'starting %s: %s' % (year, file)
               read_year(file)

        def read_year(file):
        
            def nullify(value):
                if len(value):
                    return value
                else:
                    return None

            with open(file) as f:
                reader = csv.reader(f)
                oldrecs = UsaspendingAssistanceRaw.objects.filter(fiscal_year=year, asst_cat_type = file.split('/')[-1][0])
                print 'cleaning up old records....'
                reccount = oldrecs.count()
                oldrecs.delete()
                print 'deleted %s records.' % reccount
                insert_count = 0
                for i, row in enumerate(reader):
                    if i == 0:
                        header_row = row
                    else:
                        record = UsaspendingAssistanceRaw()
                        for j,col in enumerate(row):
                            setattr(record, header_row[j], nullify(col))
                        record.save()
                        db.reset_queries()
                        insert_count = insert_count + 1

                print '%s done: %s records inserted.' % (file, insert_count)

        if len(args):
            start_time = datetime.now()
            for year in args:
                load_year(year)
                elapsed_time = datetime.now() - start_time
            print 'elasped time = ' + str(elapsed_time)
        else:
            print 'Please specify a year'