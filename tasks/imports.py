from fabric.api import *
from fabtasktic.tasks import run_command

@task
def imports(taskname=None):
    '''
    fab staging imports.imports:taskname                Runs task indicated in taskname
    '''
    if taskname is None:
        raise ValueError('Missing Task Name.  ex - fab staging imports.imports:taskname')
    run_command(taskname)

@task
def alternative_fuel_vehicles():
    '''
    fab staging imports.alternative_fuel_vehicles       Import Alternative Fuel Vehicles
    '''
    run_command('import_alternative_fuel_vehicles')

@task
def ansi_country():
    '''
    fab staging imports.ansi_country                    Import ANSI Country
    '''
    run_command('import_ansi_country')

@task
def ansi_state():
    '''
    fab staging imports.ansi_state                      Import ANSI State
    '''
    run_command('import_ansi_state')

@task
def at_codes():
    '''
    fab staging imports.at_codes                        Import AT Codes
    '''
    run_command('import_at_codes')

@task
def average_teacher_salary():
    '''
    fab staging imports.average_teacher_salary          Import Average Teacher Salary
    '''
    run_command('import_average_teacher_salary')

@task
def bilingual_ed_spending():
    '''
    fab staging imports.bilingual_ed_spending           Import Bilingual Ed Spending
    '''
    run_command('import_bilingual_ed_spending')

@task
def budget_category_subfunctions():
    '''
    fab staging imports.budget_category_subfunctions    Import Budget Category Subfunctions
    '''
    run_command('import_budget_category_subfunctions')
@task

def cfda():
    '''
    fab staging imports.cfda                            Import Catalog of Federal Domestic Assistance (CFDA)
    '''
    run_command('import_cfda')

@task
def cffr_annual():
    '''
    fab staging imports.cffr_annual                     Import CFFR Annual
    '''
    run_command('import_cffr_annual')

@task
def cffr_annual_agency():
    '''
    fab staging imports.cffr_annual_agency              Import CFFR Annual Agency
    '''
    run_command('import_cffr_annual_agency')

@task
def cffr_annual_pre93():
    '''
    fab staging imports.cffr_annual_pre93               Import CFFR Annual Agency Pre '93
    '''
    run_command('import_cffr_annual_pre93')

@task
def cffr_annual_pre93_geo():
    '''
    fab staging imports.cffr_annual_pre93_geo           Import CFFR Annual Agency Pre '93 Geo
    '''
    run_command('import_cffr_annual_pre93_geo')

@task
def cffr_annual_prog():
    '''
    fab staging imports.cffr_annual_prog                Import CFFR Annual Prog.
    '''
    run_command('import_cffr_annual_prog')

@task
def cffr_object_codes():
    '''
    fab staging imports.cffr_object_codes               Import CFFR Object Codes
    '''
    run_command('import_cffr_object_codes')

@task
def children_poverty():
    '''
    fab staging imports.children_poverty                Import Children in Poverty
    '''
    run_command('import_children_poverty')

@task
def diploma_recipient_total():
    '''
    fab staging imports.diploma_recipient_total         Import Diploma Recipient Total
    '''
    run_command('import_diploma_recipient_total')

@task
def dropouts_race():
    '''
    fab staging imports.dropouts_race                   Import Dropouts Race
    '''
    run_command('import_dropouts_race')

@task
def drug_free_school_spending():
    '''
    fab staging imports.drug_free_school_spending       Import Drug Free School Spending
    '''
    run_command('import_drug_free_school_spending')

@task
def educational_attainment():
    '''
    fab staging imports.educational_attainment          Import Educational Attainment
    '''
    run_command('import_educational_attainment')

@task
def electric_emissions():
    '''
    fab staging imports.electric_emissions              Import Electric Emissions
    '''
    run_command('import_electric_emissions')

@task
def ell_students_district():
    '''
    fab staging imports.ell_students_district           Import ELL Students District
    '''
    run_command('import_ell_students_district')

@task
def employment():
    '''
    fab staging imports.employment                      Import Employment
    '''
    run_command('import_employment')

@task
def energy_consumption():
    '''
    fab staging imports.energy_consumption              Import Energy Consumption
    '''
    run_command('import_energy_consumption')

