from django import db
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.db import connection, transaction

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
    
        cursor = connection.cursor()
        
        #load 2000-2009
        cursor.execute('''
        insert into data_populationracestate
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
        ,   sum(wa_male + wa_female) #white alone
        ,   0
        ,   sum(wac_male + wac_female - wa_male - wa_female) #white in combination
        ,   0
        ,   sum(hwa_male + hwa_female) #hispanic white alone
        ,   0
        ,   sum(hwac_male + hwac_female - hwa_male - hwa_female) #hispanic white in combination
        ,   0
        ,   sum(nhwa_male + nhwa_female) #non-hispanic white alone
        ,   0
        ,   sum(nhwac_male + nhwac_female - nhwa_male - nhwa_female) #non-hispanic white in combination
        ,   0
        ,   sum(ba_male + ba_female) #black alone
        ,   0
        ,   sum(bac_male + bac_female - ba_male - ba_female) #black in combination
        ,   0
        ,   sum(hba_male + hba_female) #hispanic black alone
        ,   0
        ,   sum(hbac_male + hbac_female - hba_male - hba_female ) #hispanic black in combination
        ,   0
        ,   sum(nhba_male + nhba_female) #non-hispanic black alone
        ,   0
        ,   sum(nhbac_male + nhbac_female - nhba_male - nhba_female) #non-hispanic black in combination
        ,   0
        ,   sum(ia_male + ia_female) #native alone
        ,   0
        ,   sum(iac_male + iac_female - ia_male - ia_female) #native in combination
        ,   0
        ,   sum(hia_male + hia_female) #hispanic native alone
        ,   0
        ,   sum(hiac_male + hiac_female - hia_male - hia_female) #hispanic native in combination
        ,   0
        ,   sum(nhia_male + nhia_female) #nonhispanic native alone
        ,   0
        ,   sum(nhiac_male + nhiac_female - nhia_male - nhia_female) #nonhispanic native in combination
        ,   0
        ,   sum(aa_male + aa_female) #asian alone
        ,   0
        ,   sum(aac_male + aac_female - aa_male - aa_female) #asian in combination
        ,   0
        ,   sum(haa_male + haa_female) #hispanic asian alone
        ,   0
        ,   sum(haac_male + haac_female - haa_male - haa_female) #hispanic asian in combination
        ,   0
        ,   sum(nhaa_male + nhaa_female) #non-hispanic asian alone
        ,   0
        ,   sum(nhaac_male + nhaac_female - nhaa_male - nhaa_female) #non-hispanic asian in combination
        ,   0
        ,   sum(na_male + na_female) #pacific islander alone
        ,   0
        ,   sum(nac_male + nac_female - na_male - na_female) #pacific islander in combination
        ,   0
        ,   sum(hna_male + hna_female) #hispanic pacific islander alone
        ,   0
        ,   sum(hnac_male + hnac_female - hna_male - hna_female) #hispanic pacific islander in combination
        ,   0
        ,   sum(nhna_male + nhna_female) #nonhispanic pacific islander alone
        ,   0
        ,   sum(nhnac_male + nhnac_female - nhna_male - nhna_female) #non-hispanic pacific islander in combination
        ,   0
        ,   NULL #asian/pacific islander alone (1990 census)
        ,   0
        ,   NULL #other (1980 census)
        ,   0
        ,   sum(tom_male + tom_female) #multiple race
        ,   0
        ,   sum(htom_male + htom_female) #multiple race hispanic
        ,   0
        ,   sum(nhtom_male + nhtom_female) #multiple race nonhispanic
        ,   0
        ,   sum(h_male + h_female) #hispanic
        ,   0
        ,   sum(nh_male + nh_female) #nonhispanic
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
        insert into data_populationracestate
        select 
            NULL
        ,	case
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
        ,	s.id
        ,	sum(population)
        ,	sum(case when race_gender in (1,2) then population else 0 end) #white alone
        , 	0
        ,	NULL #white in combination
        , 	0
        ,	NULL #hispanic white alone
        , 	0
        ,	NULL #hispanic white in combination
        , 	0
        ,	NULL #non-hispanic white alone
        , 	0
        ,	NULL #non-hispanic white in combination
        , 	0
        ,	sum(case when race_gender in (3,4) then population else 0 end) #black alone
        , 	0
        ,	NULL #black in combination
        , 	0
        ,	NULL #hispanic black alone
        , 	0
        ,	NULL #hispanic black in combination
        , 	0
        ,	NULL #non-hispanic black alone
        , 	0
        ,	NULL #non-hispanic black in combination
        , 	0
        ,	sum(case when race_gender in (5,6) then population else 0 end) #native alone
        , 	0
        ,	NULL #native in combination
        , 	0
        ,	NULL #hispanic native alone
        , 	0
        ,	NULL #hispanic native in combination
        , 	0
        ,	NULL #nonhispanic native alone
        , 	0
        ,	NULL #nonhispanic native in combination
        , 	0
        ,	NULL #asian alone
        , 	0
        ,	NULL #asian in combination
        , 	0
        ,	NULL #hispanic asian alone
        , 	0
        ,	NULL #hispanic asian in combination
        , 	0
        ,	NULL #non-hispanic asian alone
        , 	0
        ,	NULL #non-hispanic asian in combination
        , 	0
        ,	NULL #pacific islander alone
        , 	0
        ,	NULL #pacific islander in combination
        , 	0
        ,	NULL #hispanic pacific islander alone
        , 	0
        ,	NULL #hispanic pacific islander in combination
        , 	0
        ,	NULL #nonhispanic pacific islander alone
        , 	0
        ,	NULL #non-hispanic pacific islander in combination
        , 	0
        ,	sum(case when race_gender in (7,8) then population else 0 end) #asian/pacific islander alone (1990 census)
        , 	0
        ,	NULL #other (1980 census)
        , 	0
        ,	NULL #multiple race
        ,	0
        ,	NULL #multiple race hispanic
        ,	0
        ,	NULL #multiple race nonhispanic
        ,	0
        ,	NULL #hispanic
        ,	0
        ,	NULL #nonhispanic
        ,	0
        ,	now()
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
        insert into data_populationracestate
        select 
            NULL
        ,	year
        ,	s.id
        ,	sum(age_under_5 + age_5_9 + age_10_14 + age_15_19 + age_20_24 + age_25_29 
            + age_30_34 + age_35_39 + age_40_44 + age_45_49 + age_50_54 + age_55_59
            + age_60_64 + age_65_69 + age_70_74 + age_75_79 + age_80_84 + age_over_84) #total
        ,	sum(case when race_gender like '%%white%%' then age_under_5 + age_5_9 + age_10_14 + age_15_19 + age_20_24 + age_25_29 
            + age_30_34 + age_35_39 + age_40_44 + age_45_49 + age_50_54 + age_55_59
            + age_60_64 + age_65_69 + age_70_74 + age_75_79 + age_80_84 + age_over_84 else 0 end) #white alone
        , 	0
        ,	NULL #white in combination
        , 	0
        ,	NULL #hispanic white alone
        , 	0
        ,	NULL #hispanic white in combination
        , 	0
        ,	NULL #non-hispanic white alone
        , 	0
        ,	NULL #non-hispanic white in combination
        , 	0
        ,	sum(case when race_gender like '%%black%%' then age_under_5 + age_5_9 + age_10_14 + age_15_19 + age_20_24 + age_25_29 
            + age_30_34 + age_35_39 + age_40_44 + age_45_49 + age_50_54 + age_55_59
            + age_60_64 + age_65_69 + age_70_74 + age_75_79 + age_80_84 + age_over_84 else 0 end) #black alone
        , 	0
        ,	NULL #black in combination
        , 	0
        ,	NULL #hispanic black alone
        , 	0
        ,	NULL #hispanic black in combination
        , 	0
        ,	NULL #non-hispanic black alone
        , 	0
        ,	NULL #non-hispanic black in combination
        , 	0
        ,	NULL #native alone
        , 	0
        ,	NULL #native in combination
        , 	0
        ,	NULL #hispanic native alone
        , 	0
        ,	NULL #hispanic native in combination
        , 	0
        ,	NULL #nonhispanic native alone
        , 	0
        ,	NULL #nonhispanic native in combination
        , 	0
        ,	NULL #asian alone
        , 	0
        ,	NULL #asian in combination
        , 	0
        ,	NULL #hispanic asian alone
        , 	0
        ,	NULL #hispanic asian in combination
        , 	0
        ,	NULL #non-hispanic asian alone
        , 	0
        ,	NULL #non-hispanic asian in combination
        , 	0
        ,	NULL #pacific islander alone
        , 	0
        ,	NULL #pacific islander in combination
        , 	0
        ,	NULL #hispanic pacific islander alone
        , 	0
        ,	NULL #hispanic pacific islander in combination
        , 	0
        ,	NULL #nonhispanic pacific islander alone
        , 	0
        ,	NULL #non-hispanic pacific islander in combination
        , 	0
        ,	NULL #asian/pacific islander alone (1990 census)
        , 	0
        ,	sum(case when race_gender like '%%other%%' then age_under_5 + age_5_9 + age_10_14 + age_15_19 + age_20_24 + age_25_29 
            + age_30_34 + age_35_39 + age_40_44 + age_45_49 + age_50_54 + age_55_59
            + age_60_64 + age_65_69 + age_70_74 + age_75_79 + age_80_84 + age_over_84 else 0 end)  #other (1980 census)
        , 	0
        ,	NULL #multiple race
        ,	0
        ,	NULL #multiple race hispanic
        ,	0
        ,	NULL #multiple race nonhispanic
        ,	0
        ,	NULL #hispanic
        ,	0
        ,	NULL #nonhispanic
        ,	0
        ,	now()
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
        update data_populationracestate
        set 
            white_alone_percent = ROUND(white_alone / total,4) * 100
        ,	white_other_percent = ROUND(white_other / total,4) * 100
        ,	white_alone_hispanic_percent = ROUND(white_alone_hispanic / total,4) * 100
        ,	white_other_hispanic_percent = ROUND(white_other_hispanic / total,4) * 100
        ,	white_alone_nonhispanic_percent = ROUND(white_alone_nonhispanic / total,4) * 100
        ,	white_other_nonhispanic_percent = ROUND(white_other_nonhispanic / total,4) * 100
        ,	black_alone_percent = ROUND(black_alone / total,4) * 100
        ,	black_other_percent = ROUND(black_other / total,4) * 100
        ,	black_alone_hispanic_percent = ROUND(black_alone_hispanic / total,4) * 100
        ,	black_other_hispanic_percent = ROUND(black_other_hispanic / total,4) * 100
        ,	black_alone_nonhispanic_percent = ROUND(black_alone_nonhispanic / total,4) * 100
        ,	black_other_nonhispanic_percent = ROUND(black_other_nonhispanic / total,4) * 100
        ,	native_alone_percent = ROUND(native_alone / total,4) * 100
        ,	native_other_percent = ROUND(native_other / total,4) * 100
        ,	native_alone_hispanic_percent = ROUND(native_alone_hispanic / total,4) * 100
        ,	native_other_hispanic_percent = ROUND(native_other_hispanic / total,4) * 100
        ,	native_alone_nonhispanic_percent = ROUND(native_alone_nonhispanic / total,4) * 100
        ,	native_other_nonhispanic_percent = ROUND(native_other_nonhispanic / total,4) * 100
        ,	asian_alone_percent = ROUND(asian_alone / total,4) * 100
        ,	asian_other_percent = ROUND(asian_other / total,4) * 100
        ,	asian_alone_hispanic_percent = ROUND(asian_alone_hispanic / total,4) * 100
        ,	asian_other_hispanic_percent = ROUND(asian_other_hispanic / total,4) * 100
        ,	asian_alone_nonhispanic_percent = ROUND(asian_alone_nonhispanic / total,4) * 100
        ,	asian_other_nonhispanic_percent = ROUND(asian_other_nonhispanic / total,4) * 100
        ,	pacific_islander_alone_percent = ROUND(pacific_islander_alone / total,4) * 100
        ,	pacific_islander_other_percent = ROUND(pacific_islander_other / total,4) * 100
        ,	pacific_islander_alone_hispanic_percent = ROUND(pacific_islander_alone_hispanic / total,4) * 100
        ,	pacific_islander_other_hispanic_percent = ROUND(pacific_islander_other_hispanic / total,4) * 100
        ,	pacific_islander_alone_nonhispanic_percent = ROUND(pacific_islander_alone_nonhispanic / total,4) * 100
        ,	pacific_islander_other_nonhispanic_percent = ROUND(pacific_islander_other_nonhispanic / total,4) * 100
        ,	asian_pacific_islander_alone_percent = ROUND(asian_pacific_islander_alone / total,4) * 100
        ,	other_percent = ROUND(other / total,4) * 100
        ,	multiple_race_percent = ROUND(multiple_race / total,4) * 100
        ,	multiple_race_hispanic_percent = ROUND(multiple_race_hispanic/total,4) * 100
        ,	multiple_race_nonhispanic_percent = ROUND(multiple_race_nonhispanic/total,4) * 100
        ,	hispanic_percent = ROUND(hispanic/total,4) * 100
        ,	nonhispanic_percent = ROUND(nonhispanic/total,4) * 100
        ''')
        
        transaction.commit_unless_managed()