#!/usr/bin/env bash

declare database="postgres"

if [ -d ./migrations ];
then
    rm -rf migrations
    echo "Migrations Deleted"
fi

echo "\q" | psql -U postgres -d $database 2> /dev/null && psql -U postgres -c "DROP DATABASE $database;" 2> /dev/null
psql -U postgres -c "CREATE DATABASE $database;"

flask db init || .venv/bin/flask db init
flask db migrate || .venv/bin/flask db migrate
flask db upgrade || .venv/bin/flask db upgrade

python3 run.py
