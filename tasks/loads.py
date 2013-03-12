from fabric.api import *
from fabtasktic.tasks import run_command

@task
def loads(taskname=None):
    '''
    fab staging loads.loads:taskname                Runs task indicated in taskname
    '''
    if taskname is None:
        raise ValueError('Missing Task Name.  ex - fab staging loads.loads:taskname')
    run_command(taskname)

@task
def age_group():
    '''
    fab staging loads.age_group                     Loads Age Group
    '''
    run_command('load_age_group')

@task
def cfda():
    '''
    fab staging loads.cfda                          Loads Catalog of Federal Domestic Assistance (CFDA)
    '''
    run_command('load_cfda')

@task
def cffr():
    '''
    fab staging loads.cffr                          Loads CFFR
    '''
    run_command('load_cffr')
    
@task
def cffr_per_capita(year = None):
    '''
    fab staging loads.cffr_per_capita:year                          Refreshes CFFR Per-Capita Calculations
    '''
    if year is None:
        raise ValueError('Missing year')
    run_command('load_cffr_per_capita %s' % year)

@task
def cffr_program():
    '''
    fab staging loads.cffr_program                  Loads CFFR Program
    '''
    run_command('load_cffr_program')

@task
def county():
    '''
    fab staging loads.county                        Loads County
    '''
    run_command('load_county')

@task
def electric_emissions_state():
    '''
    fab staging loads.electric_emissions_state      Loads Electric Emissions By State
    '''
    run_command('load_electric_emissions_state')

@task
def energy_consumption_state():
    '''
    fab staging loads.energy_consumption_state      Loads Energy Consumption By State
    '''
    run_command('load_energy_consumption_state')

@task
def energy_production_state():
    '''
    fab staging loads.energy_production_state       Loads Energy Production By State
    '''
    run_command('load_energy_production_state')

@task
def ethnicity():
    '''
    fab staging loads.ethnicity                     Loads Ethnicity
    '''
    run_command('load_ethnicity')

@task
def federal_tax_collection_state():
    '''
    fab staging loads.federal_tax_collection_state  Loads Federal Tax Collection By State
    '''
    run_command('load_federal_tax_collection_state')

@task
def food_security_state():
    '''
    fab staging loads.food_security_state           Loads Food Security By State
    '''
    run_command('load_food_security_state')

@task
def gender():
    '''
    fab staging loads.gender                        Loads Gender
    '''
    run_command('load_gender')
    
@task
def health_insurance_state():
    '''
    fab staging loads.health_insurance_state        Loads Health Insurance By State
    '''
    run_command('load_health_insurance_state')

@task
def housing_occupancy_state():
    '''
    fab staging loads.housing_occupancy_state       Loads Housing Occupancy By State
    '''
    run_command('load_housing_occupancy_state')

@task
def labor_force_county():
    '''
    fab staging loads.labor_force_county            Loads Labor Force By County
    '''
    run_command('load_labor_force_county')

@task
def labor_force_state():
    '''
    fab staging loads.labor_force_state             Loads Labor Force By State
    '''
    run_command('load_labor_force_state')

@task
def labor_underutilization_state():
    '''
    fab staging loads.labor_underutilization_state  Loads Labor Under-utilization By State
    '''
    run_command('load_labor_underutilization_state')

@task
def median_income_state():
    '''
    fab staging loads.median_income_state           Loads Median Income By State
    '''
    run_command('load_median_income_state')

@task
def population_age_county():
    '''
    fab staging loads.population_age_county         Loads Population Age By County
    '''
    run_command('load_population_age_county')

@task
def population_age_state():
    '''
    fab staging loads.population_age_state          Loads Population Age By State
    '''
    run_command('load_population_age_state')

@task
def population_gender_county():
    '''
    fab staging loads.population_gender_county      Loads Population Gender By County
    '''
    run_command('load_population_gender_county')

@task
def population_gender_state():
    '''
    fab staging loads.population_gender_state       Loads Population Gender By State
    '''
    run_command('load_population_gender_state')

@task
def population_race_county():
    '''
    fab staging loads.population_race_county        Loads Population Race By County
    '''
    run_command('load_population_race_county')

@task
def population_race_state():
    '''
    fab staging loads.population_race_state         Loads Population Race By State
    '''
    run_command('load_population_race_state')

@task
def pupil_teacher_state():
    '''
    fab staging loads.pupil_teacher_state           Loads Pupils per Teacher By State
    '''
    run_command('load_pupil_teacher_state')

@task
def race():
    '''
    fab staging loads.race                          Loads Race
    '''
    run_command('load_race')

@task
def race_combo():
    '''
    fab staging loads.race_combo                    Loads Race Combo
    '''
    run_command('load_race_combo')

@task
def schip_enrollment_state():
    '''
    fab staging loads.schip_enrollment_state        Loads SCHIP Enrollment By State
    '''
    run_command('load_schip_enrollment_state')

@task
def school_breakfast_participation_state():
    '''
    fab staging loads.school_breakfast_participation_state  Loads School Breakfast Participation By State
    '''
    run_command('load_school_breakfast_participation_state')

@task
def school_lunch_participation_state():
    '''
    fab staging loads.school_lunch_participation_state      Loads School Lunch Participation By State
    '''
    run_command('load_school_lunch_participation_state')

@task
def snap_monthly_benefits_person_state():
    '''
    fab staging loads.snap_monthly_benefits_person_state    Loads SNAP Monthly Benefits Per Person By State
    '''
    run_command('load_snap_monthly_benefits_person_state')

@task
def snap_participation_households_state():
    '''
    fab staging loads.snap_participation_households_state   Loads SNAP Participation Households By State
    '''
    run_command('load_snap_participation_households_state')

@task
def snap_participation_people_state():
    '''
    fab staging loads.snap_participation_people_state       Loads SNAP Participation People By State
    '''
    run_command('load_snap_participation_people_state')

@task
def state():
    '''
    fab staging loads.state                         Loads State Reference
    '''
    run_command('load_state')

@task
def summer_lunch_participation_state():
    '''
    fab staging loads.summer_lunch_participation_state      Loads Summer Lunch Participation By State
    '''
    run_command('load_summer_lunch_participation_state')

@task
def tanf_participation_state():
    '''
    fab staging loads.tanf_participation_state      Loads TANF Participation By State
    '''
    run_command('load_tanf_participation_state')

@task
def usaspending_assistance(year = None):
    '''
    fab staging loads.usaspending_assistance        Loads USASpending Assistance by State/County
    '''
    if year is None:
        run_command('load_usaspending_assistance')
    else:
        run_command('load_usaspending_assistance %s' % year)

@task
def wic_benefits_state():
    '''
    fab staging loads.wic_benefits_state            Loads WIC Benefits By State
    '''
    run_command('load_wic_benefits_state')

@task
def wic_participation_state():
    '''
    fab staging loads.wic_participation_state       Loads WIC Participation By State
    '''
    run_command('load_wic_participation_state')

