-- script that creates the table set a id by defaul by 1 and UNIQUE id
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
