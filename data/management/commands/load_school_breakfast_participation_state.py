from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, SchoolBreakfastParticipationStateRaw, SchoolBreakfastParticipationState
from npp_api.data.utils import clean_state_name

# National Priorities Project Data Repository
# load_school_breakfast_participation_state
# Created 5/15/2012

# Populates School Breakfast Participation used by the API
# source model(s): SchoolBreakfastParticipationStateRaw, State
# source load command(s): import_school_breakfast_participation
# destination model:  SchoolBreakfastParticipationState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_school_breakfast_participation_state

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        state_name = ''
        total_inserts = 0
        total_updates = 0
        
        raw = SchoolBreakfastParticipationStateRaw.objects.all().order_by('state')
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
                record = SchoolBreakfastParticipationState.objects.get(year=r.year,state=state_ref_current)
                total_updates = total_updates + 1
            except:
                record = SchoolBreakfastParticipationState(year = r.year, state = state_ref_current)
                total_inserts = total_inserts + 1
            record.value = r.value
            record.save()
            db.reset_queries()
                
        print 'School Breakfast Participation (state): total records from raw data = %s' % total_raw
        print 'School Breakfast Participation (state): total inserts = %s' % total_inserts
        print 'School Breakfast Participation (state): total updates = %s' % total_updates