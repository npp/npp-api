from django import db
from django.core.management.base import NoArgsCommand
from data.models import AnsiCountyState, StateRef, CountyRef

# National Priorities Project Data Repository
# load_county_ref.py 
# Created 5/10/2011

# Populates the state reference used by the API
# source model(s): AnsiState
# source load command(s): import_ansi_county
# destination model:  CountyRef

# HOWTO:
# 1) Ensure that AnsiCountyState and StateRef are loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_county_ref

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        abbr = ''
        for c in AnsiCountyState.objects.order_by('state'):
            if c.state != abbr:
                state_ref_current = StateRef.objects.get(state_abbr=c.state)
                abbr = c.state
                #for each state, add a county-level record to be used for
                #tracking CFFR state undistributed funds
                county_ref_row = CountyRef(state_ref=state_ref_current, county_ansi='999', county_name='State undistributed')
                county_ref_row.save()
                db.reset_queries()
            county_ref_row = CountyRef(state_ref=state_ref_current, county_ansi=c.code, county_name=c.county)
            county_ref_row.save()
            db.reset_queries() 
            