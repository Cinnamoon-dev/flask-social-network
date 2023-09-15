#!/bin/bash

if [ -d ./migrations ];
then
    psql -U postgres psql -c "DROP DATABASE postgres;"
    rm -rf migrations
    echo "Migrations Deleted"
fi

psql -U postgres psql -c "CREATE DATABASE postgres;"

flask db init &&
flask db migrate &&
flask db upgrade &&

python3 run.py