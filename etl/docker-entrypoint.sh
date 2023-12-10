#!/bin/sh
python wait_for_pg.py
alembic upgrade head
python run.py $@