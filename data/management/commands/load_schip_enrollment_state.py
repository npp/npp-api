from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, SchipEnrollmentStateRaw, SchipEnrollmentState

# National Priorities Project Data Repository
# load_schip_enrollment_state.py 
# Created 5/7/2012

# Populates Schip Enrollment model used by the API
# source model(s): SchipEnrollmentStateRaw
# source load command(s): import_schip_enrollment_state
# destination model:  SchipEnrollmentState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_schip_enrollment_state

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        state_name = ''
        insert_count = 0
        update_count = 0
        unchanged_count = 0
        
        raw = SchipEnrollmentStateRaw.objects.all().order_by('state')
        total_raw = raw.count()
        
        for r in raw:
            if r.state != state_name:
                try:
                    state_ref_current = State.objects.get(state_name__iexact=r.state)
                except:
                    print 'Skipping record. Unable to find state: ' + r.state
                    continue
                state_name = r.state
            try:
                record = SchipEnrollmentState.objects.get(
                    year = r.year, state = state_ref_current)
                if record.value == r.value:
                    unchanged_count = unchanged_count + 1
                else:
                    record.value = r.value
                    record.save()
                    update_count = update_count + 1
            except:
                record = SchipEnrollmentState()
                record.year = r.year
                record.state = state_ref_current
                record.value = r.value
                record.save()
                insert_count = insert_count + 1
            db.reset_queries()
                
        print 'SCHIP Enrollment load complete. %s inserted, %s updated, %s unchanged' % (insert_count, update_count, unchanged_count)
        print 'total records from raw data = ' + str(total_raw)
