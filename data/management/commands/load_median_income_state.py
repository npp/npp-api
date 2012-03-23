from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, MedianHouseholdIncomeStateRaw, MedianIncomeState

# National Priorities Project Data Repository
# load_median_income.py 
# Created 03/23/2012

# Populates Median Income used by the API
# source model(s): MedianHouseholdIncomeStateRaw, State
# source load command(s): import_median_household_income
# destination model:  MedianIncomeState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_median_income_state

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        state_fips = ''
        total_inserts = 0
        total_updates = 0
        
        raw = MedianHouseholdIncomeStateRaw.objects.all().order_by('state_fips')
        total_raw = raw.count()
        
        for r in raw:
        
            if r.state_fips != state_fips:
                try:
                    state_ref_current = State.objects.get(state_ansi=r.state_fips)
                except:
                    print 'Skipping record. Unable to find state: ' + r.state
                    continue
                state_fips = r.state_fips
            
            try:
                record = MedianIncomeState.objects.get(year=r.year,state=state_ref_current)
                total_updates = total_updates + 1
            except:
                record = MedianIncomeState(year = r.year, state = state_ref_current)
                total_inserts = total_inserts + 1
            record.median_household_income = r.median_household_income
            record.median_household_income_moe = r.median_household_income_moe
            record.save()
            db.reset_queries()
                
        print 'Median Income (state): total records from raw data = ' + str(total_raw)
        print 'Median Income (state): total inserts = ' + str(total_inserts)
        print 'Median Income (state): total updates = ' + str(total_updates)