from django import db
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import State, Msn, EnergyConsumptionStateRaw, EnergyConsumptionState

# National Priorities Project Data Repository
# load_energy_consumption_state.py 
# Created 4/17/2012

# Populates Energy Consumption model used by the API
# source model(s): EnergyConsumptionStateRaw, State, Msn
# source load command(s): import_energy_consumption
# destination model:  EnergyConsumptionState

# HOWTO:
# 1) Ensure that State and Msn are loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_energy_consumption_state

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        state_abbr = ''
        insert_count = 0
        update_count = 0
        unchanged_count = 0
        
        #create dictionary of msn codes & their corresponding object so we
        #don't have to keep hitting the db to look this up
        msn = Msn.objects.all()
        msn_dict = {}
        for i, obj in enumerate(msn):
            msn_dict[obj.msn_code] = obj
        
        #arbitrary decision to load only 1990 and forward (b/c we're 
        #trying to get this published quickly)
        raw = EnergyConsumptionStateRaw.objects.filter(year__gt=1989).order_by('state')
        
        for r in raw:
        
            if r.state != state_abbr:
                try:
                    state_ref_current = State.objects.get(state_abbr=r.state)
                except:
                    print 'Skipping record. Unable to find state: ' + r.state
                    continue
                state_abbr = r.state
                
            try:
                msn_ref = msn_dict[r.msn]
            except:
                print 'Unable to find msn entry for msn code %s. Skipping entry' % r.msn
                continue
                        
            try:
                record = EnergyConsumptionState.objects.get(
                    state=state_ref_current,year=r.year,msn=msn_ref)
                if record.value <> r.value:
                    record.value = r.value
                    record.save()
                    db.reset_queries()
                    update_count = update_count + 1
                else:
                    unchanged_count = unchanged_count + 1
            except MultipleObjectsReturned:
                print 'error: multiple records exist for %s %s %s' % (
                    r.year, r.state, r.msn)
                continue
            except:
                record = EnergyConsumptionState(year=r.year,
                    state=state_ref_current,msn=msn_ref,
                    value=r.value)
                record.save()
                db.reset_queries()
                insert_count = insert_count + 1
                        
        print 'EnergyConsumptionState load complete. %s records updated, %s inserted, %s unchanged' % (
                    update_count, insert_count, unchanged_count)
