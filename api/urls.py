from django.conf.urls.defaults import *
from piston.resource import Resource
from npp_api.api.handlers import *
from npp_api.api.emitters import *

alternative_fuel_vehicles_handler = Resource(AlternativeFuelVehiclesHandler)
ansi_county_state_handler = Resource(AnsiCountyStateHandler)
at_codes_handler = Resource(AtCodesHandler)
average_teacher_salary_handler = Resource(AverageTeacherSalaryHandler)
bilingual_ed_spending_handler = Resource(BilingualEdSpendingHandler)
budget_category_subfunctions_handler = Resource(BudgetCategorySubfunctionsHandler)
cffr_handler = Resource(CffrHandler)
cffr_agency_handler = Resource(CffrAgencyHandler)
cffr_geo_handler = Resource(CffrGeoHandler)
cffr_individual_county_handler = Resource(CffrIndividualCountyHandler)
cffr_individual_state_handler = Resource(CffrIndividualStateHandler)
cffr_object_code_handler = Resource(CffrObjectCodeHandler)
cffr_program_handler = Resource(CffrProgramHandler)
children_poverty_state_handler = Resource(ChildrenPovertyStateHandler)
diploma_recipient_total_handler = Resource(DiplomaRecipientTotalHandler)
dropouts_race_handler = Resource(DropoutsRaceHandler)
drug_free_school_spending_handler = Resource(DrugFreeSchoolSpendingHandler)
educational_attainment_handler = Resource(EducationalAttainmentHandler)
electric_emissions_state_handler = Resource(ElectricEmissionsStateHandler)
ell_students_district_handler = Resource(EllStudentsDistrictHandler)
employment_handler = Resource(EmploymentHandler)
energy_consumption_state_handler = Resource(EnergyConsumptionStateHandler)
energy_production_state_handler = Resource(EnergyProductionStateHandler)
energy_expenditures_handler = Resource(EnergyExpendituresHandler)
enrolled_students_district_handler = Resource(EnrolledStudentsDistrictHandler)
enrollment_race_handler = Resource(EnrollmentRaceHandler)
expenditure_per_pupil_handler = Resource(ExpenditurePerPupilHandler)
families_poverty_state_handler = Resource(FamiliesPovertyStateHandler)
fcna_spending_handler = Resource(FcnaSpendingHandler)
federal_impact_aid_handler = Resource(FederalImpactAidHandler)
federal_tax_collection_state_handler = Resource(FederalTaxCollectionStateHandler)
fips_county_congress_district_handler = Resource(FipsCountyCongressDistrictHandler)
fips_state_handler = Resource(FipsStateHandler)
food_security_state_handler = Resource(FoodSecurityStateHandler)
free_lunch_eligible_handler = Resource(FreeLunchEligibleHandler)
free_reduced_lunch_eligible_handler = Resource(FreeReducedLunchEligibleHandler)
free_reduced_lunch_eligible_county_handler = Resource(FreeReducedLunchEligibleCountyHandler)
half_pints_handler = Resource(HalfPintsHandler)
head_start_enrollment_handler = Resource(HeadStartEnrollmentHandler)
health_insurance_handler = Resource(HealthInsuranceHandler)
high_school_other_handler = Resource(HighSchoolOtherHandler)
high_school_dropouts_handler = Resource(HighSchoolDropoutsHandler)
housing_occupancy_state_handler = Resource(HousingOccupancyStateHandler)
individual_education_programs_handler = Resource(IndividualEducationProgramsHandler)
kids_health_insurance_handler = Resource(KidsHealthInsuranceHandler)
labor_force_county_handler = Resource(LaborForceCountyHandler)
labor_force_state_handler = Resource(LaborForceStateHandler)
labor_underutilization_state_handler = Resource(LaborUnderutilizationStateHandler)
math_science_spending_handler = Resource(MathScienceSpendingHandler)
median_income_state_handler = Resource(MedianIncomeStateHandler)
medicaid_participation_handler = Resource(MedicaidParticipationHandler)
medicare_enrollment_handler = Resource(MedicareEnrollmentHandler)
migrant_students_handler = Resource(MigrantStudentsHandler)
military_personnel_handler = Resource(MilitaryPersonnelHandler)
msn_handler = Resource(MsnHandler)
native_ed_spending_handler = Resource(NativeEdSpendingHandler)
new_aids_cases_handler = Resource(NewAidsCasesHandler)
nces_school_district_handler = Resource(NcesSchoolDistrictHandler)
other_federal_revenue_handler = Resource(OtherFederalRevenueHandler)
people_poverty_state_handler = Resource(PeoplePovertyStateHandler)
population_congressional_district_handler = Resource(PopulationCongressionalDistrictHandler)
population_families_handler = Resource(PopulationFamiliesHandler)
population_age_county_handler = Resource(PopulationAgeCountyHandler)
population_age_state_handler = Resource(PopulationAgeStateHandler)
population_gender_county_handler = Resource(PopulationGenderCountyHandler)
population_gender_state_handler = Resource(PopulationGenderStateHandler)
population_race_county_handler = Resource(PopulationRaceCountyHandler)
population_race_state_handler = Resource(PopulationRaceStateHandler)
presidents_budget_handler = Resource(PresidentsBudgetHandler)
pupil_teacher_district_handler = Resource(PupilTeacherDistrictHandler)
pupil_teacher_state_handler = Resource(PupilTeacherStateHandler)
retired_disabled_nilf_handler = Resource(RetiredDisabledNilfHandler)
saipe_county_state_handler = Resource(SaipeCountyStateHandler)
saipe_school_handler = Resource(SaipeSchoolHandler)
schip_enrollment_state_handler = Resource(SchipEnrollmentStateHandler)
school_breakfast_participation_state_handler = Resource(SchoolBreakfastParticipationStateHandler)
school_lunch_participation_state_handler = Resource(SchoolLunchParticipationStateHandler)
snap_benefits_recipients_handler = Resource(SnapBenefitsRecipientsHandler)
snap_monthly_benefits_person_state_handler = Resource(SnapMonthlyBenefitsPersonStateHandler)
snap_participation_households_state_handler = Resource(SnapParticipationHouseholdsStateHandler)
snap_participation_people_state_handler = Resource(SnapParticipationPeopleStateHandler)
shelter_population_handler = Resource(ShelterPopulationHandler)
special_ed_funding_handler = Resource(SpecialEdFundingHandler)
state_completion_rate_handler = Resource(StateCompletionRateHandler)
state_gdp_handler = Resource(StateGdpHandler)
state_gdp_pre97_handler = Resource(StateGdpPre97Handler)
state_postal_codes_handler = Resource(StatePostalCodesHandler)
summer_lunch_participation_state_handler = Resource(SummerLunchParticipationStateHandler)
tanf_participation_state_handler = Resource(TanfParticipationStateHandler)
title_i_funding_handler = Resource(TitleIFundingHandler)
total_students_handler = Resource(TotalStudentsHandler)
subfunctions_cffr_handler = Resource(SubfunctionsCffrHandler)
vehicle_registrations_handler = Resource(VehicleRegistrationsHandler)
vocational_ed_spending_handler = Resource(VocationalEdSpendingHandler)
wic_benefits_state_handler = Resource(WicBenefitsStateHandler)
wic_participation_state_handler = Resource(WicParticipationStateHandler)

