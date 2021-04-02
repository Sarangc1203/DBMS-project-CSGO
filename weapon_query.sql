--Most effective weapon for counterterrorist depending on a particular weapon_type and hitbox--
with weapon_data as
	(select wp_type,hitbox,wp,att_side,AVG(hp_dmg) as health_damage,AVG(arm_dmg) as armor_damage
	from (select file,round,hp_dmg,arm_dmg,hitbox,wp,wp_type,att_side from esea_dmg where wp!='Unknown') as a1
	group by wp_type,wp,hitbox,att_side
	order by wp_type,hitbox,health_damage desc, armor_damage desc,wp
	),

weapon_price_data as
	(select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage
	from (select * from weapon_price where price is not NULL and weapon_price.ct = 't') as a2 natural join weapon_data
	where att_side= 'CounterTerrorist'
	)

select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage
from(select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage,rank() OVER (PARTITION BY wp_type,hitbox ORDER BY health_damage desc,armor_damage desc,wp) as rank
	from weapon_price_data
	) as a4
where rank <=1
;
--Most effective weapon for terrorist depending on a particular weapon_type and hitbox--
with weapon_data as
	(select wp_type,hitbox,wp,att_side,AVG(hp_dmg) as health_damage,AVG(arm_dmg) as armor_damage
	from (select file,round,hp_dmg,arm_dmg,hitbox,wp,wp_type,att_side from esea_dmg where wp!='Unknown') as a1
	group by wp_type,wp,hitbox,att_side
	order by wp_type,hitbox,health_damage desc, armor_damage desc,wp
	),

weapon_price_data as
	(select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage
	from (select * from weapon_price where price is not NULL and weapon_price.t = 't') as a2 natural join weapon_data
	where att_side= 'Terrorist'
	)

select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage
from(select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage,rank() OVER (PARTITION BY wp_type,hitbox ORDER BY health_damage desc,armor_damage desc,wp) as rank
	from weapon_price_data
	) as a4
where rank <=1
;
--Most effective weapon for counterterrorist depending on a particular weapon_type--
with weapon_data as
	(select wp_type,hitbox,wp,att_side,AVG(hp_dmg) as health_damage,AVG(arm_dmg) as armor_damage
	from (select file,round,hp_dmg,arm_dmg,hitbox,wp,wp_type,att_side from esea_dmg where wp!='Unknown') as a1
	group by wp_type,wp,hitbox,att_side
	order by wp_type,hitbox,health_damage desc, armor_damage desc,wp
	),

weapon_price_data as
	(select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage
	from (select * from weapon_price where price is not NULL and weapon_price.ct = 't') as a2 natural join weapon_data
	where att_side= 'CounterTerrorist'
	)

select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage
from(select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage,rank() OVER (PARTITION BY wp_type ORDER BY health_damage desc,armor_damage desc,wp) as rank
	from weapon_price_data
	) as a4
where rank <=1
;
--Most effective weapon for terrorist depending on a particular weapon_type--
with weapon_data as
	(select wp_type,hitbox,wp,att_side,AVG(hp_dmg) as health_damage,AVG(arm_dmg) as armor_damage
	from (select file,round,hp_dmg,arm_dmg,hitbox,wp,wp_type,att_side from esea_dmg where wp!='Unknown') as a1
	group by wp_type,wp,hitbox,att_side
	order by wp_type,hitbox,health_damage desc, armor_damage desc,wp
	),

weapon_price_data as
	(select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage
	from (select * from weapon_price where price is not NULL and weapon_price.t = 't') as a2 natural join weapon_data
	where att_side= 'Terrorist'
	)

select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage
from(select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage,rank() OVER (PARTITION BY wp_type ORDER BY health_damage desc,armor_damage desc,wp) as rank
	from weapon_price_data
	) as a4
where rank <=1
;
--Most effective weapon for counterterrorist depending on a particular hitbox--
with weapon_data as
	(select wp_type,hitbox,wp,att_side,AVG(hp_dmg) as health_damage,AVG(arm_dmg) as armor_damage
	from (select file,round,hp_dmg,arm_dmg,hitbox,wp,wp_type,att_side from esea_dmg where wp!='Unknown') as a1
	group by wp_type,wp,hitbox,att_side
	order by wp_type,hitbox,health_damage desc, armor_damage desc,wp
	),

weapon_price_data as
	(select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage
	from (select * from weapon_price where price is not NULL and weapon_price.ct = 't') as a2 natural join weapon_data
	where att_side= 'CounterTerrorist'
	)

select hitbox,wp_type,wp,att_side,price,health_damage,armor_damage
from(select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage,rank() OVER (PARTITION BY hitbox ORDER BY health_damage desc,armor_damage desc,wp) as rank
	from weapon_price_data
	) as a4
where rank <=1
;
--Most effective weapon for terrorist depending on a particular hitbox--
with weapon_data as
	(select wp_type,hitbox,wp,att_side,AVG(hp_dmg) as health_damage,AVG(arm_dmg) as armor_damage
	from (select file,round,hp_dmg,arm_dmg,hitbox,wp,wp_type,att_side from esea_dmg where wp!='Unknown') as a1
	group by wp_type,wp,hitbox,att_side
	order by wp_type,hitbox,health_damage desc, armor_damage desc,wp
	),

weapon_price_data as
	(select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage
	from (select * from weapon_price where price is not NULL and weapon_price.t = 't') as a2 natural join weapon_data
	where att_side= 'Terrorist'
	)

select hitbox,wp_type,wp,att_side,price,health_damage,armor_damage
from(select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage,rank() OVER (PARTITION BY hitbox ORDER BY health_damage desc,armor_damage desc,wp) as rank
	from weapon_price_data
	) as a4
where rank <=1
;
--