from django import db
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from data.models import FederalTaxCollectionStateRaw
from decimal import *
import csv

# National Priorities Project Data Repository
# import_federal_tax_collection.py

# Imports IRS Data Book Gross Collections, by Type of Tax and State
# source info: http://www.irs.gov/uac/SOI-Tax-Stats-Gross-Collections,-by-Type-of-Tax-and-State,-Fiscal-Year-IRS-Data-Book-Table-5 (accurate as of 4/11/2013)
# destination model:  FederalTaxCollectionStateRaw

# HOWTO:
# 1) Download source files from url listed above
# 2) Format downloaded file to match .csvs used in previous years. 
# 3) Make sure to re-format displayed numbers to match actual numbers before saving as .csv (the displayed numbers don't reflect all significant digits)
# 4) change SOURCE_FILE variable to the the path of the source file you just downloaded
# 5) change column (row[]) values below to reflect where column exists in csv
# 6) Run as Django management command from your project path "python manage.py import_federal_tax_collection"

# SAFE TO RE-RUN? yes

YEARS = [1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
SOURCE_FOLDER = '%s/irs/' % (settings.LOCAL_DATA_ROOT)

class Command(BaseCommand):
    args = '<year>'
    help = 'imports federal tax collection for specified year (if you year specified, imports all available years)'
    
    def handle(self, *args, **options):
    
        def clean_value(value):
            value = value.replace(' ', '')
            if value <> '':
                try:
                    value = Decimal(value.replace(',', '')) * 1000 #numbers in this data are expressed in thousands of $, so adjust here
                except:
                    value = None
            else:
                value = None
            return value
    
        def load_year(year):
        
            source_file = '%s%sIRS.csv' % (SOURCE_FOLDER,year)
            try:
                data_reader = csv.reader(open(source_file))
            except:
                print '%s file not found' % year
                return
        
            insert_count = 0
            update_count = 0
            
            for row in data_reader:
                state = row[0].strip()
                if len(state):
                    record, created = FederalTaxCollectionStateRaw.objects.get_or_create(state=state,year=year)
                    record.total_collections = clean_value(row[1])
                    record.business_income_taxes = clean_value(row[2])
                    record.income_employment_estate_trust_total = clean_value(row[3])
                    if year > 2008:
                        record.individual_witheld_fica = clean_value(row[4])
                        record.individual_notwitheld_seca = clean_value(row[5])
                        record.unemployment_insurance = clean_value(row[6])
                        record.railroad_retirement = clean_value(row[7])
                        record.estate_trust_income_tax = clean_value(row[8])
                        record.estate_tax = clean_value(row[9])
                        record.gift_tax = clean_value(row[10])
                        record.excise_taxes = clean_value(row[11])
                    else:
                        record.individual_notwitheld_seca = clean_value(row[4])
                        record.individual_witheld_fica = clean_value(row[5])
                        record.railroad_retirement = clean_value(row[6])
                        record.unemployment_insurance = clean_value(row[7])
                        record.estate_tax = clean_value(row[8])
                        record.gift_tax = clean_value(row[9])
                        record.excise_taxes = clean_value(row[10])
                    record.save()
                    db.reset_queries()
                    
                    if created:
                        insert_count = insert_count + 1
                    else:
                        update_count = update_count + 1
                    
            print 'federal tax collection import complete. %s inserted and %s updated.' % (insert_count, update_count)
                
        if len(args):
            for year in args:
                load_year(year)
        else:
            #if no args specified, load all files in the directory
            for year in YEARS:
                load_year(year)