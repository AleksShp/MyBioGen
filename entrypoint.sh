#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn my_bio_gen.wsgi:application --bind 0.0.0.0:8000