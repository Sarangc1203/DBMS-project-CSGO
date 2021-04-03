DROP TABLE match_filter;

CREATE TABLE match_filter AS (
    SELECT * FROM (SELECT tmp1.match, tmp1.map, RANK() OVER(ORDER BY tmp1.match) FROM (SELECT DISTINCT(file) AS match, map FROM esea_rounds WHERE map='de_dust2') AS tmp1) AS tmp2 WHERE tmp2.rank<=200 ORDER BY tmp2.rank
);

INSERT INTO match_filter
SELECT * FROM (SELECT tmp1.match, tmp1.map, RANK() OVER(ORDER BY tmp1.match) FROM (SELECT DISTINCT(file) AS match, map FROM esea_rounds WHERE map='de_overpass') AS tmp1) AS tmp2 WHERE tmp2.rank<=200 ORDER BY tmp2.rank;

INSERT INTO match_filter
SELECT * FROM (SELECT tmp1.match, tmp1.map, RANK() OVER(ORDER BY tmp1.match) FROM (SELECT DISTINCT(file) AS match, map FROM esea_rounds WHERE map='de_mirage') AS tmp1) AS tmp2 WHERE tmp2.rank<=200 ORDER BY tmp2.rank;

INSERT INTO match_filter
SELECT * FROM (SELECT tmp1.match, tmp1.map, RANK() OVER(ORDER BY tmp1.match) FROM (SELECT DISTINCT(file) AS match, map FROM esea_rounds WHERE map='de_cache') AS tmp1) AS tmp2 WHERE tmp2.rank<=200 ORDER BY tmp2.rank;

INSERT INTO match_filter
SELECT * FROM (SELECT tmp1.match, tmp1.map, RANK() OVER(ORDER BY tmp1.match) FROM (SELECT DISTINCT(file) AS match, map FROM esea_rounds WHERE map='de_inferno') AS tmp1) AS tmp2 WHERE tmp2.rank<=200 ORDER BY tmp2.rank;

DROP TABLE test_rounds;

CREATE TABLE test_rounds AS (
    SELECT ER.* FROM esea_rounds AS ER, match_filter as MF WHERE ER.file = MF.match
);

DROP TABLE filtered_kills;

CREATE TABLE filtered_kills AS (
    SELECT ER.*, MF.map FROM esea_kills AS ER, match_filter as MF WHERE ER.file = MF.match
);

DROP TABLE filtered_grenade;

CREATE TABLE filtered_grenade AS (
    SELECT ER.*, MF.map FROM esea_grenade AS ER, match_filter as MF WHERE ER.file = MF.match
);

DROP TABLE filtered_dmg;

CREATE TABLE filtered_dmg AS (
    SELECT ER.*, MF.map FROM esea_dmg AS ER, match_filter as MF WHERE ER.file = MF.match
);

-- COPY filtered_kills TO './filtered_esea_master_kills_demos.csv' DELIMITER ',' CSV HEADER;

\copy filtered_grenade TO './filtered_esea_master_grenade_demos.csv' DELIMITER ',' CSV HEADER;

\copy filtered_dmg TO './filtered_esea_master_dmg_demos.csv' DELIMITER ',' CSV HEADER;

-- DROP TABLE filtered_kills;
DROP TABLE filtered_dmg;
DROP TABLE filtered_grenade;
