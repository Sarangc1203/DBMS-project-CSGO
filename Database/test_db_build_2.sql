DROP TABLE test_dmg;

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
    vic_pos_y int,
    map text
);

\copy test_dmg from '/home/sarang/Desktop/Codes/COL362/Project/Database/test_dmg.csv' delimiter ',' csv header;

DROP TABLE test_grenade;

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
    vic_pos_y int,
    map text
);

\copy test_grenade from '/home/sarang/Desktop/Codes/COL362/Project/Database/test_grenade.csv' delimiter ',' csv header;

DROP TABLE test_kills;

CREATE TABLE test_kills AS (
    SELECT FK.file, FK.round, FK.tick, FK.seconds, FK.att_team, FK.vic_team, FK.att_side, FK.vic_side, FK.wp, FK.wp_type, FK.ct_alive, FK.t_alive, FK.is_bomb_planted, TD.bomb_site, TD.att_pos_x, TD.att_pos_y, TD.vic_pos_x, TD.vic_pos_y, FK.map
    FROM filtered_kills AS FK, test_dmg AS TD
    WHERE FK.file=TD.file AND FK.round=TD.round AND FK.tick=TD.tick
);

DROP TABLE filtered_kills;