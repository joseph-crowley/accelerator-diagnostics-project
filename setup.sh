#!/bin/bash

# Delete the old

# delete database
rm db.sqlite3

# delete static files
rm -rf staticfiles

# delete migrations history
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# delete pycache
find . -type d -name "__pycache__" -exec rm -r {} +

# activate the environment
./create_conda_env.sh

# Create the new database
python manage.py makemigrations core
python manage.py makemigrations docs 
python manage.py makemigrations analysis 
python manage.py makemigrations experiment

python manage.py migrate

# collect static files
python manage.py collectstatic --noinput

# create a superuser
python manage.py create_custom_superuser

# Add initial team members
python manage.py add_team_members

# Add initial docs
python manage.py add_docs

# add initial runs and data_records
python manage.py add_runs
python manage.py add_data_records

# add initial experiment groups and devices
python manage.py add_dirpi_groups
python manage.py add_dirpi_devices

# run the server
python manage.py runserver 0.0.0.0:8005

