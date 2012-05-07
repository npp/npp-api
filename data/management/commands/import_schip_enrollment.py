from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import SchipEnrollmentStateRaw
import csv
from npp_api.data.utils import clean_num

# National Priorities Project Data Repository
# import_schip_enrollment.py

# Imports HHS S-CHIP Enrollment Data
# source info: http://www.insurekidsnow.gov/professionals/reports/chipra/2010_enrollment_data.pdf (accurate as of 5/7/2012)
# destination model:  SchipEnrollmentStateRaw

# HOWTO:
# 1) Download source files from url listed above
# 2) Pull the numbers out of the PDF file into Excel
# 3) Add the new year(s) and corresponding data to the exsiting npp csv
# 4) Run as Django management command from your project path "python manage.py import_schip_enrollment

# safe to re-run? yes

SOURCE_FILE = '%s/health/chip.csv' % (settings.LOCAL_DATA_ROOT)

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
                    elif j > 0:
                        year = year_row[j]
                        try:
                            record = SchipEnrollmentStateRaw.objects.get(
                                state=state, year=year)
                            update_count = update_count + 1
                        except:
                            record = SchipEnrollmentStateRaw()
                            record.state = state
                            record.year = year
                            insert_count = insert_count + 1
                        record.value = clean_num(col)
                        record.save()
                        db.reset_queries()
                        
        print 'SCHIP enrollments import complete. %s inserted, %s updated' % (
            insert_count, update_count)
