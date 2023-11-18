<h1>MallMate</h1>

``` shell
git clone -b mallmate_101_final_log_reg_0.3.5 https://github.com/RomanSukhai/MallMate.git
cd .\MallMate\
```

створіть віртуальне середовище

``` shell
python -m venv virtenv
.\virtenv\Scripts\activate 
pip install -r requirements.txt
```

Тепер окремо запустити файл connect.py що в папці mysql

``` shell
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver
```


   ![cat](https://github.com/RomanSukhai/MallMate/assets/118640498/488761ad-a13a-438b-82df-02a00ef1bcc3)

