from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.db import connection, transaction

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        cursor = connection.cursor()
        
        #load 2000-2009
        cursor.execute('''
        insert into data_populationgenderstate
        select 
            NULL
            ,case
                when p.year = 3 then 2000
                when p.year = 4 then 2001
                when p.year = 5 then 2002
                when p.year = 6 then 2003
                when p.year = 7 then 2004
                when p.year = 8 then 2005
                when p.year = 9 then 2006
                when p.year = 10 then 2007
                when p.year = 11 then 2008
                when p.year = 12 then 2009
            end 
        ,   s.id
        ,   sum(tot_pop)
        ,   sum(tot_female)
        ,   0
        ,   sum(tot_male)
        ,   0
        ,   now()
        ,   now()
        from 
            data_populationest00raw p
            join data_state s
            on p.state = s.state_ansi
        where 
            agegrp <> 0
            and year between 3 and 12
        group by
            p.year, s.id
        ''')
        
        #load 1990-1999
        cursor.execute('''
        insert into data_populationgenderstate
        select 
            NULL
        ,   case
                when p.year = 90 then 1990
                when p.year = 91 then 1991
                when p.year = 92 then 1992
                when p.year = 93 then 1993
                when p.year = 94 then 1994
                when p.year = 95 then 1995
                when p.year = 96 then 1996
                when p.year = 97 then 1997
                when p.year = 98 then 1998
                when p.year = 99 then 1999
            end 
        ,   s.id
        ,   sum(population)
        ,   sum(case when race_gender in (2,4,6,8) then population else 0 end)
        ,   0
        ,   sum(case when race_gender in (1,3,5,7) then population else 0 end)
        ,   0
        ,   now()
        ,   now()
        from 
            data_populationest90raw p
            join data_state s
            on p.state = s.state_ansi
        group by
            p.year, s.id
        ''')
        
        #load 1980-1989
        cursor.execute('''
        insert into data_populationgenderstate
        select 
            NULL
        ,   year
        ,   s.id
        ,   sum(age_under_5 + age_5_9 + age_10_14 + age_15_19 + age_20_24 + age_25_29 
            + age_30_34 + age_35_39 + age_40_44 + age_45_49 + age_50_54 + age_55_59
            + age_60_64 + age_65_69 + age_70_74 + age_75_79 + age_80_84 + age_over_84) 
        ,   sum(case when race_gender like "%% female%%" then age_under_5 + age_5_9 + age_10_14 + age_15_19 + age_20_24 + age_25_29 
            + age_30_34 + age_35_39 + age_40_44 + age_45_49 + age_50_54 + age_55_59
            + age_60_64 + age_65_69 + age_70_74 + age_75_79 + age_80_84 + age_over_84 else 0 end) 
        ,   0
        ,   sum(case when race_gender like "%% male%%" then age_under_5 + age_5_9 + age_10_14 + age_15_19 + age_20_24 + age_25_29 
            + age_30_34 + age_35_39 + age_40_44 + age_45_49 + age_50_54 + age_55_59
            + age_60_64 + age_65_69 + age_70_74 + age_75_79 + age_80_84 + age_over_84 else 0 end) 
        ,   0
        ,   now()
        ,   now()
        from 
            data_populationest80raw p
            join data_state s
            on left(p.state_county,2) = s.state_ansi
        group by
            p.year, s.id
            ''')
              
        #calculate percentages
        cursor.execute('''
        update data_populationgenderstate
        set 
        female_percent = ROUND(female / total,4) * 100
        ,male_percent = ROUND(male / total,4) * 100
        ''')
        
        transaction.commit_unless_managed()