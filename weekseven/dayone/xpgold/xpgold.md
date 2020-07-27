CREATE TABLE student (
	id serial PRIMARY KEY,
	last_name VARCHAR(20) NOT NULL,
	first_name VARCHAR (20) NOT NULL,
	birth_date TIMESTAMP NOT NULL
)

INSERT INTO student (first_name, last_name, birth_date) 
Values ('Marc', 'Dupont', '1998-11-02 00:00:00'), ('Yoan', 'Durant', '2010-03-12 00:00:00'),('Lea', 'Martin', '1987-07-24 00:00:00'),('Sarah', 'Benichou', '1996-04-07 00:00:00'), ('lea', 'Dupont', '2003-06-14 00:00:00'), ('Omer', 'Simpson', '1980-03-10 00:00:00');

INSERT INTO student (first_name, last_name, birth_date) 
Values ('Nava', 'Gross', '1993-03-12 00:00:00');

INSERT INTO student (first_name, last_name, birth_date) 
Values ('Rafael', 'Beginsky', '1991-08-07 00:00:00'), ('Maya', 'Beginsky', '2016-10-16 00:00:00');

SELECT * FROM student;
SELECT first_name, last_name FROM student;
SELECT first_name, last_name FROM student WHERE id = 2;
SELECT first_name, last_name FROM student WHERE first_name = 'Marc' AND last_name = 'Dupont';
SELECT first_name, last_name FROM student WHERE first_name = 'Marc' OR last_name = 'Dupont';
SELECT first_name, last_name FROM student WHERE first_name LIKE '%a%';
SELECT first_name, last_name FROM student WHERE first_name LIKE 'A%';
SELECT first_name, last_name FROM student WHERE first_name LIKE '%a';
SELECT first_name, last_name FROM student WHERE (SELECT RIGHT(first_name, 2)) LIKE 'a%';
SELECT first_name, last_name FROM student WHERE id = 1 OR id = 3;
SELECT first_name, last_name, birth_date FROM student WHERE birth_date >= timestamp '2000-01-01 00:00:00';