import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root'
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS MallMate")

cursor.close()
connection.close()

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',

    database='MallMate'
)
