create view kill_data as 
	(select file,round,att_team,att_side,att_id,COUNT(*)
	from(select distinct * 
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,att_team,att_side,att_id
	)
;
--Kills per person per round per match--
select * from kill_data ;
--Kills per side per round per match--
select file,round,att_side,SUM(count) as count from kill_data group by file,round,att_side;
--Kills per team per round per match--
select file,round,att_team,SUM(count) as count from kill_data group by file,round,att_team;
--Kills per team per match--
select file,att_team,SUM(count) as count from kill_data group by file,att_team;
--Kills per person per match--
select file,att_team,att_side,att_id,SUM(count) as count from kill_data group by file,att_team,att_side,att_id;
--Kills per side per match--
select file,att_side,SUM(count) as count from kill_data group by file,att_side;
--Highest kills per person per round per match--
select file,round,att_team,att_side,att_id,count
from(select  file,round,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count desc,att_id) as rank
	from kill_data
	) as a4
where rank <=1
;
--Highest kills per person per match--
with kill_data2 as (select file,att_team,att_side,att_id,SUM(count) as count from kill_data group by file,att_team,att_side,att_id)
select file,att_team,att_side,att_id,count
from(select  file,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,att_id) as rank
	from kill_data2
	) as a4
where rank <=1
;

--Lowest kills per person per round per match--
select file,round,att_team,att_side,att_id,count
from(select  file,round,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count,att_id) as rank
	from kill_data
	) as a4
where rank <=1
;
--Lowest kills per person per match--
with kill_data2 as (select file,att_team,att_side,att_id,SUM(count) as count from kill_data group by file,att_team,att_side,att_id)
select file,att_team,att_side,att_id,count
from(select  file,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file ORDER BY file,count,att_id) as rank
	from kill_data2
	) as a4
where rank <=1
;


create view assist_data as 
	(select file,round,att_team,att_side,att_id,COUNT(*)
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		except
		select *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,att_team,att_side,att_id
	order by file,round,att_team,att_side,att_id
	)
;

--Assists per person per round per match--
select * from assist_data;
--Assists per side per round per match--
select file,round,att_side,SUM(count) as count from assist_data group by file,round,att_side;
--Assists per team per round per match--
select file,round,att_team,SUM(count) as count from assist_data group by file,round,att_team;
--Assists per person per match--
select file,att_team,att_side,att_id,SUM(count) as count from assist_data group by file,att_team,att_side,att_id;
--Assists per team per match--
select file,att_team,SUM(count) as count from assist_data group by file,att_team;
--Assists per side per match--
select file,att_side,SUM(count) as count from assist_data group by file,att_side;
--Highest assists per person round per match--
select file,round,att_team,att_side,att_id,count
from(select  file,round,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count desc,att_id) as rank
	from assist_data
	) as a4
where rank <=1
--Highest assists per person per match--
with assist_data2 as (select file,att_team,att_side,att_id,SUM(count) as count from assist_data group by file,att_team,att_side,att_id)
select file,att_team,att_side,att_id,count
from(select  file,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,att_id) as rank
	from assist_data2
	) as a4
where rank <=1
;
--Lowest assists per person round per match--
select file,round,att_team,att_side,att_id,count
from(select  file,round,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count ,att_id) as rank
	from assist_data
	) as a4
where rank <=1
--Lowest assists per person per match--
with assist_data2 as (select file,att_team,att_side,att_id,SUM(count) as count from assist_data group by file,att_team,att_side,att_id)
select file,att_team,att_side,att_id,count
from(select  file,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file ORDER BY file,count ,att_id) as rank
	from assist_data2
	) as a4
where rank <=1
;



create view death_data as
	(select file, round, vic_team, vic_side, vic_id, COUNT(*)
	from(
		select distinct *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file, round, vic_team, vic_side, vic_id
	)
;

--Deaths per person per round per match--
select * from death_data;
--Deaths per side per round per match--
select file,round,vic_side,SUM(count) as count from death_data group by file,round,vic_side;
--Deaths per team per round per match--
select file,round,vic_team,SUM(count) as count from death_data group by file,round,vic_team;
--Deaths per person per match--
select file,vic_team,vic_side,vic_id,SUM(count) as count from death_data group by file,vic_team,vic_side,vic_id;
--Deaths per team per match--
select file,vic_team,SUM(count) as count from death_data group by file,vic_team;
--Deaths per side per match--
select file,vic_side,SUM(count) as count from death_data group by file,vic_side;
--Highest deaths per person per round per match--
select file, vic_team, vic_side, vic_id,count
from(select  file,vic_team, vic_side, vic_id,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,vic_id) as rank
	from death_data
	) as a4
