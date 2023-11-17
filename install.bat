@echo off
cd /d "%~dp0"

:admin_check
    echo Потрібні права адміністратора. Перевірка прав...

    net session >nul 2>&1
    if %errorLevel% == 0 (
        echo Успіх: Права адміністратора підтверджено.
    ) else (
        echo Помилка: Поточні права недостатні.
        pause >nul
        exit /b 1
    )


@chcp 65001 >nul
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