@task
def energy_expenditures_state_annual():
    '''
    fab staging imports.energy_expenditures_state_annual    Import Energy Expenditures State Annual
    '''
    run_command('import_energy_expenditures_state_annual')

@task
def energy_production():
    '''
    fab staging imports.energy_production               Import Energy Production
    '''
    run_command('import_energy_production')

@task
def energy_state_production_estimates():
    '''
    fab staging imports.energy_state_production_estimates   Import Energy State Production Estimates
    '''
    run_command('import_energy_state_production_estimates')

@task
def enrolled_students_district():
    '''
    fab staging imports.enrolled_students_district      Import Enrolled Students District
    '''
    run_command('import_enrolled_students_district')

@task
def enrollment_race():
    '''
    fab staging imports.enrollment_race                 Import Enrollment Race
    '''
    run_command('import_enrollment_race')

@task
def expenditure_per_pupil():
    '''
    fab staging imports.expenditure_per_pupil           Import Expenditure Per Pupil
    '''
    run_command('import_expenditure_per_pupil')

@task
def families_poverty():
    '''
    fab staging imports.families_poverty                Import Families Poverty
    '''
    run_command('import_families_poverty')

@task
def fcna_spending():
    '''
    fab staging imports.fcna_spending                   Import FCNA Spending
    '''
    run_command('import_fcna_spending')

@task
def federal_impact_aid():
    '''
    fab staging imports.federal_impact_aid              Import Federal Impact Aid
    '''
    run_command('import_federal_impact_aid')

@task
def federal_tax_collection():
    '''
    fab staging imports.federal_tax_collection          Import Federal Tax Collection
    '''
    run_command('import_federal_tax_collection')

@task
def fips_countycongressdistrict():
    '''
    fab staging imports.fips_countycongressdistrict     Import FIPS County/Congress/District
    '''
    run_command('import_fips_countycongressdistrict')

@task
def food_security():
    '''
    fab staging imports.food_security                   Import Food Security
    '''
    run_command('import_food_security')

@task
def free_lunch_eligible():
    '''
    fab staging imports.free_lunch_eligible             Import Free Lunch Eligible
    '''
    run_command('import_free_lunch_eligible')

@task
def free_reduced_lunch_eligible():
    '''
    fab staging imports.free_reduced_lunch_eligible     Import Free/Reduced Lunch Eligible
    '''
    run_command('import_free_reduced_lunch_eligible')

@task
def free_reduced_lunch_eligible_county():
    '''
    fab staging imports.free_reduced_lunch_eligible_county  Import Free/Reduced Lunch Eligible County
    '''
    run_command('import_free_reduced_lunch_eligible_county')

@task
def half_pints():
    '''
    fab staging imports.half_pints                      Import Half Pints
    '''
    run_command('import_half_pints')

@task
def head_start_enrollment():
    '''
    fab staging imports.head_start_enrollment           Import Head Start Enrollment
    '''
    run_command('import_head_start_enrollment')

@task
def health_insurance():
    '''
    fab staging imports.health_insurance                Import Health Insurance
    '''
    run_command('import_health_insurance')

@task
def health_insurance_children():
    '''
    fab staging imports.health_insurance_children       Import Health Insurance Children
    '''
    run_command('import_health_insurance_children')

@task
def high_school_other():
    '''
    fab staging imports.high_school_other               Import High School Other
    '''
    run_command('import_high_school_other')

@task
def housing_occupancy():
    '''
    fab staging imports.housing_occupancy               Import Housing Occupancy
    '''
    run_command('import_housing_occupancy')

@task
def housing_units():
    '''
    fab staging imports.housing_units                   Import Housing Units
    '''
    run_command('import_housing_units')

@task
def hs_dropouts():
    '''
    fab staging imports.hs_dropouts                     Import High School Dropouts
    '''
    run_command('import_hs_dropouts')

@task
def individual_education_programs():
    '''
    fab staging imports.individual_education_programs   Import Individual Education Programs
    '''
    run_command('import_individual_education_programs')

@task
def labor_force_county():
    '''
    fab staging imports.labor_force_county              Import Labor Force County
    '''
    run_command('import_labor_force_county')

@task
def labor_force_state():
    '''
    fab staging imports.labor_force_state               Import Labor Force State
    '''
    run_command('import_labor_force_state')

