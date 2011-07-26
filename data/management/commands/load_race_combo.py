from django import db
from django.core.management.base import NoArgsCommand
from data.models import RaceCombo

# National Priorities Project Data Repository
# load_race_combo.py 
# Created 7/21/2011

# Populates the race combo reference table
# source model(s): none. categories based on those used for census annual pop. estimates
# destination model:  RaceCombo

# HOWTO:
# 1) Run as Django management command from your project path "python manage.py load_race_combo

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        race_combo_row = RaceCombo(race_combo_flag=False,race_combo_name='alone')
        race_combo_row.save()
        race_combo_row = RaceCombo(race_combo_flag=True,race_combo_name='in combination')
        race_combo_row.save()
        db.reset_queries()