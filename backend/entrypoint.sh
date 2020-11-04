#!bin/bash
python manage.py collectstatic --noinput --clear
python manage.py migrate
gunicorn project.wsgi_prod:application --log-file=- --workers=2 -b 0.0.0.0:8000