import mysql.connector
import os

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=os.environ['MYSQL_PWD']
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS MallMate")

cursor.close()
connection.close()

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=os.environ['MYSQL_PWD'],

    database='MallMate'
)
