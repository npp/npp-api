from django import db
from django.core.management.base import NoArgsCommand
from data.models import AgeGroup

# National Priorities Project Data Repository
# load_age_group.py 
# Created 7/21/2011

# Populates the age group reference table
# source model(s): none. categories based on those used for census annual pop. estimates
# destination model:  AgeGroup

# HOWTO:
# 1) Run as Django management command from your project path "python manage.py load_age_group

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        age_row = AgeGroup(age_group_name='age_0_4',age_group_desc='age 0-4')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_5_9',age_group_desc='age 5-9')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_10_14',age_group_desc='age 10-14')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_15_19',age_group_desc='age 15-19')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_20_24',age_group_desc='age 20-24')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_25_29',age_group_desc='age 25-29')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_30_34',age_group_desc='age 30-34')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_35_39',age_group_desc='age 35-39')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_40_44',age_group_desc='age 40-44')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_45_49',age_group_desc='age 45-49')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_50_54',age_group_desc='age 50-54')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_55_59',age_group_desc='age 55-59')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_60_64',age_group_desc='age 60-64')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_65_69',age_group_desc='age 65-69')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_70_74',age_group_desc='age 70-74')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_75_79',age_group_desc='age 75-79')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_80_84',age_group_desc='age 80-84')
        age_row.save()
        age_row = AgeGroup(age_group_name='age_85_over',age_group_desc='age 85 and over')
        age_row.save()
        
        db.reset_queries()