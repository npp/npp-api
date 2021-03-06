from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, SnapParticipationHouseholdsStateRaw, SnapParticipationHouseholdsState
from npp_api.data.utils import clean_state_name

# National Priorities Project Data Repository
# load_snap_participation_households_state
# Created 05/15/2012

# Populates SNAP household participation used by the API
# source model(s): SnapParticipationHouseholdsStateRaw, State
# source load command(s): import_snap_participation_households
# destination model:  SnapParticipationHouseholdsState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_snap_participation_households_state

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        state_name = ''
        total_inserts = 0
        total_updates = 0
        
        raw = SnapParticipationHouseholdsStateRaw.objects.all().order_by('state')
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
                record = SnapParticipationHouseholdsState.objects.get(year=r.year,state=state_ref_current)
                total_updates = total_updates + 1
            except:
                record = SnapParticipationHouseholdsState(year = r.year, state = state_ref_current)
                total_inserts = total_inserts + 1
            record.value = r.value
            record.save()
            db.reset_queries()
                
        print 'SNAP Household Participation (state): total records from raw data = %s' % total_raw
        print 'SNAP Household Participation (state): total inserts = %s' % total_inserts
        print 'SNAP Household Participation (state): total updates = %s' % total_updates