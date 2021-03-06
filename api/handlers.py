from piston.handler import BaseHandler, AnonymousBaseHandler
from npp_api.data.models import *
from django.conf import settings
from piston.doc import generate_doc
from django.http import Http404
from django.db import models
from django import db
import re

#for usability on commonly-used, normalized look-up values
alias_keys = {
    'state':'state_abbr'
}
def page_limits(request_get):    
    page = 1
    if 'page' in request_get:
        page = int(request_get['page'])

    lower_row = (page*settings.SEARCH_PAGINATE_BY) - settings.SEARCH_PAGINATE_BY
    upper_row = lower_row + settings.SEARCH_PAGINATE_BY
    
    return {'lower':lower_row, 'upper':upper_row}
    
def flatten(seq, container=None):
    if container is None:
        container = []
    for s in seq:
        if hasattr(s,'__iter__'):
            flatten(s,container)
        else:
            container.append(s)
    return container
    
def key_search(key, fieldlist):
    param_key = None
    for i in fieldlist:
        if hasattr(i, '__iter__'):
            if key in flatten(i):
                param_key = i[0]
        else:
            if key in i :
                param_key = key
    return param_key
        
class GenericHandler(BaseHandler):
    def __init__(self, allowed_keys, model, fields=None):
        self.model = model
        self.allowed_keys = allowed_keys
        self.fields = fields
        #self.exclude = exclude
        
        self.model_fields = []
        for f in self.model._meta.fields:
            self.model_fields.append(f.name)

    allowed_methods = ('GET',)
    
    def get_allowed_keys(self):
        return self.allowed_keys
        
    def get_actual_key(self, requested_key):
        actual_key = ''
        #is requested key an attribute of the handler's model?
        try:
            field = self.model._meta.get_field(requested_key)
            #if requested key is a FK, disregard
            if not isinstance(field,models.ForeignKey):
                actual_key = requested_key
        except:
            found_key = key_search(requested_key,self.fields)
            if found_key == requested_key:
                actual_key = requested_key
            elif found_key is not None:
                actual_key = str(found_key + '__' + requested_key)
        
        return actual_key

    def read(self, request, *args, **kwargs):
        if hasattr(self,'request'):
            request=self.request
            
        bound = page_limits(request.GET)
 
        params = {}
        for key,val in request.GET.items():
            if key in self.allowed_keys or alias_keys.has_key(key):
                actual_key = self.get_actual_key(key)
                if actual_key:
                    params[str(actual_key)] = val
                else:
                    #if requested key not found in the model or one
                    #of its related models, see if it's an alias
                    if alias_keys.has_key(key):
                        actual_key = self.get_actual_key(alias_keys[key])
                        if actual_key:
                            params[str(actual_key)] = val
        
        for key in kwargs: 
            if key in self.allowed_keys: 
                params[str(key)] = kwargs[key]
                
        records = self.model.objects.all() 
  
        # ADDED 01/05/2010 - allow a no_limit option for apps making large queries, 
        # else paginate normally
        if 'no_limit' in request.GET:
                no_limit = True
                records = records.filter(**params)
        else:
            records = records.filter(**params)[bound['lower']:bound['upper']]
        
        db.reset_queries()   
        return records

class AlternativeFuelVehiclesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'fips_state')
        model = AlternativeFuelVehicles
        super(AlternativeFuelVehiclesHandler, self).__init__(allowed_keys, model)
        
class AnsiCountyStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'ansi_state', 'code', 'county', 'ansi_class')
        model = AnsiCountyState
        super(AnsiCountyStateHandler, self).__init__(allowed_keys, model)
        
class AtCodesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('code',)
        model = AtCodes
        super(AtCodesHandler, self).__init__(allowed_keys, model)
        
class AverageTeacherSalaryHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = AverageTeacherSalary
        super(AverageTeacherSalaryHandler, self).__init__(allowed_keys, model)
        
class BilingualEdSpendingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = BilingualEdSpending
        super(BilingualEdSpendingHandler, self).__init__(allowed_keys, model)
        
class BudgetCategorySubfunctionsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('subfunction',)
        model = BudgetCategorySubfunctions
        super(BudgetCategorySubfunctionsHandler, self).__init__(allowed_keys, model)
        
class CfdaHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('program_number',)
        model = Cfda
        exclude = ('id',)
        super(CfdaHandler, self).__init__(allowed_keys, model)
        
