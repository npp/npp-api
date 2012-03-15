# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('data_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('data', ['Category'])

        # Adding model 'Source'
        db.create_table('data_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Category'])),
            ('string_id', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('data', ['Source'])

        # Adding model 'AlternativeFuelVehicles'
        db.create_table('data_alternativefuelvehicles', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['AlternativeFuelVehicles'])

        # Adding model 'AnnualStateEnergyConsumption'
        db.create_table('data_annualstateenergyconsumption', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('msn', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal('data', ['AnnualStateEnergyConsumption'])

        # Adding model 'AnnualStateEnergyExpenditures'
        db.create_table('data_annualstateenergyexpenditures', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('msn', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal('data', ['AnnualStateEnergyExpenditures'])

        # Adding model 'AnsiCountyState'
        db.create_table('data_ansicountystate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('ansi_state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ansi_class', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('data', ['AnsiCountyState'])

        # Adding model 'AnsiState'
        db.create_table('data_ansistate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ansi_state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('state_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('gnisid', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('data', ['AnsiState'])

        # Adding model 'AtCodes'
        db.create_table('data_atcodes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('assistance_type', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('data', ['AtCodes'])

        # Adding model 'AverageTeacherSalary'
        db.create_table('data_averageteachersalary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['AverageTeacherSalary'])

        # Adding model 'BilingualEdSpending'
        db.create_table('data_bilingualedspending', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['BilingualEdSpending'])

        # Adding model 'BudgetCategorySubfunctions'
        db.create_table('data_budgetcategorysubfunctions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subfunction', self.gf('django.db.models.fields.TextField')(max_length=3)),
            ('npp_budget_category', self.gf('django.db.models.fields.TextField')(max_length=64)),
        ))
        db.send_create_signal('data', ['BudgetCategorySubfunctions'])

        # Adding model 'CffrRaw'
        db.create_table('data_cffrraw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('county_code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('place_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('state_postal', self.gf('django.db.models.fields.CharField')(max_length=2, null=True)),
            ('county_name', self.gf('django.db.models.fields.CharField')(max_length=24, null=True)),
            ('place_name', self.gf('django.db.models.fields.CharField')(max_length=24, null=True)),
            ('population', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('congress_district', self.gf('django.db.models.fields.CharField')(max_length=34, null=True)),
            ('program_code', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('object_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_code', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('funding_sign', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('amount', self.gf('django.db.models.fields.BigIntegerField')()),
            ('amount_adjusted', self.gf('django.db.models.fields.BigIntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['CffrRaw'])

        # Adding model 'CffrAgency'
        db.create_table('data_cffragency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('agency_code', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=90)),
        ))
        db.send_create_signal('data', ['CffrAgency'])

        # Adding model 'CffrGeo'
        db.create_table('data_cffrgeo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('county_code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('place_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('place_name', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('state_gu', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('type_gu', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('county_gu', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('place_gu', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('split_gu', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('population', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('congress_district', self.gf('django.db.models.fields.CharField')(max_length=34, null=True)),
        ))
        db.send_create_signal('data', ['CffrGeo'])

        # Adding model 'CffrObjectCode'
        db.create_table('data_cffrobjectcode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('data', ['CffrObjectCode'])

        # Adding model 'CffrProgramRaw'
        db.create_table('data_cffrprogramraw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('program_id_code', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('program_name', self.gf('django.db.models.fields.CharField')(max_length=74)),
        ))
        db.send_create_signal('data', ['CffrProgramRaw'])

        # Adding model 'ChildrenPoverty'
        db.create_table('data_childrenpoverty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('children_total', self.gf('django.db.models.fields.IntegerField')()),
            ('children_total_moe', self.gf('django.db.models.fields.IntegerField')()),
            ('children_poverty', self.gf('django.db.models.fields.IntegerField')()),
            ('children_poverty_moe', self.gf('django.db.models.fields.IntegerField')()),
            ('children_poverty_percent', self.gf('django.db.models.fields.FloatField')()),
            ('children_poverty_percent_moe', self.gf('django.db.models.fields.FloatField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['ChildrenPoverty'])

        # Adding model 'DiplomaRecipientTotal'
        db.create_table('data_diplomarecipienttotal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['DiplomaRecipientTotal'])

        # Adding model 'DropoutsRace'
        db.create_table('data_dropoutsrace', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['DropoutsRace'])

        # Adding model 'DrugFreeSchoolSpending'
        db.create_table('data_drugfreeschoolspending', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['DrugFreeSchoolSpending'])

        # Adding model 'EducationalAttainment'
        db.create_table('data_educationalattainment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.TextField')(max_length=32)),
            ('gender', self.gf('django.db.models.fields.TextField')(max_length=16)),
            ('value_type', self.gf('django.db.models.fields.TextField')(max_length=16)),
            ('category', self.gf('django.db.models.fields.TextField')(max_length=64)),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['EducationalAttainment'])

        # Adding model 'EllStudentsDistrict'
        db.create_table('data_ellstudentsdistrict', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['EllStudentsDistrict'])

        # Adding model 'Employment'
        db.create_table('data_employment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('total_civilian_labor_force', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('white_civilian_labor_force', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('black_civilian_labor_force', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('hispanic_civilian_labor_force', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('white_unemployed', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('black_unemployed', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('hispanic_unemployed', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal('data', ['Employment'])

        # Adding model 'EnrolledStudentsDistrict'
        db.create_table('data_enrolledstudentsdistrict', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['EnrolledStudentsDistrict'])

        # Adding model 'EnrollmentRace'
        db.create_table('data_enrollmentrace', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['EnrollmentRace'])

        # Adding model 'ExpenditurePerPupil'
        db.create_table('data_expenditureperpupil', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['ExpenditurePerPupil'])

        # Adding model 'FamiliesPoverty'
        db.create_table('data_familiespoverty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('families_total', self.gf('django.db.models.fields.IntegerField')()),
            ('families_total_moe', self.gf('django.db.models.fields.IntegerField')()),
            ('families_poverty_percent', self.gf('django.db.models.fields.FloatField')()),
            ('families_poverty_percent_moe', self.gf('django.db.models.fields.FloatField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['FamiliesPoverty'])

        # Adding model 'FcnaSpending'
        db.create_table('data_fcnaspending', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['FcnaSpending'])

        # Adding model 'FederalImpactAid'
        db.create_table('data_federalimpactaid', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['FederalImpactAid'])

        # Adding model 'FederalTaxCollectionStateRaw'
        db.create_table('data_federaltaxcollectionstateraw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('total_collections', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('business_income_taxes', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('income_employment_estate_trust_total', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('individual_witheld_fica', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('individual_notwitheld_seca', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('unemployment_insurance', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('railroad_retirement', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('estate_trust_income_tax', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('estate_tax', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('gift_tax', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('excise_taxes', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['FederalTaxCollectionStateRaw'])

        # Adding model 'FipsCountyCongressDistrict'
        db.create_table('data_fipscountycongressdistrict', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('county_code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('district_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('congress', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['FipsCountyCongressDistrict'])

        # Adding model 'FipsState'
        db.create_table('data_fipsstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('data', ['FipsState'])

        # Adding model 'FoodSecurityStateRaw'
        db.create_table('data_foodsecuritystateraw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('household_total', self.gf('django.db.models.fields.IntegerField')()),
            ('no_response', self.gf('django.db.models.fields.IntegerField')()),
            ('food_secure', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('food_secure_high', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('food_secure_marginal', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('food_secure_low', self.gf('django.db.models.fields.IntegerField')()),
            ('food_secure_very_low', self.gf('django.db.models.fields.IntegerField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['FoodSecurityStateRaw'])

        # Adding model 'FreeLunchEligible'
        db.create_table('data_freeluncheligible', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['FreeLunchEligible'])

        # Adding model 'FreeReducedLunchEligible'
        db.create_table('data_freereducedluncheligible', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['FreeReducedLunchEligible'])

        # Adding model 'FreeReducedLunchEligibleCounty'
        db.create_table('data_freereducedluncheligiblecounty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('county_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['FreeReducedLunchEligibleCounty'])

        # Adding model 'HalfPints'
        db.create_table('data_halfpints', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['HalfPints'])

        # Adding model 'HeadStartEnrollment'
        db.create_table('data_headstartenrollment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('funding', self.gf('django.db.models.fields.IntegerField')()),
            ('enrollment', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['HeadStartEnrollment'])

        # Adding model 'HealthInsurance'
        db.create_table('data_healthinsurance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('all_people', self.gf('django.db.models.fields.IntegerField')()),
            ('not_covered', self.gf('django.db.models.fields.IntegerField')()),
            ('not_covered_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('not_covered_pct', self.gf('django.db.models.fields.FloatField')()),
            ('not_covered_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('covered', self.gf('django.db.models.fields.IntegerField')()),
            ('covered_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('covered_pct', self.gf('django.db.models.fields.FloatField')()),
            ('covered_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('private', self.gf('django.db.models.fields.IntegerField')()),
            ('private_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('private_pct', self.gf('django.db.models.fields.FloatField')()),
            ('private_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('private_employment', self.gf('django.db.models.fields.IntegerField')()),
            ('private_employment_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('private_employment_pct', self.gf('django.db.models.fields.FloatField')()),
            ('private_employment_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('direct_purchase', self.gf('django.db.models.fields.IntegerField')()),
            ('direct_purchase_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('direct_purchase_pct', self.gf('django.db.models.fields.FloatField')()),
            ('direct_purchase_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('govt', self.gf('django.db.models.fields.IntegerField')()),
            ('govt_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('govt_pct', self.gf('django.db.models.fields.FloatField')()),
            ('govt_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('medicaid', self.gf('django.db.models.fields.IntegerField')()),
            ('medicaid_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('medicaid_pct', self.gf('django.db.models.fields.FloatField')()),
            ('medicaid_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('medicare', self.gf('django.db.models.fields.IntegerField')()),
            ('medicare_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('medicare_pct', self.gf('django.db.models.fields.FloatField')()),
            ('medicare_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('military', self.gf('django.db.models.fields.IntegerField')()),
            ('military_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('military_pct', self.gf('django.db.models.fields.FloatField')()),
            ('military_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal('data', ['HealthInsurance'])

        # Adding model 'HighSchoolDropouts'
        db.create_table('data_highschooldropouts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['HighSchoolDropouts'])

        # Adding model 'HighSchoolOther'
        db.create_table('data_highschoolother', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['HighSchoolOther'])

        # Adding model 'HousingUnits'
        db.create_table('data_housingunits', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['HousingUnits'])

        # Adding model 'IndividualEducationPrograms'
        db.create_table('data_individualeducationprograms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['IndividualEducationPrograms'])

        # Adding model 'KidsHealthInsurance'
        db.create_table('data_kidshealthinsurance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('all_people', self.gf('django.db.models.fields.IntegerField')()),
            ('not_covered', self.gf('django.db.models.fields.IntegerField')()),
            ('not_covered_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('not_covered_pct', self.gf('django.db.models.fields.FloatField')()),
            ('not_covered_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('covered', self.gf('django.db.models.fields.IntegerField')()),
            ('covered_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('covered_pct', self.gf('django.db.models.fields.FloatField')()),
            ('covered_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('private', self.gf('django.db.models.fields.IntegerField')()),
            ('private_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('private_pct', self.gf('django.db.models.fields.FloatField')()),
            ('private_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('private_employment', self.gf('django.db.models.fields.IntegerField')()),
            ('private_employment_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('private_employment_pct', self.gf('django.db.models.fields.FloatField')()),
            ('private_employment_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('direct_purchase', self.gf('django.db.models.fields.IntegerField')()),
            ('direct_purchase_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('direct_purchase_pct', self.gf('django.db.models.fields.FloatField')()),
            ('direct_purchase_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('govt', self.gf('django.db.models.fields.IntegerField')()),
            ('govt_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('govt_pct', self.gf('django.db.models.fields.FloatField')()),
            ('govt_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('medicaid', self.gf('django.db.models.fields.IntegerField')()),
            ('medicaid_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('medicaid_pct', self.gf('django.db.models.fields.FloatField')()),
            ('medicaid_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('medicare', self.gf('django.db.models.fields.IntegerField')()),
            ('medicare_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('medicare_pct', self.gf('django.db.models.fields.FloatField')()),
            ('medicare_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('military', self.gf('django.db.models.fields.IntegerField')()),
            ('military_se', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('military_pct', self.gf('django.db.models.fields.FloatField')()),
            ('military_pct_se', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal('data', ['KidsHealthInsurance'])

        # Adding model 'LaborForceCountyRaw'
        db.create_table('data_laborforcecountyraw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('laus_code', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('state_fips', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('county_fips', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('county_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('labor_force', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('employed', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('unemployed', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('unemployment_rate', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['LaborForceCountyRaw'])

        # Adding model 'LaborUnderutilizationStateRaw'
        db.create_table('data_laborunderutilizationstateraw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('u1', self.gf('django.db.models.fields.FloatField')()),
            ('u2', self.gf('django.db.models.fields.FloatField')()),
            ('u3', self.gf('django.db.models.fields.FloatField')()),
            ('u4', self.gf('django.db.models.fields.FloatField')()),
            ('u5', self.gf('django.db.models.fields.FloatField')()),
            ('u6', self.gf('django.db.models.fields.FloatField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['LaborUnderutilizationStateRaw'])

        # Adding model 'MathScienceSpending'
        db.create_table('data_mathsciencespending', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['MathScienceSpending'])

        # Adding model 'MedicaidParticipation'
        db.create_table('data_medicaidparticipation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['MedicaidParticipation'])

        # Adding model 'MedicareEnrollment'
        db.create_table('data_medicareenrollment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['MedicareEnrollment'])

        # Adding model 'MigrantStudents'
        db.create_table('data_migrantstudents', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['MigrantStudents'])

        # Adding model 'MilitaryPersonnel'
        db.create_table('data_militarypersonnel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('military_personnel', self.gf('django.db.models.fields.IntegerField')()),
            ('civilian_personnel', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('reserve_national_guard_personnel', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['MilitaryPersonnel'])

        # Adding model 'MsnCodes'
        db.create_table('data_msncodes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('msn', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('data', ['MsnCodes'])

        # Adding model 'NativeEdSpending'
        db.create_table('data_nativeedspending', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['NativeEdSpending'])

        # Adding model 'NcesSchoolDistrict'
        db.create_table('data_ncesschooldistrict', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('district_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('county_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('county_code', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('state_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('congress_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('district_code', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('data', ['NcesSchoolDistrict'])

        # Adding model 'NewAidsCases'
        db.create_table('data_newaidscases', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['NewAidsCases'])

        # Adding model 'OtherFederalRevenue'
        db.create_table('data_otherfederalrevenue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['OtherFederalRevenue'])

        # Adding model 'OwnersRenters'
        db.create_table('data_ownersrenters', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
            ('not_in_universe', self.gf('django.db.models.fields.IntegerField')()),
            ('owned', self.gf('django.db.models.fields.IntegerField')()),
            ('rented', self.gf('django.db.models.fields.IntegerField')()),
            ('rented_no_cash', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['OwnersRenters'])

        # Adding model 'PeopleInPoverty'
        db.create_table('data_peopleinpoverty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('total_population', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('value_standard_error', self.gf('django.db.models.fields.IntegerField')()),
            ('percent', self.gf('django.db.models.fields.FloatField')()),
            ('percent_standard_error', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('data', ['PeopleInPoverty'])

        # Adding model 'PopulationCongressionalDistrict'
        db.create_table('data_populationcongressionaldistrict', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('district', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('white_alone', self.gf('django.db.models.fields.IntegerField')()),
            ('black_alone', self.gf('django.db.models.fields.IntegerField')()),
            ('american_indian_alaskan_alone', self.gf('django.db.models.fields.IntegerField')()),
            ('asian_alone', self.gf('django.db.models.fields.IntegerField')()),
            ('hawaiian_pacific_island_alone', self.gf('django.db.models.fields.IntegerField')()),
            ('other_alone', self.gf('django.db.models.fields.IntegerField')()),
            ('two_or_more_races', self.gf('django.db.models.fields.IntegerField')()),
            ('households', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['PopulationCongressionalDistrict'])

        # Adding model 'PopulationEst00Raw'
        db.create_table('data_populationest00raw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sumlev', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('stname', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('ctyname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('ethnic_origin', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('race', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('estimatesbase2000', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('popestimate2000', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('popestimate2001', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('popestimate2002', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('popestimate2003', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('popestimate2004', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('popestimate2005', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('popestimate2006', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('popestimate2007', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('popestimate2008', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('popestimate2009', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('census2010pop', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('popestimate2010', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['PopulationEst00Raw'])

        # Adding unique constraint on 'PopulationEst00Raw', fields ['state', 'county', 'gender', 'ethnic_origin', 'race']
        db.create_unique('data_populationest00raw', ['state', 'county', 'gender', 'ethnic_origin', 'race'])

        # Adding model 'PopulationEst90Raw'
        db.create_table('data_populationest90raw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('agegrp', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('race_gender', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('ethnic_origin', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('population', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['PopulationEst90Raw'])

        # Adding unique constraint on 'PopulationEst90Raw', fields ['year', 'state', 'county', 'agegrp', 'race_gender', 'ethnic_origin']
        db.create_unique('data_populationest90raw', ['year', 'state', 'county', 'agegrp', 'race_gender', 'ethnic_origin'])

        # Adding model 'PopulationFamilies'
        db.create_table('data_populationfamilies', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['PopulationFamilies'])

        # Adding model 'PupilTeacherDistrict'
        db.create_table('data_pupilteacherdistrict', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal('data', ['PupilTeacherDistrict'])

        # Adding model 'PresidentsBudget'
        db.create_table('data_presidentsbudget', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('budget_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('source_category_code', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('source_category_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('source_subcategory_code', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('source_subcategory_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('agency_code', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('bureau_code', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('bureau_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('account_code', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('account_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('treasury_agency_code', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('subfunction_code', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('subfunction_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('bea_category', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('grant_non_grant', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('on_off_budget', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('data', ['PresidentsBudget'])

        # Adding model 'PresidentsBudgetYear'
        db.create_table('data_presidentsbudgetyear', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('budget', self.gf('django.db.models.fields.related.ForeignKey')(related_name='years', to=orm['data.PresidentsBudget'])),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['PresidentsBudgetYear'])

        # Adding model 'PupilTeacherStateRaw'
        db.create_table('data_pupilteacherstateraw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('ratio', self.gf('django.db.models.fields.FloatField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['PupilTeacherStateRaw'])

        # Adding model 'RetiredDisabledNilf'
        db.create_table('data_retireddisablednilf', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
            ('employed_at_work', self.gf('django.db.models.fields.IntegerField')()),
            ('employed_absent', self.gf('django.db.models.fields.IntegerField')()),
            ('employed_on_layoff', self.gf('django.db.models.fields.IntegerField')()),
            ('unemployed_looking', self.gf('django.db.models.fields.IntegerField')()),
            ('retired_not_in_labor_force', self.gf('django.db.models.fields.IntegerField')()),
            ('disabled_not_in_labor_force', self.gf('django.db.models.fields.IntegerField')()),
            ('other_not_in_labor_force', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['RetiredDisabledNilf'])

        # Adding model 'SchipEnrollment'
        db.create_table('data_schipenrollment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['SchipEnrollment'])

        # Adding model 'StateCompletionRate'
        db.create_table('data_statecompletionrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['StateCompletionRate'])

        # Adding model 'StateLaborForceParticipation'
        db.create_table('data_statelaborforceparticipation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('civilian_noninstitutional_pop', self.gf('django.db.models.fields.IntegerField')()),
            ('civilian_labor_force', self.gf('django.db.models.fields.IntegerField')()),
            ('labor_force_participation_rate', self.gf('django.db.models.fields.FloatField')()),
            ('employment_total', self.gf('django.db.models.fields.IntegerField')()),
            ('employment_pop_rate', self.gf('django.db.models.fields.FloatField')()),
            ('unemployment_total', self.gf('django.db.models.fields.IntegerField')()),
            ('unemployment_rate', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('data', ['StateLaborForceParticipation'])

        # Adding model 'StateRenewableEnergy'
        db.create_table('data_staterenewableenergy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('fossil_coal', self.gf('django.db.models.fields.FloatField')()),
            ('fossil_gas', self.gf('django.db.models.fields.FloatField')()),
            ('fossil_oil', self.gf('django.db.models.fields.FloatField')()),
            ('nuclear_electric', self.gf('django.db.models.fields.FloatField')()),
            ('renewable_biofuels', self.gf('django.db.models.fields.FloatField')()),
            ('renewable_other', self.gf('django.db.models.fields.FloatField')()),
            ('renewable_total', self.gf('django.db.models.fields.FloatField')()),
            ('total', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('data', ['StateRenewableEnergy'])

        # Adding model 'SaipeSchool'
        db.create_table('data_saipeschool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('fips_state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('ccd_district_id', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('district_name', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('population', self.gf('django.db.models.fields.IntegerField')()),
            ('relevant_population', self.gf('django.db.models.fields.IntegerField')()),
            ('relevant_population_poverty', self.gf('django.db.models.fields.IntegerField')()),
            ('file_stamp', self.gf('django.db.models.fields.CharField')(max_length=21)),
        ))
        db.send_create_signal('data', ['SaipeSchool'])

        # Adding model 'SaipeCountyState'
        db.create_table('data_saipecountystate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('fips_state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('fips_county', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('all_age_poverty', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('all_age_poverty_90_lower', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('all_age_poverty_90_upper', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('all_age_poverty_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('all_age_poverty_percent_90_lower', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('all_age_poverty_percent_90_upper', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_0_17_poverty', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('age_0_17_poverty_90_lower', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('age_0_17_poverty_90_upper', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('age_0_17_poverty_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_0_17_poverty_percent_90_lower', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_0_17_poverty_percent_90_upper', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_5_17_related_poverty', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('age_5_17_related_poverty_90_lower', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('age_5_17_related_poverty_90_upper', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('age_5_17_related_poverty_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_5_17_related_poverty_percent_90_lower', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_5_17_related_poverty_percent_90_upper', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('median_household_income', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('median_household_income_90_lower', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('median_household_income_90_upper', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('age_0_5_poverty', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('age_0_5_poverty_90_lower', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('age_0_5_poverty_90_upper', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('age_0_5_poverty_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_0_5_poverty_percent_90_lower', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_0_5_poverty_percent_90_upper', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('state_county_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('state_postal_abbreviation', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('file_tag', self.gf('django.db.models.fields.CharField')(max_length=22)),
        ))
        db.send_create_signal('data', ['SaipeCountyState'])

        # Adding model 'SchoolBreakfastParticipation'
        db.create_table('data_schoolbreakfastparticipation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['SchoolBreakfastParticipation'])

        # Adding model 'SchoolLunchParticipation'
        db.create_table('data_schoollunchparticipation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['SchoolLunchParticipation'])

        # Adding model 'ShelterPopulation'
        db.create_table('data_shelterpopulation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('percent', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal('data', ['ShelterPopulation'])

        # Adding model 'SnapBenefitsRecipients'
        db.create_table('data_snapbenefitsrecipients', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state_fips', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('county_fips', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['SnapBenefitsRecipients'])

        # Adding model 'SnapMonthlyBenefitsPerson'
        db.create_table('data_snapmonthlybenefitsperson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('data', ['SnapMonthlyBenefitsPerson'])

        # Adding model 'SnapParticipationHouseholds'
        db.create_table('data_snapparticipationhouseholds', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['SnapParticipationHouseholds'])

        # Adding model 'SnapParticipationPeople'
        db.create_table('data_snapparticipationpeople', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['SnapParticipationPeople'])

        # Adding model 'SpecialEdFunding'
        db.create_table('data_specialedfunding', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['SpecialEdFunding'])

        # Adding model 'StateEmissions'
        db.create_table('data_stateemissions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('producer_type', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('energy_source', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('co2', self.gf('django.db.models.fields.IntegerField')()),
            ('so2', self.gf('django.db.models.fields.IntegerField')()),
            ('nox', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['StateEmissions'])

        # Adding model 'StateEnergyProductionEstimates'
        db.create_table('data_stateenergyproductionestimates', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('msn', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal('data', ['StateEnergyProductionEstimates'])

        # Adding model 'StateGdp'
        db.create_table('data_stategdp', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('fips', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('industry_code', self.gf('django.db.models.fields.IntegerField')()),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('component_code', self.gf('django.db.models.fields.IntegerField')()),
            ('component', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['StateGdp'])

        # Adding model 'StateGdpPre97'
        db.create_table('data_stategdppre97', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('fips', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('industry_code', self.gf('django.db.models.fields.IntegerField')()),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('component_code', self.gf('django.db.models.fields.IntegerField')()),
            ('component', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['StateGdpPre97'])

        # Adding model 'StateMedianIncome'
        db.create_table('data_statemedianincome', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('median_income', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('data', ['StateMedianIncome'])

        # Adding model 'StatePostalCodes'
        db.create_table('data_statepostalcodes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('data', ['StatePostalCodes'])

        # Adding model 'SubfunctionsCffr'
        db.create_table('data_subfunctionscffr', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subfunction_number', self.gf('django.db.models.fields.TextField')(max_length=3)),
            ('subfunction_name', self.gf('django.db.models.fields.TextField')(max_length=64)),
            ('cfda_program_code', self.gf('django.db.models.fields.TextField')(max_length=8)),
            ('program_name', self.gf('django.db.models.fields.TextField')(max_length=64)),
            ('at_code_1', self.gf('django.db.models.fields.TextField')(max_length=1, null=True)),
            ('at_code_2', self.gf('django.db.models.fields.TextField')(max_length=1, null=True)),
            ('at_code_3', self.gf('django.db.models.fields.TextField')(max_length=1, null=True)),
            ('at_code_4', self.gf('django.db.models.fields.TextField')(max_length=1, null=True)),
            ('at_code_5', self.gf('django.db.models.fields.TextField')(max_length=1, null=True)),
            ('at_code_6', self.gf('django.db.models.fields.TextField')(max_length=1, null=True)),
            ('at_code_7', self.gf('django.db.models.fields.TextField')(max_length=1, null=True)),
            ('at_code_8', self.gf('django.db.models.fields.TextField')(max_length=1, null=True)),
        ))
        db.send_create_signal('data', ['SubfunctionsCffr'])

        # Adding model 'SummerLunchParticipation'
        db.create_table('data_summerlunchparticipation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('data', ['SummerLunchParticipation'])

        # Adding model 'TanfFamilyStateRaw'
        db.create_table('data_tanffamilystateraw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['TanfFamilyStateRaw'])

        # Adding model 'TanfParticipationStateRaw'
        db.create_table('data_tanfparticipationstateraw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['TanfParticipationStateRaw'])

        # Adding model 'TitleIFunding'
        db.create_table('data_titleifunding', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['TitleIFunding'])

        # Adding model 'TotalStudents'
        db.create_table('data_totalstudents', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['TotalStudents'])

        # Adding model 'VehicleRegistrations'
        db.create_table('data_vehicleregistrations', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('auto_private', self.gf('django.db.models.fields.IntegerField')()),
            ('auto_public', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('auto_total', self.gf('django.db.models.fields.IntegerField')()),
            ('buses_private', self.gf('django.db.models.fields.IntegerField')()),
            ('buses_public', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('buses_total', self.gf('django.db.models.fields.IntegerField')()),
            ('trucks_private', self.gf('django.db.models.fields.IntegerField')()),
            ('trucks_public', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('trucks_total', self.gf('django.db.models.fields.IntegerField')()),
            ('all_private', self.gf('django.db.models.fields.IntegerField')()),
            ('all_public', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('all_total', self.gf('django.db.models.fields.IntegerField')()),
            ('private_commercial_per_capita', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('motorcycle_private', self.gf('django.db.models.fields.IntegerField')()),
            ('motorcycle_public', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['VehicleRegistrations'])

        # Adding model 'VocationalEdSpending'
        db.create_table('data_vocationaledspending', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('data', ['VocationalEdSpending'])

        # Adding model 'WicBenefitsStateRaw'
        db.create_table('data_wicbenefitsstateraw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['WicBenefitsStateRaw'])

        # Adding model 'WicParticipationStateRaw'
        db.create_table('data_wicparticipationstateraw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['WicParticipationStateRaw'])

        # Adding model 'CffrProgram'
        db.create_table('data_cffrprogram', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('program_code', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('program_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('program_desc', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['CffrProgram'])

        # Adding unique constraint on 'CffrProgram', fields ['year', 'program_code']
        db.create_unique('data_cffrprogram', ['year', 'program_code'])

        # Adding model 'AgeGroup'
        db.create_table('data_agegroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('age_group_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('age_group_desc', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['AgeGroup'])

        # Adding model 'Ethnicity'
        db.create_table('data_ethnicity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ethnicity_abbr', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5)),
            ('ethnicity_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('ethnicity_desc', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['Ethnicity'])

        # Adding model 'Gender'
        db.create_table('data_gender', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gender_abbr', self.gf('django.db.models.fields.CharField')(unique=True, max_length=1)),
            ('gender_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['Gender'])

        # Adding model 'Race'
        db.create_table('data_race', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race_abbr', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('race_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('race_desc', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['Race'])

        # Adding model 'RaceCombo'
        db.create_table('data_racecombo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race_combo_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('race_combo_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['RaceCombo'])

        # Adding model 'State'
        db.create_table('data_state', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state_ansi', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('state_abbr', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('state_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state_desc', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('state_gnisid', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('sort_order', self.gf('django.db.models.fields.SmallIntegerField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['State'])

        # Adding model 'County'
        db.create_table('data_county', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('county_ansi', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('county_abbr', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('county_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('county_desc', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('sort_order', self.gf('django.db.models.fields.SmallIntegerField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['County'])

        # Adding unique constraint on 'County', fields ['state', 'county_ansi']
        db.create_unique('data_county', ['state_id', 'county_ansi'])

        # Adding model 'Cffr'
        db.create_table('data_cffr', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.County'])),
            ('cffrprogram', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.CffrProgram'])),
            ('amount', self.gf('django.db.models.fields.BigIntegerField')()),
            ('amount_per_capita', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['Cffr'])

        # Adding unique constraint on 'Cffr', fields ['year', 'state', 'county', 'cffrprogram']
        db.create_unique('data_cffr', ['year', 'state_id', 'county_id', 'cffrprogram_id'])

        # Adding model 'CffrState'
        db.create_table('data_cffrstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('cffrprogram', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.CffrProgram'])),
            ('amount', self.gf('django.db.models.fields.BigIntegerField')()),
            ('amount_per_capita', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['CffrState'])

        # Adding unique constraint on 'CffrState', fields ['year', 'state', 'cffrprogram']
        db.create_unique('data_cffrstate', ['year', 'state_id', 'cffrprogram_id'])

        # Adding model 'CffrIndividualCounty'
        db.create_table('data_cffrindividualcounty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.County'])),
            ('amount', self.gf('django.db.models.fields.BigIntegerField')()),
            ('amount_per_capita', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['CffrIndividualCounty'])

        # Adding unique constraint on 'CffrIndividualCounty', fields ['year', 'state', 'county']
        db.create_unique('data_cffrindividualcounty', ['year', 'state_id', 'county_id'])

        # Adding model 'CffrIndividualState'
        db.create_table('data_cffrindividualstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('amount', self.gf('django.db.models.fields.BigIntegerField')()),
            ('amount_per_capita', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['CffrIndividualState'])

        # Adding unique constraint on 'CffrIndividualState', fields ['year', 'state']
        db.create_unique('data_cffrindividualstate', ['year', 'state_id'])

        # Adding model 'FederalTaxCollectionState'
        db.create_table('data_federaltaxcollectionstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('total', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('business_income', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('witheld_income_and_fica', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('notwitheld_income_and_seca', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('unemployment_insurance', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('railroad_retirement', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('estate_trust_income', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('estate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('gift', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('excise', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('individual_total', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['FederalTaxCollectionState'])

        # Adding unique constraint on 'FederalTaxCollectionState', fields ['year', 'state']
        db.create_unique('data_federaltaxcollectionstate', ['year', 'state_id'])

        # Adding model 'FoodSecurityState'
        db.create_table('data_foodsecuritystate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('household_total', self.gf('django.db.models.fields.IntegerField')()),
            ('no_response', self.gf('django.db.models.fields.IntegerField')()),
            ('food_secure', self.gf('django.db.models.fields.IntegerField')()),
            ('food_secure_percent', self.gf('django.db.models.fields.FloatField')()),
            ('food_secure_high', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('food_secure_high_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('food_secure_marginal', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('food_secure_marginal_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('food_secure_low', self.gf('django.db.models.fields.IntegerField')()),
            ('food_secure_low_percent', self.gf('django.db.models.fields.FloatField')()),
            ('food_secure_very_low', self.gf('django.db.models.fields.IntegerField')()),
            ('food_secure_very_low_percent', self.gf('django.db.models.fields.FloatField')()),
            ('food_insecure', self.gf('django.db.models.fields.IntegerField')()),
            ('food_insecure_percent', self.gf('django.db.models.fields.FloatField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['FoodSecurityState'])

        # Adding unique constraint on 'FoodSecurityState', fields ['year', 'state']
        db.create_unique('data_foodsecuritystate', ['year', 'state_id'])

        # Adding model 'LaborForceCounty'
        db.create_table('data_laborforcecounty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.County'])),
            ('laus_code', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('labor_force', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('employment_total', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('unemployment_total', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('unemployment_rate', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['LaborForceCounty'])

        # Adding unique constraint on 'LaborForceCounty', fields ['year', 'state', 'county']
        db.create_unique('data_laborforcecounty', ['year', 'state_id', 'county_id'])

        # Adding model 'LaborUnderutilizationState'
        db.create_table('data_laborunderutilizationstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('u1', self.gf('django.db.models.fields.FloatField')()),
            ('u2', self.gf('django.db.models.fields.FloatField')()),
            ('u3', self.gf('django.db.models.fields.FloatField')()),
            ('u4', self.gf('django.db.models.fields.FloatField')()),
            ('u5', self.gf('django.db.models.fields.FloatField')()),
            ('u6', self.gf('django.db.models.fields.FloatField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['LaborUnderutilizationState'])

        # Adding unique constraint on 'LaborUnderutilizationState', fields ['year', 'state']
        db.create_unique('data_laborunderutilizationstate', ['year', 'state_id'])

        # Adding model 'PopulationAgeCounty'
        db.create_table('data_populationagecounty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.County'])),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
            ('age_0_4', self.gf('django.db.models.fields.IntegerField')()),
            ('age_0_4_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_5_9', self.gf('django.db.models.fields.IntegerField')()),
            ('age_5_9_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_10_14', self.gf('django.db.models.fields.IntegerField')()),
            ('age_10_14_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_15_19', self.gf('django.db.models.fields.IntegerField')()),
            ('age_15_19_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_20_24', self.gf('django.db.models.fields.IntegerField')()),
            ('age_20_24_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_25_29', self.gf('django.db.models.fields.IntegerField')()),
            ('age_25_29_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_30_34', self.gf('django.db.models.fields.IntegerField')()),
            ('age_30_34_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_35_39', self.gf('django.db.models.fields.IntegerField')()),
            ('age_35_39_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_40_44', self.gf('django.db.models.fields.IntegerField')()),
            ('age_40_44_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_45_49', self.gf('django.db.models.fields.IntegerField')()),
            ('age_45_49_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_50_54', self.gf('django.db.models.fields.IntegerField')()),
            ('age_50_54_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_55_59', self.gf('django.db.models.fields.IntegerField')()),
            ('age_55_59_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_60_64', self.gf('django.db.models.fields.IntegerField')()),
            ('age_60_64_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_65_69', self.gf('django.db.models.fields.IntegerField')()),
            ('age_65_69_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_70_74', self.gf('django.db.models.fields.IntegerField')()),
            ('age_70_74_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_75_79', self.gf('django.db.models.fields.IntegerField')()),
            ('age_75_79_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_80_84', self.gf('django.db.models.fields.IntegerField')()),
            ('age_80_84_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_85_over', self.gf('django.db.models.fields.IntegerField')()),
            ('age_85_over_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_65_over', self.gf('django.db.models.fields.IntegerField')()),
            ('age_65_over_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_0_19', self.gf('django.db.models.fields.IntegerField')()),
            ('age_0_19_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['PopulationAgeCounty'])

        # Adding unique constraint on 'PopulationAgeCounty', fields ['year', 'state', 'county']
        db.create_unique('data_populationagecounty', ['year', 'state_id', 'county_id'])

        # Adding model 'PopulationAgeState'
        db.create_table('data_populationagestate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
            ('age_0_4', self.gf('django.db.models.fields.IntegerField')()),
            ('age_0_4_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_5_9', self.gf('django.db.models.fields.IntegerField')()),
            ('age_5_9_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_10_14', self.gf('django.db.models.fields.IntegerField')()),
            ('age_10_14_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_15_19', self.gf('django.db.models.fields.IntegerField')()),
            ('age_15_19_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_20_24', self.gf('django.db.models.fields.IntegerField')()),
            ('age_20_24_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_25_29', self.gf('django.db.models.fields.IntegerField')()),
            ('age_25_29_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_30_34', self.gf('django.db.models.fields.IntegerField')()),
            ('age_30_34_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_35_39', self.gf('django.db.models.fields.IntegerField')()),
            ('age_35_39_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_40_44', self.gf('django.db.models.fields.IntegerField')()),
            ('age_40_44_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_45_49', self.gf('django.db.models.fields.IntegerField')()),
            ('age_45_49_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_50_54', self.gf('django.db.models.fields.IntegerField')()),
            ('age_50_54_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_55_59', self.gf('django.db.models.fields.IntegerField')()),
            ('age_55_59_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_60_64', self.gf('django.db.models.fields.IntegerField')()),
            ('age_60_64_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_65_69', self.gf('django.db.models.fields.IntegerField')()),
            ('age_65_69_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_70_74', self.gf('django.db.models.fields.IntegerField')()),
            ('age_70_74_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_75_79', self.gf('django.db.models.fields.IntegerField')()),
            ('age_75_79_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_80_84', self.gf('django.db.models.fields.IntegerField')()),
            ('age_80_84_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_85_over', self.gf('django.db.models.fields.IntegerField')()),
            ('age_85_over_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_65_over', self.gf('django.db.models.fields.IntegerField')()),
            ('age_65_over_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('age_0_19', self.gf('django.db.models.fields.IntegerField')()),
            ('age_0_19_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['PopulationAgeState'])

        # Adding unique constraint on 'PopulationAgeState', fields ['year', 'state']
        db.create_unique('data_populationagestate', ['year', 'state_id'])

        # Adding model 'PopulationGenderCounty'
        db.create_table('data_populationgendercounty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.County'])),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
            ('female', self.gf('django.db.models.fields.IntegerField')()),
            ('female_percent', self.gf('django.db.models.fields.FloatField')()),
            ('male', self.gf('django.db.models.fields.IntegerField')()),
            ('male_percent', self.gf('django.db.models.fields.FloatField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal('data', ['PopulationGenderCounty'])

        # Adding unique constraint on 'PopulationGenderCounty', fields ['year', 'state', 'county']
        db.create_unique('data_populationgendercounty', ['year', 'state_id', 'county_id'])

        # Adding model 'PopulationGenderState'
        db.create_table('data_populationgenderstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
            ('female', self.gf('django.db.models.fields.IntegerField')()),
            ('female_percent', self.gf('django.db.models.fields.FloatField')()),
            ('male', self.gf('django.db.models.fields.IntegerField')()),
            ('male_percent', self.gf('django.db.models.fields.FloatField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['PopulationGenderState'])

        # Adding unique constraint on 'PopulationGenderState', fields ['year', 'state']
        db.create_unique('data_populationgenderstate', ['year', 'state_id'])

        # Adding model 'PopulationRaceCounty'
        db.create_table('data_populationracecounty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.County'])),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
            ('white_alone', self.gf('django.db.models.fields.IntegerField')()),
            ('white_alone_percent', self.gf('django.db.models.fields.FloatField')()),
            ('white_other', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('white_other_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('white_alone_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('white_alone_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('white_other_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('white_other_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('white_alone_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('white_alone_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('white_other_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('white_other_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('black_alone', self.gf('django.db.models.fields.IntegerField')()),
            ('black_alone_percent', self.gf('django.db.models.fields.FloatField')()),
            ('black_other', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('black_other_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('black_alone_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('black_alone_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('black_other_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('black_other_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('black_alone_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('black_alone_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('black_other_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('black_other_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('native_alone', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('native_alone_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('native_other', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('native_other_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('native_alone_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('native_alone_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('native_other_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('native_other_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('native_alone_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('native_alone_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('native_other_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('native_other_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('asian_alone', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('asian_alone_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('asian_other', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('asian_other_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('asian_alone_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('asian_alone_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('asian_other_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('asian_other_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('asian_alone_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('asian_alone_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('asian_other_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('asian_other_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('pacific_islander_alone', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pacific_islander_alone_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('pacific_islander_other', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pacific_islander_other_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('pacific_islander_alone_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pacific_islander_alone_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('pacific_islander_other_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pacific_islander_other_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('pacific_islander_alone_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pacific_islander_alone_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('pacific_islander_other_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pacific_islander_other_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('asian_pacific_islander_alone', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('asian_pacific_islander_alone_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('other', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('other_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('multiple_race', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('multiple_race_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('multiple_race_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('multiple_race_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('multiple_race_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('multiple_race_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['PopulationRaceCounty'])

        # Adding unique constraint on 'PopulationRaceCounty', fields ['year', 'state', 'county']
        db.create_unique('data_populationracecounty', ['year', 'state_id', 'county_id'])

        # Adding model 'PopulationRaceState'
        db.create_table('data_populationracestate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
            ('white_alone', self.gf('django.db.models.fields.IntegerField')()),
            ('white_alone_percent', self.gf('django.db.models.fields.FloatField')()),
            ('white_other', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('white_other_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('white_alone_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('white_alone_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('white_other_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('white_other_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('white_alone_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('white_alone_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('white_other_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('white_other_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('black_alone', self.gf('django.db.models.fields.IntegerField')()),
            ('black_alone_percent', self.gf('django.db.models.fields.FloatField')()),
            ('black_other', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('black_other_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('black_alone_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('black_alone_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('black_other_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('black_other_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('black_alone_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('black_alone_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('black_other_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('black_other_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('native_alone', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('native_alone_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('native_other', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('native_other_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('native_alone_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('native_alone_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('native_other_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('native_other_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('native_alone_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('native_alone_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('native_other_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('native_other_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('asian_alone', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('asian_alone_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('asian_other', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('asian_other_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('asian_alone_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('asian_alone_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('asian_other_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('asian_other_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('asian_alone_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('asian_alone_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('asian_other_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('asian_other_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('pacific_islander_alone', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pacific_islander_alone_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('pacific_islander_other', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pacific_islander_other_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('pacific_islander_alone_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pacific_islander_alone_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('pacific_islander_other_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pacific_islander_other_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('pacific_islander_alone_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pacific_islander_alone_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('pacific_islander_other_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pacific_islander_other_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('asian_pacific_islander_alone', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('asian_pacific_islander_alone_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('other', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('other_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('multiple_race', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('multiple_race_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('multiple_race_hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('multiple_race_hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('multiple_race_nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('multiple_race_nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('hispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('nonhispanic', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('nonhispanic_percent', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['PopulationRaceState'])

        # Adding unique constraint on 'PopulationRaceState', fields ['year', 'state']
        db.create_unique('data_populationracestate', ['year', 'state_id'])

        # Adding model 'PupilTeacherState'
        db.create_table('data_pupilteacherstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('ratio', self.gf('django.db.models.fields.FloatField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal('data', ['PupilTeacherState'])

        # Adding unique constraint on 'PupilTeacherState', fields ['year', 'state']
        db.create_unique('data_pupilteacherstate', ['year', 'state_id'])

        # Adding model 'TanfParticipationState'
        db.create_table('data_tanfparticipationstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('person', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('family', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['TanfParticipationState'])

        # Adding unique constraint on 'TanfParticipationState', fields ['year', 'state']
        db.create_unique('data_tanfparticipationstate', ['year', 'state_id'])

        # Adding model 'WicBenefitsState'
        db.create_table('data_wicbenefitsstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('amount', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['WicBenefitsState'])

        # Adding unique constraint on 'WicBenefitsState', fields ['year', 'state']
        db.create_unique('data_wicbenefitsstate', ['year', 'state_id'])

        # Adding model 'WicParticipationState'
        db.create_table('data_wicparticipationstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.State'])),
            ('value', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('data', ['WicParticipationState'])

        # Adding unique constraint on 'WicParticipationState', fields ['year', 'state']
        db.create_unique('data_wicparticipationstate', ['year', 'state_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'WicParticipationState', fields ['year', 'state']
        db.delete_unique('data_wicparticipationstate', ['year', 'state_id'])

        # Removing unique constraint on 'WicBenefitsState', fields ['year', 'state']
        db.delete_unique('data_wicbenefitsstate', ['year', 'state_id'])

        # Removing unique constraint on 'TanfParticipationState', fields ['year', 'state']
        db.delete_unique('data_tanfparticipationstate', ['year', 'state_id'])

        # Removing unique constraint on 'PupilTeacherState', fields ['year', 'state']
        db.delete_unique('data_pupilteacherstate', ['year', 'state_id'])

        # Removing unique constraint on 'PopulationRaceState', fields ['year', 'state']
        db.delete_unique('data_populationracestate', ['year', 'state_id'])

        # Removing unique constraint on 'PopulationRaceCounty', fields ['year', 'state', 'county']
        db.delete_unique('data_populationracecounty', ['year', 'state_id', 'county_id'])

        # Removing unique constraint on 'PopulationGenderState', fields ['year', 'state']
        db.delete_unique('data_populationgenderstate', ['year', 'state_id'])

        # Removing unique constraint on 'PopulationGenderCounty', fields ['year', 'state', 'county']
        db.delete_unique('data_populationgendercounty', ['year', 'state_id', 'county_id'])

        # Removing unique constraint on 'PopulationAgeState', fields ['year', 'state']
        db.delete_unique('data_populationagestate', ['year', 'state_id'])

        # Removing unique constraint on 'PopulationAgeCounty', fields ['year', 'state', 'county']
        db.delete_unique('data_populationagecounty', ['year', 'state_id', 'county_id'])

        # Removing unique constraint on 'LaborUnderutilizationState', fields ['year', 'state']
        db.delete_unique('data_laborunderutilizationstate', ['year', 'state_id'])

        # Removing unique constraint on 'LaborForceCounty', fields ['year', 'state', 'county']
        db.delete_unique('data_laborforcecounty', ['year', 'state_id', 'county_id'])

        # Removing unique constraint on 'FoodSecurityState', fields ['year', 'state']
        db.delete_unique('data_foodsecuritystate', ['year', 'state_id'])

        # Removing unique constraint on 'FederalTaxCollectionState', fields ['year', 'state']
        db.delete_unique('data_federaltaxcollectionstate', ['year', 'state_id'])

        # Removing unique constraint on 'CffrIndividualState', fields ['year', 'state']
        db.delete_unique('data_cffrindividualstate', ['year', 'state_id'])

        # Removing unique constraint on 'CffrIndividualCounty', fields ['year', 'state', 'county']
        db.delete_unique('data_cffrindividualcounty', ['year', 'state_id', 'county_id'])

        # Removing unique constraint on 'CffrState', fields ['year', 'state', 'cffrprogram']
        db.delete_unique('data_cffrstate', ['year', 'state_id', 'cffrprogram_id'])

        # Removing unique constraint on 'Cffr', fields ['year', 'state', 'county', 'cffrprogram']
        db.delete_unique('data_cffr', ['year', 'state_id', 'county_id', 'cffrprogram_id'])

        # Removing unique constraint on 'County', fields ['state', 'county_ansi']
        db.delete_unique('data_county', ['state_id', 'county_ansi'])

        # Removing unique constraint on 'CffrProgram', fields ['year', 'program_code']
        db.delete_unique('data_cffrprogram', ['year', 'program_code'])

        # Removing unique constraint on 'PopulationEst90Raw', fields ['year', 'state', 'county', 'agegrp', 'race_gender', 'ethnic_origin']
        db.delete_unique('data_populationest90raw', ['year', 'state', 'county', 'agegrp', 'race_gender', 'ethnic_origin'])

        # Removing unique constraint on 'PopulationEst00Raw', fields ['state', 'county', 'gender', 'ethnic_origin', 'race']
        db.delete_unique('data_populationest00raw', ['state', 'county', 'gender', 'ethnic_origin', 'race'])

        # Deleting model 'Category'
        db.delete_table('data_category')

        # Deleting model 'Source'
        db.delete_table('data_source')

        # Deleting model 'AlternativeFuelVehicles'
        db.delete_table('data_alternativefuelvehicles')

        # Deleting model 'AnnualStateEnergyConsumption'
        db.delete_table('data_annualstateenergyconsumption')

        # Deleting model 'AnnualStateEnergyExpenditures'
        db.delete_table('data_annualstateenergyexpenditures')

        # Deleting model 'AnsiCountyState'
        db.delete_table('data_ansicountystate')

        # Deleting model 'AnsiState'
        db.delete_table('data_ansistate')

        # Deleting model 'AtCodes'
        db.delete_table('data_atcodes')

        # Deleting model 'AverageTeacherSalary'
        db.delete_table('data_averageteachersalary')

        # Deleting model 'BilingualEdSpending'
        db.delete_table('data_bilingualedspending')

        # Deleting model 'BudgetCategorySubfunctions'
        db.delete_table('data_budgetcategorysubfunctions')

        # Deleting model 'CffrRaw'
        db.delete_table('data_cffrraw')

        # Deleting model 'CffrAgency'
        db.delete_table('data_cffragency')

        # Deleting model 'CffrGeo'
        db.delete_table('data_cffrgeo')

        # Deleting model 'CffrObjectCode'
        db.delete_table('data_cffrobjectcode')

        # Deleting model 'CffrProgramRaw'
        db.delete_table('data_cffrprogramraw')

        # Deleting model 'ChildrenPoverty'
        db.delete_table('data_childrenpoverty')

        # Deleting model 'DiplomaRecipientTotal'
        db.delete_table('data_diplomarecipienttotal')

        # Deleting model 'DropoutsRace'
        db.delete_table('data_dropoutsrace')

        # Deleting model 'DrugFreeSchoolSpending'
        db.delete_table('data_drugfreeschoolspending')

        # Deleting model 'EducationalAttainment'
        db.delete_table('data_educationalattainment')

        # Deleting model 'EllStudentsDistrict'
        db.delete_table('data_ellstudentsdistrict')

        # Deleting model 'Employment'
        db.delete_table('data_employment')

        # Deleting model 'EnrolledStudentsDistrict'
        db.delete_table('data_enrolledstudentsdistrict')

        # Deleting model 'EnrollmentRace'
        db.delete_table('data_enrollmentrace')

        # Deleting model 'ExpenditurePerPupil'
        db.delete_table('data_expenditureperpupil')

        # Deleting model 'FamiliesPoverty'
        db.delete_table('data_familiespoverty')

        # Deleting model 'FcnaSpending'
        db.delete_table('data_fcnaspending')

        # Deleting model 'FederalImpactAid'
        db.delete_table('data_federalimpactaid')

        # Deleting model 'FederalTaxCollectionStateRaw'
        db.delete_table('data_federaltaxcollectionstateraw')

        # Deleting model 'FipsCountyCongressDistrict'
        db.delete_table('data_fipscountycongressdistrict')

        # Deleting model 'FipsState'
        db.delete_table('data_fipsstate')

        # Deleting model 'FoodSecurityStateRaw'
        db.delete_table('data_foodsecuritystateraw')

        # Deleting model 'FreeLunchEligible'
        db.delete_table('data_freeluncheligible')

        # Deleting model 'FreeReducedLunchEligible'
        db.delete_table('data_freereducedluncheligible')

        # Deleting model 'FreeReducedLunchEligibleCounty'
        db.delete_table('data_freereducedluncheligiblecounty')

        # Deleting model 'HalfPints'
        db.delete_table('data_halfpints')

        # Deleting model 'HeadStartEnrollment'
        db.delete_table('data_headstartenrollment')

        # Deleting model 'HealthInsurance'
        db.delete_table('data_healthinsurance')

        # Deleting model 'HighSchoolDropouts'
        db.delete_table('data_highschooldropouts')

        # Deleting model 'HighSchoolOther'
        db.delete_table('data_highschoolother')

        # Deleting model 'HousingUnits'
        db.delete_table('data_housingunits')

        # Deleting model 'IndividualEducationPrograms'
        db.delete_table('data_individualeducationprograms')

        # Deleting model 'KidsHealthInsurance'
        db.delete_table('data_kidshealthinsurance')

        # Deleting model 'LaborForceCountyRaw'
        db.delete_table('data_laborforcecountyraw')

        # Deleting model 'LaborUnderutilizationStateRaw'
        db.delete_table('data_laborunderutilizationstateraw')

        # Deleting model 'MathScienceSpending'
        db.delete_table('data_mathsciencespending')

        # Deleting model 'MedicaidParticipation'
        db.delete_table('data_medicaidparticipation')

        # Deleting model 'MedicareEnrollment'
        db.delete_table('data_medicareenrollment')

        # Deleting model 'MigrantStudents'
        db.delete_table('data_migrantstudents')

        # Deleting model 'MilitaryPersonnel'
        db.delete_table('data_militarypersonnel')

        # Deleting model 'MsnCodes'
        db.delete_table('data_msncodes')

        # Deleting model 'NativeEdSpending'
        db.delete_table('data_nativeedspending')

        # Deleting model 'NcesSchoolDistrict'
        db.delete_table('data_ncesschooldistrict')

        # Deleting model 'NewAidsCases'
        db.delete_table('data_newaidscases')

        # Deleting model 'OtherFederalRevenue'
        db.delete_table('data_otherfederalrevenue')

        # Deleting model 'OwnersRenters'
        db.delete_table('data_ownersrenters')

        # Deleting model 'PeopleInPoverty'
        db.delete_table('data_peopleinpoverty')

        # Deleting model 'PopulationCongressionalDistrict'
        db.delete_table('data_populationcongressionaldistrict')

        # Deleting model 'PopulationEst00Raw'
        db.delete_table('data_populationest00raw')

        # Deleting model 'PopulationEst90Raw'
        db.delete_table('data_populationest90raw')

        # Deleting model 'PopulationFamilies'
        db.delete_table('data_populationfamilies')

        # Deleting model 'PupilTeacherDistrict'
        db.delete_table('data_pupilteacherdistrict')

        # Deleting model 'PresidentsBudget'
        db.delete_table('data_presidentsbudget')

        # Deleting model 'PresidentsBudgetYear'
        db.delete_table('data_presidentsbudgetyear')

        # Deleting model 'PupilTeacherStateRaw'
        db.delete_table('data_pupilteacherstateraw')

        # Deleting model 'RetiredDisabledNilf'
        db.delete_table('data_retireddisablednilf')

        # Deleting model 'SchipEnrollment'
        db.delete_table('data_schipenrollment')

        # Deleting model 'StateCompletionRate'
        db.delete_table('data_statecompletionrate')

        # Deleting model 'StateLaborForceParticipation'
        db.delete_table('data_statelaborforceparticipation')

        # Deleting model 'StateRenewableEnergy'
        db.delete_table('data_staterenewableenergy')

        # Deleting model 'SaipeSchool'
        db.delete_table('data_saipeschool')

        # Deleting model 'SaipeCountyState'
        db.delete_table('data_saipecountystate')

        # Deleting model 'SchoolBreakfastParticipation'
        db.delete_table('data_schoolbreakfastparticipation')

        # Deleting model 'SchoolLunchParticipation'
        db.delete_table('data_schoollunchparticipation')

        # Deleting model 'ShelterPopulation'
        db.delete_table('data_shelterpopulation')

        # Deleting model 'SnapBenefitsRecipients'
        db.delete_table('data_snapbenefitsrecipients')

        # Deleting model 'SnapMonthlyBenefitsPerson'
        db.delete_table('data_snapmonthlybenefitsperson')

        # Deleting model 'SnapParticipationHouseholds'
        db.delete_table('data_snapparticipationhouseholds')

        # Deleting model 'SnapParticipationPeople'
        db.delete_table('data_snapparticipationpeople')

        # Deleting model 'SpecialEdFunding'
        db.delete_table('data_specialedfunding')

        # Deleting model 'StateEmissions'
        db.delete_table('data_stateemissions')

        # Deleting model 'StateEnergyProductionEstimates'
        db.delete_table('data_stateenergyproductionestimates')

        # Deleting model 'StateGdp'
        db.delete_table('data_stategdp')

        # Deleting model 'StateGdpPre97'
        db.delete_table('data_stategdppre97')

        # Deleting model 'StateMedianIncome'
        db.delete_table('data_statemedianincome')

        # Deleting model 'StatePostalCodes'
        db.delete_table('data_statepostalcodes')

        # Deleting model 'SubfunctionsCffr'
        db.delete_table('data_subfunctionscffr')

        # Deleting model 'SummerLunchParticipation'
        db.delete_table('data_summerlunchparticipation')

        # Deleting model 'TanfFamilyStateRaw'
        db.delete_table('data_tanffamilystateraw')

        # Deleting model 'TanfParticipationStateRaw'
        db.delete_table('data_tanfparticipationstateraw')

        # Deleting model 'TitleIFunding'
        db.delete_table('data_titleifunding')

        # Deleting model 'TotalStudents'
        db.delete_table('data_totalstudents')

        # Deleting model 'VehicleRegistrations'
        db.delete_table('data_vehicleregistrations')

        # Deleting model 'VocationalEdSpending'
        db.delete_table('data_vocationaledspending')

        # Deleting model 'WicBenefitsStateRaw'
        db.delete_table('data_wicbenefitsstateraw')

        # Deleting model 'WicParticipationStateRaw'
        db.delete_table('data_wicparticipationstateraw')

        # Deleting model 'CffrProgram'
        db.delete_table('data_cffrprogram')

        # Deleting model 'AgeGroup'
        db.delete_table('data_agegroup')

        # Deleting model 'Ethnicity'
        db.delete_table('data_ethnicity')

        # Deleting model 'Gender'
        db.delete_table('data_gender')

        # Deleting model 'Race'
        db.delete_table('data_race')

        # Deleting model 'RaceCombo'
        db.delete_table('data_racecombo')

        # Deleting model 'State'
        db.delete_table('data_state')

        # Deleting model 'County'
        db.delete_table('data_county')

        # Deleting model 'Cffr'
        db.delete_table('data_cffr')

        # Deleting model 'CffrState'
        db.delete_table('data_cffrstate')

        # Deleting model 'CffrIndividualCounty'
        db.delete_table('data_cffrindividualcounty')

        # Deleting model 'CffrIndividualState'
        db.delete_table('data_cffrindividualstate')

        # Deleting model 'FederalTaxCollectionState'
        db.delete_table('data_federaltaxcollectionstate')

        # Deleting model 'FoodSecurityState'
        db.delete_table('data_foodsecuritystate')

        # Deleting model 'LaborForceCounty'
        db.delete_table('data_laborforcecounty')

        # Deleting model 'LaborUnderutilizationState'
        db.delete_table('data_laborunderutilizationstate')

        # Deleting model 'PopulationAgeCounty'
        db.delete_table('data_populationagecounty')

        # Deleting model 'PopulationAgeState'
        db.delete_table('data_populationagestate')

        # Deleting model 'PopulationGenderCounty'
        db.delete_table('data_populationgendercounty')

        # Deleting model 'PopulationGenderState'
        db.delete_table('data_populationgenderstate')

        # Deleting model 'PopulationRaceCounty'
        db.delete_table('data_populationracecounty')

        # Deleting model 'PopulationRaceState'
        db.delete_table('data_populationracestate')

        # Deleting model 'PupilTeacherState'
        db.delete_table('data_pupilteacherstate')

        # Deleting model 'TanfParticipationState'
        db.delete_table('data_tanfparticipationstate')

        # Deleting model 'WicBenefitsState'
        db.delete_table('data_wicbenefitsstate')

        # Deleting model 'WicParticipationState'
        db.delete_table('data_wicparticipationstate')


    models = {
        'data.agegroup': {
            'Meta': {'object_name': 'AgeGroup'},
            'age_group_desc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'age_group_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'data.alternativefuelvehicles': {
            'Meta': {'object_name': 'AlternativeFuelVehicles'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.annualstateenergyconsumption': {
            'Meta': {'object_name': 'AnnualStateEnergyConsumption'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msn': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'value': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.annualstateenergyexpenditures': {
            'Meta': {'object_name': 'AnnualStateEnergyExpenditures'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msn': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'value': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.ansicountystate': {
            'Meta': {'object_name': 'AnsiCountyState'},
            'ansi_class': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'ansi_state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'data.ansistate': {
            'Meta': {'object_name': 'AnsiState'},
            'ansi_state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'gnisid': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'data.atcodes': {
            'Meta': {'object_name': 'AtCodes'},
            'assistance_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'data.averageteachersalary': {
            'Meta': {'object_name': 'AverageTeacherSalary'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.bilingualedspending': {
            'Meta': {'object_name': 'BilingualEdSpending'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.budgetcategorysubfunctions': {
            'Meta': {'object_name': 'BudgetCategorySubfunctions'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'npp_budget_category': ('django.db.models.fields.TextField', [], {'max_length': '64'}),
            'subfunction': ('django.db.models.fields.TextField', [], {'max_length': '3'})
        },
        'data.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'data.cffr': {
            'Meta': {'unique_together': "(('year', 'state', 'county', 'cffrprogram'),)", 'object_name': 'Cffr'},
            'amount': ('django.db.models.fields.BigIntegerField', [], {}),
            'amount_per_capita': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'cffrprogram': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.CffrProgram']"}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.County']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.cffragency': {
            'Meta': {'object_name': 'CffrAgency'},
            'agency_code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.cffrgeo': {
            'Meta': {'object_name': 'CffrGeo'},
            'congress_district': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True'}),
            'county_code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'county_gu': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'place_gu': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'place_name': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'split_gu': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'state_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'state_gu': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'type_gu': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.cffrindividualcounty': {
            'Meta': {'unique_together': "(('year', 'state', 'county'),)", 'object_name': 'CffrIndividualCounty'},
            'amount': ('django.db.models.fields.BigIntegerField', [], {}),
            'amount_per_capita': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.County']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.cffrindividualstate': {
            'Meta': {'unique_together': "(('year', 'state'),)", 'object_name': 'CffrIndividualState'},
            'amount': ('django.db.models.fields.BigIntegerField', [], {}),
            'amount_per_capita': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.cffrobjectcode': {
            'Meta': {'object_name': 'CffrObjectCode'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_code': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'data.cffrprogram': {
            'Meta': {'unique_together': "(('year', 'program_code'),)", 'object_name': 'CffrProgram'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program_code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'program_desc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'program_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.cffrprogramraw': {
            'Meta': {'object_name': 'CffrProgramRaw'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program_id_code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'program_name': ('django.db.models.fields.CharField', [], {'max_length': '74'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.cffrraw': {
            'Meta': {'object_name': 'CffrRaw'},
            'agency_code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'amount': ('django.db.models.fields.BigIntegerField', [], {}),
            'amount_adjusted': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'congress_district': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True'}),
            'county_code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'county_name': ('django.db.models.fields.CharField', [], {'max_length': '24', 'null': 'True'}),
            'funding_sign': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'place_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'place_name': ('django.db.models.fields.CharField', [], {'max_length': '24', 'null': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'program_code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'state_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'state_postal': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.cffrstate': {
            'Meta': {'unique_together': "(('year', 'state', 'cffrprogram'),)", 'object_name': 'CffrState'},
            'amount': ('django.db.models.fields.BigIntegerField', [], {}),
            'amount_per_capita': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'cffrprogram': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.CffrProgram']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.childrenpoverty': {
            'Meta': {'object_name': 'ChildrenPoverty'},
            'children_poverty': ('django.db.models.fields.IntegerField', [], {}),
            'children_poverty_moe': ('django.db.models.fields.IntegerField', [], {}),
            'children_poverty_percent': ('django.db.models.fields.FloatField', [], {}),
            'children_poverty_percent_moe': ('django.db.models.fields.FloatField', [], {}),
            'children_total': ('django.db.models.fields.IntegerField', [], {}),
            'children_total_moe': ('django.db.models.fields.IntegerField', [], {}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.county': {
            'Meta': {'unique_together': "(('state', 'county_ansi'),)", 'object_name': 'County'},
            'county_abbr': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'county_ansi': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'county_desc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'county_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'data.diplomarecipienttotal': {
            'Meta': {'object_name': 'DiplomaRecipientTotal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.dropoutsrace': {
            'Meta': {'object_name': 'DropoutsRace'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.drugfreeschoolspending': {
            'Meta': {'object_name': 'DrugFreeSchoolSpending'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.educationalattainment': {
            'Meta': {'object_name': 'EducationalAttainment'},
            'category': ('django.db.models.fields.TextField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.TextField', [], {'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.TextField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'value_type': ('django.db.models.fields.TextField', [], {'max_length': '16'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.ellstudentsdistrict': {
            'Meta': {'object_name': 'EllStudentsDistrict'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.employment': {
            'Meta': {'object_name': 'Employment'},
            'black_civilian_labor_force': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'black_unemployed': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'hispanic_civilian_labor_force': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'hispanic_unemployed': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'total_civilian_labor_force': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'white_civilian_labor_force': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'white_unemployed': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.enrolledstudentsdistrict': {
            'Meta': {'object_name': 'EnrolledStudentsDistrict'},
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '9'})
        },
        'data.enrollmentrace': {
            'Meta': {'object_name': 'EnrollmentRace'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.ethnicity': {
            'Meta': {'object_name': 'Ethnicity'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ethnicity_abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'ethnicity_desc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'ethnicity_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'data.expenditureperpupil': {
            'Meta': {'object_name': 'ExpenditurePerPupil'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.familiespoverty': {
            'Meta': {'object_name': 'FamiliesPoverty'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'families_poverty_percent': ('django.db.models.fields.FloatField', [], {}),
            'families_poverty_percent_moe': ('django.db.models.fields.FloatField', [], {}),
            'families_total': ('django.db.models.fields.IntegerField', [], {}),
            'families_total_moe': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.fcnaspending': {
            'Meta': {'object_name': 'FcnaSpending'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.federalimpactaid': {
            'Meta': {'object_name': 'FederalImpactAid'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.federaltaxcollectionstate': {
            'Meta': {'unique_together': "(('year', 'state'),)", 'object_name': 'FederalTaxCollectionState'},
            'business_income': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'estate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'estate_trust_income': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'excise': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'gift': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'individual_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'notwitheld_income_and_seca': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'railroad_retirement': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'unemployment_insurance': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'witheld_income_and_fica': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.federaltaxcollectionstateraw': {
            'Meta': {'object_name': 'FederalTaxCollectionStateRaw'},
            'business_income_taxes': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'estate_tax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'estate_trust_income_tax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'excise_taxes': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'gift_tax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income_employment_estate_trust_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'individual_notwitheld_seca': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'individual_witheld_fica': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'railroad_retirement': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_collections': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'unemployment_insurance': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.fipscountycongressdistrict': {
            'Meta': {'object_name': 'FipsCountyCongressDistrict'},
            'congress': ('django.db.models.fields.IntegerField', [], {}),
            'county_code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'district_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_code': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'data.fipsstate': {
            'Meta': {'object_name': 'FipsState'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'data.foodsecuritystate': {
            'Meta': {'unique_together': "(('year', 'state'),)", 'object_name': 'FoodSecurityState'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'food_insecure': ('django.db.models.fields.IntegerField', [], {}),
            'food_insecure_percent': ('django.db.models.fields.FloatField', [], {}),
            'food_secure': ('django.db.models.fields.IntegerField', [], {}),
            'food_secure_high': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'food_secure_high_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'food_secure_low': ('django.db.models.fields.IntegerField', [], {}),
            'food_secure_low_percent': ('django.db.models.fields.FloatField', [], {}),
            'food_secure_marginal': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'food_secure_marginal_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'food_secure_percent': ('django.db.models.fields.FloatField', [], {}),
            'food_secure_very_low': ('django.db.models.fields.IntegerField', [], {}),
            'food_secure_very_low_percent': ('django.db.models.fields.FloatField', [], {}),
            'household_total': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_response': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.foodsecuritystateraw': {
            'Meta': {'object_name': 'FoodSecurityStateRaw'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'food_secure': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'food_secure_high': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'food_secure_low': ('django.db.models.fields.IntegerField', [], {}),
            'food_secure_marginal': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'food_secure_very_low': ('django.db.models.fields.IntegerField', [], {}),
            'household_total': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_response': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.freeluncheligible': {
            'Meta': {'object_name': 'FreeLunchEligible'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.freereducedluncheligible': {
            'Meta': {'object_name': 'FreeReducedLunchEligible'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.freereducedluncheligiblecounty': {
            'Meta': {'object_name': 'FreeReducedLunchEligibleCounty'},
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'county_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.gender': {
            'Meta': {'object_name': 'Gender'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gender_abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1'}),
            'gender_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'data.halfpints': {
            'Meta': {'object_name': 'HalfPints'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.headstartenrollment': {
            'Meta': {'object_name': 'HeadStartEnrollment'},
            'enrollment': ('django.db.models.fields.IntegerField', [], {}),
            'funding': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.healthinsurance': {
            'Meta': {'object_name': 'HealthInsurance'},
            'all_people': ('django.db.models.fields.IntegerField', [], {}),
            'covered': ('django.db.models.fields.IntegerField', [], {}),
            'covered_pct': ('django.db.models.fields.FloatField', [], {}),
            'covered_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'covered_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'direct_purchase': ('django.db.models.fields.IntegerField', [], {}),
            'direct_purchase_pct': ('django.db.models.fields.FloatField', [], {}),
            'direct_purchase_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'direct_purchase_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'govt': ('django.db.models.fields.IntegerField', [], {}),
            'govt_pct': ('django.db.models.fields.FloatField', [], {}),
            'govt_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'govt_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medicaid': ('django.db.models.fields.IntegerField', [], {}),
            'medicaid_pct': ('django.db.models.fields.FloatField', [], {}),
            'medicaid_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'medicaid_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'medicare': ('django.db.models.fields.IntegerField', [], {}),
            'medicare_pct': ('django.db.models.fields.FloatField', [], {}),
            'medicare_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'medicare_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'military': ('django.db.models.fields.IntegerField', [], {}),
            'military_pct': ('django.db.models.fields.FloatField', [], {}),
            'military_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'military_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'not_covered': ('django.db.models.fields.IntegerField', [], {}),
            'not_covered_pct': ('django.db.models.fields.FloatField', [], {}),
            'not_covered_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'not_covered_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'private': ('django.db.models.fields.IntegerField', [], {}),
            'private_employment': ('django.db.models.fields.IntegerField', [], {}),
            'private_employment_pct': ('django.db.models.fields.FloatField', [], {}),
            'private_employment_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'private_employment_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'private_pct': ('django.db.models.fields.FloatField', [], {}),
            'private_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'private_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.highschooldropouts': {
            'Meta': {'object_name': 'HighSchoolDropouts'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.highschoolother': {
            'Meta': {'object_name': 'HighSchoolOther'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.housingunits': {
            'Meta': {'object_name': 'HousingUnits'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.individualeducationprograms': {
            'Meta': {'object_name': 'IndividualEducationPrograms'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.kidshealthinsurance': {
            'Meta': {'object_name': 'KidsHealthInsurance'},
            'all_people': ('django.db.models.fields.IntegerField', [], {}),
            'covered': ('django.db.models.fields.IntegerField', [], {}),
            'covered_pct': ('django.db.models.fields.FloatField', [], {}),
            'covered_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'covered_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'direct_purchase': ('django.db.models.fields.IntegerField', [], {}),
            'direct_purchase_pct': ('django.db.models.fields.FloatField', [], {}),
            'direct_purchase_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'direct_purchase_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'govt': ('django.db.models.fields.IntegerField', [], {}),
            'govt_pct': ('django.db.models.fields.FloatField', [], {}),
            'govt_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'govt_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medicaid': ('django.db.models.fields.IntegerField', [], {}),
            'medicaid_pct': ('django.db.models.fields.FloatField', [], {}),
            'medicaid_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'medicaid_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'medicare': ('django.db.models.fields.IntegerField', [], {}),
            'medicare_pct': ('django.db.models.fields.FloatField', [], {}),
            'medicare_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'medicare_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'military': ('django.db.models.fields.IntegerField', [], {}),
            'military_pct': ('django.db.models.fields.FloatField', [], {}),
            'military_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'military_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'not_covered': ('django.db.models.fields.IntegerField', [], {}),
            'not_covered_pct': ('django.db.models.fields.FloatField', [], {}),
            'not_covered_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'not_covered_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'private': ('django.db.models.fields.IntegerField', [], {}),
            'private_employment': ('django.db.models.fields.IntegerField', [], {}),
            'private_employment_pct': ('django.db.models.fields.FloatField', [], {}),
            'private_employment_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'private_employment_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'private_pct': ('django.db.models.fields.FloatField', [], {}),
            'private_pct_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'private_se': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.laborforcecounty': {
            'Meta': {'unique_together': "(('year', 'state', 'county'),)", 'object_name': 'LaborForceCounty'},
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.County']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'employment_total': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labor_force': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'laus_code': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'unemployment_rate': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'unemployment_total': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.laborforcecountyraw': {
            'Meta': {'object_name': 'LaborForceCountyRaw'},
            'county_fips': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'county_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'employed': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labor_force': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'laus_code': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'state_fips': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'unemployed': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'unemployment_rate': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.laborunderutilizationstate': {
            'Meta': {'unique_together': "(('year', 'state'),)", 'object_name': 'LaborUnderutilizationState'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'u1': ('django.db.models.fields.FloatField', [], {}),
            'u2': ('django.db.models.fields.FloatField', [], {}),
            'u3': ('django.db.models.fields.FloatField', [], {}),
            'u4': ('django.db.models.fields.FloatField', [], {}),
            'u5': ('django.db.models.fields.FloatField', [], {}),
            'u6': ('django.db.models.fields.FloatField', [], {}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.laborunderutilizationstateraw': {
            'Meta': {'object_name': 'LaborUnderutilizationStateRaw'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'u1': ('django.db.models.fields.FloatField', [], {}),
            'u2': ('django.db.models.fields.FloatField', [], {}),
            'u3': ('django.db.models.fields.FloatField', [], {}),
            'u4': ('django.db.models.fields.FloatField', [], {}),
            'u5': ('django.db.models.fields.FloatField', [], {}),
            'u6': ('django.db.models.fields.FloatField', [], {}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.mathsciencespending': {
            'Meta': {'object_name': 'MathScienceSpending'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.medicaidparticipation': {
            'Meta': {'object_name': 'MedicaidParticipation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.medicareenrollment': {
            'Meta': {'object_name': 'MedicareEnrollment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.migrantstudents': {
            'Meta': {'object_name': 'MigrantStudents'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.militarypersonnel': {
            'Meta': {'object_name': 'MilitaryPersonnel'},
            'civilian_personnel': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'military_personnel': ('django.db.models.fields.IntegerField', [], {}),
            'reserve_national_guard_personnel': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.msncodes': {
            'Meta': {'object_name': 'MsnCodes'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msn': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'data.nativeedspending': {
            'Meta': {'object_name': 'NativeEdSpending'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.ncesschooldistrict': {
            'Meta': {'object_name': 'NcesSchoolDistrict'},
            'congress_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'county_code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'county_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'district_code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'district_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'state_code': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'data.newaidscases': {
            'Meta': {'object_name': 'NewAidsCases'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.otherfederalrevenue': {
            'Meta': {'object_name': 'OtherFederalRevenue'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        'data.ownersrenters': {
            'Meta': {'object_name': 'OwnersRenters'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'not_in_universe': ('django.db.models.fields.IntegerField', [], {}),
            'owned': ('django.db.models.fields.IntegerField', [], {}),
            'rented': ('django.db.models.fields.IntegerField', [], {}),
            'rented_no_cash': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'total': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.peopleinpoverty': {
            'Meta': {'object_name': 'PeopleInPoverty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percent': ('django.db.models.fields.FloatField', [], {}),
            'percent_standard_error': ('django.db.models.fields.FloatField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'total_population': ('django.db.models.fields.IntegerField', [], {}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'value_standard_error': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.populationagecounty': {
            'Meta': {'unique_together': "(('year', 'state', 'county'),)", 'object_name': 'PopulationAgeCounty'},
            'age_0_19': ('django.db.models.fields.IntegerField', [], {}),
            'age_0_19_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_0_4': ('django.db.models.fields.IntegerField', [], {}),
            'age_0_4_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_10_14': ('django.db.models.fields.IntegerField', [], {}),
            'age_10_14_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_15_19': ('django.db.models.fields.IntegerField', [], {}),
            'age_15_19_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_20_24': ('django.db.models.fields.IntegerField', [], {}),
            'age_20_24_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_25_29': ('django.db.models.fields.IntegerField', [], {}),
            'age_25_29_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_30_34': ('django.db.models.fields.IntegerField', [], {}),
            'age_30_34_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_35_39': ('django.db.models.fields.IntegerField', [], {}),
            'age_35_39_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_40_44': ('django.db.models.fields.IntegerField', [], {}),
            'age_40_44_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_45_49': ('django.db.models.fields.IntegerField', [], {}),
            'age_45_49_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_50_54': ('django.db.models.fields.IntegerField', [], {}),
            'age_50_54_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_55_59': ('django.db.models.fields.IntegerField', [], {}),
            'age_55_59_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_5_9': ('django.db.models.fields.IntegerField', [], {}),
            'age_5_9_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_60_64': ('django.db.models.fields.IntegerField', [], {}),
            'age_60_64_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_65_69': ('django.db.models.fields.IntegerField', [], {}),
            'age_65_69_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_65_over': ('django.db.models.fields.IntegerField', [], {}),
            'age_65_over_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_70_74': ('django.db.models.fields.IntegerField', [], {}),
            'age_70_74_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_75_79': ('django.db.models.fields.IntegerField', [], {}),
            'age_75_79_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_80_84': ('django.db.models.fields.IntegerField', [], {}),
            'age_80_84_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_85_over': ('django.db.models.fields.IntegerField', [], {}),
            'age_85_over_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.County']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'total': ('django.db.models.fields.IntegerField', [], {}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.populationagestate': {
            'Meta': {'unique_together': "(('year', 'state'),)", 'object_name': 'PopulationAgeState'},
            'age_0_19': ('django.db.models.fields.IntegerField', [], {}),
            'age_0_19_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_0_4': ('django.db.models.fields.IntegerField', [], {}),
            'age_0_4_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_10_14': ('django.db.models.fields.IntegerField', [], {}),
            'age_10_14_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_15_19': ('django.db.models.fields.IntegerField', [], {}),
            'age_15_19_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_20_24': ('django.db.models.fields.IntegerField', [], {}),
            'age_20_24_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_25_29': ('django.db.models.fields.IntegerField', [], {}),
            'age_25_29_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_30_34': ('django.db.models.fields.IntegerField', [], {}),
            'age_30_34_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_35_39': ('django.db.models.fields.IntegerField', [], {}),
            'age_35_39_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_40_44': ('django.db.models.fields.IntegerField', [], {}),
            'age_40_44_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_45_49': ('django.db.models.fields.IntegerField', [], {}),
            'age_45_49_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_50_54': ('django.db.models.fields.IntegerField', [], {}),
            'age_50_54_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_55_59': ('django.db.models.fields.IntegerField', [], {}),
            'age_55_59_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_5_9': ('django.db.models.fields.IntegerField', [], {}),
            'age_5_9_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_60_64': ('django.db.models.fields.IntegerField', [], {}),
            'age_60_64_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_65_69': ('django.db.models.fields.IntegerField', [], {}),
            'age_65_69_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_65_over': ('django.db.models.fields.IntegerField', [], {}),
            'age_65_over_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_70_74': ('django.db.models.fields.IntegerField', [], {}),
            'age_70_74_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_75_79': ('django.db.models.fields.IntegerField', [], {}),
            'age_75_79_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_80_84': ('django.db.models.fields.IntegerField', [], {}),
            'age_80_84_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_85_over': ('django.db.models.fields.IntegerField', [], {}),
            'age_85_over_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'total': ('django.db.models.fields.IntegerField', [], {}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.populationcongressionaldistrict': {
            'Meta': {'object_name': 'PopulationCongressionalDistrict'},
            'american_indian_alaskan_alone': ('django.db.models.fields.IntegerField', [], {}),
            'asian_alone': ('django.db.models.fields.IntegerField', [], {}),
            'black_alone': ('django.db.models.fields.IntegerField', [], {}),
            'district': ('django.db.models.fields.IntegerField', [], {}),
            'hawaiian_pacific_island_alone': ('django.db.models.fields.IntegerField', [], {}),
            'households': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other_alone': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'two_or_more_races': ('django.db.models.fields.IntegerField', [], {}),
            'white_alone': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.populationest00raw': {
            'Meta': {'unique_together': "(('state', 'county', 'gender', 'ethnic_origin', 'race'),)", 'object_name': 'PopulationEst00Raw'},
            'census2010pop': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ctyname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'estimatesbase2000': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'ethnic_origin': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'popestimate2000': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'popestimate2001': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'popestimate2002': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'popestimate2003': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'popestimate2004': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'popestimate2005': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'popestimate2006': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'popestimate2007': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'popestimate2008': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'popestimate2009': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'popestimate2010': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'stname': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'sumlev': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'data.populationest90raw': {
            'Meta': {'unique_together': "(('year', 'state', 'county', 'agegrp', 'race_gender', 'ethnic_origin'),)", 'object_name': 'PopulationEst90Raw'},
            'agegrp': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ethnic_origin': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'race_gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'update_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'data.populationfamilies': {
            'Meta': {'object_name': 'PopulationFamilies'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.populationgendercounty': {
            'Meta': {'unique_together': "(('year', 'state', 'county'),)", 'object_name': 'PopulationGenderCounty'},
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.County']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'female': ('django.db.models.fields.IntegerField', [], {}),
            'female_percent': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male': ('django.db.models.fields.IntegerField', [], {}),
            'male_percent': ('django.db.models.fields.FloatField', [], {}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'total': ('django.db.models.fields.IntegerField', [], {}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.populationgenderstate': {
            'Meta': {'unique_together': "(('year', 'state'),)", 'object_name': 'PopulationGenderState'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'female': ('django.db.models.fields.IntegerField', [], {}),
            'female_percent': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male': ('django.db.models.fields.IntegerField', [], {}),
            'male_percent': ('django.db.models.fields.FloatField', [], {}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'total': ('django.db.models.fields.IntegerField', [], {}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.populationracecounty': {
            'Meta': {'unique_together': "(('year', 'state', 'county'),)", 'object_name': 'PopulationRaceCounty'},
            'asian_alone': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'asian_alone_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'asian_alone_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'asian_alone_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'asian_alone_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'asian_alone_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'asian_other': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'asian_other_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'asian_other_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'asian_other_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'asian_other_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'asian_other_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'asian_pacific_islander_alone': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'asian_pacific_islander_alone_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'black_alone': ('django.db.models.fields.IntegerField', [], {}),
            'black_alone_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'black_alone_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'black_alone_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'black_alone_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'black_alone_percent': ('django.db.models.fields.FloatField', [], {}),
            'black_other': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'black_other_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'black_other_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'black_other_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'black_other_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'black_other_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.County']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiple_race': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'multiple_race_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'multiple_race_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'multiple_race_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'multiple_race_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'multiple_race_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'native_alone': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'native_alone_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'native_alone_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'native_alone_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'native_alone_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'native_alone_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'native_other': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'native_other_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'native_other_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'native_other_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'native_other_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'native_other_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'other': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'other_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'pacific_islander_alone': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pacific_islander_alone_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pacific_islander_alone_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'pacific_islander_alone_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pacific_islander_alone_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'pacific_islander_alone_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'pacific_islander_other': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pacific_islander_other_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pacific_islander_other_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'pacific_islander_other_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pacific_islander_other_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'pacific_islander_other_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'total': ('django.db.models.fields.IntegerField', [], {}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'white_alone': ('django.db.models.fields.IntegerField', [], {}),
            'white_alone_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'white_alone_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'white_alone_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'white_alone_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'white_alone_percent': ('django.db.models.fields.FloatField', [], {}),
            'white_other': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'white_other_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'white_other_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'white_other_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'white_other_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'white_other_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.populationracestate': {
            'Meta': {'unique_together': "(('year', 'state'),)", 'object_name': 'PopulationRaceState'},
            'asian_alone': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'asian_alone_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'asian_alone_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'asian_alone_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'asian_alone_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'asian_alone_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'asian_other': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'asian_other_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'asian_other_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'asian_other_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'asian_other_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'asian_other_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'asian_pacific_islander_alone': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'asian_pacific_islander_alone_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'black_alone': ('django.db.models.fields.IntegerField', [], {}),
            'black_alone_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'black_alone_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'black_alone_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'black_alone_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'black_alone_percent': ('django.db.models.fields.FloatField', [], {}),
            'black_other': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'black_other_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'black_other_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'black_other_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'black_other_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'black_other_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiple_race': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'multiple_race_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'multiple_race_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'multiple_race_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'multiple_race_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'multiple_race_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'native_alone': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'native_alone_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'native_alone_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'native_alone_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'native_alone_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'native_alone_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'native_other': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'native_other_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'native_other_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'native_other_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'native_other_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'native_other_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'other': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'other_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'pacific_islander_alone': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pacific_islander_alone_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pacific_islander_alone_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'pacific_islander_alone_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pacific_islander_alone_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'pacific_islander_alone_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'pacific_islander_other': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pacific_islander_other_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pacific_islander_other_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'pacific_islander_other_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pacific_islander_other_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'pacific_islander_other_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'total': ('django.db.models.fields.IntegerField', [], {}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'white_alone': ('django.db.models.fields.IntegerField', [], {}),
            'white_alone_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'white_alone_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'white_alone_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'white_alone_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'white_alone_percent': ('django.db.models.fields.FloatField', [], {}),
            'white_other': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'white_other_hispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'white_other_hispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'white_other_nonhispanic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'white_other_nonhispanic_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'white_other_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.presidentsbudget': {
            'Meta': {'object_name': 'PresidentsBudget'},
            'account_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'account_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'agency_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bea_category': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'budget_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'bureau_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'bureau_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'grant_non_grant': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'on_off_budget': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'source_category_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'source_category_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'source_subcategory_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'source_subcategory_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'subfunction_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'subfunction_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'treasury_agency_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'data.presidentsbudgetyear': {
            'Meta': {'object_name': 'PresidentsBudgetYear'},
            'budget': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'years'", 'to': "orm['data.PresidentsBudget']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'data.pupilteacherdistrict': {
            'Meta': {'object_name': 'PupilTeacherDistrict'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.pupilteacherstate': {
            'Meta': {'unique_together': "(('year', 'state'),)", 'object_name': 'PupilTeacherState'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ratio': ('django.db.models.fields.FloatField', [], {}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.pupilteacherstateraw': {
            'Meta': {'object_name': 'PupilTeacherStateRaw'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ratio': ('django.db.models.fields.FloatField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.race': {
            'Meta': {'object_name': 'Race'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race_abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'race_desc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'race_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'data.racecombo': {
            'Meta': {'object_name': 'RaceCombo'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race_combo_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'race_combo_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'data.retireddisablednilf': {
            'Meta': {'object_name': 'RetiredDisabledNilf'},
            'disabled_not_in_labor_force': ('django.db.models.fields.IntegerField', [], {}),
            'employed_absent': ('django.db.models.fields.IntegerField', [], {}),
            'employed_at_work': ('django.db.models.fields.IntegerField', [], {}),
            'employed_on_layoff': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other_not_in_labor_force': ('django.db.models.fields.IntegerField', [], {}),
            'retired_not_in_labor_force': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'total': ('django.db.models.fields.IntegerField', [], {}),
            'unemployed_looking': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.saipecountystate': {
            'Meta': {'object_name': 'SaipeCountyState'},
            'age_0_17_poverty': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'age_0_17_poverty_90_lower': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'age_0_17_poverty_90_upper': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'age_0_17_poverty_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_0_17_poverty_percent_90_lower': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_0_17_poverty_percent_90_upper': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_0_5_poverty': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'age_0_5_poverty_90_lower': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'age_0_5_poverty_90_upper': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'age_0_5_poverty_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_0_5_poverty_percent_90_lower': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_0_5_poverty_percent_90_upper': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_5_17_related_poverty': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'age_5_17_related_poverty_90_lower': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'age_5_17_related_poverty_90_upper': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'age_5_17_related_poverty_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_5_17_related_poverty_percent_90_lower': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'age_5_17_related_poverty_percent_90_upper': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'all_age_poverty': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'all_age_poverty_90_lower': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'all_age_poverty_90_upper': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'all_age_poverty_percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'all_age_poverty_percent_90_lower': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'all_age_poverty_percent_90_upper': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'file_tag': ('django.db.models.fields.CharField', [], {'max_length': '22'}),
            'fips_county': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'fips_state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'median_household_income': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'median_household_income_90_lower': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'median_household_income_90_upper': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'state_county_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'state_postal_abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.saipeschool': {
            'Meta': {'object_name': 'SaipeSchool'},
            'ccd_district_id': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'district_name': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'file_stamp': ('django.db.models.fields.CharField', [], {'max_length': '21'}),
            'fips_state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {}),
            'relevant_population': ('django.db.models.fields.IntegerField', [], {}),
            'relevant_population_poverty': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.schipenrollment': {
            'Meta': {'object_name': 'SchipEnrollment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.schoolbreakfastparticipation': {
            'Meta': {'object_name': 'SchoolBreakfastParticipation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.schoollunchparticipation': {
            'Meta': {'object_name': 'SchoolLunchParticipation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.shelterpopulation': {
            'Meta': {'object_name': 'ShelterPopulation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percent': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.snapbenefitsrecipients': {
            'Meta': {'object_name': 'SnapBenefitsRecipients'},
            'county_fips': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'state_fips': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.snapmonthlybenefitsperson': {
            'Meta': {'object_name': 'SnapMonthlyBenefitsPerson'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.FloatField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.snapparticipationhouseholds': {
            'Meta': {'object_name': 'SnapParticipationHouseholds'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.snapparticipationpeople': {
            'Meta': {'object_name': 'SnapParticipationPeople'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.source': {
            'Meta': {'object_name': 'Source'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'string_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'data.specialedfunding': {
            'Meta': {'object_name': 'SpecialEdFunding'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.state': {
            'Meta': {'object_name': 'State'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'}),
            'state_abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'state_ansi': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'state_desc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'state_gnisid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'data.statecompletionrate': {
            'Meta': {'object_name': 'StateCompletionRate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.stateemissions': {
            'Meta': {'object_name': 'StateEmissions'},
            'co2': ('django.db.models.fields.IntegerField', [], {}),
            'energy_source': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nox': ('django.db.models.fields.IntegerField', [], {}),
            'producer_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'so2': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.stateenergyproductionestimates': {
            'Meta': {'object_name': 'StateEnergyProductionEstimates'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msn': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'value': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.stategdp': {
            'Meta': {'object_name': 'StateGdp'},
            'component': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'component_code': ('django.db.models.fields.IntegerField', [], {}),
            'fips': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'industry_code': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.stategdppre97': {
            'Meta': {'object_name': 'StateGdpPre97'},
            'component': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'component_code': ('django.db.models.fields.IntegerField', [], {}),
            'fips': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'industry_code': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.statelaborforceparticipation': {
            'Meta': {'object_name': 'StateLaborForceParticipation'},
            'civilian_labor_force': ('django.db.models.fields.IntegerField', [], {}),
            'civilian_noninstitutional_pop': ('django.db.models.fields.IntegerField', [], {}),
            'employment_pop_rate': ('django.db.models.fields.FloatField', [], {}),
            'employment_total': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labor_force_participation_rate': ('django.db.models.fields.FloatField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'unemployment_rate': ('django.db.models.fields.FloatField', [], {}),
            'unemployment_total': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.statemedianincome': {
            'Meta': {'object_name': 'StateMedianIncome'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'median_income': ('django.db.models.fields.FloatField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.statepostalcodes': {
            'Meta': {'object_name': 'StatePostalCodes'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'data.staterenewableenergy': {
            'Meta': {'object_name': 'StateRenewableEnergy'},
            'fossil_coal': ('django.db.models.fields.FloatField', [], {}),
            'fossil_gas': ('django.db.models.fields.FloatField', [], {}),
            'fossil_oil': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nuclear_electric': ('django.db.models.fields.FloatField', [], {}),
            'renewable_biofuels': ('django.db.models.fields.FloatField', [], {}),
            'renewable_other': ('django.db.models.fields.FloatField', [], {}),
            'renewable_total': ('django.db.models.fields.FloatField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.subfunctionscffr': {
            'Meta': {'object_name': 'SubfunctionsCffr'},
            'at_code_1': ('django.db.models.fields.TextField', [], {'max_length': '1', 'null': 'True'}),
            'at_code_2': ('django.db.models.fields.TextField', [], {'max_length': '1', 'null': 'True'}),
            'at_code_3': ('django.db.models.fields.TextField', [], {'max_length': '1', 'null': 'True'}),
            'at_code_4': ('django.db.models.fields.TextField', [], {'max_length': '1', 'null': 'True'}),
            'at_code_5': ('django.db.models.fields.TextField', [], {'max_length': '1', 'null': 'True'}),
            'at_code_6': ('django.db.models.fields.TextField', [], {'max_length': '1', 'null': 'True'}),
            'at_code_7': ('django.db.models.fields.TextField', [], {'max_length': '1', 'null': 'True'}),
            'at_code_8': ('django.db.models.fields.TextField', [], {'max_length': '1', 'null': 'True'}),
            'cfda_program_code': ('django.db.models.fields.TextField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program_name': ('django.db.models.fields.TextField', [], {'max_length': '64'}),
            'subfunction_name': ('django.db.models.fields.TextField', [], {'max_length': '64'}),
            'subfunction_number': ('django.db.models.fields.TextField', [], {'max_length': '3'})
        },
        'data.summerlunchparticipation': {
            'Meta': {'object_name': 'SummerLunchParticipation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.tanffamilystateraw': {
            'Meta': {'object_name': 'TanfFamilyStateRaw'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.tanfparticipationstate': {
            'Meta': {'unique_together': "(('year', 'state'),)", 'object_name': 'TanfParticipationState'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'family': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.tanfparticipationstateraw': {
            'Meta': {'object_name': 'TanfParticipationStateRaw'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.titleifunding': {
            'Meta': {'object_name': 'TitleIFunding'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.totalstudents': {
            'Meta': {'object_name': 'TotalStudents'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.vehicleregistrations': {
            'Meta': {'object_name': 'VehicleRegistrations'},
            'all_private': ('django.db.models.fields.IntegerField', [], {}),
            'all_public': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'all_total': ('django.db.models.fields.IntegerField', [], {}),
            'auto_private': ('django.db.models.fields.IntegerField', [], {}),
            'auto_public': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'auto_total': ('django.db.models.fields.IntegerField', [], {}),
            'buses_private': ('django.db.models.fields.IntegerField', [], {}),
            'buses_public': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'buses_total': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motorcycle_private': ('django.db.models.fields.IntegerField', [], {}),
            'motorcycle_public': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'private_commercial_per_capita': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'trucks_private': ('django.db.models.fields.IntegerField', [], {}),
            'trucks_public': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'trucks_total': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.vocationaledspending': {
            'Meta': {'object_name': 'VocationalEdSpending'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.wicbenefitsstate': {
            'Meta': {'unique_together': "(('year', 'state'),)", 'object_name': 'WicBenefitsState'},
            'amount': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.wicbenefitsstateraw': {
            'Meta': {'object_name': 'WicBenefitsStateRaw'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.wicparticipationstate': {
            'Meta': {'unique_together': "(('year', 'state'),)", 'object_name': 'WicParticipationState'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.State']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.wicparticipationstateraw': {
            'Meta': {'object_name': 'WicParticipationStateRaw'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['data']