urlpatterns = patterns('django.views.generic.simple',
    #documentation urls
    url(r'^$', 'direct_to_template', {'template': 'api/index.html'}),
    (r'^alternative_fuel_vehicles.html$', 'direct_to_template', {'template': 'api/alternative_fuel_vehicles.html'}),
    (r'^ansi_county_state.html$', 'direct_to_template', {'template': 'api/ansi_county_state.html'}),
    (r'^at_codes.html$', 'direct_to_template', {'template': 'api/at_codes.html'}),
    (r'^average_teacher_salary.html$', 'direct_to_template', {'template': 'api/average_teacher_salary.html'}),
    (r'^bilingual_ed_spending.html$', 'direct_to_template', {'template': 'api/bilingual_ed_spending.html'}),
    (r'^budget_category_subfunctions.html$', 'direct_to_template', {'template': 'api/budget_category_subfunctions.html'}),
    (r'^cffr.html$', 'direct_to_template', {'template': 'api/cffr.html'}),
    (r'^children_poverty.html$', 'direct_to_template', {'template': 'api/children_poverty.html'}),
    (r'^diploma_recipient_total.html$', 'direct_to_template', {'template': 'api/diploma_recipient_total.html'}),
    (r'^dropouts_race.html$', 'direct_to_template', {'template': 'api/dropouts_race.html'}),
    (r'^drug_free_school_spending.html$', 'direct_to_template', {'template': 'api/drug_free_school_spending.html'}),
    (r'^educational_attainment.html$', 'direct_to_template', {'template': 'api/educational_attainment.html'}),
    (r'^electric_emissions.html$', 'direct_to_template', {'template': 'api/electric_emissions.html'}),
    (r'^ell_students_district.html$', 'direct_to_template', {'template': 'api/ell_students_district.html'}),
    (r'^employment.html$', 'direct_to_template', {'template': 'api/employment.html'}),
    (r'^energy_consumption.html$', 'direct_to_template', {'template': 'api/energy_consumption.html'}),
    (r'^energy_production.html$', 'direct_to_template', {'template': 'api/energy_production.html'}),
    (r'^energy_expenditures.html$', 'direct_to_template', {'template': 'api/energy_expenditures.html'}),
    (r'^enrolled_students_district.html$', 'direct_to_template', {'template': 'api/enrolled_students_district.html'}),
    (r'^enrollment_race.html$', 'direct_to_template', {'template': 'api/enrollment_race.html'}),
    (r'^expenditure_per_pupil.html$', 'direct_to_template', {'template': 'api/expenditure_per_pupil.html'}),
    (r'^families_poverty.html$', 'direct_to_template', {'template': 'api/families_poverty.html'}),
    (r'^fcna_spending.html$', 'direct_to_template', {'template': 'api/fcna_spending.html'}),
    (r'^federal_impact_aid.html$', 'direct_to_template', {'template': 'api/federal_impact_aid.html'}),
    (r'^federal_tax_collection.html$', 'direct_to_template', {'template': 'api/federal_tax_collection.html'}),
    (r'^fips_county_congress_district.html$', 'direct_to_template', {'template': 'api/fips_county_congress_district.html'}),
    (r'^food_security.html$', 'direct_to_template', {'template': 'api/food_security.html'}),
    (r'^free_lunch_eligible.html$', 'direct_to_template', {'template': 'api/free_lunch_eligible.html'}),
    (r'^free_reduced_lunch_eligible.html$', 'direct_to_template', {'template': 'api/free_reduced_lunch_eligible.html'}),
    (r'^free_reduced_lunch_eligible_county.html$', 'direct_to_template', {'template': 'api/free_reduced_lunch_eligible_county.html'}),
    (r'^half_pints.html$', 'direct_to_template', {'template': 'api/half_pints.html'}),
    (r'^head_start_enrollment.html$', 'direct_to_template', {'template': 'api/head_start_enrollment.html'}),
    (r'^health_insurance.html$', 'direct_to_template', {'template': 'api/health_insurance.html'}),
    (r'^high_school_dropouts.html$', 'direct_to_template', {'template': 'api/high_school_dropouts.html'}),
    (r'^high_school_other.html$', 'direct_to_template', {'template': 'api/high_school_other.html'}),
    (r'^housing_occupancy.html$', 'direct_to_template', {'template': 'api/housing_occupancy.html'}),
    (r'^individual_education_programs.html$', 'direct_to_template', {'template': 'api/individual_education_programs.html'}),
    (r'^kids_health_insurance.html$', 'direct_to_template', {'template': 'api/kids_health_insurance.html'}),
    (r'^labor_force.html$', 'direct_to_template', {'template': 'api/labor_force.html'}),
    (r'^labor_underutilization.html$', 'direct_to_template', {'template': 'api/labor_underutilization.html'}),
    (r'^nces_school_district.html$', 'direct_to_template', {'template': 'api/nces_school_district.html'}),
    (r'^math_science_spending.html$', 'direct_to_template', {'template': 'api/math_science_spending.html'}),
    (r'^median_income.html$', 'direct_to_template', {'template': 'api/median_income.html'}),
    (r'^medicaid_participation.html$', 'direct_to_template', {'template': 'api/medicaid_participation.html'}),
    (r'^medicare_enrollment.html$', 'direct_to_template', {'template': 'api/medicare_enrollment.html'}),
    (r'^migrant_students.html$', 'direct_to_template', {'template': 'api/migrant_students.html'}),
    (r'^military_personnel.html$', 'direct_to_template', {'template': 'api/military_personnel.html'}),
    (r'^native_ed_spending.html$', 'direct_to_template', {'template': 'api/native_ed_spending.html'}),
    (r'^new_aids_cases.html$', 'direct_to_template', {'template': 'api/new_aids_cases.html'}),
    (r'^other_federal_revenue.html$', 'direct_to_template', {'template': 'api/other_federal_revenue.html'}),
    (r'^payments_individuals.html$', 'direct_to_template', {'template': 'api/payments_individuals.html'}),
    (r'^people_poverty.html$', 'direct_to_template', {'template': 'api/people_poverty.html'}),
    (r'^population_congressional_district.html$', 'direct_to_template', {'template': 'api/population_congressional_district.html'}),
    (r'^population_families.html$', 'direct_to_template', {'template': 'api/population_families.html'}),
    (r'^population_age.html$', 'direct_to_template', {'template': 'api/population_age.html'}),
    (r'^population_gender.html$', 'direct_to_template', {'template': 'api/population_gender.html'}),
    (r'^population_race.html$', 'direct_to_template', {'template': 'api/population_race.html'}),
    (r'^pupil_teacher.html$', 'direct_to_template', {'template': 'api/pupil_teacher.html'}),
    (r'^retired_disabled_nilf.html$', 'direct_to_template', {'template': 'api/retired_disabled_nilf.html'}),
    (r'^saipe_county_state.html$', 'direct_to_template', {'template': 'api/saipe_county_state.html'}),
    (r'^saipe_school.html$', 'direct_to_template', {'template': 'api/saipe_school.html'}),
    (r'^schip_enrollment.html$', 'direct_to_template', {'template': 'api/schip_enrollment.html'}),
    (r'^school_breakfast_participation.html$', 'direct_to_template', {'template': 'api/school_breakfast_participation.html'}),
    (r'^school_lunch_participation.html$', 'direct_to_template', {'template': 'api/school_lunch_participation.html'}),
    (r'^shelter_population.html$', 'direct_to_template', {'template': 'api/shelter_population.html'}),
    (r'^special_ed_funding.html$', 'direct_to_template', {'template': 'api/special_ed_funding.html'}),
    (r'^snap_benefits_recipients.html$', 'direct_to_template', {'template': 'api/snap_benefits_recipients.html'}),
    (r'^snap_monthly_benefits_person.html$', 'direct_to_template', {'template': 'api/snap_monthly_benefits_person.html'}),
    (r'^snap_participation_households.html$', 'direct_to_template', {'template': 'api/snap_participation_households.html'}),
    (r'^snap_participation_people.html$', 'direct_to_template', {'template': 'api/snap_participation_people.html'}),
    (r'^state_completion_rate.html$', 'direct_to_template', {'template': 'api/state_completion_rate.html'}),
    (r'^state_gdp.html$', 'direct_to_template', {'template': 'api/state_gdp.html'}),
    (r'^state_gdp_pre97.html$', 'direct_to_template', {'template': 'api/state_gdp_pre97.html'}),
    (r'^vehicle_registrations.html$', 'direct_to_template', {'template':'api/vehicle_registrations.html'}),
    (r'^summer_lunch_participation.html$', 'direct_to_template', {'template': 'api/summer_lunch_participation.html'}),
    (r'^subfunctions_cffr.html$', 'direct_to_template', {'template': 'api/subfunctions_cffr.html'}),
    (r'^tanf_participation.html$', 'direct_to_template', {'template': 'api/tanf_participation.html'}),
    (r'^title_i_funding.html$', 'direct_to_template', {'template': 'api/title_i_funding.html'}),
    (r'^total_students.html$', 'direct_to_template', {'template': 'api/total_students.html'}),
    (r'^vocational_ed_spending.html$', 'direct_to_template', {'template': 'api/vocational_ed_spending.html'}),
    (r'^wic_benefits.html$', 'direct_to_template', {'template': 'api/wic_benefits.html'}),
    (r'^wic_participation.html$', 'direct_to_template', {'template': 'api/wic_participation.html'}),
)

