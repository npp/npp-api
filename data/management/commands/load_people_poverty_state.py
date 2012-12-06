from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, PeoplePovertyState, PeoplePovertyStateRaw
from npp_api.data.utils import clean_state_name

# National Priorities Project Data Repository
# load_people_poverty_state
# Created 12/6/2012

# Populates People In Poverty Table used by the API
# source model(s): PeoplePovertyStateRaw, State
# source load command(s): import_people_poverty
# destination model:  PeoplePovertyState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_people_poverty_state

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        state_name = ''
        total_inserts = 0
        total_updates = 0
        
        raw = PeoplePovertyStateRaw.objects.all().order_by('state')
        total_raw = raw.count()
        
        for r in raw:
        
            if r.state != state_name:
                clean_state = clean_state_name(r.state)
                try:
                    state_ref_current = State.objects.get(state_name=clean_state)
                except:
                    print 'Skipping record. Unable to find state: ' + clean_state
                    continue
                state_name = r.state
            
            try:
                record = PeoplePovertyState.objects.get(year=r.year,state=state_ref_current)
                total_updates = total_updates + 1
            except:
                record = PeoplePovertyState(year = r.year, state = state_ref_current)
                total_inserts = total_inserts + 1
            record.total_population = r.total_population
            record.value = r.value
            record.value_standard_error = r.value_standard_error
            record.percent = r.percent
            record.percent_standard_error = r.percent_standard_error
            record.save()
            db.reset_queries()
                
        print 'People In Poverty (state): total records from raw data = %s' % total_raw
        print 'People In Poverty (state): total inserts = %s' % total_inserts
        print 'People In Poverty (state): total updates = %s' % total_updates