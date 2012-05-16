from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, SnapMonthlyBenefitsPersonStateRaw, SnapMonthlyBenefitsPersonState

# National Priorities Project Data Repository
# load_snap_monthly_benefits_person_state
# Created 05/15/2012

# Populates SNAP household participation used by the API
# source model(s): SnapMonthlyBenefitsPersonStateRaw, State
# source load command(s): import_snap_monthly_benefits_person
# destination model:  SnapMonthlyBenefitsPersonState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_snap_monthly_benefits_person_state

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        state_name = ''
        total_inserts = 0
        total_updates = 0
        
        raw = SnapMonthlyBenefitsPersonStateRaw.objects.all().order_by('state')
        total_raw = raw.count()
        
        for r in raw:
        
            if r.state != state_name:
                try:
                    if r.state.lower().find('virgin islands') > -1:
                        r.state = 'U.S. Virgin Islands'
                    state_ref_current = State.objects.get(state_name=r.state)
                except:
                    print 'Skipping record. Unable to find state: %s' % r.state
                    continue
                state_name = r.state
            
            try:
                record = SnapMonthlyBenefitsPersonState.objects.get(year=r.year,state=state_ref_current)
                total_updates = total_updates + 1
            except:
                record = SnapMonthlyBenefitsPersonState(year = r.year, state = state_ref_current)
                total_inserts = total_inserts + 1
            record.value = r.value
            record.save()
            db.reset_queries()
                
        print 'SNAP Monthly Benefits/Person (state): total records from raw data = %s' % total_raw
        print 'SNAP Monthly Benefits/Person (state): total inserts = %s' % total_inserts
        print 'SNAP Monthly Benefits/Person (state): total updates = %s' % total_updates