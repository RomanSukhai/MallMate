@echo off
@chcp 65001 >nul
call virtenv\Scripts\activate
python manage.py runserver
pause
