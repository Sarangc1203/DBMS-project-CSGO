CREATE TABLE esea_dmg (
    file text,
    round smallint,
    tick int,
    seconds decimal(12,4),
    att_team text,
    vic_team text,
    att_side text,
    vic_side text,
    hp_dmg smallint,
    arm_dmg smallint,
    is_bomb_planted boolean,
    bomb_site text,
    hitbox text,
    wp text,
    wp_type text,
    att_id bigint,
    att_rank smallint,
    vic_id bigint,
    vic_rank smallint,
    att_pos_x decimal(25,20),
    att_pos_y decimal(25,20),
    vic_pos_x decimal(25,20),
    vic_pos_y decimal(25,20)
);


CREATE TABLE esea_grenade (
    file text,
    round smallint,
    seconds decimal(12,4),
    att_team text,
    vic_team text,
    att_id bigint,
    vic_id decimal,
    att_side text,
    vic_side text,
    hp_dmg smallint,
    arm_dmg smallint,
    is_bomb_planted boolean,
    bomb_site text,
    hitbox text,
    nade text,
    att_rank smallint,
    vic_rank decimal,
    att_pos_x decimal(25,20),
    att_pos_y decimal(25,20),
    nade_land_x decimal(25,20),
    nade_land_y decimal(25,20),
    vic_pos_x decimal(25,20),
    vic_pos_y decimal(25,20)
);


CREATE TABLE esea_kills (
    file text,
    round smallint,
    tick int,
    seconds decimal(12,4),
    att_team text,
    vic_team text,
    att_side text,
    vic_side text,
    wp text,
    wp_type text,
    ct_alive smallint,
    t_alive smallint,
    is_bomb_planted boolean
);

CREATE TABLE esea_rounds (
    file text,
    map text,
    round smallint,
    start_seconds decimal(12,4),
    end_seconds decimal(12,4),
    winner_team text,
    winner_side text,
    round_type text,
    ct_eq_val int,
    t_eq_val int
);

CREATE TABLE map_data (
    MapName text,
    EndX decimal(25,20),
    EndY decimal(25,20),
    ResX int,
    ResY int,
    StartX decimal(25,20),
    StartY decimal(25,20)
);

CREATE TABLE test_dmg (
    file text,
    round smallint,
    tick int,
    seconds decimal(12,4),
    att_team text,
    vic_team text,
    att_side text,
    vic_side text,
    hp_dmg smallint,
    arm_dmg smallint,
    is_bomb_planted boolean,
    bomb_site text,
    hitbox text,
    wp text,
    wp_type text,
    att_id bigint,
    att_rank smallint,
    vic_id bigint,
    vic_rank smallint,
    att_pos_x int,
    att_pos_y int,
    vic_pos_x int,
    vic_pos_y int
);

CREATE TABLE test_grenade (
    file text,
    round smallint,
    seconds decimal(12,4),
    att_team text,
    vic_team text,
    att_id bigint,
    vic_id decimal,
    att_side text,
    vic_side text,
    hp_dmg smallint,
    arm_dmg smallint,
    is_bomb_planted boolean,
    bomb_site text,
    hitbox text,
    nade text,
    att_rank smallint,
    vic_rank decimal,
    att_pos_x int,
    att_pos_y int,
    nade_land_x int,
    nade_land_y int,
    vic_pos_x int,
    vic_pos_y int
);

-- CREATE TABLE mm_grenade (
--     serial_no bigint,
--     file text,
--     map text,
--     round smallint,
--     start_seconds decimal(12,4),
--     seconds decimal(12,4),
--     end_seconds decimal(12,4),
--     att_team text,
--     vic_team text,
--     att_id bigint,
--     vic_id decimal,
--     att_side text,
--     vic_side text,
--     hp_dmg smallint,
--     arm_dmg smallint,
--     is_bomb_planted boolean,
--     bomb_site text,
--     hitbox text,
--     nade text,
--     winner_team text,
--     winner_side text,
--     att_rank smallint,
--     vic_rank decimal,
--     att_pos_x decimal(25,20),
--     att_pos_y decimal(25,20),
--     nade_land_x decimal(25,20),
--     nade_land_y decimal(25,20),
--     vic_pos_x decimal(25,20),
--     vic_pos_y decimal(25,20),
--     round_type text,
--     ct_eq_val int,
--     t_eq_val int,
--     avg_match_rank decimal
-- );

