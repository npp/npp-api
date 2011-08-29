from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import AverageTeacherSalary
import csv

# National Priorities Project Data Repository
# import_average_teacher_salary.py

# Imports Department of Education Average Full Time Teacher Salaries
# source info: http://nces.ed.gov/programs/digest/ (accurate as of 8/29/2011)
# npp csv: http://assets.nationalpriorities.org/raw_data/education/average_teacher_salary.csv (updated 6/25/2010)
# destination model:  AverageTeacherSalary

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_average_teacher_salary"]

# Safe to re-run?  Yes. 

SOURCE_FILE = '%s/education/average_teacher_salary.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
        insert_count = 0
        update_count = 0
        for i, row in enumerate(data_reader):
            if i == 0:
                year_row = row;            
            else:
                for j,col in enumerate(row):
                    if j == 0:
                        state = col
                    else:
                        if len(state):
                            year = year_row[j]
                            try:
                                record = AverageTeacherSalary.objects.get(year=year,state=state)
                                update_count = update_count + 1
                            except MultipleObjectsReturned:
                                print 'error: multiple records found for year %s and state %s. value not inserted' % (year,state)
                                continue
                            except:
                                record = AverageTeacherSalary()
                                record.year = year
                                record.state = state
                                insert_count = insert_count + 1
                            
                            record.value = col
                            record.save()
                            db.reset_queries()
                            
        print 'Import complete: %s records updated, %s records inserted' % (update_count, insert_count)