where rank <=1
;
--Highest deaths per person per match--
with death_data2 as (select file,vic_team,vic_side,vic_id,SUM(count) as count from death_data group by file,vic_team,vic_side,vic_id)
select file, vic_team, vic_side, vic_id,count
from(select  file,vic_team, vic_side, vic_id,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,vic_id) as rank
	from death_data2
	) as a4
where rank <=1
;
--Lowest deaths per person per round per match--
select file, vic_team, vic_side, vic_id,count
from(select  file,vic_team, vic_side, vic_id,count,rank() OVER (PARTITION BY file ORDER BY file,count ,vic_id) as rank
	from death_data
	) as a4
where rank <=1
;
--Lowest deaths per person per match--
with death_data2 as (select file,vic_team,vic_side,vic_id,SUM(count) as count from death_data group by file,vic_team,vic_side,vic_id)
select file, vic_team, vic_side, vic_id,count
from(select  file,vic_team, vic_side, vic_id,count,rank() OVER (PARTITION BY file ORDER BY file,count,vic_id) as rank
	from death_data2
	) as a4
where rank <=1
;



--Kill/Death ratio per person per match--
create view kdratio as
	(with kill_data2 as (select file,att_team,att_side,att_id,SUM(count) as kills from kill_data group by file,att_team,att_side,att_id),
	 death_data2 as (select file,vic_team,vic_side,vic_id,SUM(count) as deaths from death_data group by file,vic_team,vic_side,vic_id)

	select file,att_team,att_side,att_id,ROUND( cast(kills as decimal)/deaths,2) as ratio
	from kill_data2 natural join death_data2
	where att_team=vic_team and att_side =vic_side and att_id = vic_id
	)
;
--Highest Kill/Death ratio per person per match--
select file,att_team,att_side,att_id,ratio
from(select  file,att_team,att_side,att_id,ratio,rank() OVER (PARTITION BY file ORDER BY file,ratio desc,att_id) as rank
	from kdratio
	) as a4
where rank <=1
;
--Lowest Kill/Death ratio per person per match--
select file,att_team,att_side,att_id,ratio
from(select  file,att_team,att_side,att_id,ratio,rank() OVER (PARTITION BY file ORDER BY file,ratio ,att_id) as rank
	from kdratio
	) as a4
where rank <=1
;



--MOST VALUABLE PLAYER per match--
create view mvp as 
	(with kill_data2 as (select file,att_team,att_side,att_id,SUM(count) as kills from kill_data group by file,att_team,att_side,att_id),
	assist_data2 as (select file,att_team,att_side,att_id,SUM(count) as assists from assist_data group by file,att_team,att_side,att_id),
	value_data as (select file,att_team,att_side,att_id,(kills+assists) as value from kill_data2 natural join assist_data2)
	select file,att_team,att_side,att_id,value
	from(select  file,att_team,att_side,att_id,value,rank() OVER (PARTITION BY file ORDER BY file,value desc,att_id) as rank
		from value_data
		) as a4
	where rank <=1
	)
;

--PER PLAYER STATISTICS--
with kill_data2 as (select att_id,SUM(count) as kills from kill_data group by att_id),
assist_data2 as (select att_id,SUM(count) as assists from assist_data group by att_id),
death_data2 as (select vic_id as att_id,SUM(count) as deaths from death_data group by vic_id),
mvp2 as (select att_id,COUNT(*) as num_mvp from mvp group by att_id) 

select att_id,kills,assists,deaths,ROUND( cast(kills as decimal)/deaths,2) as ratio,num_mvp from kill_data2 natural join assist_data2 natural join death_data2 natural join mvp2
;

drop view mvp;
drop view kdratio;
drop view kill_data;
drop view death_data;
drop view assist_data;

