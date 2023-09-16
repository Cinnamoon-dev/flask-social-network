#!/bin/bash

if [ -d ./migrations ];
then
    psql -U postgres -c "DROP DATABASE postgres;"
    rm -rf migrations
    echo "Migrations Deleted"
fi

psql -U postgres -c "CREATE DATABASE postgres;"

flask db init &&
flask db migrate &&
flask db upgrade &&

python3 run.py