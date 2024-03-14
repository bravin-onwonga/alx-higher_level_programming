-- Creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create table cities
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES state(id)
);
