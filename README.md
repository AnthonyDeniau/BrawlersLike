Documentation:
https://whimsical.com/WboxgSbAXjTsGqwRpErdJz

Initialize venv:
python -m venv venv
. venv/Scripts/activate
cd backend
pip install -r requirements.txt

Create new django app:
. venv/Scripts/activate
cd backend
python manage.py startapp brawler ./apps/brawler

Add the app in project/settings.py