@task
def labor_underutilization():
    '''
    fab staging imports.labor_underutilization          Import Labor Under-utilization
    '''
    run_command('import_labor_underutilization')

@task
def math_science_spending():
    '''
    fab staging imports.math_science_spending           Import Math/Science Spending
    '''
    run_command('import_math_science_spending')

@task
def median_household_income():
    '''
    fab staging imports.median_household_income         Import Median Household Income
    '''
    run_command('import_median_household_income')

@task
def medicaid_participation():
    '''
    fab staging imports.medicaid_participation         Import Medicaid Participation
    '''
    run_command('import_medicaid_participation')

@task
def medicare_enrollment():
    '''
    fab staging imports.medicare_enrollment             Import Medicare Enrollment
    '''
    run_command('import_medicare_enrollment')

@task
def migrant_students():
    '''
    fab staging imports.migrant_students                Import Migrant Students
    '''
    run_command('import_migrant_students')

@task
def military_personnel():
    '''
    fab staging imports.military_personnel              Import Military Personnel
    '''
    run_command('import_military_personnel')

@task
def msn():
    '''
    fab staging imports.msn                             Import MSN
    '''
    run_command('import_msn')

@task
def native_ed_spending():
    '''
    fab staging imports.native_ed_spending              Import Native Ed. Spending
    '''
    run_command('import_native_ed_spending')

@task
def nces_sd_codes():
    '''
    fab staging imports.nces_sd_codes                   Import NCES SD Codes
    '''
    run_command('import_nces_sd_codes')

@task
def new_aids_cases():
    '''
    fab staging imports.new_aids_cases                  Import New Aids Cases
    '''
    run_command('import_new_aids_cases')

@task
def other_federal_revenue():
    '''
    fab staging imports.other_federal_revenue           Import Other Federal Revenue
    '''
    run_command('import_other_federal_revenue')

@task
def owners_renters():
    '''
    fab staging imports.owners_renters                  Import Owners/Renters
    '''
    run_command('import_owners_renters')

@task
def people_in_poverty():
    '''
    fab staging imports.people_in_poverty               Import People In Poverty
    '''
    run_command('import_people_in_poverty')

@task
def population_congressional_district():
    '''
    fab staging imports.population_congressional_district   Import Population By Cong. District
    '''
    run_command('import_population_congressional_district')

@task
def population_est_10():
    '''
    fab staging imports.population_est_10               Import Population Est '10
    '''
    run_command('import_population_est_10')
    
@task
def population_est_00():
    '''
    fab staging imports.population_est_00               Import Population Est '00
    '''
    run_command('import_population_est_00')

@task
def population_est_90():
    '''
    fab staging imports.population_est_90               Import Population Est '90
    '''
    run_command('import_population_est_90')

@task
def population_families():
    '''
    fab staging imports.population_families             Import Population Families
    '''
    run_command('import_population_families')

@task
def presidents_budget():
    '''
    fab staging imports.presidents_budget               Import President's Budget
    '''
    run_command('import_presidents_budget')

@task
def presidents_budget_receipts():
    '''
    fab staging imports.presidents_budget_receipts      Import President's Budget Receipts
    '''
    run_command('import_presidents_budget_receipts')

@task
def pupil_teacher():
    '''
    fab staging imports.pupil_teacher                   Import Pupil Per Teacher
    '''
    run_command('import_pupil_teacher')

@task
def pupil_teacher_district():
    '''
    fab staging imports.pupil_teacher_district          Import Pupil Per Teacher By District
    '''
    run_command('import_pupil_teacher_district')

@task
def retired_disabled_nilf():
    '''
    fab staging imports.retired_disabled_nilf           Import Retired/Disabled NILF
    '''
    run_command('import_retired_disabled_nilf')

@task
def saipe_county_state():
    '''
    fab staging imports.saipe_county_state              Import SAIPE County/State
    '''
    run_command('import_saipe_county_state')

@task
def saipe_school():
    '''
    fab staging imports.saipe_school                    Import SAIPE School
    '''
    run_command('import_saipe_school')

@task
def schip_enrollment():
    '''
    fab staging imports.schip_enrollment                Import S-CHIP Enrollment
    '''
    run_command('import_schip_enrollment')

