**MallMate**

!fix реєстрація, логін
!add зміна паролю
!change зміни в БД

## Створення БД

1. код для створення БД:

   ```sql
   CREATE DATABASE mallmatebd;
   USE mallmatebd;

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
   ```
   ![WW2.jpg](..%2F..%2F..%2FDownloads%2FWW2.jpg)
