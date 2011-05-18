from django import db
from django.core.management.base import NoArgsCommand
from data.models import CffrProgramRaw, CffrProgram

# National Priorities Project Data Repository
# load_cffr_program.py 
# Created 5/10/2011

# Populates the CFFR program codes used by the API
# source model(s): CffrProgramRaw
# source load command(s): import_cffr_annual_prog
# destination model:  CffrProgram

# HOWTO:
# 1) Ensure that CffrProgramRaw is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_cffr_program"

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        record_count = 0
        error_count = 0
        for y in CffrProgramRaw.objects.values('year').distinct():
            year_current = y['year']
            records_current = CffrProgram.objects.filter(year=year_current).count()
            # if we already have records loaded for this year, skip it
            if records_current == 0: 
                for p in CffrProgramRaw.objects.filter(year=year_current):
                    record = CffrProgram(year=p.year, program_code=p.program_id_code, program_name = p.program_name)
                    
                    try:
                        record.save()
                        db.reset_queries()
                        record_count = record_count + 1
                    except:
                        print 'Failed load for ' + str(p.year) + ' ' + str(p.program_id_code)
                        error_count = error_count + 1
                        
            else:
                print str(records_current) + ' CffrProgram records already loaded for ' + str(year_current) + '. No ' + str(year_current) + ' will be loaded.'
        
        print str(record_count) + ' records loaded. Number of errors was ' + str(error_count) + '.'
