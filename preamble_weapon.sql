drop view budget_data_ct;
drop view budget_data_t;
drop view weapon_price_ct;
drop view weapon_price_t;
create view weapon_price_ct as  
	(with weapon_data as
		(select wp_type,hitbox,wp,att_side,AVG(hp_dmg) as health_damage,AVG(arm_dmg) as armor_damage
		from (select file,round,hp_dmg,arm_dmg,hitbox,wp,wp_type,att_side from esea_dmg where wp!='Unknown') as a1
		group by wp_type,wp,hitbox,att_side
		order by wp_type,hitbox,health_damage desc, armor_damage desc,wp
		)

	select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage
	from (select * from weapon_price where price is not NULL and weapon_price.ct = 't') as a2 natural join weapon_data
	where att_side= 'CounterTerrorist'
	)
;
create view weapon_price_t as  
	(with weapon_data as
		(select wp_type,hitbox,wp,att_side,AVG(hp_dmg) as health_damage,AVG(arm_dmg) as armor_damage
		from (select file,round,hp_dmg,arm_dmg,hitbox,wp,wp_type,att_side from esea_dmg where wp!='Unknown') as a1
		group by wp_type,wp,hitbox,att_side
		order by wp_type,hitbox,health_damage desc, armor_damage desc,wp
		)

	select wp_type,hitbox,wp,att_side,price,health_damage,armor_damage
	from (select * from weapon_price where price is not NULL and weapon_price.t = 't') as a2 natural join weapon_data
	where att_side= 'Terrorist'
	)
;	
create view budget_data_ct as
	(with equipment_data as (select wp_type,wp,price,AVG(health_damage) as health_damage,AVG(armor_damage) as armor_damage from weapon_data_ct where wp_type = 'Equipment' group by wp_type,wp,price),
	grenade_data as (select wp_type,wp,price,AVG(health_damage) as health_damage,AVG(armor_damage) as armor_damage from weapon_data_ct where wp_type = 'Grenade' group by wp_type,wp,price),
	a1 as(select equipment_data.wp as Equipment_weapon,grenade_data.wp as Grenade_weapon, (equipment_data.price + grenade_data.price) as price, (equipment_data.health_damage + grenade_data.health_damage) as health_damage , (equipment_data.armor_damage + grenade_data.armor_damage) as armor_damage from equipment_data join grenade_data on grenade_data.wp_type!=equipment_data.wp_type),

	heavy_data as (select wp_type,wp,price,AVG(health_damage) as health_damage,AVG(armor_damage) as armor_damage from weapon_data_ct where wp_type = 'Heavy' group by wp_type,wp,price),
	pistol_data as (select wp_type,wp,price,AVG(health_damage) as health_damage,AVG(armor_damage) as armor_damage from weapon_data_ct where wp_type = 'Pistol' group by wp_type,wp,price),
	a2 as (select heavy_data.wp as Heavy_weapon,pistol_data.wp as Pistol_weapon, (heavy_data.price + pistol_data.price) as price, (heavy_data.health_damage + pistol_data.health_damage) as health_damage , (heavy_data.armor_damage + pistol_data.armor_damage) as armor_damage from heavy_data join pistol_data on heavy_data.wp_type!=pistol_data.wp_type),

	rifle_data as (select wp_type,wp,price,AVG(health_damage) as health_damage,AVG(armor_damage) as armor_damage from weapon_data_ct where wp_type = 'Rifle' group by wp_type,wp,price),
	smg_data as (select wp_type,wp,price,AVG(health_damage) as health_damage,AVG(armor_damage) as armor_damage from weapon_data_ct where wp_type = 'SMG' group by wp_type,wp,price),
	a3 as (select rifle_data.wp as Rifle_weapon,smg_data.wp as SMG_weapon, (rifle_data.price + smg_data.price) as price, (rifle_data.health_damage + smg_data.health_damage) as health_damage , (rifle_data.armor_damage + smg_data.armor_damage) as armor_damage from rifle_data join smg_data on rifle_data.wp_type!=smg_data.wp_type),

	a4 as (select  Equipment_weapon, Grenade_weapon, Heavy_weapon, Pistol_weapon, (a1.price + a2.price) as price, (a1.health_damage + a2.health_damage) as health_damage , (a1.armor_damage + a2.armor_damage) as armor_damage from a1 join a2 on a1.Equipment_weapon!=a2.Heavy_weapon),

	sniper_data as (select wp_type,wp,price,AVG(health_damage) as health_damage,AVG(armor_damage) as armor_damage from weapon_data_ct where wp_type = 'Sniper' group by wp_type,wp,price),
	a5 as (select  Rifle_weapon, SMG_weapon, sniper_data.wp as Sniper_weapon, (a3.price + sniper_data.price) as price, (a3.health_damage + sniper_data.health_damage) as health_damage , (a3.armor_damage + sniper_data.armor_damage) as armor_damage from a3 join sniper_data on a3.Rifle_weapon!=sniper_data.wp)

	select  Equipment_weapon, Grenade_weapon, Heavy_weapon, Pistol_weapon,  Rifle_weapon, SMG_weapon, Sniper_weapon,(a4.price + a5.price) as price, (a4.health_damage + a5.health_damage)/7 as health_damage , (a4.armor_damage + a5.armor_damage)/7 as armor_damage from a4 join a5 on a4.Equipment_weapon!=a5.Sniper_weapon
	)
