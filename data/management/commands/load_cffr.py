from django import db
from django.core.management.base import NoArgsCommand
from django.db.models import Sum
from data.models import CffrRaw, CffrProgram, CffrState, State, County, Cffr

# National Priorities Project Data Repository
# load_cffr.py 
# Created 5/11/2011

# Populates the Cffr model and the CffrState summary table used by the API
# source model(s): CffrRaw
# source load command(s): import_cffr
# destination model:  Cffr, CffrState

# HOWTO:
# 1) Ensure that CffrRaw, CffrProgram, State, County is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_cffr"

#to run the process for all years, set load_this_year to ''
load_this_year = ''

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
            
        def get_state(**lookup):
            state_ref_current = State.objects.get(**lookup)
            return state_ref_current
            
        def get_county(**lookup):
            county_ref_current = County.objects.get(**lookup)
            return county_ref_current
            
        def get_program(**lookup):
            program_ref_current = CffrProgram.objects.get(**lookup)
            return program_ref_current
        
        def load_year(year_current):
            record_count = 0
            error_count = 0
            skip_count = 0
            state_saved = ''
            county_saved = ''
            program_saved = ''
            
            records_current = Cffr.objects.filter(year=year_current).count()
            #if we already have records loaded for this year, skip it
            if records_current == 0:
            
                fields=['year', 'state_code', 'county_code', 'program_code']
                statelookup = {}
                countylookup = {}
                programlookup = {}
                for p in CffrRaw.objects.filter(year=year_current).values(*fields).annotate(total=Sum('amount_adjusted')).order_by('state_code', 'county_code', 'program_code'):
                    
                    state_code = p['state_code']
                    county_code = p['county_code']
                    program_code = p['program_code']
              
                    try:
                        if state_saved != state_code:
                            statelookup['state_ansi'] = state_code
                            state_ref_current = get_state(**statelookup)
                            state_saved = state_code
                            countylookup['county_ansi'] = county_code
                            countylookup['state'] = state_ref_current.id
                            county_ref_current = get_county(**countylookup)
                            county_saved = county_code
                        if county_saved != county_code:
                            countylookup['county_ansi'] = county_code
                            countylookup['state'] = state_ref_current.id
                            county_ref_current = get_county(**countylookup)
                            county_saved = county_code
                        if program_saved != program_code:
                            programlookup['year'] = year_current
                            programlookup['program_code'] = program_code
                            program_ref_current = get_program(**programlookup)
                    except:
                        #in case a CFFR record comes thru with a state, county, or program code that doesn't have a match in the corresponding reference data
                        skip_count = skip_count + 1
                        print 'Record skipped. ' + str(year_current) + ' state=' + state_code + ' county=' + county_code + ' program=' + program_code
                        continue
                        
                    record = Cffr(year=year_current, state=state_ref_current, county=county_ref_current, cffrprogram=program_ref_current, amount=p['total'])
                
                    try:
                        record.save()
                        db.reset_queries()
                        record_count = record_count + 1
                        try:
                            print str(year_current) + ' state=' + state_code + ' county=' + county_code + ' program=' + program_code + ' amount=' + str(p['total'])
                        except:
                            print 'cffr record loaded'
                    except:
                        print 'Failed load for ' + str(year_current) + ' state=' + state_code + ' county=' + county_code + ' program=' + program_code
                        error_count = error_count + 1
                        
                print str(year_current) + ': ' + str(record_count) + ' records loaded. ' + str(skip_count) + ' records skipped. Number of errors was ' + str(error_count) + '.'
                
            else:
                print str(records_current) + ' Cffr records already loaded for ' + str(year_current) + '. No ' + str(year_current) + ' will be loaded.'
                
        def load_year_state(year_current):
            record_count = 0
            error_count = 0
            skip_count = 0
            state_saved = ''
            program_saved = ''
            
            records_current = CffrState.objects.filter(year=year_current).count()
            #if we already have records loaded for this year, skip it
            if records_current == 0:
                fields = ['year', 'state', 'cffrprogram']
                statelookup = {}
                programlookup = {}
                state_totals = Cffr.objects.filter(year=year_current).values(*fields).annotate(amount=Sum('amount')).order_by('state', 'cffrprogram')
                for s in state_totals:
                    state_id = s['state']
                    program_id = s['cffrprogram']
              
                    try:
                        if state_saved != state_id:
                            statelookup['id'] = state_id
                            state_ref_current = get_state(**statelookup)
                            state_saved = state_id
                        if program_saved != program_id:
                            programlookup['year'] = year_current
                            programlookup['id'] = program_id
                            program_ref_current = get_program(**programlookup)
                            
                    except:
                        skip_count = skip_count + 1
                        print 'Record skipped. ' + str(year_current) + ' state=' + str(state_id) + ' program=' + str(program_id)
                        continue
                
                    record = CffrState(year=year_current, state=state_ref_current, cffrprogram = program_ref_current, amount=s['amount'])
                    
                    try:
                        record.save()
                        db.reset_queries()
                        record_count = record_count + 1
                        try:
                            print str(year_current) + ' state=' + state_ref_current.state_ansi + ' program=' + program_ref_current.program_code + ' amount=' + str(s['amount'])
                        except:
                            print 'cffrstate loaded'
                    except:
                        print 'Failed load for ' + str(year_current) + ' state=' + state_ref_current.state_ansi + ' program=' + program_ref_current.program_code
                        error_count = error_count + 1
                    
            else:
                print str(records_current) + ' CffrState records already loaded for ' + str(year_current) + '. No ' + str(year_current) + ' will be loaded.'
                
        if load_this_year:    
            load_year(load_this_year)
            load_year_state(load_this_year)
        else:
            for y in CffrRaw.objects.values('year').distinct():
                year_current = y['year']
                load_year(year_current)
                load_year_state(year_current)
        
        
