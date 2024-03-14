-- Creates the MySQL server user user_0d_1 and grants priviledges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_Pwd@';

GRANT ALL PRIVILEGES
ON *.*
TO 'user_0d_1'@'localhost'
WITH GRANT OPTION;
