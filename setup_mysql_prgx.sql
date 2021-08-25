-- Prepares a MySQL server with specific parameters for PRGX challenge database
-- Creates db prgx
CREATE DATABASE IF NOT EXISTS prgx_db;
-- Creates user 'prgx_user' if doesn't exist
CREATE USER IF NOT EXISTS 'prgx_user'@'localhost';
-- Sets password for user 'prgx_user'
SET PASSWORD FOR 'prgx_user'@'localhost' = 'prgx_pwd';
-- Grants privileges to 'prgx_user' on db
GRANT ALL PRIVILEGES ON prgx_db.* TO 'prgx_user'@'localhost';