urlpatterns += patterns('',
    #api urls
    url(r'^alternative_fuel_vehicles/$', alternative_fuel_vehicles_handler),
    url(r'^alternative_fuel_vehicles/list\.(?P<emitter_format>.+)', alternative_fuel_vehicles_handler),
    url(r'^ansi_county_state/$', ansi_county_state_handler),
    url(r'^ansi_county_state/list\.(?P<emitter_format>.+)', ansi_county_state_handler),
    url(r'^at_codes/$', at_codes_handler),
    url(r'^at_codes/list\.(?P<emitter_format>.+)', at_codes_handler),
    url(r'^average_teacher_salary/$', average_teacher_salary_handler),
    url(r'^average_teacher_salary/list\.(?P<emitter_format>.+)', average_teacher_salary_handler),
    url(r'^bilingual_ed_spending/$', bilingual_ed_spending_handler),
    url(r'^bilingual_ed_spending/list\.(?P<emitter_format>.+)', bilingual_ed_spending_handler),
    url(r'^budget_category_subfunctions/$', budget_category_subfunctions_handler),
    url(r'^budget_category_subfunctions/list\.(?P<emitter_format>.+)', budget_category_subfunctions_handler),
    url(r'^cffr/$', cffr_handler),
    url(r'^schip/$', cffr_handler, {'program_code': 93.767, }),
    url(r'^schip/list\.(?P<emitter_format>.+)', cffr_handler, {'program_code': 93.767, }),
    url(r'^cffr/list\.(?P<emitter_format>.+)', cffr_handler),
    url(r'^cffragency/$', cffr_agency_handler),
    url(r'^cffragency/list\.(?P<emitter_format>.+)', cffr_agency_handler),   
    url(r'^cffrgeo/$', cffr_geo_handler),
    url(r'^cffrgeo/list\.(?P<emitter_format>.+)', cffr_geo_handler),
    url(r'^cffrobjectcode/$', cffr_object_code_handler),
    url(r'^cffrobjectcode/list\.(?P<emitter_format>.+)', cffr_object_code_handler), 
    url(r'^cffrprogram/$', cffr_program_handler),
    url(r'^cffrprogram/list\.(?P<emitter_format>.+)', cffr_program_handler),
    url(r'^children_poverty_state/', children_poverty_state_handler),
    url(r'^children_poverty_state/list\.(?P<emitter_format>.+)', children_poverty_state_handler),
    url(r'^diploma_recipient_total/$', diploma_recipient_total_handler),
    url(r'^diploma_recipient_total/list\.(?P<emitter_format>.+)', diploma_recipient_total_handler),
    url(r'^dropouts_race/$', dropouts_race_handler),
    url(r'^dropouts_race/list\.(?P<emitter_format>.+)', dropouts_race_handler),
    url(r'^drug_free_school_spending/$', drug_free_school_spending_handler),
    url(r'^drug_free_school_spending/list\.(?P<emitter_format>.+)', drug_free_school_spending_handler),
    url(r'^educational_attainment/$', educational_attainment_handler),
    url(r'^educational_attainment/list\.(?P<emitter_format>.+)', educational_attainment_handler),
    url(r'^electric_emissions_state/$', electric_emissions_state_handler),
    url(r'^electric_emissions_state/list\.(?P<emitter_format>.+)', electric_emissions_state_handler),
    url(r'^ell_students_district/$', ell_students_district_handler),
    url(r'^ell_students_district/list\.(?P<emitter_format>.+)', ell_students_district_handler),
    url(r'^employment/$', employment_handler),
    url(r'^employment/list\.(?P<emitter_format>.+)', employment_handler),
    url(r'^energy_consumption_state/$', energy_consumption_state_handler),
    url(r'^energy_consumption_state/list\.(?P<emitter_format>.+)', energy_consumption_state_handler),
    url(r'^energy_production_state/$', energy_production_state_handler),
    url(r'^energy_production_state/list\.(?P<emitter_format>.+)', energy_production_state_handler),
    url(r'^energy_expenditures/$', energy_expenditures_handler),
    url(r'^energy_expenditures/list\.(?P<emitter_format>.+)', energy_expenditures_handler),
    url(r'^enrolled_students_district/', enrolled_students_district_handler),
    url(r'^enrolled_students_district/list\.(?P<emitter_format>.+)', enrolled_students_district_handler),
    url(r'^enrollment_race/', enrollment_race_handler),
    url(r'^enrollment_race/list\.(?P<emitter_format>.+)', enrollment_race_handler),
    url(r'^expenditure_per_pupil/$', expenditure_per_pupil_handler),
    url(r'^expenditure_per_pupil/list\.(?P<emitter_format>.+)', expenditure_per_pupil_handler),
    url(r'^families_poverty_state/', families_poverty_state_handler),
    url(r'^families_poverty_state/list\.(?P<emitter_format>.+)', families_poverty_state_handler),
    url(r'^fcna_spending/', fcna_spending_handler),
    url(r'^fcna_spending/list\.(?P<emitter_format>.+)', fcna_spending_handler),
    url(r'^federal_impact_aid/', federal_impact_aid_handler),
    url(r'^federal_impact_aid/list\.(?P<emitter_format>.+)', federal_impact_aid_handler),
    url(r'^federal_tax_collection_state/', federal_tax_collection_state_handler),
    url(r'^federal_tax_collection_state/list\.(?P<emitter_format>.+)', federal_tax_collection_state_handler),
    url(r'^fips_county_congress_district/$', fips_county_congress_district_handler),
    url(r'^fips_county_congress_district/list\.(?P<emitter_format>.+)', fips_county_congress_district_handler),
    url(r'^fips_state/$', fips_state_handler),
    url(r'^fips_state/list\.(?P<emitter_format>.+)', fips_state_handler),
    url(r'^food_security_state/$', food_security_state_handler),
    url(r'^food_security_state/list\.(?P<emitter_format>.+)', food_security_state_handler),
    url(r'^free_lunch_eligible/$', free_lunch_eligible_handler),
    url(r'^free_lunch_eligible/list\.(?P<emitter_format>.+)', free_lunch_eligible_handler),
    url(r'^free_reduced_lunch_eligible/$', free_reduced_lunch_eligible_handler),
    url(r'^free_reduced_lunch_eligible/list\.(?P<emitter_format>.+)', free_reduced_lunch_eligible_handler),
    url(r'^free_reduced_lunch_eligible_county/$', free_reduced_lunch_eligible_county_handler),
    url(r'^free_reduced_lunch_eligible_county/list\.(?P<emitter_format>.+)', free_reduced_lunch_eligible_county_handler),
    url(r'^half_pints/$', half_pints_handler),
    url(r'^half_pints/list\.(?P<emitter_format>.+)', half_pints_handler),
    url(r'^head_start_enrollment/$', head_start_enrollment_handler),
    url(r'^head_start_enrollment/list\.(?P<emitter_format>.+)', head_start_enrollment_handler),
    url(r'^health_insurance/$', health_insurance_handler),
    url(r'^health_insurance/list\.(?P<emitter_format>.+)', health_insurance_handler),
    url(r'^high_school_dropouts/$', high_school_dropouts_handler),
    url(r'^high_school_dropouts/list\.(?P<emitter_format>.+)', high_school_dropouts_handler),
    url(r'^high_school_other/$', high_school_other_handler),
    url(r'^high_school_other/list\.(?P<emitter_format>.+)', high_school_other_handler),
    url(r'^housing_occupancy_state/$', housing_occupancy_state_handler),
    url(r'^housing_occupancy_state/list\.(?P<emitter_format>.+)', housing_occupancy_state_handler),
    url(r'^individual_education_programs/$', individual_education_programs_handler),
    url(r'^individual_education_programs/list\.(?P<emitter_format>.+)', individual_education_programs_handler),
    url(r'^kids_health_insurance/$', kids_health_insurance_handler),
    url(r'^kids_health_insurance/list\.(?P<emitter_format>.+)', kids_health_insurance_handler),
    url(r'^labor_force_county/$', labor_force_county_handler),
    url(r'^labor_force_county/list\.(?P<emitter_format>.+)',labor_force_county_handler),
    url(r'^labor_force_state/$', labor_force_state_handler),
    url(r'^labor_force_state/list\.(?P<emitter_format>.+)',labor_force_state_handler),
    url(r'^labor_underutilization_state/$', labor_underutilization_state_handler),
    url(r'^labor_underutilization_state/list\.(?P<emitter_format>.+)',labor_underutilization_state_handler),
    url(r'^math_science_spending/$', math_science_spending_handler),
    url(r'^math_science_spending/list\.(?P<emitter_format>.+)', math_science_spending_handler),
    url(r'^median_income_state/$', median_income_state_handler),
    url(r'^median_income_state/list\.(?P<emitter_format>.+)', median_income_state_handler),
    url(r'^medicaid_participation/$', medicaid_participation_handler),
    url(r'^medicaid_participation/list\.(?P<emitter_format>.+)', medicaid_participation_handler),
    url(r'^medicare_enrollment/$', medicare_enrollment_handler),
    url(r'^medicare_enrollment/list\.(?P<emitter_format>.+)', medicare_enrollment_handler),
    url(r'^migrant_students/$', migrant_students_handler),
    url(r'^migrant_students/list\.(?P<emitter_format>.+)', migrant_students_handler),
    url(r'^military_personnel/$', military_personnel_handler),
    url(r'^military_personnel/list\.(?P<emitter_format>.+)', military_personnel_handler),
    url(r'^msn/$', msn_handler),
    url(r'^msn/list\.(?P<emitter_format>.+)', msn_handler),
    url(r'^native_ed_spending/$', native_ed_spending_handler),
    url(r'^native_ed_spending/list\.(?P<emitter_format>.+)', native_ed_spending_handler),
    url(r'^nces_school_district/$', nces_school_district_handler),
    url(r'^nces_school_district/list\.(?P<emitter_format>.+)', nces_school_district_handler),
    url(r'^new_aids_cases/$', new_aids_cases_handler),
    url(r'^new_aids_cases/list\.(?P<emitter_format>.+)', new_aids_cases_handler),
    url(r'^other_federal_revenue/$', other_federal_revenue_handler),
    url(r'^other_federal_revenue/list\.(?P<emitter_format>.+)', other_federal_revenue_handler),
    url(r'^payments_individuals_county/$', cffr_individual_county_handler),
    url(r'^payments_individuals_county/list\.(?P<emitter_format>.+)', cffr_individual_county_handler),
    url(r'^payments_individuals_state/$', cffr_individual_state_handler),
    url(r'^payments_individuals_state/list\.(?P<emitter_format>.+)', cffr_individual_state_handler),
    url(r'^people_poverty_state/$', people_poverty_state_handler),
    url(r'^people_poverty_state/list\.(?P<emitter_format>.+)', people_poverty_state_handler),
    url(r'^population_congressional_district/$', population_congressional_district_handler),
    url(r'^population_congressional_district/list\.(?P<emitter_format>.+)', population_congressional_district_handler),
    url(r'^population_families/$', population_families_handler),
    url(r'^population_families/list\.(?P<emitter_format>.+)', population_families_handler),
    url(r'^population_age_county$', population_age_county_handler),
    url(r'^population_age_county/list\.(?P<emitter_format>.+)', population_age_county_handler),
    url(r'^population_age_state$', population_age_state_handler),
    url(r'^population_age_state/list\.(?P<emitter_format>.+)', population_age_state_handler),
    url(r'^population_gender_county$', population_gender_county_handler),
    url(r'^population_gender_county/list\.(?P<emitter_format>.+)', population_gender_county_handler),
    url(r'^population_gender_state$', population_gender_state_handler),
    url(r'^population_gender_state/list\.(?P<emitter_format>.+)', population_gender_state_handler),
    url(r'^population_race_county$', population_race_county_handler),
    url(r'^population_race_county/list\.(?P<emitter_format>.+)', population_race_county_handler),
    url(r'^population_race_state$', population_race_state_handler),
    url(r'^population_race_state/list\.(?P<emitter_format>.+)', population_race_state_handler),
    url(r'^presidents_budget/$', presidents_budget_handler),
    url(r'^presidents_budget/list\.(?P<emitter_format>.+)', presidents_budget_handler),
    url(r'^pupil_teacher_district/$', pupil_teacher_district_handler),
    url(r'^pupil_teacher_district/list\.(?P<emitter_format>.+)', pupil_teacher_district_handler),
    url(r'^pupil_teacher_state/$', pupil_teacher_state_handler),
    url(r'^pupil_teacher_state/list\.(?P<emitter_format>.+)', pupil_teacher_state_handler),
    url(r'^retired_disabled_nilf/$', retired_disabled_nilf_handler),
    url(r'^retired_disabled_nilf/list\.(?P<emitter_format>.+)', retired_disabled_nilf_handler),
    url(r'^saipe_county_state/$', saipe_county_state_handler),
    url(r'^saipe_county_state/list\.(?P<emitter_format>.+)', saipe_county_state_handler),
    url(r'^saipe_school/$', saipe_school_handler),
    url(r'^saipe_school/list\.(?P<emitter_format>.+)', saipe_school_handler),
    url(r'^schip_enrollment_state/$', schip_enrollment_state_handler),
    url(r'^schip_enrollment_state/list\.(?P<emitter_format>.+)', schip_enrollment_state_handler),
    url(r'^school_breakfast_participation_state/$', school_breakfast_participation_state_handler),
    url(r'^school_breakfast_participation_state/list\.(?P<emitter_format>.+)', school_breakfast_participation_state_handler),
    url(r'^school_lunch_participation_state/$', school_lunch_participation_state_handler),
    url(r'^school_lunch_participation_state/list\.(?P<emitter_format>.+)', school_lunch_participation_state_handler),
    url(r'^shelter_population/$', shelter_population_handler),
    url(r'^shelter_population/list\.(?P<emitter_format>.+)', shelter_population_handler),
    url(r'^special_ed_funding/$', special_ed_funding_handler),
    url(r'^special_ed_funding/list\.(?P<emitter_format>.+)', special_ed_funding_handler),
    url(r'^snap_benefits_recipients/$', snap_benefits_recipients_handler),
    url(r'^snap_benefits_recipients/list\.(?P<emitter_format>.+)', snap_benefits_recipients_handler),
    url(r'^snap_monthly_benefits_person_state/$', snap_monthly_benefits_person_state_handler),
    url(r'^snap_monthly_benefits_person_state/list\.(?P<emitter_format>.+)', snap_monthly_benefits_person_state_handler),
    url(r'^snap_participation_households_state/$', snap_participation_households_state_handler),
    url(r'^snap_participation_households_state/list\.(?P<emitter_format>.+)', snap_participation_households_state_handler),
    url(r'^snap_participation_people_state/$', snap_participation_people_state_handler),
    url(r'^snap_participation_people_state/list\.(?P<emitter_format>.+)', snap_participation_people_state_handler),
    url(r'^state_completion_rate/$', state_completion_rate_handler),
    url(r'^state_completion_rate/list\.(?P<emitter_format>.+)', state_completion_rate_handler),
    url(r'^state_gdp/$', state_gdp_handler),
    url(r'^state_gdp/list\.(?P<emitter_format>.+)', state_gdp_handler),
    url(r'^state_gdp_pre97/$', state_gdp_pre97_handler),
    url(r'^state_gdp_pre97/list\.(?P<emitter_format>.+)', state_gdp_pre97_handler),
    url(r'^state_postal_codes/$', state_postal_codes_handler),
    url(r'^state_postal_codes/list\.(?P<emitter_format>.+)', state_postal_codes_handler),
    url(r'^vehicle_registrations/$', vehicle_registrations_handler),
    url(r'^vehicle_registrations/list\.(?P<emitter_format>.+)', vehicle_registrations_handler),
    url(r'^subfunctions_cffr/$', subfunctions_cffr_handler),
    url(r'^subfunctions_cffr/list\.(?P<emitter_format>.+)', subfunctions_cffr_handler),
    url(r'^summer_lunch_participation_state/$', summer_lunch_participation_state_handler),
    url(r'^summer_lunch_participation_state/list\.(?P<emitter_format>.+)', summer_lunch_participation_state_handler),
    url(r'^tanf_participation_state/$', tanf_participation_state_handler),
    url(r'^tanf_participation_state/list\.(?P<emitter_format>.+)', tanf_participation_state_handler),
    url(r'^total_students/$', total_students_handler),
    url(r'^total_students/list\.(?P<emitter_format>.+)', total_students_handler),
    url(r'^title_i_funding/$', title_i_funding_handler),
    url(r'^title_i_funding/list\.(?P<emitter_format>.+)', title_i_funding_handler),
    url(r'^vocational_ed_spending/$', vocational_ed_spending_handler),
    url(r'^vocational_ed_spending/list\.(?P<emitter_format>.+)', vocational_ed_spending_handler),
    url(r'^wic_benefits_state/$', wic_benefits_state_handler),
    url(r'^wic_benefits_state/list\.(?P<emitter_format>.+)', wic_benefits_state_handler),
    url(r'^wic_participation_state/$', wic_participation_state_handler),
    url(r'^wic_participation_state/list\.(?P<emitter_format>.+)', wic_participation_state_handler),
)