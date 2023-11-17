read -p "Введіть ваш пароль від MySQL: " MYSQL_PASSWORD
echo "Ви ввели: $MYSQL_PASSWORD"
export MYSQL_PWD=$MYSQL_PASSWORD

python -m venv virtenv
source virtenv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
