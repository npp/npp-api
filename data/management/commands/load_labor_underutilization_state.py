from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, LaborUnderutilizationStateRaw, LaborUnderutilizationState

# National Priorities Project Data Repository
# load_labor_underutilization_state.py 
# Created 9/12/2011

# Populates Labor Underutilization used by the API
# source model(s): LaborUnderutilizationStateRaw, State
# destination model:  LaborUnderutilizationState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py labor_underutilization_state

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        state_name = ''
        total_inserts = 0
        total_updates = 0
        
        underutilization = LaborUnderutilizationStateRaw.objects.all().order_by('state')
        total_raw = underutilization.count()
        
        for u in underutilization:
        
            if u.state != state_name:
                try:
                    state_ref_current = State.objects.get(state_name=u.state)
                except:
                    print 'Skipping record. Unable to find state: ' + u.state
                    continue
                state_name = u.state
                
            try:
                record = LaborUnderutilizationState.objects.get(year=u.year,state=state_ref_current)
                total_updates = total_updates + 1
            except:
                record = LaborUnderutilizationState(year = u.year, state = state_ref_current)
                total_inserts = total_inserts + 1
            record.u1 = u.u1
            record.u2 = u.u2
            record.u3 = u.u3
            record.u4 = u.u4
            record.u5 = u.u5
            record.u6 = u.u6
                
            record.save()
            db.reset_queries()
                
        print 'Labor Underutilization: total records from raw data = ' + str(total_raw)
        print 'Labor Underutilization: total inserts = ' + str(total_inserts)
        print 'Labor Underutilization: total updates = ' + str(total_updates)