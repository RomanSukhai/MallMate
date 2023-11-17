@echo off
cd /d "%~dp0"

chcp 65001
set /p MYSQL_PASSWORD=Введіть ваш пароль від MYSQL: 
echo Ви ввели: %MYSQL_PASSWORD%
setx MYSQL_PWD "%MYSQL_PASSWORD%" /M

python -m venv virtenv 
call virtenv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate 
python manage.py runserver
pause
