from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, WicParticipationStateRaw, WicParticipationState

# National Priorities Project Data Repository
# load_wic_participation_state.py 
# Created 7/11/2011

# Populates Wic Benefits used by the API
# source model(s): WicParticipationStateRaw
# source load command(s): import_wic_participation_state
# destination model:  WicParticipationState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_wic_participation_state

# Safe to rerun: no

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        state_name = ''
        total_inserts = 0
        
        wic = WicParticipationStateRaw.objects.filter(type='total').order_by('state')
        total_raw = wic.count()
        
        for w in wic:
            if w.state != state_name:
                try:
                    state_ref_current = State.objects.get(state_name=w.state)
                except:
                    print 'Skipping record. Unable to find state: ' + w.state
                    continue
            state_name = w.state
            record = WicParticipationState(year = w.year, state = state_ref_current, value = w.value)
            record.save()
            db.reset_queries()
            total_inserts = total_inserts + 1
                
        print 'total records from raw data = ' + str(total_raw)
        print 'total inserts = ' + str(total_inserts)
