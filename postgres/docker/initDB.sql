CREATE USER playarea2_user WITH PASSWORD 'playarea2_password';
CREATE DATABASE playarea2_db;
GRANT ALL ON DATABASE playarea2_db TO playarea2_user;

ALTER USER playarea2_user CREATEDB;

CREATE USER playarea2_user_testing WITH PASSWORD 'playarea2_password_testing';
CREATE DATABASE playarea2_db_testing;
GRANT ALL PRIVILEGES ON DATABASE playarea2_db_testing TO playarea2_user_testing;
