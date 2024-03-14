-- Creates the database hbtn_0d_usa and the table states in it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switches to hbtn_0d_usa database
USE hbtn_0d_usa;

-- Creates table with auto_increment key
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);
