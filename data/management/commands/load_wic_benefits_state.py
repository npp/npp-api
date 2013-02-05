from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, WicBenefitsStateRaw, WicBenefitsState
from npp_api.data.utils import clean_state_name

# National Priorities Project Data Repository
# load_wic_benefits_state.py 
# Created 7/11/2011

# Populates Wic Benefits used by the API
# source model(s): WicBenefitsStateRaw
# source load command(s): import_wic_benefits_state
# destination model:  WicBenefitsState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_wic_benefits_state"

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        state_name = ''
        total_inserts = 0
        total_updates = 0
        
        wic = WicBenefitsStateRaw.objects.filter(type='total').order_by('state')
        total_raw = wic.count()
        
        for w in wic:
            if w.state != state_name:
                clean_state = clean_state_name(w.state)
                try:
                    state_ref_current = State.objects.get(state_name__iexact=clean_state)
                except:
                    print 'Skipping record. Unable to find state: %s' % clean_state
                    continue
                state_name = w.state
                
            try:
                record = WicBenefitsState.objects.get(year = w.year, state = state_ref_current)
                record.amount = w.value
                record.save()
                total_updates = total_updates + 1
            except:
                record = WicBenefitsState(year = w.year, state = state_ref_current, amount = w.value)
                record.save()
                total_inserts = total_inserts + 1
            db.reset_queries()
                
        print 'total records from raw data = %s' % total_raw
        print 'total inserts = %s' % total_inserts
        print 'total_updates = %s' % total_updates