;

create view budget_data_t as
	(with equipment_data as (select wp_type,wp,price,AVG(health_damage) as health_damage,AVG(armor_damage) as armor_damage from weapon_data_t where wp_type = 'Equipment' group by wp_type,wp,price),
	grenade_data as (select wp_type,wp,price,AVG(health_damage) as health_damage,AVG(armor_damage) as armor_damage from weapon_data_t where wp_type = 'Grenade' group by wp_type,wp,price),
	a1 as(select equipment_data.wp as Equipment_weapon,grenade_data.wp as Grenade_weapon, (equipment_data.price + grenade_data.price) as price, (equipment_data.health_damage + grenade_data.health_damage) as health_damage , (equipment_data.armor_damage + grenade_data.armor_damage) as armor_damage from equipment_data join grenade_data on grenade_data.wp_type!=equipment_data.wp_type),

	heavy_data as (select wp_type,wp,price,AVG(health_damage) as health_damage,AVG(armor_damage) as armor_damage from weapon_data_t where wp_type = 'Heavy' group by wp_type,wp,price),
	pistol_data as (select wp_type,wp,price,AVG(health_damage) as health_damage,AVG(armor_damage) as armor_damage from weapon_data_t where wp_type = 'Pistol' group by wp_type,wp,price),
	a2 as (select heavy_data.wp as Heavy_weapon,pistol_data.wp as Pistol_weapon, (heavy_data.price + pistol_data.price) as price, (heavy_data.health_damage + pistol_data.health_damage) as health_damage , (heavy_data.armor_damage + pistol_data.armor_damage) as armor_damage from heavy_data join pistol_data on heavy_data.wp_type!=pistol_data.wp_type),

	rifle_data as (select wp_type,wp,price,AVG(health_damage) as health_damage,AVG(armor_damage) as armor_damage from weapon_data_t where wp_type = 'Rifle' group by wp_type,wp,price),
	smg_data as (select wp_type,wp,price,AVG(health_damage) as health_damage,AVG(armor_damage) as armor_damage from weapon_data_t where wp_type = 'SMG' group by wp_type,wp,price),
	a3 as (select rifle_data.wp as Rifle_weapon,smg_data.wp as SMG_weapon, (rifle_data.price + smg_data.price) as price, (rifle_data.health_damage + smg_data.health_damage) as health_damage , (rifle_data.armor_damage + smg_data.armor_damage) as armor_damage from rifle_data join smg_data on rifle_data.wp_type!=smg_data.wp_type),

	a4 as (select  Equipment_weapon, Grenade_weapon, Heavy_weapon, Pistol_weapon, (a1.price + a2.price) as price, (a1.health_damage + a2.health_damage) as health_damage , (a1.armor_damage + a2.armor_damage) as armor_damage from a1 join a2 on a1.Equipment_weapon!=a2.Heavy_weapon),

	sniper_data as (select wp_type,wp,price,AVG(health_damage) as health_damage,AVG(armor_damage) as armor_damage from weapon_data_t where wp_type = 'Sniper' group by wp_type,wp,price),
	a5 as (select  Rifle_weapon, SMG_weapon, sniper_data.wp as Sniper_weapon, (a3.price + sniper_data.price) as price, (a3.health_damage + sniper_data.health_damage) as health_damage , (a3.armor_damage + sniper_data.armor_damage) as armor_damage from a3 join sniper_data on a3.Rifle_weapon!=sniper_data.wp)

	select  Equipment_weapon, Grenade_weapon, Heavy_weapon, Pistol_weapon,  Rifle_weapon, SMG_weapon, Sniper_weapon,(a4.price + a5.price) as price, (a4.health_damage + a5.health_damage)/7 as health_damage , (a4.armor_damage + a5.armor_damage)/7 as armor_damage from a4 join a5 on a4.Equipment_weapon!=a5.Sniper_weapon
	)
;