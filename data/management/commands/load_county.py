from django import db
from django.core.management.base import NoArgsCommand
from data.models import AnsiCountyState, State, County

# National Priorities Project Data Repository
# load_county.py 
# Created 5/10/2011

# Populates the state reference used by the API
# source model(s): AnsiState
# source load command(s): import_ansi_county
# destination model:  County

# HOWTO:
# 1) Ensure that AnsiCountyState and State are loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_county

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        abbr = ''
        for c in AnsiCountyState.objects.order_by('state'):
            if c.state != abbr:
                state_ref_current = State.objects.get(state_abbr=c.state)
                abbr = c.state
                #for each state, add 1) a county-level record to be used for
                #tracking CFFR state undistributed funds 2) an "unknown" county
                #record
                county_ref_row = County(state=state_ref_current, county_ansi='999', county_name='State undistributed')
                county_ref_row.save()
                county_ref_row = County(state=state_ref_current, county_ansi='000', county_name='Unknown county')
                county_ref_row.save()
                db.reset_queries()
            county_ref_row = County(state=state_ref_current, county_ansi=c.code, county_name=c.county)
            county_ref_row.save()
            
            db.reset_queries() 
            
        #add county row to correspond to US Undistributed state record
        state_ref_current = State.objects.get(state_ansi='99')
        county_ref_row = County(state=state_ref_current, county_ansi = '999', county_name = 'U.S. undistributed')
        county_ref_row.save()
        db.reset_queries()
            