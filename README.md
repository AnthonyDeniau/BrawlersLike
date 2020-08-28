Documentation:
https://whimsical.com/WboxgSbAXjTsGqwRpErdJz

Initialize venv:
python -m venv venv
. venv/Scripts/activate
cd backend
pip install -r requirements.txt

Create the user:
python manage.py createsuperuser

Create new django app:
. venv/Scripts/activate
cd backend
python manage.py startapp brawler ./apps/brawler

Add the app in project/settings.py

Run Server:
python manage.py runserver

Apply models change:
python manage.py makemigrations
python manage.py migrate
