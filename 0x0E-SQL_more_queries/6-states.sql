-- Create a database and a table in it with id as primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
		id INT AUTO_INCREMENT NOT NULL,
		name VARCHAR(256) NOT NULL,
		PRIMARY KEY(id));
