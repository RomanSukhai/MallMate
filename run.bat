@echo off
cd /d "%~dp0"
@chcp 65001 >nul
call virtenv\Scripts\activate
python manage.py runserver
pause
