--שאילתא 1
SELECT count(*),air_force,target_city
FROM mission
WHERE EXTRACT(YEAR FROM mission_date) = 1943
GROUP BY target_city,air_force
order by count(air_force) desc --limit 1;

--שאילתא 1 ניתוח בלי אינדקס 57 מילי שניות בערך
explain analyze SELECT count(*),air_force,target_city
FROM mission
WHERE EXTRACT(YEAR FROM mission_date) = 1943
GROUP BY target_city,air_force
order by count(air_force) desc;

--הוספת אינדקס על השנה
create index idx_mission_year on mission(EXTRACT(YEAR FROM mission_date));

-- שאילתא 1 ניתוח עם אינדקס 15 מילי שניות לערך
explain analyze SELECT count(*),air_force,target_city
FROM mission
WHERE EXTRACT(YEAR FROM mission_date) = 1943
GROUP BY target_city,air_force
order by count(air_force) desc;

--מחיקת אינדקס
drop index idx_mission_year

--שאילתא 2
select bomb_damage_assessment,count(target_country) 
from mission
where bomb_damage_assessment is not null 
and airborne_aircraft > 5
group by target_country ,bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1

--שאילתא 2 ניתוח בלי אינדקס 60 מילי שניות בערך
explain analyze select bomb_damage_assessment,count(target_country) 
from mission
where bomb_damage_assessment is not null 
and airborne_aircraft > 5
group by target_country ,bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1

--הוספת אינדקס
create index idx_airborne_aircraft on mission(airborne_aircraft)

--שאילתא 2 ניתוח עם אינדקס 11 מילי שניות לערך
explain analyze select bomb_damage_assessment,count(target_country) 
from mission
where bomb_damage_assessment is not null 
and airborne_aircraft > 5
group by target_country ,bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1