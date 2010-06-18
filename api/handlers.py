from piston.handler import BaseHandler, AnonymousBaseHandler
from npp.data.models import AnnualStateEnergyConsumption, AnnualStateEnergyExpenditures, CFFR, StateEnergyProductionEstimates, MSNCodes, StatePostalCodes, FIPSState
from npp.data.models import ANSICountyState, FIPSCountyCongressDistrict, NCESSchoolDistrict, CFFRGeo, CFFRAgency, CFFRObjectCode, CFFRProgram, SAIPESchool
from npp.data.models import StateEmissions, IRSGrossCollections, VehicleRegistrations, StateMedianIncome, StatePopulationEstimates, SAIPECountyState
from npp.data.models import StateUnemployment, CountyUnemployment, AlternativeFuelVehicles, PresidentsBudget, NewAIDSCases, MedicaidParticipation, SCHIPEnrollment
from django.conf import settings
from piston.doc import generate_doc

def page_limits(request_get):    
    page = 1
    if 'page' in request_get:
        page = int(request_get['page'])

    lower_row = (page*settings.SEARCH_PAGINATE_BY) - settings.SEARCH_PAGINATE_BY
    upper_row = lower_row + settings.SEARCH_PAGINATE_BY
    
    return {'lower':lower_row, 'upper':upper_row}
    
class GenericHandler(BaseHandler):
    def __init__(self, allowed_keys, model, fields=None):
        self.model = model
        self.allowed_keys = allowed_keys
        self.fields = fields

    allowed_methods = ('GET',)

    def read(self, request):
        bound = page_limits(request.GET)

        params = {}
        for key,val in request.GET.items():
            if key in self.allowed_keys:
                params[str(key)] = val
 
        records = self.model.objects.all()           
        records = records.filter(**params)[bound['lower']:bound['upper']]
            
        return records
        
class AlternativeFuelVehiclesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'fips_state')
        model = AlternativeFuelVehicles
        super(AlternativeFuelVehiclesHandler, self).__init__(allowed_keys, model)
        
class ANSICountyStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'ansi_state', 'code', 'county', 'ansi_class')
        model = ANSICountyState
        super(ANSICountyStateHandler, self).__init__(allowed_keys, model)
        
class CFFRHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'state_code', 'county_code', 'place_code', 'state_postal', 'congressional_district', 'program_code', 'object_type', 'agency_code', 'funding_sign')
        model = CFFR
        super(CFFRHandler, self).__init__(allowed_keys, model)
        
class CFFRAgencyHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'agency_code', 'agency_name')
        model = CFFRAgency
        super(CFFRAgencyHandler, self).__init__(allowed_keys, model)
        
class CFFRGeoHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'state_code', 'county_code', 'place_code', 'place_name', 'state_gu', 'type_gu', 'county_gu', 'place_gu', 'split_gu', 'congress_district')
        model = CFFRGeo
        super(CFFRGeoHandler, self).__init__(allowed_keys, model)
        
class CFFRObjectCodeHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'object_code', 'category')
        model = CFFRObjectCode
        super(CFFRObjectCodeHandler, self).__init__(allowed_keys, model)
        
class CFFRProgramHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'program_id_code', 'program_name')
        model = CFFRProgram
        super(CFFRProgramHandler, self).__init__(allowed_keys, model)
        
class CountyUnemploymentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state_fips', 'county_fips', 'year')
        model = CountyUnemployment
        super(CountyUnemploymentHandler, self).__init__(allowed_keys, model)
    
class EnergyConsumptionHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'msn', 'year', 'value', 'state')
        model = AnnualStateEnergyConsumption
        super(EnergyConsumptionHandler, self).__init__(allowed_keys, model)

class EnergyExpendituresHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'msn', 'year', 'value', 'state')
        model = AnnualStateEnergyConsumption
        super(EnergyExpendituresHandler, self).__init__(allowed_keys, model)
        
class EnergyProductionEstimatesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'msn', 'year', 'value', 'state')
        model = StateEnergyProductionEstimates
        super(EnergyProductionEstimatesHandler, self).__init__(allowed_keys, model)
        
class FIPSCountyCongressDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state_code', 'county_code', 'district_code', 'congress')
        model = FIPSCountyCongressDistrict
        super(FIPSCountyCongressDistrictHandler, self).__init__(allowed_keys, model)
        
class IRSGrossCollectionsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = IRSGrossCollections
        super(IRSGrossCollectionsHandler, self).__init__(allowed_keys, model)

class MedicaidParticipationHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = MedicaidParticipation
        super(MedicaidParticipationHandler, self).__init__(allowed_keys, model)
        
class MSNCodeHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('msn', 'description', 'unit')
        model = MSNCodes
        super(MSNCodeHandler, self).__init__(allowed_keys, model)
        
class NewAIDSCasesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = NewAIDSCases
        super(NewAIDSCasesHandler, self).__init__(allowed_keys, model)
        
class NCESSchoolDistrictHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'district_name', 'county_name', 'county_code', 'state_code', 'congress_code', 'district_code')
        model = NCESSchoolDistrict
        super(NCESSchoolDistrictHandler, self).__init__(allowed_keys, model)
        
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
        
class SCHIPEnrollmentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = SCHIPEnrollment
        super(SCHIPEnrollmentHandler, self).__init__(allowed_keys, model)
        
class StateEmissionsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year', 'producer_type', 'energy_source')
        model = StateEmissions
        super(StateEmissionsHandler, self).__init__(allowed_keys, model)
        
class StateMedianIncomeHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'start_year', 'end_year')
        model = StateMedianIncome
        super(StateMedianIncomeHandler, self).__init__(allowed_keys, model)
        
class StatePopulationEstimatesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = StatePopulationEstimates
        super(StatePopulationEstimatesHandler, self).__init__(allowed_keys, model)
        
class StatePostalCodesHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('code', 'state')
        model = StatePostalCodes
        super(StatePostalCodesHandler, self).__init__(allowed_keys, model)
        
class StateUnemploymentHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('year', 'state')
        model = StateUnemployment
        super(StateUnemploymentHandler, self).__init__(allowed_keys, model)
        
class FIPSStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('code', 'state')
        model = FIPSState
        super(FIPSStateHandler, self).__init__(allowed_keys, model)
        
class SAIPESchoolHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'fips_state', 'ccd_district_id', 'district_name')
        model = SAIPESchool
        super(SAIPESchoolHandler, self).__init__(allowed_keys, model)
        
class SAIPECountyStateHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('id', 'year', 'fips_state', 'fips_county', 'state_county_name', 'state_postal_abbreviation')
        model = SAIPECountyState
        super(SAIPECountyStateHandler, self).__init__(allowed_keys, model)
        
class VehicleRegistrationsHandler(GenericHandler):
    def __init__(self):
        allowed_keys = ('state', 'year')
        model = VehicleRegistrations
        super(VehicleRegistrationsHandler, self).__init__(allowed_keys, model)