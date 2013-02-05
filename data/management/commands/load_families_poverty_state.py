from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, FamiliesPovertyState, FamiliesPovertyStateRaw
from npp_api.data.utils import clean_state_name

# National Priorities Project Data Repository
# load_families_poverty_state
# Created 12/6/2012

# Populates Families In Poverty Table used by the API
# source model(s): FamiliesPovertyStateRaw, State
# source load command(s): import_families_poverty
# destination model:  FamiliesPovertyState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_families_poverty_state

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        state_name = ''
        total_inserts = 0
        total_updates = 0
        
        raw = FamiliesPovertyStateRaw.objects.all().order_by('state')
        total_raw = raw.count()
        
        for r in raw:
        
            if r.state != state_name:
                clean_state = clean_state_name(r.state)
                try:
                    state_ref_current = State.objects.get(state_name__iexact=clean_state)
                except:
                    print 'Skipping record. Unable to find state: ' + clean_state
                    continue
                state_name = r.state
            
            try:
                record = FamiliesPovertyState.objects.get(year=r.year,state=state_ref_current)
                total_updates = total_updates + 1
            except:
                record = FamiliesPovertyState(year = r.year, state = state_ref_current)
                total_inserts = total_inserts + 1
            record.families_total = r.families_total
            record.families_total_moe = r.families_total_moe
            record.families_poverty_percent = r.families_poverty_percent
            record.families_poverty_percent_moe = r.families_poverty_percent_moe
            record.save()
            db.reset_queries()
                
        print 'Families In Poverty (state): total records from raw data = %s' % total_raw
        print 'Families In Poverty (state): total inserts = %s' % total_inserts
        print 'Families In Poverty (state): total updates = %s' % total_updates