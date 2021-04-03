#!/bin/sh

sudo -u postgres psql project -f ./Database/preamble_weapon.sql
DATABASE_HOST=127.0.0.1 DATABASE_USERNAME=postgres DATABASE_PORT=5432 DATABASE_NAME=project python3 app.py