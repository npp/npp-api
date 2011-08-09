from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import PupilTeacherStateRaw
import csv

# National Priorities Project Data Repository
# import_pupil_teacher.py

# Imports State Level Pupil Teacher Ratio
# source info: http://nces.ed.gov/ccd/bat/index.asp (accurate as of 8/09/2011)
# npp csv: http://assets.nationalpriorities.org/education/teacher_pupil_ratio.csv (updated 7/20/2010)
# destination model:  PupilTeacherStateRaw

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_pupil_teacher

# safe to re-run: NO

SOURCE_FILE = '%s/doe.gov/pupil_teacher_ratio.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
        for i, row in enumerate(data_reader):
            if i == 0:
                year_row = row;
            elif len(row[0]):
                for j,col in enumerate(row):
                    if j == 0:
                        state = col
                    elif j > 0:
                        if len(state):
                            year = year_row[j]
                            value = col
                            record = PupilTeacherStateRaw()
                            record.state = state
                            record.year = year
                            record.ratio = value
                            record.save()
                            db.reset_queries()
            else:
                return