from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.exceptions import MultipleObjectsReturned
from data.models import LaborUnderutilizationStateRaw
from BeautifulSoup import BeautifulSoup, SoupStrainer
import urllib2
import re
import csv

# National Priorities Project Data Repository
# import_labor_underutilization

# Imports alternative measures of labor underutilization from the Bureau of Labor Statistics
# source info: yearly files on http://www.bls.gov/lau/stalt.htm (accurate as of 5/1/12)
# npp csv: 
# destination model:  LaborUnderutilizationStateRaw

# HOWTO:
# 1) Make sure base for URLs below is still accurate 
# 2) Adjust YEARS as necessary
# 3) Run as Django management command from your prjoect path "python manage.py import_labor_underutilization"

# Safe to re-run: YES..will re-load data as necessary

URL = 'http://www.bls.gov/lau/'
YEARS = [2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
SAVE_FILE = '%s/bls.gov/' % (settings.LOCAL_DATA_ROOT)

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        def clean_num(value):
            if value.strip()=='':
                value=None
            else:
                try:
                    value=float(value.replace(',', '').replace(' ', ''))
                except:
                    value=None
            return value

        for year in YEARS:
            insert_count = 0
            update_count = 0
            if year < 2009:
                url = '%sstalt%s.htm' % (URL,str(year)[-2:])
            else:
                url = '%sstalt%s%s.htm' % (URL,str(year)[-2:],'q4')
        
            try:
                page = urllib2.urlopen(url)
                print '%s - scraping labor underutilization: %s' % (year,url)
            except:
                print 'No labor underutilization page for %s. full URL is %s' % (year,url)
                continue
            
            #underemployment table should have an id of 'alternmeas' + the year,
            #so just parse that portion of the page
            strainerTag = SoupStrainer('table', id=re.compile('alt'))
            table = BeautifulSoup(page, parseOnlyThese=strainerTag)
            
            if len(table) < 1:
                print 'no underemployment table found on page %s' % url
                continue
            elif len(table) > 1:
                print 'duplicate tables found on page %s' % url
                continue
                
            #get a list of data headers
            headers = table.find('thead').findAll(text=re.compile("U-"))
            headers = [x.lower().replace('-','') for x in headers]    
            
            #scrape data & store in dictionary form
            data = {}
            rows = table.find('tbody').findAll('tr')
            for row in rows:
                state = row.th.text
                if data.has_key(state):
                    print 'error: duplicate row found for state %s' % state
                    continue
                else:
                    data[state] = {}
                cols = row.findAll('td')
                for i, col in enumerate(cols):
                    data[state][headers[i]] = col.text

                #insert/update 
                try:
                    record = LaborUnderutilizationStateRaw.objects.get(year=year,state=state)
                    update_count = update_count + 1
                except:
                    record = LaborUnderutilizationStateRaw(year=year,state=state)
                    insert_count = insert_count + 1
                record.u1 = clean_num(data[state]['u1'])
                record.u2 = clean_num(data[state]['u2'])
                record.u3 = clean_num(data[state]['u3'])
                record.u4 = clean_num(data[state]['u4'])
                record.u5 = clean_num(data[state]['u5'])
                record.u6 = clean_num(data[state]['u6'])
                record.save()
                db.reset_queries()
                
            print '%s - %s rows scraped' % (year,len(data))
            print '%s - %s records inserted and %s records updated' % (year,insert_count,update_count)
            
            #TO DO: write to a csv file and save for posterity
            #filename = '%slabor_underutilization_%s.csv' % (SAVE_FILE,year)
            
            