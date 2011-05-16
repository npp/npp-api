from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import AnsiState
import csv

# National Priorities Project Data Repository
# import_ansi_state.py 
# Created 5/9/2011

# Imports ANSI State Codes made available by Census Bureau
# source file: http://www.census.gov/geo/www/ansi/state.txt (accurate as of 5/9/2011)
# source info: http://www.census.gov/geo/www/ansi/statetables.html
# npp cache: http://assets.nationalpriorities.org/raw_data/??????
# destination model:  AnsiState

# HOWTO:
# 1) Download source file from url listed above
# 2) change SOURCE_FILE variable to the the path of the source file you just downloaded
# 3) Run as Django management command from your project path "python manage.py import_ansi_state

SOURCE_FILE = '%s/census.gov/state.txt' % settings.LOCAL_DATA_ROOT

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        csv.register_dialect('pipes', delimiter='|')
        with open(SOURCE_FILE, 'r') as f:
            data_reader = csv.reader(f, dialect='pipes')
            i=0
            for row in data_reader:
                if (i==0):
                    fields = row
                else:
                    j=0
                    row_dict = {}
                    for column in fields:
                        row_dict[column] = row[j]            
                        j = j + 1
                    db_row =AnsiState(ansi_state=row_dict['STATE'], 
                        state=row_dict['STUSAB'], state_name=row_dict['STATE_NAME'], gnisid=row_dict['STATENS'])
                    db_row.save()
                    db.reset_queries()        
                i = i + 1