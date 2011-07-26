from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.db import connection, transaction

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        cursor = connection.cursor()
        
        #load 2000-2009
        cursor.execute('''
        insert into data_populationagestate
        select 
            NULL
        ,   case
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
        ,   sum(case agegrp when 1 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 2 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 3 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 4 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 5 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 6 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 7 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 8 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 9 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 10 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 11 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 12 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 13 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 14 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 15 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 16 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 17 then tot_pop else 0 end)
        ,   0
        ,   sum(case agegrp when 18 then tot_pop else 0 end)
        ,   0
        ,  sum(case when agegrp > 13 then tot_pop else 0 end)
        ,   0
        ,   sum(case when agegrp between 1 and 4 then tot_pop else 0 end)
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
        insert into data_populationagestate
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
        ,   sum(case when agegrp between 0 and 1 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 2 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 3 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 4 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 5 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 6 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 7 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 8 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 9 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 10 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 11 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 12 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 13 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 14 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 15 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 16 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 17 then population else 0 end)
        ,   0
        ,   sum(case agegrp when 18 then population else 0 end)
        ,   0
        ,  sum(case when agegrp > 13 then population else 0 end) 
        ,   0
        ,   sum(case when agegrp between 0 and 4 then population else 0 end)
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
        insert into data_populationagestate
        select 
            NULL
        ,   year
        ,   s.id
        ,   sum(age_under_5 + age_5_9 + age_10_14 + age_15_19 + age_20_24 + age_25_29 
            + age_30_34 + age_35_39 + age_40_44 + age_45_49 + age_50_54 + age_55_59
            + age_60_64 + age_65_69 + age_70_74 + age_75_79 + age_80_84 + age_over_84)
        ,   sum(age_under_5)
        ,   0
        ,   sum(age_5_9)
        ,   0
        ,   sum(age_10_14)
        ,   0
        ,   sum(age_15_19)
        ,   0
        ,sum(age_20_24)
        ,   0
        ,   sum(age_25_29)
        ,   0
        ,   sum(age_30_34)
        ,   0
        ,   sum(age_35_39)
        ,   0
        ,   sum(age_40_44 )
        ,   0
        ,   sum(age_45_49)
        ,   0
        ,   sum(age_50_54)
        ,   0
        ,   sum(age_55_59)
        ,   0
        ,   sum(age_60_64) 
        ,   0
        ,   sum(age_65_69)
        ,   0
        ,   sum(age_70_74)
        ,   0
        ,   sum(age_75_79)
        ,   0
        ,   sum(age_80_84)
        ,   0
        ,   sum(age_over_84)
        ,   0
        ,   sum(age_65_69 + age_70_74 + age_75_79 + age_80_84 + age_over_84)
        ,   0
        ,   sum(age_under_5 + age_5_9 + age_10_14 + age_15_19)
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
        update data_populationagestate
        set 
            age_0_4_percent = ROUND(age_0_4 / total,4)
        ,   age_5_9_percent = ROUND(age_5_9 / total,4)
        ,   age_10_14_percent = ROUND(age_10_14 / total,4)
        ,   age_15_19_percent = ROUND(age_15_19 / total,4)
        ,   age_20_24_percent = ROUND(age_20_24 / total,4)
        ,   age_25_29_percent = ROUND(age_25_29 / total,4)
        ,   age_30_34_percent = ROUND(age_30_34 / total,4)
        ,   age_35_39_percent = ROUND(age_35_39 / total,4)
        ,   age_40_44_percent = ROUND(age_40_44 / total,4)
        ,   age_45_49_percent = ROUND(age_45_49 / total,4)
        ,   age_50_54_percent = ROUND(age_50_54 / total,4)
        ,   age_55_59_percent = ROUND(age_55_59 / total,4)
        ,   age_60_64_percent = ROUND(age_60_64 / total,4)
        ,   age_65_69_percent = ROUND(age_65_69 / total,4)
        ,   age_70_74_percent = ROUND(age_70_74 / total,4)
        ,   age_75_79_percent = ROUND(age_75_79 / total,4)
        ,   age_80_84_percent = ROUND(age_80_84 / total,4)
        ,   age_85_over_percent = ROUND(age_85_over / total,4)
        ,   age_65_over_percent = ROUND(age_65_over / total,4)
        ,   age_0_19_percent = ROUND(age_0_19 / total,4)
        ''')
        
        transaction.commit_unless_managed()