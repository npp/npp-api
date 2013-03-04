from django import db
from django.db import transaction
from django.conf import settings
from django.core.management.base import NoArgsCommand
from data.models import Cfda
import csv, os, glob
from dateutil.parser import *
import traceback

# National Priorities Project Data Repository
# import_cfda

# Imports Catalog of Federal Domestic Assistance (CFDA) file
# source info: ftp://ftp.cfda.gov/usaspending/
# destination model: Cfda

# safe to re-run: yes

SOURCE_DIR = '%s/cfda' % settings.LOCAL_DATA_ROOT

class Command(NoArgsCommand):
    
    @transaction.commit_on_success
    def handle_noargs(self, **options):
    
        def clean_text(s):
            s = s.strip().decode("windows-1252")
            if s.lower() == 'none.':
                s = s[:-1]
            elif s.lower() == 'not applicable.':
                s = s[:-1]
            elif s.lower() == 'no data available.':
                s = s[:-1]
            return s
        def clean_end_punct(s):
            if len(s) and s[-1] == '.':
                return s[:-1].strip()
            else:
                return s.strip()
        def clean_flag(s):
            if s.strip().lower() == 'yes':
                return True
            else:
                return False
            
        update_count = 0
        insert_count = 0
        update_list = []
        
        dir_path = os.path.join('%s/programs-full-usaspending*.csv' % SOURCE_DIR)
        for file in glob.glob(dir_path):
            data_reader = csv.reader(open(file))
            for i, row in enumerate(data_reader):
                if i == 0:
                    header_row = row
                else:
                    try:
                        program_number = row[1]
                        record = Cfda.objects.get(program_number=program_number)
                        update_count = update_count + 1
                        update_list.append(program_number)
                    except:
                        record = Cfda()
                        record.program_number=program_number
                        insert_count = insert_count + 1
                    record.program_title = clean_text(row[0])
                    record.popular_name = clean_text(row[2])
                    record.agency_name = clean_text(row[3])
                    record.authorization = clean_text(row[4])
                    record.objective = clean_text(row[5])
                    record.assistance_type = clean_text(row[6])
                    record.use = clean_text(row[7])
                    record.applicant_eligibility = clean_text(row[8])
                    record.beneficiary_eligibility = clean_text(row[9])
                    record.credentials = clean_text(row[10])
                    record.preapplication_coordination = clean_text(row[11])
                    record.application_procedure = clean_text(row[12])
                    record.award_procedure = clean_text(row[13])
                    record.deadline = clean_text(row[14])
                    record.approval_time_range = clean_text(row[15])
                    record.appeals = clean_text(row[16])
                    record.renewal = clean_text(row[17])
                    record.formula_matching_grant_request = clean_text(row[18])
                    record.assistance_length_time = clean_text(row[19])
                    record.reports = clean_text(row[20])
                    record.audits = clean_text(row[21])
                    record.record = clean_text(row[22])
                    record.account_id = clean_end_punct(row[23])
                    record.obligations = clean_text(row[24])
                    record.range_average_assistance = clean_text(row[25])
                    record.accomplishments = clean_text(row[26])
                    record.regulations = clean_text(row[27])
                    record.regional_local_office = clean_text(row[28])
                    record.headquarters_office = clean_text(row[29])
                    record.web_address = clean_end_punct(row[30])
                    #related_program 
                    record.example_projects = clean_text(row[32])
                    record.selection_criteria = clean_text(row[33])
                    record.url = clean_text(row[34])
                    record.recovery_flag = clean_flag(row[35])
                    record.omb_agency_code = clean_text(row[36])
                    record.omb_bureau_code = clean_text(row[37])
                    record.published_date = parse(clean_text(row[38]))
                    try:
                        record.save()
                        db.reset_queries()
                    except:
                        traceback.print_exc()
                        for j,col in enumerate(row):
                            print '%s: %s %s' % (header_row[j], len(col), col.decode("windows-1252"))
                        return

            print 'CFDA loaded: %s records inserted, %s updated' % (insert_count, update_count)
            if update_count > 0:
                print 'updated programs: %s' % update_list