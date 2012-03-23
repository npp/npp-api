from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.title
    
class Source(models.Model):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category)
    string_id = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.title
    
### "raw" models (i.e., represent data as it is pulled in from the source)

class AlternativeFuelVehicles(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField()

class AnnualStateEnergyConsumption(models.Model):
    state = models.CharField(max_length=2)
    msn = models.CharField(max_length=5)
    year = models.IntegerField()
    value = models.FloatField(null=True)
    
class AnnualStateEnergyExpenditures(models.Model):
    state = models.CharField(max_length=2)
    msn = models.CharField(max_length=5)
    year = models.IntegerField()
    value = models.FloatField(null=True)
    
class AnsiCountyState(models.Model):
    state = models.CharField(max_length=2)
    ansi_state = models.CharField(max_length=2)
    code = models.CharField(max_length=3)
    county = models.CharField(max_length=255)
    ansi_class = models.CharField(max_length=2)
    
class AnsiState(models.Model):
    ansi_state = models.CharField(max_length=2)
    state = models.CharField(max_length=2)
    state_name = models.CharField(max_length=50)
    gnisid = models.CharField(max_length=8)
    
class AtCodes(models.Model):
    code = models.CharField(max_length=1)
    assistance_type = models.CharField(max_length=64)
    
class AverageTeacherSalary(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField()
    
class BilingualEdSpending(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class BudgetCategorySubfunctions(models.Model):
    subfunction = models.TextField(max_length=3)
    npp_budget_category = models.TextField(max_length=64)

class CffrRaw(models.Model):
    year = models.IntegerField()
    state_code = models.CharField(max_length=2)
    county_code = models.CharField(max_length=3)
    place_code =  models.CharField(max_length=5)
    state_postal =  models.CharField(max_length=2, null=True)
    county_name =  models.CharField(max_length=24, null=True)
    place_name =  models.CharField(max_length=24, null=True)
    population =  models.IntegerField(null=True)
    congress_district =  models.CharField(max_length=34, null=True)
    program_code =  models.CharField(max_length=6)
    object_type =  models.CharField(max_length=2)
    agency_code =  models.CharField(max_length=4)
    funding_sign =  models.CharField(max_length=1)
    amount =  models.BigIntegerField()
    amount_adjusted = models.BigIntegerField(null=True)
    
class CffrAgency(models.Model):
    year = models.IntegerField()
    agency_code = models.CharField(max_length=4)
    agency_name = models.CharField(max_length=90)
    
class CffrGeo(models.Model):
    year = models.IntegerField()
    state_code = models.CharField(max_length=2)
    county_code = models.CharField(max_length=3)
    place_code =  models.CharField(max_length=5)
    place_name =  models.CharField(max_length=24)
    state_gu = models.CharField(max_length=2)
    type_gu = models.CharField(max_length=1)
    county_gu = models.CharField(max_length=3)
    place_gu = models.CharField(max_length=3)
    split_gu = models.CharField(max_length=3)
    population =  models.IntegerField(null=True)
    congress_district =  models.CharField(max_length=34, null=True)
    
class CffrObjectCode(models.Model):
    object_code = models.CharField(max_length=2)
    category = models.CharField(max_length=80)

class CffrProgramRaw(models.Model):
    year = models.IntegerField()
    program_id_code = models.CharField(max_length=6)
    program_name = models.CharField(max_length=74)
    
class ChildrenPoverty(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    children_total = models.IntegerField()
    children_total_moe = models.IntegerField()
    children_poverty = models.IntegerField()
    children_poverty_moe = models.IntegerField()
    children_poverty_percent = models.FloatField()
    children_poverty_percent_moe = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
class DiplomaRecipientTotal(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    key = models.CharField(max_length=32)
    value = models.IntegerField(null=True)
    
class DropoutsRace(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    key = models.CharField(max_length=32)
    value = models.IntegerField(null=True)

class DrugFreeSchoolSpending(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class EducationalAttainment(models.Model):
    year = models.IntegerField()
    state = models.TextField(max_length=32)
    gender = models.TextField(max_length=16)
    value_type = models.TextField(max_length=16)
    category = models.TextField(max_length=64)
    value = models.IntegerField(null=True)
    
class EllStudentsDistrict(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class Employment(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    total_civilian_labor_force = models.FloatField(null=True)
    white_civilian_labor_force = models.FloatField(null=True)
    black_civilian_labor_force = models.FloatField(null=True)
    hispanic_civilian_labor_force = models.FloatField(null=True)
    white_unemployed = models.FloatField(null=True)
    black_unemployed = models.FloatField(null=True)
    hispanic_unemployed = models.FloatField(null=True)
    
class EnrolledStudentsDistrict(models.Model):
    year = models.CharField(max_length=9)
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=64)
    value = models.IntegerField(null=True)
    
class EnrollmentRace(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    key = models.CharField(max_length=32)
    value = models.IntegerField(null=True)

class ExpenditurePerPupil(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class FamiliesPoverty(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    families_total = models.IntegerField()
    families_total_moe = models.IntegerField()
    families_poverty_percent = models.FloatField()
    families_poverty_percent_moe = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
class FcnaSpending(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class FederalImpactAid(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class FederalTaxCollectionStateRaw(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=255)
    total_collections = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    business_income_taxes = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    income_employment_estate_trust_total = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    individual_witheld_fica = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    individual_notwitheld_seca = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    unemployment_insurance = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    railroad_retirement = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    estate_trust_income_tax = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    estate_tax = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    gift_tax = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    excise_taxes = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class FipsCountyCongressDistrict(models.Model):
    state_code = models.CharField(max_length=2)
    county_code = models.CharField(max_length=3)
    district_code = models.CharField(max_length=2)
    congress = models.IntegerField()
    
class FipsState(models.Model):
    state = models.CharField(max_length=2)
    code = models.CharField(max_length=64)
    
class FoodSecurityStateRaw(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    household_total = models.IntegerField()
    no_response = models.IntegerField()
    food_secure = models.IntegerField(null=True)
    food_secure_high = models.IntegerField(null=True)
    food_secure_marginal = models.IntegerField(null=True)
    food_secure_low = models.IntegerField()
    food_secure_very_low = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
class FreeLunchEligible(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class FreeReducedLunchEligible(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class FreeReducedLunchEligibleCounty(models.Model):
    year = models.IntegerField()
    county_name = models.CharField(max_length=128, null=True)
    state = models.CharField(max_length=2, null=True)
    amount = models.IntegerField(null=True)
    
class HalfPints(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField()
    
class HeadStartEnrollment(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    funding = models.IntegerField()
    enrollment = models.IntegerField()
    
class HealthInsurance(models.Model):
    state = models.CharField(max_length=64)
    year = models.IntegerField()
    all_people = models.IntegerField()
    not_covered = models.IntegerField()
    not_covered_se = models.FloatField(null=True)
    not_covered_pct = models.FloatField()
    not_covered_pct_se = models.FloatField(null=True)
    covered = models.IntegerField()
    covered_se = models.FloatField(null=True)
    covered_pct = models.FloatField()
    covered_pct_se = models.FloatField(null=True)
    private = models.IntegerField()
    private_se = models.FloatField(null=True)
    private_pct = models.FloatField()
    private_pct_se = models.FloatField(null=True)
    private_employment = models.IntegerField()
    private_employment_se = models.FloatField(null=True)
    private_employment_pct = models.FloatField()
    private_employment_pct_se = models.FloatField(null=True)
    direct_purchase = models.IntegerField()
    direct_purchase_se = models.FloatField(null=True)
    direct_purchase_pct = models.FloatField()
    direct_purchase_pct_se = models.FloatField(null=True)
    govt = models.IntegerField()
    govt_se = models.FloatField(null=True)
    govt_pct = models.FloatField()
    govt_pct_se = models.FloatField(null=True)
    medicaid = models.IntegerField()
    medicaid_se = models.FloatField(null=True)
    medicaid_pct = models.FloatField()
    medicaid_pct_se = models.FloatField(null=True) 
    medicare = models.IntegerField()
    medicare_se = models.FloatField(null=True)
    medicare_pct = models.FloatField()
    medicare_pct_se = models.FloatField(null=True)
    military = models.IntegerField()
    military_se = models.FloatField(null=True)
    military_pct = models.FloatField()
    military_pct_se = models.FloatField(null=True)

class HighSchoolDropouts(models.Model):
    state = models.CharField(max_length=2)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    
class HighSchoolOther(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    key = models.CharField(max_length=32)
    value = models.IntegerField(null=True)
    
class HousingUnits(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    
class IndividualEducationPrograms(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class KidsHealthInsurance(models.Model):
    state = models.CharField(max_length=64)
    year = models.IntegerField()
    all_people = models.IntegerField()
    not_covered = models.IntegerField()
    not_covered_se = models.FloatField(null=True)
    not_covered_pct = models.FloatField()
    not_covered_pct_se = models.FloatField(null=True)
    covered = models.IntegerField()
    covered_se = models.FloatField(null=True)
    covered_pct = models.FloatField()
    covered_pct_se = models.FloatField(null=True)
    private = models.IntegerField()
    private_se = models.FloatField(null=True)
    private_pct = models.FloatField()
    private_pct_se = models.FloatField(null=True)
    private_employment = models.IntegerField()
    private_employment_se = models.FloatField(null=True)
    private_employment_pct = models.FloatField()
    private_employment_pct_se = models.FloatField(null=True)
    direct_purchase = models.IntegerField()
    direct_purchase_se = models.FloatField(null=True)
    direct_purchase_pct = models.FloatField()
    direct_purchase_pct_se = models.FloatField(null=True)
    govt = models.IntegerField()
    govt_se = models.FloatField(null=True)
    govt_pct = models.FloatField()
    govt_pct_se = models.FloatField(null=True)
    medicaid = models.IntegerField()
    medicaid_se = models.FloatField(null=True)
    medicaid_pct = models.FloatField()
    medicaid_pct_se = models.FloatField(null=True) 
    medicare = models.IntegerField()
    medicare_se = models.FloatField(null=True)
    medicare_pct = models.FloatField()
    medicare_pct_se = models.FloatField(null=True)
    military = models.IntegerField()
    military_se = models.FloatField(null=True)
    military_pct = models.FloatField()
    military_pct_se = models.FloatField(null=True)
    
class LaborForceCountyRaw(models.Model):
    year = models.IntegerField()
    laus_code = models.CharField(max_length=8)
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    county_name = models.CharField(max_length=255)
    labor_force = models.IntegerField(null=True)
    employed = models.IntegerField(null=True)
    unemployed = models.IntegerField(null=True)
    unemployment_rate = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
class LaborUnderutilizationStateRaw(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=64)
    u1 = models.FloatField()
    u2 = models.FloatField()
    u3 = models.FloatField()
    u4 = models.FloatField()
    u5 = models.FloatField()
    u6 = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
class MathScienceSpending(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class MedianHouseholdIncomeStateRaw(models.Model):
    year = models.IntegerField()
    state_fips = models.CharField(max_length=2)
    state = models.CharField(max_length=32)
    median_household_income = models.FloatField(null=True)
    median_household_income_moe = models.IntegerField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class MedicaidParticipation(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    
class MedicareEnrollment(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    population = models.IntegerField(null=True)
    percent = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
class MigrantStudents(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class MilitaryPersonnel(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    military_personnel = models.IntegerField()
    civilian_personnel = models.IntegerField(null=True)
    reserve_national_guard_personnel = models.IntegerField(null=True)

class MsnCodes(models.Model):
    msn = models.CharField(max_length=5)
    description = models.TextField()
    unit = models.CharField(max_length=255)
    
class NativeEdSpending(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class NcesSchoolDistrict(models.Model):
    state = models.CharField(max_length=2)
    district_name = models.CharField(max_length=255)
    county_name = models.CharField(max_length=255)
    county_code = models.CharField(max_length=4)
    state_code = models.CharField(max_length=2)
    congress_code = models.CharField(max_length=2)
    district_code = models.CharField(max_length=6)
    
class NewAidsCases(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    
class OtherFederalRevenue(models.Model):
    year = models.CharField(max_length=16)
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class OwnersRenters(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    total = models.IntegerField()
    not_in_universe = models.IntegerField()
    owned = models.IntegerField()
    rented = models.IntegerField()
    rented_no_cash = models.IntegerField()
    
class PeopleInPoverty(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    total_population = models.IntegerField()
    value = models.IntegerField()
    value_standard_error = models.IntegerField()
    percent = models.FloatField()
    percent_standard_error = models.FloatField()

#deprecated?    
class PopulationCongressionalDistrict(models.Model):
    year = models.IntegerField()
    district = models.IntegerField()
    state = models.CharField(max_length=32)
    white_alone = models.IntegerField()
    black_alone = models.IntegerField()
    american_indian_alaskan_alone = models.IntegerField()
    asian_alone = models.IntegerField()
    hawaiian_pacific_island_alone = models.IntegerField()
    other_alone = models.IntegerField()
    two_or_more_races = models.IntegerField()
    households = models.IntegerField()
    
class PopulationEst00Raw(models.Model):
    sumlev = models.CharField(max_length=3)
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=3)
    stname = models.CharField(max_length=32)
    ctyname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    ethnic_origin = models.CharField(max_length=1)
    race = models.CharField(max_length=1)
    estimatesbase2000 = models.IntegerField(null=True)
    popestimate2000 = models.IntegerField(null=True)
    popestimate2001 = models.IntegerField(null=True)
    popestimate2002 = models.IntegerField(null=True)
    popestimate2003 = models.IntegerField(null=True)
    popestimate2004 = models.IntegerField(null=True)
    popestimate2005 = models.IntegerField(null=True)
    popestimate2006 = models.IntegerField(null=True)
    popestimate2007 = models.IntegerField(null=True)
    popestimate2008 = models.IntegerField(null=True)
    popestimate2009 = models.IntegerField(null=True)
    census2010pop = models.IntegerField(null=True)
    popestimate2010 = models.IntegerField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('state', 'county', 'gender', 'ethnic_origin', 'race')
    
class PopulationEst90Raw(models.Model):
    year = models.CharField(max_length=2)
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=3)
    agegrp = models.CharField(max_length=2)
    race_gender = models.CharField(max_length=2)
    ethnic_origin = models.CharField(max_length=1)
    population = models.IntegerField(null=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state', 'county', 'agegrp', 'race_gender', 'ethnic_origin')
    
class PopulationFamilies(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    value = models.IntegerField()
    
class PupilTeacherDistrict(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.FloatField(null=True)
    
class PresidentsBudget(models.Model):
    budget_type = models.CharField(max_length=32)
    source_category_code = models.IntegerField(null=True)
    source_category_name = models.CharField(max_length=255, null=True)
    source_subcategory_code = models.IntegerField(null=True)
    source_subcategory_name = models.CharField(max_length=255, null=True)
    agency_code = models.IntegerField(null=True)
    agency_name = models.CharField(max_length=255)
    bureau_code = models.IntegerField(null=True)
    bureau_name = models.CharField(max_length=255)
    account_code = models.IntegerField(null=True)
    account_name = models.CharField(max_length=255)
    treasury_agency_code = models.IntegerField(null=True)
    subfunction_code = models.IntegerField(null=True)
    subfunction_title = models.CharField(max_length=255, null=True)
    bea_category = models.CharField(max_length=32, null=True)
    grant_non_grant = models.CharField(max_length=32, null=True)
    on_off_budget = models.CharField(max_length=32)
    
class PresidentsBudgetYear(models.Model):
    budget = models.ForeignKey('PresidentsBudget', related_name='years')
    year = models.CharField(max_length=4)
    value = models.IntegerField()
    
class PupilTeacherStateRaw(models.Model):
    state = models.CharField(max_length=2)
    year = models.IntegerField()
    ratio = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
class RetiredDisabledNilf(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    total = models.IntegerField()
    employed_at_work = models.IntegerField()
    employed_absent = models.IntegerField()
    employed_on_layoff = models.IntegerField()
    unemployed_looking = models.IntegerField()
    retired_not_in_labor_force = models.IntegerField()
    disabled_not_in_labor_force = models.IntegerField()
    other_not_in_labor_force = models.IntegerField()
    
class SchipEnrollment(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    
class StateCompletionRate(models.Model):
    state = models.CharField(max_length=2)
    year = models.IntegerField()
    key = models.CharField(max_length=16)
    value = models.IntegerField(null=True)

class StateLaborForceParticipation(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    civilian_noninstitutional_pop = models.IntegerField()
    civilian_labor_force = models.IntegerField()
    labor_force_participation_rate = models.FloatField()
    employment_total = models.IntegerField()
    employment_pop_rate = models.FloatField()
    unemployment_total = models.IntegerField()
    unemployment_rate = models.FloatField()
    
class StateRenewableEnergy(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    fossil_coal = models.FloatField()
    fossil_gas = models.FloatField()
    fossil_oil = models.FloatField()
    nuclear_electric = models.FloatField()
    renewable_biofuels = models.FloatField()
    renewable_other = models.FloatField()
    renewable_total = models.FloatField()
    total = models.FloatField()
    
class SaipeSchool(models.Model):
    year = models.IntegerField()
    fips_state = models.CharField(max_length=2)
    ccd_district_id = models.CharField(max_length=5)
    district_name = models.CharField(max_length=65)
    population = models.IntegerField()
    relevant_population = models.IntegerField()
    relevant_population_poverty = models.IntegerField()
    file_stamp = models.CharField(max_length=21)
    
class SaipeCountyState(models.Model):
    year = models.IntegerField()
    fips_state = models.CharField(max_length=2)
    fips_county = models.CharField(max_length=3)
    
    all_age_poverty = models.IntegerField(null=True)
    all_age_poverty_90_lower = models.IntegerField(null=True)
    all_age_poverty_90_upper = models.IntegerField(null=True)
    all_age_poverty_percent = models.FloatField(null=True)
    all_age_poverty_percent_90_lower = models.FloatField(null=True)
    all_age_poverty_percent_90_upper = models.FloatField(null=True)
    
    age_0_17_poverty = models.IntegerField(null=True)
    age_0_17_poverty_90_lower = models.IntegerField(null=True)
    age_0_17_poverty_90_upper = models.IntegerField(null=True)
    age_0_17_poverty_percent = models.FloatField(null=True)
    age_0_17_poverty_percent_90_lower = models.FloatField(null=True)
    age_0_17_poverty_percent_90_upper = models.FloatField(null=True)
    
    age_5_17_related_poverty = models.IntegerField(null=True)
    age_5_17_related_poverty_90_lower = models.IntegerField(null=True)
    age_5_17_related_poverty_90_upper = models.IntegerField(null=True)
    age_5_17_related_poverty_percent = models.FloatField(null=True)
    age_5_17_related_poverty_percent_90_lower = models.FloatField(null=True)
    age_5_17_related_poverty_percent_90_upper = models.FloatField(null=True)
    
    median_household_income = models.IntegerField(null=True)
    median_household_income_90_lower = models.IntegerField(null=True)
    median_household_income_90_upper = models.IntegerField(null=True)
    
    age_0_5_poverty = models.IntegerField(null=True)
    age_0_5_poverty_90_lower = models.IntegerField(null=True)
    age_0_5_poverty_90_upper = models.IntegerField(null=True)
    age_0_5_poverty_percent = models.FloatField(null=True)
    age_0_5_poverty_percent_90_lower = models.FloatField(null=True)
    age_0_5_poverty_percent_90_upper = models.FloatField(null=True)
    
    state_county_name = models.CharField(max_length=45)
    state_postal_abbreviation = models.CharField(max_length=2)
    file_tag = models.CharField(max_length=22)
    
class SchoolBreakfastParticipation(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    value = models.IntegerField()
    
class SchoolLunchParticipation(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    value = models.IntegerField()
    
class ShelterPopulation(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    value = models.IntegerField()
    percent = models.FloatField(null=True)
    
class SnapBenefitsRecipients(models.Model):
    state_fips = models.CharField(max_length=2)
    county_fips = models.CharField(max_length=3)
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    
class SnapMonthlyBenefitsPerson(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.FloatField()
    
class SnapParticipationHouseholds(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField()

class SnapParticipationPeople(models.Model):
    state = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField()
    
class SpecialEdFunding(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class StateEmissions(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=16)
    producer_type = models.CharField(max_length=64)
    energy_source = models.CharField(max_length=64)
    co2 = models.IntegerField()
    so2 = models.IntegerField()
    nox = models.IntegerField()
    
class StateEnergyProductionEstimates(models.Model):
    state = models.CharField(max_length=2)
    msn = models.CharField(max_length=5)
    year = models.IntegerField()
    value = models.FloatField(null=True)
    
class StateGdp(models.Model):
    year = models.IntegerField()
    fips = models.IntegerField()
    state = models.CharField(max_length=32)
    industry_code = models.IntegerField()
    industry = models.CharField(max_length=64)
    component_code = models.IntegerField()
    component = models.CharField(max_length=128)
    value = models.IntegerField()

class StateGdpPre97(models.Model):
    year = models.IntegerField()
    fips = models.IntegerField()
    state = models.CharField(max_length=32)
    industry_code = models.IntegerField()
    industry = models.CharField(max_length=64)
    component_code = models.IntegerField()
    component = models.CharField(max_length=128)
    value = models.IntegerField()
    
class StatePostalCodes(models.Model):
    code = models.CharField(max_length=2)
    state = models.CharField(max_length=32)
    
class SubfunctionsCffr(models.Model):
    subfunction_number = models.TextField(max_length=3)
    subfunction_name = models.TextField(max_length=64)
    cfda_program_code = models.TextField(max_length=8)
    program_name = models.TextField(max_length=64)
    at_code_1 = models.TextField(max_length=1, null=True)
    at_code_2 = models.TextField(max_length=1, null=True)
    at_code_3 = models.TextField(max_length=1, null=True)
    at_code_4 = models.TextField(max_length=1, null=True)
    at_code_5 = models.TextField(max_length=1, null=True)
    at_code_6 = models.TextField(max_length=1, null=True)
    at_code_7 = models.TextField(max_length=1, null=True)
    at_code_8 = models.TextField(max_length=1, null=True)
    
class SummerLunchParticipation(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    value = models.IntegerField()

class TanfFamilyStateRaw(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    value = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
class TanfParticipationStateRaw(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    value = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
class TitleIFunding(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class TotalStudents(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    value = models.IntegerField(null=True)

class VehicleRegistrations(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=32)
    auto_private = models.IntegerField()
    auto_public = models.IntegerField(null=True)
    auto_total = models.IntegerField()
    buses_private = models.IntegerField()
    buses_public = models.IntegerField(null=True)
    buses_total = models.IntegerField()
    trucks_private = models.IntegerField()
    trucks_public = models.IntegerField(null=True)
    trucks_total = models.IntegerField()
    all_private = models.IntegerField()
    all_public = models.IntegerField(null=True)
    all_total = models.IntegerField()
    private_commercial_per_capita = models.FloatField(null=True)
    motorcycle_private = models.IntegerField()
    motorcycle_public = models.IntegerField(null=True)

class VocationalEdSpending(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2)
    agency_name = models.CharField(max_length=128)
    agency_id = models.CharField(max_length=7)
    amount = models.IntegerField(null=True)
    
class WicBenefitsStateRaw(models.Model):
    place = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
class WicParticipationStateRaw(models.Model):
    place = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    year = models.IntegerField()
    value = models.IntegerField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
   

### public-facing data models, including reference tables.
### ideally, these will in separate files someday

### reference models
class CffrProgram(models.Model):
    year = models.IntegerField()
    program_code = models.CharField(max_length=6)
    program_name = models.CharField(max_length=255)
    program_desc = models.CharField(max_length=255,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'program_code')

class AgeGroup(models.Model):
    age_group_name = models.CharField(max_length=20, unique=True)
    age_group_desc = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Ethnicity(models.Model):
    ethnicity_abbr = models.CharField(max_length=5,unique=True)
    ethnicity_name = models.CharField(max_length=50,unique=True)
    ethnicity_desc = models.CharField(max_length=255,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
class Gender(models.Model):
    gender_abbr = models.CharField(max_length=1, unique=True)
    gender_name = models.CharField(max_length=10, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Race(models.Model):
    race_abbr = models.CharField(max_length=20,unique=True)
    race_name = models.CharField(max_length=50,unique=True)
    race_desc = models.CharField(max_length=255,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
class RaceCombo(models.Model):
    race_combo_flag = models.BooleanField()
    race_combo_name = models.CharField(max_length=20,unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class State(models.Model):
    state_ansi = models.CharField(max_length=2,unique=True)
    state_abbr = models.CharField(max_length=2,unique=True)
    state_name = models.CharField(max_length=50)
    state_desc = models.CharField(max_length=255,null=True)
    state_gnisid = models.CharField(max_length=10,null=True)
    sort_order = models.SmallIntegerField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class County(models.Model):
    state = models.ForeignKey(State)
    county_ansi = models.CharField(max_length=3)
    county_abbr = models.CharField(max_length=20)
    county_name = models.CharField(max_length=100)
    county_desc = models.CharField(max_length=255,null=True)
    sort_order = models.SmallIntegerField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('state', 'county_ansi')

### the actual data
class Cffr(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    county = models.ForeignKey(County)
    cffrprogram = models.ForeignKey(CffrProgram)
    amount = models.BigIntegerField()
    amount_per_capita = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state', 'county', 'cffrprogram')
        
class CffrState(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    cffrprogram = models.ForeignKey(CffrProgram)
    amount = models.BigIntegerField()
    amount_per_capita = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state', 'cffrprogram')
        
class CffrIndividualCounty(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    county = models.ForeignKey(County)
    amount = models.BigIntegerField()
    amount_per_capita = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state', 'county')

class CffrIndividualState(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    amount = models.BigIntegerField()
    amount_per_capita = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state')
        
class FederalTaxCollectionState(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    total = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    business_income = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    witheld_income_and_fica = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    notwitheld_income_and_seca = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    unemployment_insurance = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    railroad_retirement = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    estate_trust_income = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    estate = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    gift = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    excise = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    individual_total = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state')
        
class FoodSecurityState(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    household_total = models.IntegerField()
    no_response = models.IntegerField()
    food_secure = models.IntegerField()
    food_secure_percent = models.FloatField()
    food_secure_high = models.IntegerField(null=True)
    food_secure_high_percent = models.FloatField(null=True)
    food_secure_marginal = models.IntegerField(null=True)
    food_secure_marginal_percent = models.FloatField(null=True)
    food_secure_low = models.IntegerField()
    food_secure_low_percent = models.FloatField()
    food_secure_very_low = models.IntegerField()
    food_secure_very_low_percent = models.FloatField()
    food_insecure = models.IntegerField()
    food_insecure_percent = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state')
        
class LaborForceCounty(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    county = models.ForeignKey(County)
    laus_code = models.CharField(max_length=8)
    labor_force = models.IntegerField(null=True) #is this the civilian labor force?
    employment_total = models.IntegerField(null=True)
    unemployment_total = models.IntegerField(null=True)
    unemployment_rate = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state', 'county')
    
class LaborUnderutilizationState(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    u1 = models.FloatField()
    u2 = models.FloatField()
    u3 = models.FloatField()
    u4 = models.FloatField()
    u5 = models.FloatField()
    u6 = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state')
        
class MedianIncomeState(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    median_household_income = models.FloatField()
    median_household_income_moe = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state')

#July 2011.  Following models (PopulationCounty & PopulationState would, in theory, hold a normalized structure of every possible year, gender, race, ethnicity, & age combination for the census population estimates.  Because it wasn't practical to load & implement this highly normalized model in the API and search tool, the population data facets are presented as individual APIs.  This is easier, but it does mean we lose the ability to combine the facets (e.g., # of hispanic black females over 65).  Leaving the proposed model here for future reference.
#class PopulationCounty(models.Model):
#    year = models.IntegerField()
#    state = models.ForeignKey(State)
#    county = models.ForeignKey(County)
#    gender = models.ForeignKey(Gender)
#    race = models.ForeignKey(Race)
#    race_combo = models.ForeignKey(RaceCombo)
#    ethnicity = models.ForeignKey(Ethnicity)
#    age_group = models.ForeignKey(AgeGroup)
#    value = models.IntegerField()
#    create_date = models.DateField(auto_now_add=True)
#    update_date = models.DateField(auto_now=True)
#    
#    class Meta:
#        unique_together = ('year', 'state', 'county', 'gender', 'race', 'race_combo','ethnicity','age_group')

#class PopulationState(models.Model):
#    year = models.IntegerField()
#    state = models.ForeignKey(State)
#    gender = models.ForeignKey(Gender)
#    race = models.ForeignKey(Race)
#    race_combo = models.ForeignKey(RaceCombo)
#    ethnicity = models.ForeignKey(Ethnicity)
#    age_group = models.ForeignKey(AgeGroup)
#    value = models.IntegerField()
#    create_date = models.DateField(auto_now_add=True)
#    update_date = models.DateField(auto_now=True)
#    
#   class Meta:
#        unique_together = ('year', 'state', 'gender', 'race', 'race_combo','ethnicity','age_group')
    
class PopulationAgeCounty(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    county = models.ForeignKey(County)
    total = models.IntegerField()
    age_0_4 = models.IntegerField()
    age_0_4_percent = models.FloatField(null=True)
    age_5_9 = models.IntegerField()
    age_5_9_percent = models.FloatField(null=True)
    age_10_14 = models.IntegerField()
    age_10_14_percent = models.FloatField(null=True)
    age_15_19 = models.IntegerField()
    age_15_19_percent = models.FloatField(null=True)
    age_20_24 = models.IntegerField()
    age_20_24_percent = models.FloatField(null=True)
    age_25_29 = models.IntegerField()
    age_25_29_percent = models.FloatField(null=True)
    age_30_34 = models.IntegerField()
    age_30_34_percent = models.FloatField(null=True)
    age_35_39 = models.IntegerField()
    age_35_39_percent = models.FloatField(null=True)
    age_40_44 = models.IntegerField()
    age_40_44_percent = models.FloatField(null=True)
    age_45_49 = models.IntegerField()
    age_45_49_percent = models.FloatField(null=True)
    age_50_54 = models.IntegerField()
    age_50_54_percent = models.FloatField(null=True)
    age_55_59 = models.IntegerField()
    age_55_59_percent = models.FloatField(null=True)
    age_60_64 = models.IntegerField()
    age_60_64_percent = models.FloatField(null=True)
    age_65_69 = models.IntegerField()
    age_65_69_percent = models.FloatField(null=True)
    age_70_74 = models.IntegerField()
    age_70_74_percent = models.FloatField(null=True)
    age_75_79 = models.IntegerField()
    age_75_79_percent = models.FloatField(null=True)
    age_80_84 = models.IntegerField()
    age_80_84_percent = models.FloatField(null=True)
    age_85_over = models.IntegerField()
    age_85_over_percent = models.FloatField(null=True)
    age_65_over = models.IntegerField()
    age_65_over_percent = models.FloatField(null=True)
    age_0_19 = models.IntegerField()
    age_0_19_percent = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state', 'county')

class PopulationAgeState(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    total = models.IntegerField()
    age_0_4 = models.IntegerField()
    age_0_4_percent = models.FloatField(null=True)
    age_5_9 = models.IntegerField()
    age_5_9_percent = models.FloatField(null=True)
    age_10_14 = models.IntegerField()
    age_10_14_percent = models.FloatField(null=True)
    age_15_19 = models.IntegerField()
    age_15_19_percent = models.FloatField(null=True)
    age_20_24 = models.IntegerField()
    age_20_24_percent = models.FloatField(null=True)
    age_25_29 = models.IntegerField()
    age_25_29_percent = models.FloatField(null=True)
    age_30_34 = models.IntegerField()
    age_30_34_percent = models.FloatField(null=True)
    age_35_39 = models.IntegerField()
    age_35_39_percent = models.FloatField(null=True)
    age_40_44 = models.IntegerField()
    age_40_44_percent = models.FloatField(null=True)
    age_45_49 = models.IntegerField()
    age_45_49_percent = models.FloatField(null=True)
    age_50_54 = models.IntegerField()
    age_50_54_percent = models.FloatField(null=True)
    age_55_59 = models.IntegerField()
    age_55_59_percent = models.FloatField(null=True)
    age_60_64 = models.IntegerField()
    age_60_64_percent = models.FloatField(null=True)
    age_65_69 = models.IntegerField()
    age_65_69_percent = models.FloatField(null=True)
    age_70_74 = models.IntegerField()
    age_70_74_percent = models.FloatField(null=True)
    age_75_79 = models.IntegerField()
    age_75_79_percent = models.FloatField(null=True)
    age_80_84 = models.IntegerField()
    age_80_84_percent = models.FloatField(null=True)
    age_85_over = models.IntegerField()
    age_85_over_percent = models.FloatField(null=True)
    age_65_over = models.IntegerField()
    age_65_over_percent = models.FloatField(null=True)
    age_0_19 = models.IntegerField()
    age_0_19_percent = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state')

class PopulationGenderCounty(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    county = models.ForeignKey(County)
    total = models.IntegerField()
    female = models.IntegerField()
    female_percent = models.FloatField()
    male = models.IntegerField()
    male_percent = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True,auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state', 'county')

class PopulationGenderState(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    total = models.IntegerField()
    female = models.IntegerField()
    female_percent = models.FloatField()
    male = models.IntegerField()
    male_percent = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state')
        
class PopulationRaceCounty(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    county = models.ForeignKey(County)
    total = models.IntegerField()
    white_alone = models.IntegerField()
    white_alone_percent = models.FloatField()
    white_other = models.IntegerField(null=True)
    white_other_percent = models.FloatField(null=True)
    white_alone_hispanic = models.IntegerField(null=True)
    white_alone_hispanic_percent = models.FloatField(null=True)
    white_other_hispanic = models.IntegerField(null=True)
    white_other_hispanic_percent = models.FloatField(null=True)
    white_alone_nonhispanic = models.IntegerField(null=True)
    white_alone_nonhispanic_percent = models.FloatField(null=True)
    white_other_nonhispanic = models.IntegerField(null=True)
    white_other_nonhispanic_percent = models.FloatField(null=True)
    black_alone = models.IntegerField()
    black_alone_percent = models.FloatField()
    black_other = models.IntegerField(null=True)
    black_other_percent = models.FloatField(null=True)
    black_alone_hispanic = models.IntegerField(null=True)
    black_alone_hispanic_percent = models.FloatField(null=True)
    black_other_hispanic = models.IntegerField(null=True)
    black_other_hispanic_percent = models.FloatField(null=True)
    black_alone_nonhispanic = models.IntegerField(null=True)
    black_alone_nonhispanic_percent = models.FloatField(null=True)
    black_other_nonhispanic = models.IntegerField(null=True)
    black_other_nonhispanic_percent = models.FloatField(null=True)
    native_alone = models.IntegerField(null=True)
    native_alone_percent = models.FloatField(null=True)
    native_other = models.IntegerField(null=True)
    native_other_percent = models.FloatField(null=True)
    native_alone_hispanic = models.IntegerField(null=True)
    native_alone_hispanic_percent = models.FloatField(null=True)
    native_other_hispanic = models.IntegerField(null=True)
    native_other_hispanic_percent = models.FloatField(null=True)
    native_alone_nonhispanic = models.IntegerField(null=True)
    native_alone_nonhispanic_percent = models.FloatField(null=True)
    native_other_nonhispanic = models.IntegerField(null=True)
    native_other_nonhispanic_percent = models.FloatField(null=True)
    asian_alone = models.IntegerField(null=True)
    asian_alone_percent = models.FloatField(null=True)
    asian_other = models.IntegerField(null=True)
    asian_other_percent = models.FloatField(null=True)
    asian_alone_hispanic = models.IntegerField(null=True)
    asian_alone_hispanic_percent = models.FloatField(null=True)
    asian_other_hispanic = models.IntegerField(null=True)
    asian_other_hispanic_percent = models.FloatField(null=True)
    asian_alone_nonhispanic = models.IntegerField(null=True)
    asian_alone_nonhispanic_percent = models.FloatField(null=True)
    asian_other_nonhispanic = models.IntegerField(null=True)
    asian_other_nonhispanic_percent = models.FloatField(null=True)
    pacific_islander_alone = models.IntegerField(null=True)
    pacific_islander_alone_percent = models.FloatField(null=True)
    pacific_islander_other = models.IntegerField(null=True)
    pacific_islander_other_percent = models.FloatField(null=True)
    pacific_islander_alone_hispanic = models.IntegerField(null=True)
    pacific_islander_alone_hispanic_percent = models.FloatField(null=True)
    pacific_islander_other_hispanic = models.IntegerField(null=True)
    pacific_islander_other_hispanic_percent = models.FloatField(null=True)
    pacific_islander_alone_nonhispanic = models.IntegerField(null=True)
    pacific_islander_alone_nonhispanic_percent = models.FloatField(null=True)
    pacific_islander_other_nonhispanic = models.IntegerField(null=True)
    pacific_islander_other_nonhispanic_percent = models.FloatField(null=True)
    asian_pacific_islander_alone = models.IntegerField(null=True)
    asian_pacific_islander_alone_percent = models.FloatField(null=True)
    other = models.IntegerField(null=True)
    other_percent = models.FloatField(null=True)
    multiple_race = models.IntegerField(null=True)
    multiple_race_percent = models.FloatField(null=True)
    multiple_race_hispanic = models.IntegerField(null=True)
    multiple_race_hispanic_percent = models.FloatField(null=True)
    multiple_race_nonhispanic = models.IntegerField(null=True)
    multiple_race_nonhispanic_percent = models.FloatField(null=True)
    hispanic = models.IntegerField(null=True)
    hispanic_percent = models.FloatField(null=True)
    nonhispanic = models.IntegerField(null=True)
    nonhispanic_percent = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state', 'county')

class PopulationRaceState(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    total = models.IntegerField()
    white_alone = models.IntegerField()
    white_alone_percent = models.FloatField()
    white_other = models.IntegerField(null=True)
    white_other_percent = models.FloatField(null=True)
    white_alone_hispanic = models.IntegerField(null=True)
    white_alone_hispanic_percent = models.FloatField(null=True)
    white_other_hispanic = models.IntegerField(null=True)
    white_other_hispanic_percent = models.FloatField(null=True)
    white_alone_nonhispanic = models.IntegerField(null=True)
    white_alone_nonhispanic_percent = models.FloatField(null=True)
    white_other_nonhispanic = models.IntegerField(null=True)
    white_other_nonhispanic_percent = models.FloatField(null=True)
    black_alone = models.IntegerField()
    black_alone_percent = models.FloatField()
    black_other = models.IntegerField(null=True)
    black_other_percent = models.FloatField(null=True)
    black_alone_hispanic = models.IntegerField(null=True)
    black_alone_hispanic_percent = models.FloatField(null=True)
    black_other_hispanic = models.IntegerField(null=True)
    black_other_hispanic_percent = models.FloatField(null=True)
    black_alone_nonhispanic = models.IntegerField(null=True)
    black_alone_nonhispanic_percent = models.FloatField(null=True)
    black_other_nonhispanic = models.IntegerField(null=True)
    black_other_nonhispanic_percent = models.FloatField(null=True)
    native_alone = models.IntegerField(null=True)
    native_alone_percent = models.FloatField(null=True)
    native_other = models.IntegerField(null=True)
    native_other_percent = models.FloatField(null=True)
    native_alone_hispanic = models.IntegerField(null=True)
    native_alone_hispanic_percent = models.FloatField(null=True)
    native_other_hispanic = models.IntegerField(null=True)
    native_other_hispanic_percent = models.FloatField(null=True)
    native_alone_nonhispanic = models.IntegerField(null=True)
    native_alone_nonhispanic_percent = models.FloatField(null=True)
    native_other_nonhispanic = models.IntegerField(null=True)
    native_other_nonhispanic_percent = models.FloatField(null=True)
    asian_alone = models.IntegerField(null=True)
    asian_alone_percent = models.FloatField(null=True)
    asian_other = models.IntegerField(null=True)
    asian_other_percent = models.FloatField(null=True)
    asian_alone_hispanic = models.IntegerField(null=True)
    asian_alone_hispanic_percent = models.FloatField(null=True)
    asian_other_hispanic = models.IntegerField(null=True)
    asian_other_hispanic_percent = models.FloatField(null=True)
    asian_alone_nonhispanic = models.IntegerField(null=True)
    asian_alone_nonhispanic_percent = models.FloatField(null=True)
    asian_other_nonhispanic = models.IntegerField(null=True)
    asian_other_nonhispanic_percent = models.FloatField(null=True)
    pacific_islander_alone = models.IntegerField(null=True)
    pacific_islander_alone_percent = models.FloatField(null=True)
    pacific_islander_other = models.IntegerField(null=True)
    pacific_islander_other_percent = models.FloatField(null=True)
    pacific_islander_alone_hispanic = models.IntegerField(null=True)
    pacific_islander_alone_hispanic_percent = models.FloatField(null=True)
    pacific_islander_other_hispanic = models.IntegerField(null=True)
    pacific_islander_other_hispanic_percent = models.FloatField(null=True)
    pacific_islander_alone_nonhispanic = models.IntegerField(null=True)
    pacific_islander_alone_nonhispanic_percent = models.FloatField(null=True)
    pacific_islander_other_nonhispanic = models.IntegerField(null=True)
    pacific_islander_other_nonhispanic_percent = models.FloatField(null=True)
    asian_pacific_islander_alone = models.IntegerField(null=True)
    asian_pacific_islander_alone_percent = models.FloatField(null=True)
    other = models.IntegerField(null=True)
    other_percent = models.FloatField(null=True)
    multiple_race = models.IntegerField(null=True)
    multiple_race_percent = models.FloatField(null=True)
    multiple_race_hispanic = models.IntegerField(null=True)
    multiple_race_hispanic_percent = models.FloatField(null=True)
    multiple_race_nonhispanic = models.IntegerField(null=True)
    multiple_race_nonhispanic_percent = models.FloatField(null=True)
    hispanic = models.IntegerField(null=True)
    hispanic_percent = models.FloatField(null=True)
    nonhispanic = models.IntegerField(null=True)
    nonhispanic_percent = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state')

class PupilTeacherState(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    ratio = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True,auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state')
        
class TanfParticipationState(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    person = models.IntegerField(null=True)
    family = models.IntegerField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state')

class WicBenefitsState(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    amount = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state')

class WicParticipationState(models.Model):
    year = models.IntegerField()
    state = models.ForeignKey(State)
    value = models.FloatField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('year', 'state')