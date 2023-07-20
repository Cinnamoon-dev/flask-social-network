#!/bin/bash

if [ -d ./migrations ];
then
    rm -rf migrations
    echo "Migrations Deleted"
fi

flask db init &&
flask db migrate &&
flask db upgrade &&

python3 run.py