**УВАГА: Не запускати!**

Логін і реєстрація швидше за все не працюють через зміни в models.py. Потім це буде виправлено, але зараз я йду спати.

## Створення БД

   код для створення БД:

   ```sql
   CREATE DATABASE mallmatedb;
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
   ![cat](https://github.com/RomanSukhai/MallMate/assets/118640498/d23677c0-01d2-4a4a-98e4-faf102485ac8)
