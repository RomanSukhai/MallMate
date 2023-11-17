@echo off
set /p MYSQL_PASSWORD=Введіть ваш пароль від MYSQL: 
echo Ви ввели: %MYSQL_PASSWORD%

python -m virtualenv virtenv 
.\virtenv\Scripts\activate 
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate 
python manage.py runserver
pause