@task
def school_breakfast_participation():
    '''
    fab staging imports.school_breakfast_participation  Import School Breakfast Participation
    '''
    run_command('import_school_breakfast_participation')

@task
def school_lunch_participation():
    '''
    fab staging imports.school_lunch_participation      Import School Lunch Participation
    '''
    run_command('import_school_lunch_participation')

@task
def shelter_population():
    '''
    fab staging imports.shelter_population              Import Shelter Population
    '''
    run_command('import_shelter_population')

@task
def snap_benefits_recipients():
    '''
    fab staging imports.snap_benefits_recipients        Import SNAP Benefits Recipients
    '''
    run_command('import_snap_benefits_recipients')

@task
def snap_monthly_benefits_person():
    '''
    fab staging imports.snap_monthly_benefits_person    Import SNAP Monthly Benefits Per Person
    '''
    run_command('import_snap_monthly_benefits_person')

@task
def snap_participation_households():
    '''
    fab staging imports.snap_participation_households   Import SNAP Participation Households
    '''
    run_command('import_snap_participation_households')

@task
def snap_participation_people():
    '''
    fab staging imports.snap_participation_people       Import SNAP Participation People
    '''
    run_command('import_snap_participation_people')

@task
def special_ed_funding():
    '''
    fab staging imports.special_ed_funding              Import Special Ed. Funding
    '''
    run_command('import_special_ed_funding')

@task
def state_completion_rate():
    '''
    fab staging imports.state_completion_rate           Import State Completion Rate
    '''
    run_command('import_state_completion_rate')

@task
def state_gdp():
    '''
    fab staging imports.state_gdp                       Import State GDP
    '''
    run_command('import_state_gdp')

@task
def state_gdp_pre97():
    '''
    fab staging imports.state_gdp_pre97                 Import State GDP Pre '97
    '''
    run_command('import_state_gdp_pre97')

@task
def state_unemployment():
    '''
    fab staging imports.state_unemployment              Import State Unemployment
    '''
    run_command('import_state_unemployment')

@task
def subfunction_cffr():
    '''
    fab staging imports.subfunction_cffr                Import Sub-function CFFR
    '''
    run_command('import_subfunction_cffr')

@task
def summer_lunch_participation():
    '''
    fab staging imports.summer_lunch_participation      Import Summer Lunch Participation
    '''
    run_command('import_summer_lunch_participation')

@task
def tanf_family():
    '''
    fab staging imports.tanf_family                     Import TANF Family
    '''
    run_command('import_tanf_family')

@task
def tanf_participation():
    '''
    fab staging imports.tanf_participation              Import TANF Participation
    '''
    run_command('import_tanf_participation')

@task
def title_i_funding():
    '''
    fab staging imports.title_i_funding                 Import Title I Funding
    '''
    run_command('import_title_i_funding')

@task
def total_students():
    '''
    fab staging imports.total_students                  Import Total Students
    '''
    run_command('import_total_students')
    
@task
def create_usaspending_assistance(fiscal_year = None, archive_date = None):
    '''
    fab staging imports.create_usaspending_assistance:fiscal_year,archive_date   Create USASpending Assistance Files
    '''
    if fiscal_year is None:
        raise ValueError('Missing fiscal year')
    elif archive_date is None:
        raise ValueError('Missing archive date')
    run_command('create_usaspending_assistance %s %s' % (fiscal_year, archive_date))

@task
def usaspending_assistance(year = None):
    '''
    fab staging imports.usaspending_assistance          Import USASpending Assistance
    '''
    if year is None:
        raise ValueError('Missing year')
    run_command('import_usaspending_assistance %s' % year)

@task
def vehicle_registrations():
    '''
    fab staging imports.vehicle_registrations           Import Vehicle Registrations
    '''
    run_command('import_vehicle_registrations')

@task
def vocational_ed_spending():
    '''
    fab staging imports.vocational_ed_spending          Import Vocational Ed. Spending
    '''
    run_command('import_vocational_ed_spending')

@task
def wic_benefits_state():
    '''
    fab staging imports.wic_benefits_state              Import WIC Benefits By State
    '''
    run_command('import_wic_benefits_state')

@task
def wic_participation_state():
    '''
    fab staging imports.wic_participation_state         Import WIC Participation By State
    '''
    run_command('import_wic_participation_state')
