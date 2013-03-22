from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import pandas as pd
import numpy as np
from pandas import DataFrame
from decimal import Decimal
from datetime import datetime
import os, glob

# National Priorities Project Data Repository
# create_usaspending_assistance.py

# Aggregates and re-formats raw data from USASpending monthly archives
# http://usaspending.gov/data) and writes output to the raw_data folder

# Safe to re-run: yes

SOURCE_DIR = '%s/usaspending/datafeeds' % (settings.LOCAL_DATA_ROOT)
OUTPUT_DIR = '%s/usaspending' % (settings.LOCAL_DATA_ROOT)

class Command(BaseCommand):
    args = '<fiscal_year>, <archive_date>'
    help = 'Creates aggregate files from raw USASpending.gov archive files. Requires fiscal and date of the archive file (yyyymmdd)'
    
    def handle(self, *args, **options):
    
        def create_aggregate(year, archive_date):
        
            recip_cat_type_names = {
                'f':'For-Profit Organization',
                'g':'Government',
                'h':'Higher Education',
                'n':'Non-Profit Organization',
                'o':'Other',
                'i':'Individual'
            }

            def clean_cfda(value):
                if value == '00.000':
                    return '99.999'
                else:
                    return value

            def clean_country(row):
                country = row['recipient_country_code']
                state = row['recipient_state_code']
                if country == 'missing' and state <> '99':
                    #TOLOG: record has missing country
                    if state <> '99':
                        #note: incoming country codes are inconsistent for
                        #US territories (e.g., PR country could be Puerto
                        #Rico or USA)
                        #Not fixing this now--not sure of the right way.
                        return 'USA'
                    else:
                        return None
                else:
                    return country
                        
            def clean_state(row):
                country = row['recipient_country_code']
                state = row['recipient_state_code']
                if country <> 'USA' and state == 'VA':
                    #TOLOG: valid state w/ incorrect country
                    #logic needs fleshed out
                    return None
                elif country <> 'USA' and state in ['00','99']:
                    #technically, if the country code is a U.S. territory or
                    #outlying area, we should return '99' for a missing state
                    return None
                elif state in ['0','00']:
                    return '99'
                else:
                    return state

            def clean_county(row):
                country = row['recipient_country_code']
                state = row['recipient_state_code']
                county = row['recipient_county_code']
                if country <> 'USA':
                    return None
                elif state == '99' and county <> '999':
                    #TOLOG: rare, but it happens--county code w/o state code
                    return '999'
                elif county in ['0','00','000']:
                    return '999'
                else:
                    return county
                    
            def clean_recip_cat_type(value):
                list = value.split(': ', 1)
                if len(list) == 2 and len(list[1]):
                    return list
                elif len(list) == 2:
                    list[1] = recip_cat_type_names.get(list[0],'Unknown Value')
                    return list
                else:
                    list.append(recip_cat_type_names.get(list[0],'Unknown Value'))
                    return list

            collist = [
                'unique_transaction_id',
                'cfda_program_num',
                'recipient_county_code',
                'agency_code',
                'fed_funding_amount',
                'non_fed_funding_amount',
                'total_funding_amount',
                'assistance_type',
                'cfda_program_title',
                'face_loan_guran',
                'orig_sub_guran',
                'fiscal_year',
                'recip_cat_type',
                'asst_cat_type',
                'recipient_country_code',
                'recipient_state_code'
            ]
            
            dir_path = os.path.join('%s/%s_All*_%s.csv' % (SOURCE_DIR, year, archive_date))
            for file in glob.glob(dir_path):
            
                file_name = file.split('/')[-1]
                assistance_type = file_name.split('_')[2][0].lower()
                print 'starting file %s' % file_name
                reader = pd.read_csv(file, usecols=collist, index_col=0, iterator=True, chunksize=3000,
                    dtype={'cfda_program_num':np.object, 'recipient_county_code':np.object, 'recipient_state_code':np.object, 'fiscal_year':np.object}
                )
                details = pd.concat([chunk for chunk in reader], ignore_index=True)
              
                #clean up missing values (so they're not excluded from the groupby)  
                details = details.fillna({
                    'fyq': 'missing',
                    'cfda_program_num': '99.999',
                    'recipient_county_code': '999',
                    'recipient_country_code': 'missing',
                    'uri': 'missing',
                    'recipient_state_code': '99'
                })
                
                #clean up cfda program numbers
                details['cfda_program_num'] = details['cfda_program_num'].apply(lambda x: clean_cfda(x))

                #aggregate numeric fields
                totals = details.groupby([
                    details['cfda_program_num'],
                    details['cfda_program_title'],
                    details['agency_code'],
                    details['recipient_county_code'],
                    details['recipient_state_code'],
                    details['recipient_country_code'],
                    details['assistance_type'],
                    details['fiscal_year'],
                    details['asst_cat_type'],
                    details['recip_cat_type'],
                ]).sum()
                totals = totals.reset_index()
                
                #split codes and descriptions into separate columns
                totals['agency_code'], totals['agency_name'] = zip(
                    *totals['agency_code'].apply(lambda x: x.split(': ', 1)))
                totals['assistance_type'], totals['assistance_type_name'] = zip(
                    *totals['assistance_type'].apply(lambda x: x.split(': ', 1)))
                totals['recip_cat_type'], totals['recip_cat_type_name'] = zip(
                    *totals['recip_cat_type'].apply(lambda x: clean_recip_cat_type(x)))
                #totals['recip_cat_type'], totals['recip_cat_type_name'] = zip(
                #    *totals['recip_cat_type'].apply(lambda x: x.split(': ', 1)))

                #clean countries, states, counties
                totals['recipient_country_code'] = totals.apply(lambda row: clean_country(row),axis=1)
                totals['recipient_state_code'] = totals.apply(lambda row: clean_state(row), axis=1)
                totals['recipient_county_code'] = totals.apply(lambda row: clean_county(row), axis=1)

                #fix up data types
                totals.fed_funding_amount = totals.fed_funding_amount.astype(np.int64)
                totals.non_fed_funding_amount = totals.non_fed_funding_amount.astype(np.int64)
                totals.total_funding_amount = totals.total_funding_amount.astype(np.int64)
                totals.face_loan_guran = totals.face_loan_guran.astype(np.int64)
                totals.orig_sub_guran = totals.orig_sub_guran.astype(np.int64)

                #save file and cleanup
                totals.to_csv('%s/%stotals%s.csv' % (
                    OUTPUT_DIR, assistance_type, year), index=False)
                print 'saved file %s/%stotals%s.csv' % (
                    OUTPUT_DIR, assistance_type, year)
                if assistance_type == 'l':
                    print 'total orig_sub_guran: %s, total face_loan_guran: %s' % (
                        totals['orig_sub_guran'].sum(), totals['face_loan_guran'].sum())
                else:
                    print 'total fed_funding_amount: %s ' % totals['fed_funding_amount'].sum()
                del details
                del totals
        
        if len(args) == 2:
            start_time = datetime.now()
            create_aggregate(args[0], args[1])
            elapsed_time = datetime.now() - start_time
            print 'elasped time = ' + str(elapsed_time)
        elif len(args) > 2:
            print 'Too many arguments. Please specify a fiscal year and archive date (yyyymmdd).'
        else:
            print 'Please specify a fiscal year and archive date (yyyymmdd).'

