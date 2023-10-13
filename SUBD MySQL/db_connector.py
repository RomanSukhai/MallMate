import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='rootnamor2004',
            database='mallmatedb'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {str(e)}")
        return None
