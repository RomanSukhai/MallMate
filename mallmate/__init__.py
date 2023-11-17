import mysql.connector
import os

MYSQL_PWD = os.environ.get('MYSQL_PWD', 'ВСТАНОВІТЬ ПАРОЛЬ')
# print(MYSQL_PWD)

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=MYSQL_PWD
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS MallMate")

cursor.close()
connection.close()

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=MYSQL_PWD,

    database='MallMate'
)
