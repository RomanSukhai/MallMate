from mysqlx import Error
from db_connector import create_connection

connection = create_connection()

if connection:
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            email VARCHAR(320),
            password VARCHAR(128)
        );
        
        CREATE TABLE UserPasswordResetRequest (
            id INT AUTO_INCREMENT PRIMARY KEY,
            request_id VARCHAR(16) UNIQUE,
            user_email VARCHAR(320),
            create_datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
            duration SMALLINT UNSIGNED DEFAULT 10,
            valid TINYINT(1) DEFAULT 1
        );
        """
        cursor.execute(create_table_query)
        print("Table created successfully")
    except Error as e:
        print(f"Error: {str(e)}")
    finally:
        cursor.close()
        connection.close()
