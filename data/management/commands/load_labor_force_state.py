from django import db
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import State, LaborForceStateRaw, LaborForceState

# National Priorities Project Data Repository
# load_labor_force_state.py 
# Created 4/26/2012

# Populates Labor Force State model used by the API
# source model(s): LaborForceStateRaw, State
# source load command(s): load_labor_force_state
# destination model:  LaborForceState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_labor_force_state

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        fips = ''
        insert_count = 0
        update_count = 0
        
        raw = LaborForceStateRaw.objects.all().order_by('area_fips')
        
        for r in raw:
        
            if len(r.area_fips) == 2 and r.area.lower().find('county') == -1 and r.area.lower().find('city') == -1:
                if r.area_fips != fips:
                    try:
                        state_ref_current = State.objects.get(state_ansi=r.area_fips)
                    except:
                        print 'Skipping record. Unable to find state fips: ' + r.area_fips
                        continue
                    fips = r.area_fips
            else:
                #skip this record--it represents a metro area or other non-state area
                continue

            try:
                record = LaborForceState.objects.get(
                    state=state_ref_current,year=r.year)
                update_count = update_count + 1
            except MultipleObjectsReturned:
                print 'error: multiple records exist for %s %s' % (
                    r.year, r.area_fips)
                continue
            except:
                insert_count = insert_count + 1
                record = LaborForceState(year=r.year,
                    state=state_ref_current)

            record.civilian_noninstitutional_pop = r.civilian_noninstitutional_pop
            record.labor_force_total = r. labor_force_total
            record.labor_force_participation_rate = r.labor_force_participation_rate
            record.employment_total = r.employment_total
            record.employment_pop_rate = r.employment_pop_rate
            record.unemployment_total = r.unemployment_total
            record.unemployment_rate = r.unemployment_rate
            record.save()
            db.reset_queries()
                        
        print 'state labor force load complete. %s records updated, %s inserted' % (
                    update_count, insert_count)
