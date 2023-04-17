-- script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
--create user, password and grant privileges
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT PRIVILEGES ON 'hbnb_test_db'.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES
