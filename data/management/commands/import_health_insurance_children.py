from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import KidsHealthInsurance
import csv

# National Priorities Project Data Repository
# import_kids_health_insurance.py
# Updated 6/21/2010, Joshua Ruihley, Sunlight Foundation

# Imports Census Health Insurance Coverage Data
# source info: http://www.census.gov/hhes/www/hlthins/ (accurate as of 11/4/2011)
# npp csv: http://assets.nationalpriorities.org/raw_data/health/kids_hi.csv (updated 6/21/2010)
# destination model:  KidsHealthInsurance

# HOWTO:
# 1) Download source files from url listed above
# 2) Convert source file to .csv with same formatting as npp csv
# 3) change SOURCE_FILE variable to the the path of the source file you just created
# 5) Run as Django management command from your project path "python manage.py import_kids_health_insurance

SOURCE_FILE = '%s/health/children_hi.csv' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        data_reader = csv.reader(open(SOURCE_FILE))
        
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
        
        for i, row in enumerate(data_reader):
            if i == 0:
                header_row = row;            
            else:
                record = KidsHealthInsurance()
                for j,col in enumerate(row):
                    if j == 0:
                        setattr(record, header_row[j], col)
                    else:
                        setattr(record, header_row[j], clean_num(col))
                record.all_people = record.all_people * 1000
                record.not_covered = record.not_covered * 1000
                record.covered = record.covered * 1000
                record.private = record.private * 1000
                record.private_employment = record.private_employment * 1000
                record.direct_purchase = record.direct_purchase * 1000
                record.govt = record.govt * 1000
                record.medicaid = record.medicaid * 1000
                record.medicare = record.medicare * 1000
                record.military = record.military * 1000
                record.save()