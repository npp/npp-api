from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, FoodSecurityStateRaw, FoodSecurityState
from npp_api.data.utils import get_percent

# National Priorities Project Data Repository
# load_food_security_state.py 
# Created 9/07/2011

# Populates Food Security/Insecurity data used by the API
# source model(s): FoodSecurityStateRaw
# destination model:  FoodSecurityState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_food_security_state

# Safe to rerun: no

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        state_name = ''
        total_inserts = 0
        
        food = FoodSecurityStateRaw.objects.order_by('state')
        total_raw = food.count()
        
        for f in food:
            if f.state != state_name:
                try:
                    state_ref_current = State.objects.get(state_abbr=f.state)
                except:
                    print 'Skipping record. Unable to find state: %s ' % f.state
                    continue
            state_name = f.state
            
            record = FoodSecurityState()
            record.year = f.year
            record.state = state_ref_current
            record.household_total = f.household_total
            record.no_response = f.no_response
            if f.year >= 2005:
                #high food security vs marginal food security differentiation only availabe in years >= 2005
                record.food_secure = f.food_secure_high + f.food_secure_marginal
                record.food_secure_high = f.food_secure_high
                record.food_secure_high_percent = get_percent(f.food_secure_high,f.household_total)
                record.food_secure_marginal = f.food_secure_marginal
                record.food_secure_marginal_percent = get_percent(f.food_secure_marginal,f.household_total)
            else:
                record.food_secure = f.food_secure
            record.food_secure_low = f.food_secure_low
            record.food_secure_low_percent = get_percent(f.food_secure_low,f.household_total)
            record.food_secure_very_low = f.food_secure_very_low
            record.food_secure_very_low_percent = get_percent(f.food_secure_very_low,f.household_total)
            record.food_secure_percent = get_percent(record.food_secure,f.household_total)
            record.food_insecure = f.food_secure_low + f.food_secure_very_low
            record.food_insecure_percent = get_percent(record.food_insecure,f.household_total)
            
            #print '%s %s %s %s' % (record.year, record.state.state_abbr, record.food_secure_percent, record.food_insecure_percent)
            record.save()
            db.reset_queries()
            total_inserts = total_inserts + 1
                
        print 'total records from raw data = ' + str(total_raw)
        print 'total inserts = ' + str(total_inserts)
