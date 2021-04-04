# !/bin/sh

# sudo -u postgres psql project -f ./Database/preamble_weapon.sql
DATABASE_HOST=10.17.10.70 DATABASE_USERNAME=group_26 DATABASE_PASSWORD=cBUmPQdPum7L5 DATABASE_PORT=5432 DATABASE_NAME=group_26 python3 FRONT_END/app.py