--Kills per person per round per match--
select file,round,att_team,att_side,att_id,COUNT(*)
from(select distinct * 
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file,round,att_team,att_side,att_id
;

--Kills per side per round per match--
select file,round,att_side,COUNT(*)
from(select distinct * 
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file,round,att_side
;

--Kills per team per round per match--
select file,round,att_team,COUNT(*)
from(select distinct * 
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file,round,att_team
;
--Kills per team per match--
select file,att_team,COUNT(*)
from(select distinct * 
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file,att_team
;
y file,att_team
;
--Kills per person per match--
select file,att_team,att_side,att_id,COUNT(*)
from(select distinct * 
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file,att_team,att_side,att_id
;
--Kills per side per match--
select file,att_side,COUNT(*)
from(select distinct * 
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file,att_side
;

--Assists per person per round per match--
select file,round,att_team,att_side,att_id,COUNT(*)
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
;
--Assists per side per round per match--
select file,round,att_side,COUNT(*)
from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
	from esea_dmg
	except
	select *
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file,round,att_side
order by file,round,att_side
;
--Assists per team per round per match--
select file,round,att_team,COUNT(*)
from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
	from esea_dmg
	except
	select *
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file,round,att_team
order by file,round,att_team
;
--Assists per person per match--
select file,att_team,att_side,att_id,COUNT(*)
from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
	from esea_dmg
	except
	select *
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file,att_team,att_side,att_id
order by file,att_team,att_side,att_id
;
--Assists per side per match--
select file,att_side,COUNT(*)
from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
	from esea_dmg
	except
	select *
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file,att_side
order by file,att_side
;
--Assists per team per match--
select file,att_team,COUNT(*)
from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
	from esea_dmg
	except
	select *
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file,att_team
order by file,att_team
;
--Deaths per person per round per match--
select file, round, vic_team, vic_side, vic_id, COUNT(*)
from(
	select distinct *
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file, round, vic_team, vic_side, vic_id
;
--Deaths per side per round per match--
select file, round,vic_side,COUNT(*)
from(
	select distinct *
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file, round, vic_side
;
--Deaths per team per round per match--
select file, round, vic_team,COUNT(*)
from(
	select distinct *
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file, round, vic_team
;
--Deaths per person per match--
select file,  vic_team, vic_side, vic_id, COUNT(*)
from(
	select distinct *
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file,  vic_team, vic_side, vic_id
;
--Deaths per side per match--
select file, vic_side,COUNT(*)
from(
	select distinct *
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file, vic_side
;
--Deaths per team per match--
select file, vic_team,COUNT(*)
from(
	select distinct *
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
	) as a3
group by file, vic_team
;
--Highest kills per person per round per match--
with kill_data as 
	(select file,round,att_team,att_side,att_id,COUNT(*)
	from(select distinct * 
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,att_team,att_side,att_id
	)

select file,round,att_team,att_side,att_id,count
from(select  file,round,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count desc,att_id) as rank
	from kill_data
	) as a4
where rank <=1
;

--Highest kills per person per match--
with kill_data as 
	(select file,att_team,att_side,att_id,COUNT(*)
	from(select distinct * 
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,att_team,att_side,att_id
	)

select file,att_team,att_side,att_id,count
from(select  file,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,att_id) as rank
	from kill_data
	) as a4
where rank <=1
;
--Highest kills per team per round per match--
with kill_data as 
	(select file,round,att_team,COUNT(*)
	from(select distinct * 
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,att_team
	)

select file,round,att_team,count
from(select  file,round,att_team,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count desc,att_team) as rank
	from kill_data
	) as a4
where rank <=1
;

--Highest kills per team per match--
with kill_data as 
	(select file,att_team,COUNT(*)
	from(select distinct * 
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,att_team
	)

select file,att_team,count
from(select  file,att_team,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,att_team) as rank
	from kill_data
	) as a4
where rank <=1
;

--Highest kills per side per round per match--
with kill_data as 
	(select file,round,att_side,COUNT(*)
	from(select distinct * 
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,att_side
	)

select file,round,att_side,count
from(select  file,round,att_side,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count desc,att_side) as rank
	from kill_data
	) as a4
where rank <=1
;

--Highest kills per side per match--
with kill_data as 
	(select file,att_side,COUNT(*)
	from(select distinct * 
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,att_side
	)

select file,att_side,count
from(select  file,att_side,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,att_side) as rank
	from kill_data
	) as a4
where rank <=1
;
--Highest assists per person per round per match--
with assist_data as
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
	

select file,round,att_team,att_side,att_id,count
from(select  file,round,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count desc,att_id) as rank
	from assist_data
	) as a4
where rank <=1
;
--Highest assists per person per match--
with assist_data as
	(select file,att_team,att_side,att_id,COUNT(*)
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		except
		select *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,att_team,att_side,att_id
	order by file,att_team,att_side,att_id
	)
	

select file,att_team,att_side,att_id,count
from(select  file,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,att_id) as rank
	from assist_data
	) as a4
where rank <=1
;
--Highest assists per side per round per match--
with assist_data as
	(select file,round,att_side,COUNT(*)
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		except
		select *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,att_side
	order by file,round,att_side
	)
	

select file,round,att_side,count
from(select  file,round,att_side,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count desc,att_side) as rank
	from assist_data
	) as a4
where rank <=1
;
--Highest assists per per side per match--
with assist_data as
	(select file,att_side,COUNT(*)
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		except
		select *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,att_side
	order by file,att_side
	)
	

select file,att_side,count
from(select  file,att_side,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,att_side) as rank
	from assist_data
	) as a4
where rank <=1
;

--Highest assists per team per round per match--
with assist_data as
	(select file,round,att_team,COUNT(*)
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		except
		select *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,att_team
	order by file,round,att_team
	)
	

select file,round,att_team,count
from(select  file,round,att_team,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count desc,att_team) as rank
	from assist_data
	) as a4
where rank <=1
;
--Highest assists per team per match--
with assist_data as
	(select file,att_team,COUNT(*)
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		except
		select *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,att_team
	order by file,att_team
	)
	

select file,att_team,count
from(select  file,att_team,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,att_team) as rank
	from assist_data
	) as a4
where rank <=1
;

--Highest deaths per person per match--
with death_data as
	(select file,  vic_team, vic_side, vic_id, COUNT(*)
	from(
		select distinct *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,  vic_team, vic_side, vic_id
	)

select file, vic_team, vic_side, vic_id,count
from(select  file,vic_team, vic_side, vic_id,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,vic_id) as rank
	from death_data
	) as a4
where rank <=1
;

--Highest deaths per team per round per match--
with death_data as
	(select file,round,vic_team, COUNT(*)
	from(
		select distinct *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,vic_team
	)

select file,round, vic_team,count
from(select  file,round,vic_team,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count desc,vic_team) as rank
	from death_data
	) as a4
where rank <=1
;
--Highest deaths per team per match--
with death_data as
	(select file,  vic_team, COUNT(*)
	from(
		select distinct *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file, vic_team
	)

select file, vic_team,count
from(select  file,vic_team,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,vic_team) as rank
	from death_data
	) as a4
where rank <=1
;
--Highest deaths per side per round per match--
with death_data as
	(select file,round,vic_side, COUNT(*)
	from(
		select distinct *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,vic_side
	)

select file,round, vic_side,count
from(select  file,round,vic_side,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count desc,vic_side) as rank
	from death_data
	) as a4
where rank <=1
;
--Highest deaths per side per match--
with death_data as
	(select file,  vic_side, COUNT(*)
	from(
		select distinct *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file, vic_side
	)

select file, vic_side,count
from(select  file,vic_side,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,vic_side) as rank
	from death_data
	) as a4
where rank <=1
;
--Lowest kills per person per round per match--
with kill_data as 
	(select file,round,att_team,att_side,att_id,COUNT(*)
	from(select distinct * 
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,att_team,att_side,att_id
	)

select file,round,att_team,att_side,att_id,count
from(select  file,round,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count,att_id) as rank
	from kill_data
	) as a4
where rank <=1
;
--Lowest kills per person per match--
with kill_data as 
	(select file,att_team,att_side,att_id,COUNT(*)
	from(select distinct * 
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,att_team,att_side,att_id
	)

select file,att_team,att_side,att_id,count
from(select  file,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file ORDER BY file,count,att_id) as rank
	from kill_data
	) as a4
where rank <=1
;
--Lowest kills per side per round per match--
with kill_data as 
	(select file,round,att_side,COUNT(*)
	from(select distinct * 
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,att_side
	)

select file,round,att_side,count
from(select  file,round,att_side,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count,att_side) as rank
	from kill_data
	) as a4
where rank <=1
;

--Lowest kills per side per match--
with kill_data as 
	(select file,att_side,COUNT(*)
	from(select distinct * 
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,att_side
	)

select file,att_side,count
from(select  file,att_side,count,rank() OVER (PARTITION BY file ORDER BY file,count,att_side) as rank
	from kill_data
	) as a4
where rank <=1
;
--Lowest assists per person per round per match--
with assist_data as
	(select file,round,att_team,att_side,att_id,COUNT(*)
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		where att_team!='World'
		except
		select *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,att_team,att_side,att_id
	order by file,round,att_team,att_side,att_id

	)
	

select file,round,att_team,att_side,att_id,count
from(select  file,round,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count,att_id) as rank
	from assist_data
	) as a4
where rank <=1
;
--Lowest assists per person per match--
with assist_data as
	(select file,att_team,att_side,att_id,COUNT(*)
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		where att_team!='World'
		except
		select *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,att_team,att_side,att_id
	order by file,att_team,att_side,att_id
	)
	

select file,att_team,att_side,att_id,count
from(select  file,att_team,att_side,att_id,count,rank() OVER (PARTITION BY file ORDER BY file,count,att_id) as rank
	from assist_data
	) as a4
where rank <=1
;
--Lowest assists per side per round per match--
with assist_data as
	(select file,round,att_side,COUNT(*)
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		where att_team!='World'
		except
		select *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,att_side
	order by file,round,att_side
	)
	

select file,round,att_side,count
from(select  file,round,att_side,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count,att_side) as rank
	from assist_data
	) as a4
where rank <=1
;
--Lowest assists per per side per match--
with assist_data as
	(select file,att_side,COUNT(*)
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		where att_team!='World'
		except
		select *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,att_side
	order by file,att_side
	)
	

select file,att_side,count
from(select  file,att_side,count,rank() OVER (PARTITION BY file ORDER BY file,count,att_side) as rank
	from assist_data
	) as a4
where rank <=1
;

--Lowest assists per team per round per match--
with assist_data as
	(select file,round,att_team,COUNT(*)
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		where att_team!='World'
		except
		select *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,att_team
	order by file,round,att_team
	)
	

select file,round,att_team,count
from(select  file,round,att_team,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count,att_team) as rank
	from assist_data
	) as a4
where rank <=1
;
--Lowest assists per team per match--
with assist_data as
	(select file,att_team,COUNT(*)
	from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
		from esea_dmg
		where att_team!='World'
		except
		select *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,att_team
	order by file,att_team
	)
	

select file,att_team,count
from(select  file,att_team,count,rank() OVER (PARTITION BY file ORDER BY file,count,att_team) as rank
	from assist_data
	) as a4
where rank <=1
;

--Lowest deaths per person per match--
with death_data as
	(select file,  vic_team, vic_side, vic_id, COUNT(*)
	from(
		select distinct *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,  vic_team, vic_side, vic_id
	)

select file, vic_team, vic_side, vic_id,count
from(select  file,vic_team, vic_side, vic_id,count,rank() OVER (PARTITION BY file ORDER BY file,count,vic_id) as rank
	from death_data
	) as a4
where rank <=1
;

--Lowest deaths per team per round per match--
with death_data as
	(select file,round,vic_team, COUNT(*)
	from(
		select distinct *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,vic_team
	)

select file,round, vic_team,count
from(select  file,round,vic_team,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count,vic_team) as rank
	from death_data
	) as a4
where rank <=1
;
--Lowest deaths per team per match--
with death_data as
	(select file,  vic_team, COUNT(*)
	from(
		select distinct *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file, vic_team
	)

select file, vic_team,count
from(select  file,vic_team,count,rank() OVER (PARTITION BY file ORDER BY file,count,vic_team) as rank
	from death_data
	) as a4
where rank <=1
;
--Lowest deaths per side per round per match--
with death_data as
	(select file,round,vic_side, COUNT(*)
	from(
		select distinct *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file,round,vic_side
	)

select file,round, vic_side,count
from(select  file,round,vic_side,count,rank() OVER (PARTITION BY file,round ORDER BY file,round,count,vic_side) as rank
	from death_data
	) as a4
where rank <=1
;
--Lowest deaths per side per match--
with death_data as
	(select file,  vic_side, COUNT(*)
	from(
		select distinct *
		from(select file, round, tick,att_team,vic_team,att_side,vic_side,hp_dmg,arm_dmg,att_id,vic_id 
			from esea_dmg
			) as a1 natural join (select file,round,tick,att_team,vic_team,att_side,vic_side from esea_kills) as a2
		) as a3
	group by file, vic_side
	)

select file, vic_side,count
from(select  file,vic_side,count,rank() OVER (PARTITION BY file ORDER BY file,count,vic_side) as rank
	from death_data
	) as a4
where rank <=1
;