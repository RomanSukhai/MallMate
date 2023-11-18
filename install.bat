@echo off
@chcp 65001 >nul
python -m venv virtenv 
call virtenv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate 
python manage.py runserver
pause
