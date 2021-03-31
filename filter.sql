SELECT * FROM (SELECT tmp1.match, RANK() OVER(ORDER BY tmp1.match) FROM (SELECT DISTINCT(file) AS match FROM esea_rounds WHERE map='de_dust2') AS tmp1) AS tmp2 WHERE tmp2.rank<=100 ORDER BY tmp2.rank;

CREATE TABLE match_filter AS (
    SELECT * FROM (SELECT tmp1.match, RANK() OVER(ORDER BY tmp1.match) FROM (SELECT DISTINCT(file) AS match FROM esea_rounds WHERE map='de_dust2') AS tmp1) AS tmp2 WHERE tmp2.rank<=100 ORDER BY tmp2.rank
);

SELECT ER.* FROM esea_rounds AS ER, match_filter as MF WHERE ER.file = MF.match;

CREATE TABLE filtered_rounds AS (
    SELECT ER.* FROM esea_rounds AS ER, match_filter as MF WHERE ER.file = MF.match
);

CREATE TABLE filtered_kills AS (
    SELECT ER.* FROM esea_kills AS ER, match_filter as MF WHERE ER.file = MF.match
);

CREATE TABLE filtered_grenade AS (
    SELECT ER.* FROM esea_grenade AS ER, match_filter as MF WHERE ER.file = MF.match
);

CREATE TABLE filtered_dmg AS (
    SELECT ER.* FROM esea_dmg AS ER, match_filter as MF WHERE ER.file = MF.match
);

CREATE TABLE weapons AS (
    select distinct wp_type, wp from esea_dmg order by wp_type, wp
);

SELECT count(distinct file) FROM filtered_kills as tmp;


COPY filtered_grenade TO '/home/sarang/Desktop/Codes/COL362/Project/Database/filtered_esea_master_grenades_demos.csv' DELIMITER ',' CSV HEADER;

COPY filtered_kills TO '/home/sarang/Desktop/Codes/COL362/Project/Database/filtered_esea_master_kills_demos.csv' DELIMITER ',' CSV HEADER;

COPY filtered_rounds TO '/home/sarang/Desktop/Codes/COL362/Project/Database/filtered_esea_meta_demos.csv' DELIMITER ',' CSV HEADER;

COPY filtered_dmg TO '/home/sarang/Desktop/Codes/COL362/Project/Database/filtered_esea_master_dmg_demos.csv' DELIMITER ',' CSV HEADER;

COPY weapons TO '/home/sarang/Desktop/Codes/COL362/Project/weapons.csv' DELIMITER ',' CSV HEADER;