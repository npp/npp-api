from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import Msn
import csv

# National Priorities Project Data Repository
# import_msn.py 
# Created 4/16/2012

# Import MSN (menomic series names) used in the State Energy Data System (SEDS)
# source file: http://www.eia.gov/state/seds/seds-technical-notes-complete.cfm#data (codes & descriptions)
# npp cache: http://assets.nationalpriorities.org/raw_data/??????
# destination model:  Msn

# HOWTO:
# 1) Download source file from url listed above
# 2) change SOURCE_FILE variable to the the path of the source file you just downloaded
# 3) Run as Django management command from your project path "python manage.py import_ansi_state

# Safe to re-run: yes

SOURCE_FILE = '%s/energy/msn.csv' % settings.LOCAL_DATA_ROOT

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        with open(SOURCE_FILE, 'r') as f:
            data_reader = csv.reader(f)
            i=0
            insert_count = 0
            update_count = 0
            for row in data_reader:
                if (i==0):
                    fields = row
                else:
                    j=0
                    row_dict = {}
                    for column in fields:
                        row_dict[column] = row[j]            
                        j = j + 1
                    try:
                        db_row = Msn.objects.get(msn_code = row_dict['msn'])
                        db_row.msn_desc = row_dict['description']
                        db_row.msn_unit = row_dict['unit']
                        update_count = update_count + 1
                    except:
                        db_row =Msn(msn_code=row_dict['msn'], 
                        msn_desc=row_dict['description'], msn_unit=row_dict['unit'])
                        insert_count = insert_count + 1
                    db_row.save()
                    db.reset_queries()
                i = i + 1
                
        print 'msn insert complete. %s rows updated, %s rows inserted.' % (update_count, insert_count)