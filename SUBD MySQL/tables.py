from mysqlx import Error
from db_connector import create_connection

connection = create_connection()

if connection:
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL ,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL
        )
        
        """
        cursor.execute(create_table_query)
        print("Table created successfully")
    except Error as e:
        print(f"Error: {str(e)}")
    finally:
        cursor.close()
        connection.close()
