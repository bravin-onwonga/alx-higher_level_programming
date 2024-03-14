-- Creates a new user user_0d_2 and a new database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
INDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT
ON hbtn_0d_2
TO 'user_0d_2'@'localhost'
WITH GRANT OPTION;