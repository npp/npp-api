from django import db
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db.models import Sum
from data.models import PopulationEst10Raw, PopulationEst00Raw, PopulationGenderCounty, State, County
from datetime import datetime
from pandas import DataFrame
import pandas as pd
import numpy as np

# National Priorities Project Data Repository
# load_population_gender_county

# Populates Population Data used by API

# Safe to rerun: yes

class Command(BaseCommand):
    args = '<decade>'
    help = 'Loads county population estimates for the specified decade [90, 00, 10]'
    
    @transaction.commit_on_success  
    def handle(self, *args, **options):
    
        def load_years(years):
            for year in years:
                print 'loading %s' %  year
                pop = DataFrame(index=['state','county'])
                column = 'popestimate%s' % year
                
                #create a DataFrame for each series of population estimates:
                #total, male, and female
                query = ("PopulationEst%sRaw.objects.values('state','county')" 
                    ".filter(gender='0',ethnic_origin='0')"  
                    ".annotate(population=Sum(column))" % args[0])
                total_pop = eval(query) 
                total_pop = DataFrame.from_records(
                    total_pop,
                    index=['state','county'])
                total_pop.columns = ['total']
                if np.isnan(total_pop.sum()):
                    #No data yet for the current year, which means no data yet
                    #for future years in the decade, so stop right here
                    print 'No data for year %s. Stopping load.' % year
                    return 0
                query = ("PopulationEst%sRaw.objects.values('state','county')"
                    ".filter(gender='1',ethnic_origin='0')"
                    ".annotate(population=Sum(column))" % args[0])
                male_pop = eval(query)
                male_pop = DataFrame.from_records(
                    male_pop,
                    index=['state','county'])
                male_pop.columns = ['male']
                query = ("PopulationEst%sRaw.objects.values('state','county')"
                    ".filter(gender='2',ethnic_origin='0')"
                    ".annotate(population=Sum(column))" % args[0])
                female_pop = eval(query)
                female_pop = DataFrame.from_records(
                    female_pop,
                    index=['state','county'])
                female_pop.columns = ['female']
                
                #merge the total, male, and female DataFrames into final, master df
                pop = pd.merge(pop,
                    total_pop,
                    how='right',
                    left_index=True,
                    right_index=True)
                pop = pd.merge(pop,
                    male_pop,
                    how='right',
                    left_index=True,
                    right_index=True)
                pop = pd.merge(pop,
                    female_pop,
                    how='right',
                    left_index=True,
                    right_index=True)
                
                #calculate male and female percentages and merge those in, too
                male_percent = DataFrame(pop.apply(
                    lambda row: row['male']*1.0/row['total']*100,axis=1),
                    columns=['male_percent'])
                pop = pd.merge(pop,
                    male_percent,
                    left_index=True,
                    right_index=True)
                female_percent = DataFrame(pop.apply(
                    lambda row: row['female']*1.0/row['total']*100,axis=1),
                    columns=['female_percent'])
                pop = pd.merge(pop,
                    female_percent,
                    left_index=True,
                    right_index=True)
                
                #add DataFrame contents to database
                #DataFrame is indexed by state code and county code
                #i.e., p[0][0] = state code & p[0][1] = county code
                for p in pop.itertuples():
                    state_id = states['id'][p[0][0]]
                    county_id = counties['id'][p[0][0]][p[0][1]]
                    try:
                        record = PopulationGenderCounty.objects.get(
                            state = state_id,
                            county = county_id,
                            year = year)
                    except:
                        record = PopulationGenderCounty()
                        record.state_id = state_id
                        record.county_id = county_id
                        record.year = year
                    record.total = p[1]
                    record.male = p[2]
                    record.female = p[3]
                    record.male_percent = str(p[4])
                    record.female_percent = str(p[5])
                    record.save()
                    db.reset_queries()
                
        start_time = datetime.now()
        if len(args):
            states = DataFrame.from_records(State.objects.values(
                'id','state_ansi'),index=['state_ansi'])
            counties = DataFrame.from_records(County.objects.values(
                'id','state__state_ansi','county_ansi'),
                index=['state__state_ansi','county_ansi'])
            if args[0] == '10':
                if PopulationEst10Raw.objects.count():
                    years = ['2010','2011','2012','2013','2014','2015',
                        '2016','2017','2018','2019','2020']
                    load_years(years)
                else:
                    print ("No population data in the "
                        "2010-2020 table (PopulationEst10Raw), "
                        "so there's nothing to do.")
                    return 0
            elif args[0] == '00':
                if PopulationEst00Raw.objects.count():
                    years = ['2000','2001','2002','2003','2004','2005',
                        '2006','2007','2008','2009','2010']
                    load_years(years)
                else:
                    print ("No population data in the "
                        "2000-2010 table (PopulationEst00Raw), "
                        "so there's nothing to do.")
                    return 0
            elif args[0] == '90':
                print ("The 90s population estimates are no longer subject to"
                    "change, so we're not loading them anymore.")
            else:
                print 'Invalid decade: please specify 10, 00, or 90'
        else:
            print 'Please specify a decade: 10, 00, or 09'
        elapsed_time = datetime.now() - start_time
        print 'total elasped time = %s ' % elapsed_time