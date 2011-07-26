from django import db
from django.core.management.base import NoArgsCommand
from data.models import Race

# National Priorities Project Data Repository
# load_race.py 
# Created 7/21/2011

# Populates the race reference table
# source model(s): none. races based on those used for census annual pop. estimates
# destination model:  Race

# HOWTO:
# 1) Run as Django management command from your project path "python manage.py load_race

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        race_row = Race(race_abbr='a', race_name='asian', race_desc='Asian')
        race_row.save()
        race_row = Race(race_abbr='b', race_name='black', race_desc='Black or African American')
        race_row.save()
        race_row = Race(race_abbr='n', race_name='native', race_desc='American Indian and Alaska Native')
        race_row.save()
        race_row = Race(race_abbr='p', race_name='pacific', race_desc='Native Hawaiian or other Pacific Islander')
        race_row.save()
        race_row = Race(race_abbr='w', race_name='white', race_desc='White')
        race_row.save()
        race_row = Race(race_abbr='ap', race_name='asian pacific', race_desc='Asian or Pacific Islander')
        race_row.save()
        race_row = Race(race_abbr='o', race_name='other', race_desc='Other')
        race_row.save()
        db.reset_queries()