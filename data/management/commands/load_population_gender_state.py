from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.db import connection, transaction

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        cursor = connection.cursor()
        
        #load 2000-2010
        cursor.execute('''
        CREATE TEMPORARY TABLE normalized_years (
            state CHAR(2), 
            county CHAR(3), 
            gender CHAR(1), 
            ethnic_origin CHAR(1),
            race CHAR(1), 
            VALUE INT, 
            YEAR INT);
        ''')
        
        cursor.execute('''
        INSERT INTO normalized_years
            SELECT
              state
            , county
            , gender
            , ethnic_origin
            , race
            , popestimate2000 AS 'value'
            , 2000 AS 'year'
            FROM 
             data_populationest00raw
             UNION
             SELECT
              state
            , county
            , gender
            , ethnic_origin
            , race
            , popestimate2001 AS 'value'
            , 2001 AS 'year'                    
            FROM 
             data_populationest00raw
             UNION
             SELECT
              state
            , county
            , gender
            , ethnic_origin
            , race
            , popestimate2002 AS 'value'
            , 2002 AS 'year'
            FROM 
             data_populationest00raw
             UNION
             SELECT
              state
            , county
            , gender
            , ethnic_origin
            , race
            , popestimate2003 AS 'value'
            , 2003 AS 'year'
            FROM 
             data_populationest00raw
             UNION
             SELECT
              state
            , county
            , gender
            , ethnic_origin
            , race
            , popestimate2004 AS 'value'
            , 2004 AS 'year'
            FROM 
             data_populationest00raw
             UNION
             SELECT
              state
            , county
            , gender
            , ethnic_origin
            , race
            , popestimate2005 AS 'value'
            , 2005 AS 'year'
            FROM 
             data_populationest00raw
             UNION
             SELECT
              state
            , county
            , gender
            , ethnic_origin
            , race
            , popestimate2006 AS 'value'
            , 2006 AS 'year'
            FROM 
             data_populationest00raw
             UNION
             SELECT
              state
            , county
            , gender
            , ethnic_origin
            , race
            , popestimate2007 AS 'value'
            , 2007 AS 'year'
            FROM 
             data_populationest00raw
             UNION
             SELECT
              state
            , county
            , gender
            , ethnic_origin
            , race
            , popestimate2008 AS 'value'
            , 2008 AS 'year'
            FROM 
             data_populationest00raw
             UNION
             SELECT
              state
            , county
            , gender
            , ethnic_origin
            , race
            , popestimate2009 AS 'value'
            , 2009 AS 'year'
            FROM 
             data_populationest00raw
             UNION
             SELECT
              state
            , county
            , gender
            , ethnic_origin
            , race
            , popestimate2010 AS 'value'
            , 2010 AS 'year'
            FROM 
             data_populationest00raw
            ;
            ''')

        cursor.execute('''
            insert into data_populationgenderstate
            SELECT 
                NULL
            ,   YEAR
            ,   s.id
            ,   SUM(CASE WHEN gender = 0 THEN VALUE ELSE 0 END) AS 'total'
            ,   SUM(CASE WHEN gender = 2 THEN VALUE ELSE 0 END) AS 'female'
            ,   0
            ,   SUM(CASE WHEN gender = 1 THEN VALUE ELSE 0 END) AS 'male'
            ,   0
            ,   NOW()
            ,   NOW()
            FROM 
                normalized_years p
                JOIN data_state s
                ON p.state = s.state_ansi
            WHERE race = 0 AND ethnic_origin = 0 
            GROUP BY
                YEAR, s.id
               ;
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
              
        #calculate percentages
        cursor.execute('''
        update data_populationgenderstate
        set 
        female_percent = ROUND(female / total,4) * 100
        ,male_percent = ROUND(male / total,4) * 100
        ''')
        
        transaction.commit_unless_managed()