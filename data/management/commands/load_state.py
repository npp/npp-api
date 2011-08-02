from django import db
from django.core.management.base import NoArgsCommand
from data.models import AnsiState, State

# National Priorities Project Data Repository
# load_state.py 
# Created 5/10/2011

# Populates the state reference used by the API
# source model(s): AnsiState
# source load command(s): import_ansi_state
# destination model:  State

# HOWTO:
# 1) Ensure that AnsiState model is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_state

# Safe to re-run?  Yes.

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        update_count = 0
        insert_count = 0
        
        for s in AnsiState.objects.all():
            state_change = False
            try:
                state_ref_row = State.objects.get(state_ansi=s.ansi_state)
                if state_ref_row.state_abbr <> s.state:
                    state_change = True
                    state_ref_row.state_abbr = s.state
                if state_ref_row.state_name <> s.state_name:
                    state_change = True
                    state_ref_row.state_name = s.state_name
                if state_ref_row.state_gnisid <> s.gnisid:
                    state_change = True
                    state_ref_row.state_gnisid = s.gnisid
                if state_change:
                    state_ref_row.save()
                    print str(s.ansi_state) + '(' + str(s.state) + ') updated'
                    update_count = update_count + 1
            except:
                state_ref_row = State(state_ansi=s.ansi_state, state_abbr = s.state, state_name = s.state_name, state_gnisid = s.gnisid)
                state_ref_row.save()
                insert_count = insert_count + 1
                print str(s.ansi_state) + '(' + str(s.state) + ') inserted'
                
        # a few ancillary state records (e.g., Undistributed funds, terriories not in the state ansi file)
        more_states = {}
        more_states['99'] = ['UD','U.S. undistributed']
        more_states['64'] = ['FM','Federated States of Micronesia']
        more_states['68'] = ['MH', 'Marshall Islands']
        more_states['70'] = ['PW', 'Palau']
        for s in more_states:
            try:
                state_ref_row = State(state_ansi=s, state_abbr = more_states[s][0], state_name = more_states[s][1])
                state_ref_row.save()
                insert_count = insert_count + 1
                print str(s) + '(' + str(more_states[s][0]) + ') inserted'
            except:
                continue
        
        db.reset_queries()
        