#!/bin/sh

# touch filtered_esea_master_kills_demos.csv
touch filtered_esea_master_grenade_demos.csv
touch filtered_esea_master_dmg_demos.csv

chmod 777 filtered_*

sudo -u postgres psql project -f test_db_build_1.sql

DATABASE_HOST=127.0.0.1 DATABASE_USERNAME=postgres DATABASE_PORT=5432 DATABASE_NAME=project python3 table_xy_to_pixel.py

sudo -u postgres psql project -f test_db_build_2.sql

rm -f filtered_esea_master_dmg_demos.csv
rm -f filtered_esea_master_grenade_demos.csv

touch test_dmg.csv
touch test_kills.csv
touch test_grenade.csv
touch test_rounds.csv

chmod 777 test_*

sudo -u postgres psql project -f test_db_build_3.sql