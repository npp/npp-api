from django import db
from django.core.management.base import NoArgsCommand
from data.models import Ethnicity

# National Priorities Project Data Repository
# load_ethnicity.py 
# Created 7/21/2011

# Populates the ethnicity reference table
# source model(s): none. categories based on those used for census annual pop. estimates
# destination model:  Ethnicity

# HOWTO:
# 1) Run as Django management command from your project path "python manage.py load_ethnicity

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        ethnicity_row = Ethnicity(ethnicity_abbr='H',ethnicity_name='hispanic',ethnicity_desc='of Hispanic/Latino origin')
        ethnicity_row.save()
        ethnicity_row = Ethnicity(ethnicity_abbr='NH',ethnicity_name='not hispanic',ethnicity_desc='not of Hispanic/Latino origin')
        ethnicity_row.save()
        db.reset_queries()