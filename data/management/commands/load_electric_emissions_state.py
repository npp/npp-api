from django import db
from django.db import transaction
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import State, Msn, ElectricEmissionsStateRaw, ElectricEmissionsState

# National Priorities Project Data Repository
# load_electric_emissions_state.py 
# Created 4/20/2012

# Populates Electric Emissions model used by the API
# source model(s): EnergyProductionStateRaw, State, Msn
# source load command(s): import_electric_emissions
# destination model:  ElectricEmissionsState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_electric_emissions_state"

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    @transaction.commit_on_success
    def handle_noargs(self, **options):
    
        state_abbr = ''
        insert_count = 0
        update_count = 0
        unchanged_count = 0

        raw = ElectricEmissionsStateRaw.objects.all().order_by('state')
        
        for r in raw:
        
            if r.state != state_abbr:
                try:
                    state_ref_current = State.objects.get(state_abbr=r.state)
                except:
                    print 'Skipping record. Unable to find state: ' + r.state
                    continue
                state_abbr = r.state
  
            try:
                record = ElectricEmissionsState.objects.get(
                    state=state_ref_current,
                    year = r.year,
                    producer_type = r.producer_type,
                    energy_source = r.energy_source)
                if record.co2 <> r.co2 or record.so2 <> r.so2 or record.nox <> r.nox:
                    record.co2 = r.co2
                    record.so2 = r.so2
                    record.nox = r.nox
                    record.save()
                    db.reset_queries()
                    update_count = update_count + 1
                else:
                    unchanged_count = unchanged_count + 1
            except MultipleObjectsReturned:
                print 'error: multiple records exist for %s %s %s %s' % (
                    r.year, r.state, r.producer_type, r.energy_source)
                continue
            except:
                record = ElectricEmissionsState(year=r.year,
                    state=state_ref_current,
                    producer_type = r.producer_type, 
                    energy_source = r.energy_source,
                    co2 = r.co2,
                    so2 = r.so2,
                    nox = r.nox)
                record.save()
                db.reset_queries()
                insert_count = insert_count + 1
                        
        print 'EnergyProductionState load complete. %s records updated, %s inserted, %s unchanged' % (
                    update_count, insert_count, unchanged_count)
