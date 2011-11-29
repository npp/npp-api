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
        state_name = ''
        total_inserts = 0
        total_updates = 0
        
        raw = FederalTaxCollectionStateRaw.objects.all().order_by('state')
        total_raw = raw.count()
        
        for r in raw:
        
            if r.state != state_name:
                try:
                    if r.state.lower().find('undistributed') >= 0:
                        state_ref_current = State.objects.get(state_abbr='UD')
                    elif r.state.lower().find('maryland and district') >= 0:
                        state_ref_current = State.objects.get(state_abbr='MD')
                    else:
                        state_ref_current = State.objects.get(state_name=r.state)
                except:
                    #print 'Skipping record. Unable to find state: ' + r.state
                    continue
                state_name = r.state
            
            record, created = FederalTaxCollectionState.objects.get_or_create(state=state_ref_current,year=r.year)
            record.total = r.total_collections
            record.business_income = r.business_income_taxes
            record.individual_total = r.individual_total
            record.individual_witheld_fica = r.individual_witheld_fica
            record.individual_notwitheld_seca = r.individual_notwitheld_seca
            record.individual_unemployment = r.individual_unemployment
            record.individual_railroad_retirement = r.individual_railroad_retirement
            record.individual_estate_trust_income = r.individual_estate_trust_income
            record.estate = r.estate_tax
            record.gift = r.gift_tax
            record.excise = r.excise_taxes
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
                individual_total=Sum('individual_total'),
                individual_witheld_fica=Sum('individual_witheld_fica'),
                individual_notwitheld_seca=Sum('individual_notwitheld_seca'),
                individual_unemployment=Sum('individual_unemployment'),
                individual_railroad_retirement=Sum('individual_railroad_retirement'),
                individual_estate_trust_income=Sum('individual_estate_trust_income'),
                estate=Sum('estate_tax'),
                gift=Sum('gift_tax'),
                excise=Sum('excise_taxes')
                ))
        for i in international:
            record, created = FederalTaxCollectionState.objects.get_or_create(state=state_ref_current,year=i['year'])
            record.total = i.get('total_collections')
            record.business_income = i.get('business_income')
            record.individual_total = i.get('individual_total')
            record.individual_witheld_fica = i.get('individual_witheld_fica')
            record.individual_notwitheld_seca = i.get('individual_notwitheld_seca')
            record.individual_unemployment = i.get('individual_unemployment')
            record.individual_railroad_retirement = i.get('individual_railroad_retirement')
            record.individual_estate_trust_income = i.get('individual_estate_trust_income')
            record.estate = i.get('estate')
            record.gift = i.get('gift')
            record.excise = i.get('excise')
            if created:
                total_inserts = total_inserts + 1
            else:
                total_updates = total_updates + 1
            record.save()
            db.reset_queries()
                
        print 'Federal Tax Collection: total records from raw data = ' + str(total_raw)
        print 'Federal Tax Collection: total inserts = ' + str(total_inserts)
        print 'Federal Tax Collection: total updates = ' + str(total_updates)