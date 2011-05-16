from django import db
from django.core.management.base import NoArgsCommand
from data.models import AnsiState, StateRef

# National Priorities Project Data Repository
# load_state_ref.py 
# Created 5/10/2011

# Populates the state reference used by the API
# source model(s): AnsiState
# source load command(s): import_ansi_state
# destination model:  StateRef

# HOWTO:
# 1) Ensure that AnsiState model is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_state_ref

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        for s in AnsiState.objects.all():
            state_ref_row = StateRef(state_ansi=s.ansi_state, state_abbr = s.state, state_name = s.state_name, state_gnisid = s.gnisid)
            state_ref_row.save()
            db.reset_queries() 
        state_ref_row = StateRef(state_ansi='99', state_abbr='UD', state_name='U.S. undistributed')
        state_ref_row.save()
        db.reset_queries()