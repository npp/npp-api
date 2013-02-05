from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, FederalTaxCollectionStateRaw, FederalTaxCollectionState
from django.db.models import Sum, Q

# National Priorities Project Data Repository
# load_federal_tax_collection_state.py 
# Created 11/28/2011

# Populates Federal Tax Collection used by the API
# source model(s): FederalTaxCollectionStateRaw, State
# source load command(s): import_federal_tax_collection
# destination model:  FederalTaxCollectionState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_federal_tax_collection_state

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        def clean_value(value):
            if value is not None:
                return value
            else:
                return 0
            
        state_name = ''
        total_inserts = 0
        total_updates = 0
        
        raw = FederalTaxCollectionStateRaw.objects.all().order_by('state')
        total_raw = raw.count()
        
        for r in raw:
        
            if r.state != state_name:
                try:
                    if r.state.lower().find('undistributed') >= 0:
                        state_ref_current = State.objects.get(state_abbr__iexact='UD')
                    elif r.state.lower().find('maryland and district') >= 0:
                        state_ref_current = State.objects.get(state_abbr__iexact='MD')
                    else:
                        state_ref_current = State.objects.get(state_name__iexact=r.state)
                except:
                    #print 'Skipping record. Unable to find state: ' + r.state
                    continue
                state_name = r.state
            
            record, created = FederalTaxCollectionState.objects.get_or_create(state=state_ref_current,year=r.year)
            record.total = r.total_collections
            record.business_income = r.business_income_taxes
            record.witheld_income_and_fica = r.individual_witheld_fica
            record.notwitheld_income_and_seca = r.individual_notwitheld_seca
            record.unemployment_insurance = r.unemployment_insurance
            record.railroad_retirement = r.railroad_retirement
            record.estate_trust_income = r.estate_trust_income_tax
            record.estate = r.estate_tax
            record.gift = r.gift_tax
            record.excise = r.excise_taxes
            record.individual_total = (clean_value(r.individual_witheld_fica) + 
                clean_value(r. individual_notwitheld_seca) + clean_value(r.estate_trust_income_tax) + 
                clean_value(r.estate_tax) + clean_value(r.gift_tax) + clean_value(r.excise_taxes))
            if created:
                total_inserts = total_inserts + 1
            else:
                total_updates = total_updates + 1
            record.save()
            db.reset_queries()
            
        #calculate "other international taxes," the group & labeling of which vary from year to year
        state_ref_current = State.objects.get(state_abbr='OI')
        international = (FederalTaxCollectionStateRaw.objects.filter(Q(state__icontains='other')|Q(state__icontains='armed service')|Q(state__icontains='international',year__gt=2005))
            .values('year')
            .annotate(
                total_collections=Sum('total_collections'),
                business_income=Sum('business_income_taxes'),
                witheld_income_and_fica=Sum('individual_witheld_fica'),
                notwitheld_income_and_seca=Sum('individual_notwitheld_seca'),
                unemployment_insurance=Sum('unemployment_insurance'),
                railroad_retirement=Sum('railroad_retirement'),
                estate_trust_income=Sum('estate_trust_income_tax'),
                estate=Sum('estate_tax'),
                gift=Sum('gift_tax'),
                excise=Sum('excise_taxes')
                ))
        for i in international:
            record, created = FederalTaxCollectionState.objects.get_or_create(state=state_ref_current,year=i['year'])
            record.total = i.get('total_collections')
            record.business_income = i.get('business_income')
            record.witheld_income_and_fica = i.get('witheld_income_and_fica')
            record.notwitheld_income_and_seca = i.get('notwitheld_income_and_seca')
            record.unemployment_insurance = i.get('unemployment_insurance')
            record.railroad_retirement = i.get('railroad_retirement')
            record.estate_trust_income = i.get('estate_trust_income_tax')
            record.estate = i.get('estate')
            record.gift = i.get('gift')
            record.excise = i.get('excise')
            record.individual_total = (clean_value(i.get('witheld_income_and_fica')) + 
                clean_value(i.get('notwitheld_income_and_seca')) +
                clean_value(i.get('estate_trust_income')) + clean_value(i.get('estate')) + 
                clean_value(i.get('gift')) + clean_value(i.get('excise')))
            if created:
                total_inserts = total_inserts + 1
            else:
                total_updates = total_updates + 1
            record.save()
            db.reset_queries()
                
        print 'Federal Tax Collection: total records from raw data = ' + str(total_raw)
        print 'Federal Tax Collection: total inserts = ' + str(total_inserts)
        print 'Federal Tax Collection: total updates = ' + str(total_updates)