class CffrHandler(GenericHandler):
    def __init__(self):
        #for the Cffr handler, allowed keys & field names depend on the
        #request params, so defer their definition until read() is performed
        self.allowed_keys = ()
        self.model = 'TBD'
        self.fields = ()
        
    def read(self, request, *args, **kwargs):
        self.request = request
        fields = ['year', 'amount', 'amount_per_capita', ('cffrprogram', ('program_code', 'program_name')), ('state', ('state_ansi', 'state_abbr', 'state_name'))]
        allowed_keys = ['year', 'program_code', 'state_abbr', 'state_ansi']
        aggregate = self.request.GET.get('total')
        if aggregate == 'state':
            self.model = CffrState
        else:
            #note we're not handling aggregate = country or sending back
            #any messages re: invalid values for the total param
            fields.append(('county',('county_ansi', 'county_name')))
            allowed_keys.append('county_ansi')
            allowed_keys.append('county_name')
            self.model = Cffr
        self.fields = tuple(fields)
        self.allowed_keys = tuple(allowed_keys)
        return super(CffrHandler, self).read(self, *args, **kwargs)
        
class CffrIndividualCountyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_ansi', 'state_abbr', 'county_ansi')
        fields = ('year', 'amount', 'amount_per_capita', ('state', ('state_ansi', 'state_abbr', 'state_name')),('county', ('county_ansi', 'county_name')))
        model = CffrIndividualCounty
        super(CffrIndividualCountyHandler, self).__init__(allowed_keys, model, fields)
        
class CffrIndividualStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_ansi', 'state_abbr')
        fields = ('year', 'amount', 'amount_per_capita', ('state', ('state_ansi', 'state_abbr', 'state_name')))
        model = CffrIndividualState
        super(CffrIndividualStateHandler, self).__init__(allowed_keys, model, fields)
        
class CffrAgencyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'agency_code', 'agency_name')
        model = CffrAgency
        super(CffrAgencyHandler, self).__init__(allowed_keys, model)
        
class CffrGeoHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'state_code', 'county_code', 'place_code', 'place_name', 'state_gu', 'type_gu', 'county_gu', 'place_gu', 'split_gu', 'congress_district')
        model = CffrGeo
        super(CffrGeoHandler, self).__init__(allowed_keys, model)
        
class CffrObjectCodeHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'object_code', 'category')
        model = CffrObjectCode
        super(CffrObjectCodeHandler, self).__init__(allowed_keys, model)
        
class CffrProgramHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'program_code', 'program_name')
        exclude = ('id', 'program_desc')
        model = CffrProgram
        super(CffrProgramHandler, self).__init__(allowed_keys, model)
        
class ChildrenPovertyStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'state_abbr', 'state_ansi', 'year')
        fields = ('year', 'children_total', 'children_total_moe',
            'children_poverty', 'children_poverty_moe',
            'children_poverty_percent', 'children_poverty_percent_moe',
            ('state', ('state_ansi', 'state_abbr', 'state_name')))
        model = ChildrenPovertyState
        super(ChildrenPovertyStateHandler, self).__init__(allowed_keys, model, fields)
        
class DiplomaRecipientTotalHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'key')
        model = DiplomaRecipientTotal
        super(DiplomaRecipientTotalHandler, self).__init__(allowed_keys, model)
        
class DropoutsRaceHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'key')
        model = DropoutsRace
        super(DropoutsRaceHandler, self).__init__(allowed_keys, model)
    
class DrugFreeSchoolSpendingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = DrugFreeSchoolSpending
        super(DrugFreeSchoolSpendingHandler, self).__init__(allowed_keys, model)
        
class EducationalAttainmentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state', 'gender', 'value_type', 'category')
        model = EducationalAttainment
        super(EducationalAttainmentHandler, self).__init__(allowed_keys, model)
        
class ElectricEmissionsStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'state_name', 'producer_type', 'energy_source')
        model = ElectricEmissionsState
        fields = ('year', ('state', ('state_ansi', 'state_abbr',
            'state_name')), 'producer_type', 'energy_source', 'co2', 'so2', 'nox')
        super(ElectricEmissionsStateHandler, self).__init__(allowed_keys, model, fields)
        
class EmploymentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = Employment
        super(EmploymentHandler, self).__init__(allowed_keys, model)
    
class EnergyConsumptionStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('msn_code', 'year', 'state_abbr', 'state_name', 'state_ansi')
        model = EnergyConsumptionState
        fields = ('year', 'value', ('state', ('state_ansi', 'state_abbr',
            'state_name')), ('msn', ('msn_code', 'msn_desc', 'msn_unit')))
        super(EnergyConsumptionStateHandler, self).__init__(allowed_keys, model, fields)
        
class EnergyProductionStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('msn_code', 'year', 'state_abbr', 'state_name', 'state_ansi')
        model = EnergyProductionState
        fields = ('year', 'value', ('state', ('state_ansi', 'state_abbr',
            'state_name')), ('msn', ('msn_code', 'msn_desc', 'msn_unit')))
        super(EnergyProductionStateHandler, self).__init__(allowed_keys, model, fields)

class EnergyExpendituresHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'msn', 'year', 'value', 'state')
        model = AnnualStateEnergyExpenditures
        super(EnergyExpendituresHandler, self).__init__(allowed_keys, model)
        
class EnrolledStudentsDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state', )
        model = EnrolledStudentsDistrict
        super(EnrolledStudentsDistrictHandler, self).__init__(allowed_keys, model)
        
class EnrollmentRaceHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'key')
        model = EnrollmentRace
        super(EnrollmentRaceHandler, self).__init__(allowed_keys, model)
        
class EnergyProductionEstimatesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'msn', 'year', 'value', 'state')
        model = StateEnergyProductionEstimates
        super(EnergyProductionEstimatesHandler, self).__init__(allowed_keys, model)

class EllStudentsDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = EllStudentsDistrict
        super(EllStudentsDistrictHandler, self).__init__(allowed_keys, model)
        
class ExpenditurePerPupilHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = ExpenditurePerPupil
        super(ExpenditurePerPupilHandler, self).__init__(allowed_keys, model)
        
class FamiliesPovertyStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'state_abbr', 'state_ansi', 'year')
        fields = ('year', 'families_total', 'families_total_moe',
            'families_poverty_percent', 'families_poverty_percent_moe',
            ('state', ('state_ansi', 'state_abbr', 'state_name')))
        model = FamiliesPovertyState
        super(FamiliesPovertyStateHandler, self).__init__(allowed_keys, model, fields)
        
class FcnaSpendingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = FcnaSpending
        super(FcnaSpendingHandler, self).__init__(allowed_keys, model)
        
class FederalImpactAidHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = FederalImpactAid
        super(FederalImpactAidHandler, self).__init__(allowed_keys, model)
        
class FederalTaxCollectionStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi')
        model = FederalTaxCollectionState
        fields = ('year', 'total', 'business_income', 'individual_total', 'witheld_income_and_fica',
            'notwitheld_income_and_seca', 'unemployment_insurance', 'railroad_retirement',
            'estate_trust_income', 'estate', 'gift', 'excise', 
            ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(FederalTaxCollectionStateHandler, self).__init__(allowed_keys, model,fields)
        
class FipsCountyCongressDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state_code', 'county_code', 'district_code', 'congress')
        model = FipsCountyCongressDistrict
        super(FipsCountyCongressDistrictHandler, self).__init__(allowed_keys, model)
        
class FipsStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('code', 'state')
        model = FipsState
        super(FipsStateHandler, self).__init__(allowed_keys, model)
        
class FoodSecurityStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi')
        model = FoodSecurityState
        fields = ('year', ('state', ('state_ansi', 'state_abbr', 'state_name')), 'household_total', 'no_response', 'food_secure', 'food_secure_percent', 'food_secure_high', 'food_secure_high_percent', 'food_secure_marginal', 'food_secure_marginal_percent', 'food_secure_low', 'food_secure_low_percent', 'food_secure_very_low', 'food_secure_very_low_percent', 'food_insecure', 'food_insecure_percent')
        super(FoodSecurityStateHandler, self).__init__(allowed_keys, model,fields)

class FreeLunchEligibleHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = FreeLunchEligible
        super(FreeLunchEligibleHandler, self).__init__(allowed_keys, model)
        
class FreeReducedLunchEligibleHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = FreeReducedLunchEligible
        super(FreeReducedLunchEligibleHandler, self).__init__(allowed_keys, model)
        
class FreeReducedLunchEligibleCountyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'county_name', 'year')
        model = FreeReducedLunchEligibleCounty
        super(FreeReducedLunchEligibleCountyHandler, self).__init__(allowed_keys, model)
        
class HalfPintsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = HalfPints
        super(HalfPintsHandler, self).__init__(allowed_keys, model)
        
class HeadStartEnrollmentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = HeadStartEnrollment
        super(HeadStartEnrollmentHandler, self).__init__(allowed_keys, model)
                
class HealthInsuranceStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = HealthInsuranceState
        fields = ('year', ('state', ('state_ansi', 'state_abbr', 'state_name')),
            'year', 'pop', 'pop_moe', 'pop_ins', 'pop_ins_percent', 
            'pop_no_ins', 'pop_no_ins_percent', 'pop_under_18',
            'pop_under_18_moe', 'pop_under_18_private',
            'pop_under_18_private_moe', 'pop_under_18_public',
            'pop_under_18_public_moe', 'pop_under_18_private_public',
            'pop_under_18_private_public_moe', 'pop_under_18_ins',
            'pop_under_18_ins_percent', 'pop_under_18_no_ins',
            'pop_under_18_no_ins_moe', 'pop_under_18_no_ins_percent',
            'pop_18_34', 'pop_18_34_moe', 'pop_18_34_private',
            'pop_18_34_private_moe', 'pop_18_34_public', 
            'pop_18_34_public_moe', 'pop_18_34_private_public',
            'pop_18_34_private_public_moe', 'pop_18_34_ins',
            'pop_18_34_ins_percent', 'pop_18_34_no_ins', 
            'pop_18_34_no_ins_moe', 'pop_18_34_no_ins_percent',
            'pop_35_64', 'pop_35_64_moe', 'pop_35_64_private',
            'pop_35_64_private_moe', 'pop_35_64_public',
            'pop_35_64_public_moe', 'pop_35_64_private_public',
            'pop_35_64_private_public_moe', 'pop_35_64_ins',
            'pop_35_64_ins_percent', 'pop_35_64_no_ins',
            'pop_35_64_no_ins_moe', 'pop_35_64_no_ins_percent',
            'pop_18_64', 'pop_18_64_private', 'pop_18_64_public',
            'pop_18_64_private_public', 'pop_18_64_ins', 
            'pop_18_64_ins_percent', 'pop_18_64_no_ins',
            'pop_18_64_no_ins_moe', 'pop_18_64_no_ins_percent',
            'pop_over_64', 'pop_over_64_moe', 'pop_over_64_private',
            'pop_over_64_private_moe', 'pop_over_64_public',
            'pop_over_64_public_moe', 'pop_over_64_private_public',
            'pop_over_64_private_public_moe', 'pop_over_64_ins',
            'pop_over_64_ins_percent', 'pop_over_64_no_ins',
            'pop_over_64_no_ins_moe', 'pop_over_64_no_ins_percent')
        super(HealthInsuranceStateHandler, self).__init__(allowed_keys, model, fields)

class HighSchoolDropoutsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = HighSchoolDropouts
        super(HighSchoolDropoutsHandler, self).__init__(allowed_keys, model)
        
class HighSchoolOtherHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'key')
        model = HighSchoolOther
        super(HighSchoolOtherHandler, self).__init__(allowed_keys, model)
                
class HousingOccupancyStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'state_name')
        model = HousingOccupancyState
        fields = ('year', ('state', ('state_ansi', 'state_abbr', 'state_name')),
            'total_units', 'total_units_moe', 'occupied_units', 'occupied_units_moe', 'occupied_units_percent',
            'occupied_units_percent_moe', 'vacant_units', 'vacant_units_moe', 'vacant_units_percent',
            'vacant_units_percent_moe', 'owner_occupied', 'owner_occupied_moe', 
            'owner_occupied_percent','owner_occupied_percent_moe', 'owner_vacancy_rate',
            'owner_vacancy_rate_moe', 'renter_occupied', 'renter_occupied_moe', 
           'renter_occupied_percent', 'renter_occupied_percent_moe', 'renter_vacancy_rate',
            'renter_vacancy_rate_moe')
        super(HousingOccupancyStateHandler, self).__init__(allowed_keys, model, fields)

class IndividualEducationProgramsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = IndividualEducationPrograms
        super(IndividualEducationProgramsHandler, self).__init__(allowed_keys, model)

class LaborForceCountyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'state_name', 'county_ansi', 'county_name')
        model = LaborForceCounty
        fields = ('year', ('state', ('state_ansi', 'state_abbr', 'state_name')), ('county', ('county_ansi', 'county_name')), 'laus_code', 'labor_force_total', 'employment_total', 'unemployment_total', 'unemployment_rate')
        super(LaborForceCountyHandler, self).__init__(allowed_keys, model,fields)
        
class LaborForceStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'state_name')
        model = LaborForceState
        fields = ('year', ('state', ('state_ansi', 'state_abbr', 'state_name')),
            'civilian_noninstitutional_pop', 'labor_force_total',
            'labor_force_participation_rate', 'employment_total',
            'employment_pop_rate', 'unemployment_total', 'unemployment_rate')
        super(LaborForceStateHandler, self).__init__(allowed_keys, model,fields)
        
class LaborUnderutilizationStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi')
        model = LaborUnderutilizationState
        fields = ('year', ('state', ('state_ansi', 'state_abbr', 'state_name')), 'u1', 'u2', 'u3', 'u4', 'u5', 'u6')
        super(LaborUnderutilizationStateHandler, self).__init__(allowed_keys, model,fields)
        
class MathScienceSpendingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = MathScienceSpending
        super(MathScienceSpendingHandler, self).__init__(allowed_keys, model)
        
class MedianIncomeStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi')
        model = MedianIncomeState
        fields = ('year', 'total', 'median_household_income', 'median_household_income_moe',
            ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(MedianIncomeStateHandler, self).__init__(allowed_keys, model,fields)

class MedicaidParticipationHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = MedicaidParticipation
        super(MedicaidParticipationHandler, self).__init__(allowed_keys, model)
        
class MedicareEnrollmentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = MedicareEnrollment
        super(MedicareEnrollmentHandler, self).__init__(allowed_keys, model)

class MigrantStudentsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = MigrantStudents
        super(MigrantStudentsHandler, self).__init__(allowed_keys, model)
        
class MilitaryPersonnelHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = MilitaryPersonnel
        super(MilitaryPersonnelHandler, self).__init__(allowed_keys, model)
        
class MsnHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('msn_code', 'msn_unit')
        fields = ('msn_code', 'msn_desc', 'msn_unit')
        model = Msn
        super(MsnHandler, self).__init__(allowed_keys, model, fields)
        
class NativeEdSpendingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = NativeEdSpending
        super(NativeEdSpendingHandler, self).__init__(allowed_keys, model)
        
class NewAidsCasesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = NewAidsCases
        super(NewAidsCasesHandler, self).__init__(allowed_keys, model)
        
class NcesSchoolDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'district_name', 'county_name', 'county_code', 'state_code', 'congress_code', 'district_code')
        model = NcesSchoolDistrict
        super(NcesSchoolDistrictHandler, self).__init__(allowed_keys, model)
        
class OtherFederalRevenueHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = OtherFederalRevenue
        super(OtherFederalRevenueHandler, self).__init__(allowed_keys, model)
        
class PeoplePovertyStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'state_abbr', 'state_ansi', 'year')
        model = PeoplePovertyState
        fields = ('year', 'total_population', 'value',
            'value_standard_error', 'percent',
            'percent_standard_error',
            ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(PeoplePovertyStateHandler, self).__init__(allowed_keys, model, fields)
        
class PopulationAgeCountyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'state_abbr', 'state_ansi', 'county_ansi', 'year')
        model = PopulationAgeCounty
        fields = ('year', 'total', 'age_0_4','age_0_4_percent','age_5_9','age_5_9_percent','age_10_14','age_10_14_percent','age_15_19','age_15_19_percent','age_20_24','age_20_24_percent','age_25_29','age_25_29_percent','age_30_34','age_30_34_percent','age_35_39','age_35_39_percent','age_40_44','age_40_44_percent','age_45_49','age_45_49_percent','age_50_54','age_50_54_percent','age_55_59','age_55_59_percent','age_60_64','age_60_64_percent','age_65_69','age_65_69_percent','age_70_74','age_70_74_percent','age_75_79','age_75_79_percent','age_80_84','age_80_84_percent','age_85_over','age_85_over_percent','age_65_over','age_65_over_percent','age_0_19','age_0_19_percent',('state', ('state_ansi', 'state_abbr', 'state_name')), ('county', ('county_ansi', 'county_name')))
        super(PopulationAgeCountyHandler, self).__init__(allowed_keys, model, fields)        

class PopulationAgeStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'state_abbr', 'state_ansi', 'year')
        model = PopulationAgeState
        #7/11: couldn't get documented regex feature to work (below), so typing in every freaking field in the model
        #fields = ('year', 'total', re.compile('^age_'), ('state', ('state_ansi', 'state_abbr', 'state_name')))
        fields = ('year', 'total', 'age_0_4','age_0_4_percent','age_5_9','age_5_9_percent','age_10_14','age_10_14_percent','age_15_19','age_15_19_percent','age_20_24','age_20_24_percent','age_25_29','age_25_29_percent','age_30_34','age_30_34_percent','age_35_39','age_35_39_percent','age_40_44','age_40_44_percent','age_45_49','age_45_49_percent','age_50_54','age_50_54_percent','age_55_59','age_55_59_percent','age_60_64','age_60_64_percent','age_65_69','age_65_69_percent','age_70_74','age_70_74_percent','age_75_79','age_75_79_percent','age_80_84','age_80_84_percent','age_85_over','age_85_over_percent','age_65_over','age_65_over_percent','age_0_19','age_0_19_percent',('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(PopulationAgeStateHandler, self).__init__(allowed_keys, model,fields)
        
class PopulationCongressionalDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'district', 'year')
        model = PopulationCongressionalDistrict
        super(PopulationCongressionalDistrictHandler, self).__init__(allowed_keys, model)
        
class PopulationFamiliesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = PopulationFamilies
        super(PopulationFamiliesHandler, self).__init__(allowed_keys, model)

class PopulationGenderCountyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'state_abbr', 'state_ansi', 'county_ansi', 'year')
        model = PopulationGenderCounty
        fields = ('year', 'total', 'female', 'female_percent', 'male', 'male_percent', ('state', ('state_ansi', 'state_abbr', 'state_name')), ('county', ('county_ansi', 'county_name')))
        super(PopulationGenderCountyHandler, self).__init__(allowed_keys, model, fields)        

class PopulationGenderStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'state_abbr', 'state_ansi', 'year')
        model = PopulationGenderState
        fields = ('year', 'total', 'female', 'female_percent', 'male', 'male_percent', ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(PopulationGenderStateHandler, self).__init__(allowed_keys, model, fields)
        
class PopulationRaceCountyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'state_abbr', 'state_ansi', 'county_ansi', 'year')
        model = PopulationRaceCounty
        fields = ('year', 'total', 'white_alone','white_alone_percent','white_other','white_other_percent','white_alone_hispanic','white_alone_hispanic_percent','white_other_hispanic','white_other_hispanic_percent','white_alone_nonhispanic','white_alone_nonhispanic_percent','white_other_nonhispanic','white_other_nonhispanic_percent','black_alone','black_alone_percent','black_other','black_other_percent','black_alone_hispanic','black_alone_hispanic_percent','black_other_hispanic','black_other_hispanic_percent','black_alone_nonhispanic','black_alone_nonhispanic_percent','black_other_nonhispanic','black_other_nonhispanic_percent','native_alone','native_alone_percent','native_other','native_other_percent','native_alone_hispanic','native_alone_hispanic_percent','native_other_hispanic','native_other_hispanic_percent','native_alone_nonhispanic','native_alone_nonhispanic_percent','native_other_nonhispanic','native_other_nonhispanic_percent','asian_alone','asian_alone_percent','asian_other','asian_other_percent','asian_alone_hispanic','asian_alone_hispanic_percent','asian_other_hispanic','asian_other_hispanic_percent','asian_alone_nonhispanic','asian_alone_nonhispanic_percent','asian_other_nonhispanic','asian_other_nonhispanic_percent','pacific_islander_alone','pacific_islander_alone_percent','pacific_islander_other','pacific_islander_other_percent','pacific_islander_alone_hispanic','pacific_islander_alone_hispanic_percent','pacific_islander_other_hispanic','pacific_islander_other_hispanic_percent','pacific_islander_alone_nonhispanic','pacific_islander_alone_nonhispanic_percent','pacific_islander_other_nonhispanic','pacific_islander_other_nonhispanic_percent','asian_pacific_islander_alone','asian_pacific_islander_alone_percent','other','other_percent','multiple_race','multiple_race_percent','multiple_race_hispanic','multiple_race_hispanic_percent','multiple_race_nonhispanic','multiple_race_nonhispanic_percent','hispanic','hispanic_percent','nonhispanic','nonhispanic_percent',('state', ('state_ansi', 'state_abbr', 'state_name')), ('county', ('county_ansi', 'county_name')))
        super(PopulationRaceCountyHandler, self).__init__(allowed_keys, model, fields)  
        
class PopulationRaceStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'state_abbr', 'state_ansi', 'year')
        model = PopulationRaceState
        fields = ('year', 'total','white_alone','white_alone_percent','white_other','white_other_percent','white_alone_hispanic','white_alone_hispanic_percent','white_other_hispanic','white_other_hispanic_percent','white_alone_nonhispanic','white_alone_nonhispanic_percent','white_other_nonhispanic','white_other_nonhispanic_percent','black_alone','black_alone_percent','black_other','black_other_percent','black_alone_hispanic','black_alone_hispanic_percent','black_other_hispanic','black_other_hispanic_percent','black_alone_nonhispanic','black_alone_nonhispanic_percent','black_other_nonhispanic','black_other_nonhispanic_percent','native_alone','native_alone_percent','native_other','native_other_percent','native_alone_hispanic','native_alone_hispanic_percent','native_other_hispanic','native_other_hispanic_percent','native_alone_nonhispanic','native_alone_nonhispanic_percent','native_other_nonhispanic','native_other_nonhispanic_percent','asian_alone','asian_alone_percent','asian_other','asian_other_percent','asian_alone_hispanic','asian_alone_hispanic_percent','asian_other_hispanic','asian_other_hispanic_percent','asian_alone_nonhispanic','asian_alone_nonhispanic_percent','asian_other_nonhispanic','asian_other_nonhispanic_percent','pacific_islander_alone','pacific_islander_alone_percent','pacific_islander_other','pacific_islander_other_percent','pacific_islander_alone_hispanic','pacific_islander_alone_hispanic_percent','pacific_islander_other_hispanic','pacific_islander_other_hispanic_percent','pacific_islander_alone_nonhispanic','pacific_islander_alone_nonhispanic_percent','pacific_islander_other_nonhispanic','pacific_islander_other_nonhispanic_percent','asian_pacific_islander_alone','asian_pacific_islander_alone_percent','other','other_percent','multiple_race','multiple_race_percent','multiple_race_hispanic','multiple_race_hispanic_percent','multiple_race_nonhispanic','multiple_race_nonhispanic_percent','hispanic','hispanic_percent','nonhispanic','nonhispanic_percent',('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(PopulationRaceStateHandler, self).__init__(allowed_keys, model, fields)

class PupilTeacherDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = PupilTeacherDistrict
        super(PupilTeacherDistrictHandler, self).__init__(allowed_keys, model) 
        
class PupilTeacherStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi')
        model = PupilTeacherState
        fields = ('year', 'ratio', ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(PupilTeacherStateHandler, self).__init__(allowed_keys, model, fields)
               
class PresidentsBudgetHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('budget_type', 'source_category_code', 'source_subcategory_code', 'agency_code', 'bureau_code', 'account_code', 'treasury_agency_code', 'subfunction_code', 'grant_non_grant')
        model = PresidentsBudget
        fields = ('budget_type', 'source_category_code', 'source_category_name',
            'source_subcategory_code', 'source_subcategory_name', 'agency_code',
            'agency_name', 'bureau_code', 'bureau_name', 'account_code',
            'account_name', 'treasury_agency_code', 'subfunction_code',
            'subfunction_title', 'bea_category', 'grant_non_grant',
            'on_off_budget', ('years', ('year', 'value',),),)
        super(PresidentsBudgetHandler, self).__init__(allowed_keys, model, fields)
        
class RetiredDisabledNilfHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = RetiredDisabledNilf
        super(RetiredDisabledNilfHandler, self).__init__(allowed_keys, model)
        
class SaipeSchoolHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'fips_state', 'ccd_district_id', 'district_name')
        model = SaipeSchool
        super(SaipeSchoolHandler, self).__init__(allowed_keys, model)
        
class SaipeCountyStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'fips_state', 'fips_county', 'state_county_name', 'state_postal_abbreviation')
        model = SaipeCountyState
        super(SaipeCountyStateHandler, self).__init__(allowed_keys, model)
        
class SchipEnrollmentStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'state_name')
        model = SchipEnrollmentState
        fields = ('year', 'value', ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(SchipEnrollmentStateHandler, self).__init__(allowed_keys, model, fields)

class SchoolBreakfastParticipationStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'state_name')
        model = SchoolBreakfastParticipationState
        fields = ('year', 'value', ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(SchoolBreakfastParticipationStateHandler, self).__init__(allowed_keys, model, fields)
        
class SchoolLunchParticipationStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'state_name')
        model = SchoolLunchParticipationState
        fields = ('year', 'value', ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(SchoolLunchParticipationStateHandler, self).__init__(allowed_keys, model, fields)
        
class ShelterPopulationHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = ShelterPopulation
        super(ShelterPopulationHandler, self).__init__(allowed_keys, model)
        
class SnapBenefitsRecipientsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state_fips', 'county_fips', 'name', 'year')
        model = SnapBenefitsRecipients
        super(SnapBenefitsRecipientsHandler, self).__init__(allowed_keys, model)
        
class SnapMonthlyBenefitsPersonStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'state_name')
        model = SnapMonthlyBenefitsPersonState
        fields = ('year', 'value', ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(SnapMonthlyBenefitsPersonStateHandler, self).__init__(allowed_keys, model, fields)
        
class SnapParticipationHouseholdsStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'state_name')
        model = SnapParticipationHouseholdsState
        fields = ('year', 'value', ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(SnapParticipationHouseholdsStateHandler, self).__init__(allowed_keys, model, fields)
        
class SnapParticipationPeopleStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'state_name')
        model = SnapParticipationPeopleState
        fields = ('year', 'value', ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(SnapParticipationPeopleStateHandler, self).__init__(allowed_keys, model, fields)
        
class SpecialEdFundingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = SpecialEdFunding
        super(SpecialEdFundingHandler, self).__init__(allowed_keys, model)
        
class StateCompletionRateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'key')
        model = StateCompletionRate
        super(StateCompletionRateHandler, self).__init__(allowed_keys, model)
      
class StateGdpHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = StateGdp
        super(StateGdpHandler, self).__init__(allowed_keys, model)

class StateGdpPre97Handler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = StateGdp
        super(StateGdpPre97Handler, self).__init__(allowed_keys, model)

class StatePostalCodesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('code', 'state')
        model = StatePostalCodes
        super(StatePostalCodesHandler, self).__init__(allowed_keys, model)
        
class SubfunctionsCffrHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('subfunction_number', 'cfda_program_code', 'at_code_1', 'at_code_2',
            'at_code_3', 'at_code_4', 'at_code_5', 'at_code_6' ,'at_code_7', 'at_code_8')
        model = SubfunctionsCffr
        super(SubfunctionsCffrHandler, self).__init__(allowed_keys, model)
        
class SummerLunchParticipationStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'state_name')
        model = SummerLunchParticipationState
        fields = ('year', 'value', ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(SummerLunchParticipationStateHandler, self).__init__(allowed_keys, model, fields)
        
class TanfParticipationStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi')
        model = TanfParticipationState
        fields = ('year', 'person', 'family', ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(TanfParticipationStateHandler, self).__init__(allowed_keys, model,fields)
        
class TitleIFundingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = TitleIFunding
        super(TitleIFundingHandler, self).__init__(allowed_keys, model)
        
class TotalStudentsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = TotalStudents
        super(TotalStudentsHandler, self).__init__(allowed_keys, model)
        
class UsaspendingAssistanceCountyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'program_number', 'county_ansi')
        model = UsaspendingAssistanceCounty
        fields = ('year', 'fed_funding', 'fed_funding_per_capita', 'loan_value',
            'loan_value_per_capita', 'loan_subsidy', 'loan_subsidy_per_capita',
            ('state', ('state_ansi', 'state_abbr', 'state_name')),
            ('cfda', ('program_title', 'program_number')),
            ('county', ('county_ansi', 'county_name')))
        super(UsaspendingAssistanceCountyHandler, self).__init__(allowed_keys, model, fields)
        
class UsaspendingAssistanceStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'program_number')
        model = UsaspendingAssistanceState
        fields = ('year', 'fed_funding', 'fed_funding_per_capita', 'loan_value',
            'loan_value_per_capita', 'loan_subsidy', 'loan_subsidy_per_capita',
            ('cfda', ('program_title', 'program_number')),
            ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(UsaspendingAssistanceStateHandler, self).__init__(allowed_keys, model, fields)
        
class VehicleRegistrationsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = VehicleRegistrations
        super(VehicleRegistrationsHandler, self).__init__(allowed_keys, model)
        
class VocationalEdSpendingHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'agency_name', 'agency_id')
        model = VocationalEdSpending
        super(VocationalEdSpendingHandler, self).__init__(allowed_keys, model)
        
class WicBenefitsStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'state_name')
        model = WicBenefitsState
        fields = ('year', 'amount', ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(WicBenefitsStateHandler, self).__init__(allowed_keys, model,fields)
        
class WicParticipationStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state_abbr', 'state_ansi', 'state_name')
        model = WicParticipationState
        fields = ('year', 'value', ('state', ('state_ansi', 'state_abbr', 'state_name')))
        super(WicParticipationStateHandler, self).__init__(allowed_keys, model,fields)
        
# BRENDAN 01/05/2010
class SCHIPHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'state_code', 'county_code', 'place_code', 'state_postal', 'congressional_district','program_code')
        model = Cffr
        super(CffrHandler, self).__init__(allowed_keys, model)

