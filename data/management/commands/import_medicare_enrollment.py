from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import MedicareEnrollment
import csv
import sys
import traceback

# National Priorities Project Data Repository
# import_medicare_enrollment.py

# Imports HHS Medicare Enrollment Totals
# source info: http://www.cms.gov/DataCompendium/ (select year->State Data zip file-->Table VII.4 (accurate as of 3/15/2012)
# npp csv: http://assets.nationalpriorities.org/raw_data/health/medicare/medicare_enrollment_[year].csv (updated 3/15/2012)
# destination model:  MedicareEnrollment

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv (i.e., delete extra rows at top & bottom; add 'state' to header column text)
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 4) Run as Django management command from your project path "python manage.py import_medicare_enrollment

# Safe to re-run: YES.

class Command(NoArgsCommand):

    def handle_noargs(self, **options):
    
        def clean_num(value):
            if value.strip()=='':
                value=None
            elif value.find(".") <> -1:
                value = value.replace(",","")
                value = float(value)
            else:
                value = value.replace(",","")
                value = int(value)
            return value
            
        for year in range(2001, 2015):
            source_file = '%s/health/medicare/medicare_enrollment_%s.csv' % (settings.LOCAL_DATA_ROOT, year)
            try:
                data_reader = csv.reader(open(source_file))
                insert_count = 0
                update_count = 0
                error_count = 0
                statelist = []
                poplist = []
                valuelist = []
                percentlist = []
                for i, row in enumerate(data_reader):
                    if i == 0:
                        header_row = row
                        for j,col in enumerate(header_row):
                            if len(col.strip()) and col.lower().find('state') > -1:
                                statelist.append(j)
                            elif len(col.strip()) and col.lower().find('percent') > -1:
                                percentlist.append(j)
                            elif len(col.strip()) and col.lower().find('population') > -1:
                                poplist.append(j)
                            elif len(col.strip()) and col.lower().find('enrollee') > -1:
                                valuelist.append(j)
                    elif i > 0:
                        for j, v in enumerate(statelist):
                            if row[v].strip() <> '' and row[v].lower().find('all') == -1:
                                try:
                                    state = row[v]
                                    record, created = MedicareEnrollment.objects.get_or_create(state=state,year=year)
                                    record.year = year
                                    record.state = row[v]
                                    record.population = clean_num(row[poplist[j]])
                                    record.value = clean_num(row[valuelist[j]])
                                    record.percent = clean_num(row[percentlist[j]])
                                    record.save()
                                    db.reset_queries()
                                except:
                                    print 'Error inserting/updating record for year %s, state %s' % (year, state)
                                    print sys.exc_info()[1]
                                    #traceback.print_exc(sys.exc_info()[2])
                                    error_count = error_count + 1
                                    continue
                                
                                if created:
                                    insert_count = insert_count + 1
                                else:
                                    update_count = update_count + 1
            
                print '%s medicare enrollment complete. %s records updated, %s inserted' % (year, update_count, insert_count)
                
            except:
                    continue