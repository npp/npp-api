from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, HousingOccupancyStateRaw, HousingOccupancyState
from npp_api.data.utils import clean_num, get_percent, get_proportion_moe

# National Priorities Project Data Repository
# load_housing_occupancy.py 
# Created 5/24/2012

# Populates Housing Occupancy used by the API
# source model(s): HousingOccupancyStateRaw, State
# source load command(s): import_housing_occupancy
# destination model:  HousingOccupancyState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_median_housing_occupancy"

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        state_fips = ''
        total_inserts = 0
        total_updates = 0
        
        raw = HousingOccupancyStateRaw.objects.all().order_by('state_fips')
        total_raw = raw.count()
        
        for r in raw:
        
            if r.state_fips != state_fips:
                try:
                    state_ref_current = State.objects.get(state_ansi=r.state_fips)
                except:
                    print 'Skipping record. Unable to find state: ' + r.state
                    continue
                state_fips = r.state_fips
            
            try:
                record = HousingOccupancyState.objects.get(year=r.year,state=state_ref_current)
                total_updates = total_updates + 1
            except:
                record = HousingOccupancyState(year = r.year, state = state_ref_current)
                total_inserts = total_inserts + 1
                
            record.total_units = r.total_units
            if str(r.total_units_moe).find('*****') > -1:
                record.total_units_moe = 0
            else:
                record.total_units_moe = clean_num(r.total_units_moe)
            record.occupied_units = r.occupied_units
            record.occupied_units_moe = clean_num(r.occupied_units_moe)
            if r.occupied_units_percent is not None:
                record.occupied_units_percent = r.occupied_units_percent
                record.occupied_units_percent_moe = clean_num(r.occupied_units_percent_moe)
            else:
                record.occupied_units_percent = get_percent(
                    record.occupied_units, record.total_units)
                record.occupied_units_percent_moe = get_proportion_moe(
                    record.occupied_units, record.total_units, 
                    record.occupied_units_moe, record.total_units_moe) * 100
            record.vacant_units = r.vacant_units
            record.vacant_units_moe = clean_num(r.vacant_units_moe)
            if r.vacant_units_percent is not None:
                record.vacant_units_percent = r.vacant_units_percent
                record.vacant_units_percent_moe = clean_num(r.vacant_units_percent_moe)
            else:
                record.vacant_units_percent = get_percent(
                    record.vacant_units, record.total_units)
                record.vacant_units_percent_moe = get_proportion_moe(
                    record.vacant_units, record.total_units, 
                    record.vacant_units_moe, record.total_units_moe) * 100
            record.owner_vacancy_rate = r.owner_vacancy_rate
            record.owner_vacancy_rate_moe = clean_num(r.owner_vacancy_rate_moe)
            record.renter_vacancy_rate = r.renter_vacancy_rate
            record.renter_vacancy_rate_moe = clean_num(r.renter_vacancy_rate_moe)
            record.owner_occupied = r.owner_occupied
            record.owner_occupied_moe = clean_num(r.owner_occupied_moe)
            if r.owner_occupied_percent is not None:
                record.owner_occupied_percent = r.owner_occupied_percent
                record.owner_occupied_percent_moe = clean_num(r.owner_occupied_percent_moe)
            else:
                record.owner_occupied_percent = get_percent(
                    record.owner_occupied, record.occupied_units)
                record.owner_occupied_percent_moe = get_proportion_moe(
                    record.owner_occupied, record.occupied_units, 
                    record.owner_occupied_moe, record.occupied_units_moe) * 100
            record.renter_occupied = r.renter_occupied
            record.renter_occupied_moe = clean_num(r.renter_occupied_moe)
            if r.renter_occupied_percent is not None:
                record.renter_occupied_percent = r.renter_occupied_percent
                record.renter_occupied_percent_moe = clean_num(r.renter_occupied_percent_moe)
            else:
                record.renter_occupied_percent = get_percent(
                    record.renter_occupied, record.occupied_units)
                record.renter_occupied_percent_moe = get_proportion_moe(
                    record.renter_occupied, record.occupied_units,
                    record.renter_occupied_moe, record.occupied_units_moe) * 100
            record.save()
            db.reset_queries()
                
        print 'Housing Occupancy (state): total records from raw data = ' + str(total_raw)
        print 'Housing Occupancy (state): total inserts = ' + str(total_inserts)
        print 'Housing Occupancy (state): total updates = ' + str(total_updates)