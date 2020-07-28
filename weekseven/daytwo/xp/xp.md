#exercise 1
UPDATE student SET first_name = 'Lea' WHERE first_name = 'lea';
UPDATE student SET birth_date = '1998-02-11 00:00:00' WHERE (first_name = 'Lea' OR first_name = 'Marc') AND last_name = 'Dupont';

DELETE FROM student WHERE first_name = 'Lea' AND last_name = 'Dupont';

SELECT count(*) FROM student;
SELECT count(*) FROM student WHERE birth_date >= timestamp '2000-01-01 00:00:00';

ALTER TABLE student ADD COLUMN math_grade SMALLINT;
UPDATE student SET math_grade = 80 WHERE id = 1;
UPDATE student SET math_grade = 90 WHERE id = 2 OR id = 4;
UPDATE student SET math_grade = 100 WHERE id = 6;
SELECT count(math_grade) FROM student WHERE math_grade > 83;
INSERT INTO student (first_name, last_name, birth_date, math_grade) VALUES ('Omer', 'Simpson', '1980-03-10 00:00:00', 70);
SELECT first_name, last_name, count(math_grade) AS total_grade FROM student GROUP BY first_name, last_name;
SELECT sum(math_grade) FROM student;

#exercise 2
SELECT * FROM items ORDER BY price ASC;
SELECT * FROM items WHERE price > 80 ORDER BY price DESC;
SELECT f_name, l_name FROM customers ORDER BY f_name ASC LIMIT 3;
SELECT * FROM (SELECT f_name, l_name FROM customers ORDER BY f_name DESC LIMIT 2) AS foo ORDER BY f_name ASC;
SELECT l_name FROM customers ORDER BY l_name DESC;

CREATE TABLE purchases (
	customer_id INTEGER,
	item_id INTEGER,
	FOREIGN KEY (customer_id) REFERENCES customers (id),
	FOREIGN KEY (item_id) REFERENCES items (id)
);

INSERT INTO purchases (customer_id) VALUES (5);
INSERT INTO purchases (customer_id, item_id) VALUES (5, 2), (2, 3), (1, 1), (3, 2), (4, 3);

SELECT * FROM purchases;
SELECT * FROM purchases INNER JOIN customers ON purchases.customer_id = customers.id;
SELECT items.type FROM purchases INNER JOIN items ON purchases.item_id = items.id WHERE customer_id = 4;
SELECT * FROM purchases INNER JOIN items ON purchases.item_id = items.id WHERE items.type = 'Large Desk' OR items.type = 'Small Desk';