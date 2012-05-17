from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, TanfParticipationStateRaw, TanfFamilyStateRaw, TanfParticipationState
from npp_api.data.utils import clean_state_name

# National Priorities Project Data Repository
# load_tanf_participation_state.py 
# Created 8/5/2011

# Populates Tanf Participation used by the API
# source model(s): TanfParticipationStateRaw, TanfFamilyStateRaw, State
# source load command(s): import_tanf_participation_state
# destination model:  TanfParticipationState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_tanf_participation_state"

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        state_name = ''
        total_inserts = 0
        total_updates = 0
        
        person = TanfParticipationStateRaw.objects.all().order_by('state')
        total_raw = person.count()
        
        for t in person:
        
            if t.state != state_name:
                clean_state = clean_state_name(t.state)
                try:
                    state_ref_current = State.objects.get(state_name=clean_state)
                except:
                    print 'Skipping record. Unable to find state: ' + clean_state
                    continue
                state_name = t.state
                
            try:
                record = TanfParticipationState.objects.get(year=t.year,state=state_ref_current)
                record.person = t.value
                total_updates = total_updates + 1
            except:
                record = TanfParticipationState(year = t.year, state = state_ref_current, person = t.value)
                total_inserts = total_inserts + 1
                
            record.save()
            db.reset_queries()
                
        print 'TANF person: total records from raw data = ' + str(total_raw)
        print 'TANF person: total inserts = ' + str(total_inserts)
        print 'TANF person: total updates = ' + str(total_updates)
        
        #update records with info re: # families
        
        state_name = ''
        total_inserts = 0
        total_updates = 0
        state_ref_current = ''
        
        family = TanfFamilyStateRaw.objects.all().order_by('state')
        total_raw = family.count()
        
        for t in family:
        
            if t.state != state_name:
                clean_state = clean_state_name(t.state)
                try:
                    state_ref_current = State.objects.get(state_name=clean_state)
                except:
                    print 'Skipping record. Unable to find state: ' + clean_state
                    continue
                state_name = t.state
                
            try:
                record = TanfParticipationState.objects.get(year=t.year,state=state_ref_current)
                record.family = t.value
                total_updates = total_updates + 1
            except:
                record = TanfParticipationState(year = t.year, state = state_ref_current, family = t.value)
                total_inserts = total_inserts + 1
                
            record.save()
            db.reset_queries()
                
        print 'TANF family: total records from raw data = ' + str(total_raw)
        print 'TANF family: total inserts = ' + str(total_inserts)
        print 'TANF family: total updates = ' + str(total_updates)
