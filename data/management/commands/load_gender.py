from django import db
from django.core.management.base import NoArgsCommand
from data.models import Gender

# National Priorities Project Data Repository
# load_gender.py 
# Created 7/21/2011

# Populates the gender reference table
# source model(s): none
# destination model:  Gender

# HOWTO:
# 1) Run as Django management command from your project path "python manage.py load_gender

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        gender_row = Gender(gender_abbr='F', gender_name = 'female')
        gender_row.save()
        gender_row = Gender(gender_abbr='M', gender_name = 'male')
        gender_row.save()
        db.reset_queries()