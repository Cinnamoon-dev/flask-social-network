#!/usr/bin/env bash

if [ -d /api/migrations ]; 
then
    rm -rf /api/migrations
    echo "MIGRATIONS DELETED"
fi

flask db init &&
flask db migrate &&
flask db upgrade &&

python3 run.py