-- CREATE TABLE mm_dmg (
--     serial_no int,
--     file text,
--     map text,
--     match_date text,
--     round smallint,
--     tick int,
--     seconds decimal(12,4),
--     att_team text,
--     vic_team text,
--     att_side text,
--     vic_side text,
--     hp_dmg smallint,
--     arm_dmg smallint,
--     is_bomb_planted boolean,
--     bomb_site text,
--     hitbox text,
--     wp text,
--     wp_type text,
--     award int,
--     winner_team text,
--     winner_side text,
--     att_id bigint,
--     att_rank smallint,
--     vic_id bigint,
--     vic_rank smallint,
--     att_pos_x decimal(25,20),
--     att_pos_y decimal(25,20),
--     vic_pos_x decimal(25,20),
--     vic_pos_y decimal(25,20),
--     round_type text,
--     ct_eq_val int,
--     t_eq_val int,
--     avg_match_rank decimal
-- );


-- \copy esea_dmg from '/home/sarang/Desktop/Codes/COL362/Project/Database/esea_master_dmg_demos.part1.csv' delimiter ',' csv header;
-- \copy esea_dmg from 'D:\6th sem\col362 database management\project\archive\esea_master_dmg_demos.part2.csv' delimiter ',' csv header;

\copy test_dmg from '/home/sarang/Desktop/Codes/COL362/Project/Database/Filtered_data/test_dmg.csv' delimiter ',' csv header;

\copy test_grenade from '/home/sarang/Desktop/Codes/COL362/Project/Database/Filtered_data/test_grenade.csv' delimiter ',' csv header;

\copy esea_grenade from '/home/sarang/Desktop/Codes/COL362/Project/Database/esea_master_grenades_demos.part1.csv' delimiter ',' csv header;
-- \copy esea_grenade from 'D:\6th sem\col362 database management\project\archive\esea_master_grenades_demos.part2.csv' delimiter ',' csv header;

ALTER TABLE esea_grenade
ALTER COLUMN vic_id TYPE bigint,
ALTER COLUMN vic_rank TYPE smallint;
;


\copy esea_kills from '/home/sarang/Desktop/Codes/COL362/Project/Database/esea_master_kills_demos.part1.csv' delimiter ',' csv header;
-- \copy esea_kills from 'D:\6th sem\col362 database management\project\archive\esea_master_kills_demos.part2.csv' delimiter ',' csv header;

\copy esea_rounds from '/home/sarang/Desktop/Codes/COL362/Project/Database/esea_meta_demos.part1.csv' delimiter ',' csv header;
-- \copy esea_rounds from 'D:\6th sem\col362 database management\project\archive\esea_meta_demos.part2.csv' delimiter ',' csv header;

-- \copy map_data from 'D:\6th sem\col362 database management\project\archive\map_data.csv' delimiter ',' csv header;


-- \copy mm_grenade from 'D:\6th sem\col362 database management\project\archive\mm_grenades_demos.csv' delimiter ',' csv header;

-- ALTER TABLE mm_grenade
-- ALTER COLUMN vic_id TYPE bigint,
-- ALTER COLUMN vic_rank TYPE smallint,
-- ALTER COLUMN avg_match_rank TYPE smallint;


-- \copy mm_dmg from 'D:\6th sem\col362 database management\project\archive\mm_master_demos.csv' delimiter ',' csv header;

-- ALTER TABLE mm_dmg
-- ALTER COLUMN avg_match_rank TYPE smallint;


