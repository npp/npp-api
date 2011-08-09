from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, PupilTeacherStateRaw, PupilTeacherState

# National Priorities Project Data Repository
# load_pupil_teacher_state.py 
# Created 8/5/2011

# Populates Pupil Teacher data used by the API
# source model(s): PupilTeacherStateRaw, PupilTeacherState, State
# source load command(s): import_pupil_teacher
# destination model:  PupilTeacherState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_pupil_teacher_state

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        state_name = ''
        total_inserts = 0
        total_updates = 0
        
        data = PupilTeacherStateRaw.objects.all().order_by('state')
        total_raw = data.count()
        
        for d in data:
        
            if d.state != state_name:
                try:
                    state_ref_current = State.objects.get(state_abbr=d.state)
                except:
                    print 'Skipping record. Unable to find state: ' + d.state
                    continue
                state_name = d.state
                
            try:
                record = PupilTeacherState.objects.get(year=d.year,state=state_ref_current)
                record.ratio = d.ratio
                total_updates = total_updates + 1
            except:
                record = PupilTeacherState(year = d.year, state = state_ref_current, ratio = d.ratio)
                total_inserts = total_inserts + 1
                
            record.save()
            db.reset_queries()
                
        print 'Pupil/Teacher: total records from raw data = ' + str(total_raw)
        print 'Pupil/Teacher: total inserts = ' + str(total_inserts)
        print 'Pupil/Teacher: total updates = ' + str(total_updates)
