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

CREATE TABLE test_kills (
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
    is_bomb_planted boolean,
    bomb_site text,
    att_pos_x int,
    att_pos_y int,
    vic_pos_x int,
    vic_pos_y int,
    map text
);

\copy test_kills from '/home/sarang/Desktop/Codes/COL362/Project/Database/test_kills.csv' delimiter ',' csv header;

DROP TABLE test_rounds;

CREATE TABLE test_rounds (
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

\copy test_rounds from '/home/sarang/Desktop/Codes/COL362/Project/Database/test_rounds.csv' delimiter ',' csv header;

DROP TABLE weapon_price;

CREATE TABLE weapon_price(
    wp_type text,
    wp text,
    price int,
    ct boolean,
    t boolean
 
);

\copy weapon_price from '/home/sarang/Desktop/Codes/COL362/Project/Database/weapons_price.csv' delimiter ',' csv header;