CREATE TABLE items (
	id SERIAL NOT NULL,
	type VARCHAR(30) PRIMARY KEY, 
	price INTEGER NOT NULL
)

CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	f_name VARCHAR NOT NULL,
	l_name VARCHAR NOT NULL
)

INSERT INTO items (type, price) VALUES ('Small Desk', 100), ('Large Desk', 300), ('Fan', 80)

INSERT INTO customers (f_name, l_name) VALUES ('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson')

SELECT * FROM items
SELECT * FROM items WHERE price > 80
SELECT * FROM items WHERE price < 30
SELECT * FROM customers WHERE l_name = 'Smith'
SELECT * FROM customers WHERE f_name != 'Craig'