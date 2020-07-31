#1 
SELECT first_name AS "First Name", last_name AS "Last Name" FROM employees

#2
SELECT department_id FROM employees GROUP BY department_id HAVING COUNT(department_id) = 1

#3
SELECT * FROM employees ORDER BY first_name DESC

#4
SELECT employee_id, first_name, last_name, salary, (salary*0.15) AS pf FROM employees ORDER BY salary ASC

#5
SELECT employee_id, first_name, last_name, salary FROM employees ORDER BY salary ASC

#6
SELECT sum(salary) FROM employees

#7
SELECT max(salary), min(salary) FROM employees

#8 
SELECT count(*) as totalemployees, sum(salary) AS totalsalary, (sum(salary)/count(*)) AS averagesalary FROM employees

#9
SELECT count(*) FROM employees

#10
SELECT COUNT(DISTINCT(job_id)) FROM employees

#11
SELECT UPPER(first_name) FROM EMPLOYEES

#12
SELECT SUBSTRING(first_name FOR 3) FROM EMPLOYEES

#13
SELECT 175*214+625

#14
SELECT FIRST_NAME, LAST_NAME FROM employees

#15
SELECT trim(FIRST_NAME) FROM employees

#16
SELECT FIRST_NAME, last_name, (char_length(first_name) + char_length(last_name)) FROM employees

#17
SELECT FIRST_NAME FROM employees WHERE first_name ~ '[0-9]'

#18
SELECT * FROM employees LIMIT 10

#19
SELECT employee_id, round((salary/12), 2) FROM employees LIMIT 10

#tables
#1
CREATE TABLE countries2(
	country_id SERIAL PRIMARY KEY,
	country_name varchar (20) NOT NULL UNIQUE,
	region_id smallint NOT NULL
)

#2
CREATE TABLE countries3(
	country_id SERIAL PRIMARY KEY,
	country_name varchar (20) NOT NULL UNIQUE,
	region_id smallint NOT NULL,
	FOREIGN KEY (region_id) REFERENCES regions (region_id)
)

#3
CREATE TABLE dup_countries AS TABLE countries WITH NO DATA;

#4
CREATE TABLE dup_countries_with_data AS TABLE countries;

#5
???????????I dont get the instructions....

#6
CREATE TABLE jobs2 (
	job_id SERIAL PRIMARY KEY,
	job_title varchar(25) NOT NULL UNIQUE,
	min_salary numeric(8, 2),
	max_salary numeric(8, 2),
	constraint valid_numeric
      check(MAX_SALARY < 25000)
)

#7
CREATE TABLE countriesz(
	country_id SERIAL PRIMARY KEY,
	country_name VARCHAR (20) CHECK(country_name in('Italy', 'India', 'China')),
	region_id smallint
)

#8 - (primary key makes sure its unique, so unless I'm misunderstanding the question I think this is all)
CREATE TABLE countriesz(
	country_id SERIAL PRIMARY KEY,
	country_name VARCHAR (20),
	region_id smallint
)

#9
CREATE TABLE jobz (
	job_id SERIAL PRIMARY KEY,
	job_title VARCHAR (20) DEFAULT '',
	min_salary smallint DEFAULT 8000,
	max_salary smallint
)

#10
CREATE TABLE countries(
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR (20),
    region_id SMALLINT
)

#11
CREATE TABLE countries(
	country_id SERIAL PRIMARY KEY,
	country_name VARCHAR(20),
	region_id smallint
)

#12
CREATE TABLE countriesa(
	country_id smallint,
	country_name VARCHAR(20),
	region_id smallint,
	PRIMARY KEY(country_id, region_id)
)

#13
CREATE TABLE job_history(
    employee_id SMALLINT UNIQUE,
    start_date timestamp,
    end_date timestamp,
    job_id smallint,
    department_id SMALLINT,
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
)

#14 (I followed the intructions despite the fact that the departments table doesnt have a manager id column....)
CREATE TABLE employees(
    employee_id SERIAL PRIMARY KEY,
	first_name varchar (50),
	last_name varchar (50),
	email varchar (50),
	phone_number integer,
	hire_date date,
	job_id smallint,
	salary smallint,
	commission smallint,
	manager_id smallint,
	department_id smallint,
    FOREIGN KEY (department_id, manager_id) REFERENCES departments (department_id, manager_id)
)

#15
CREATE TABLE employees2(
    employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR (20),
	last_name VARCHAR (20),
	email VARCHAR (50),
	phone_number INTEGER,
	hire_date DATE,
	job_id smallint,
	salary smallint,
	commission smallint,
	manager_id smallint,
	department_id smallint,
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
	FOREIGN KEY (job_id) REFERENCES jobs(job_id)
)

#16
CREATE TABLE employees3(
    employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR (20),
	last_name VARCHAR (20),
	job_id smallint,
	salary smallint,
	FOREIGN KEY (job_id) REFERENCES jobs(job_id) ON DELETE RESTRICT ON UPDATE CASCADE
)

#WEIRD MIDDLE SECTION ASSIGNMENTS
CREATE TABLE employees4(
    employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR (20),
	last_name VARCHAR (20),
	job_id smallint,
	salary smallint,
	FOREIGN KEY (job_id) REFERENCES jobs(job_id) ON DELETE CASCADE ON UPDATE RESTRICT
)

CREATE TABLE employees4(
    employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR (20),
	last_name VARCHAR (20),
	job_id smallint,
	salary smallint,
	FOREIGN KEY (job_id) REFERENCES jobs(job_id) ON DELETE SET NULL ON UPDATE SET NULL
)

CREATE TABLE employees4(
    employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR (20),
	last_name VARCHAR (20),
	job_id smallint,
	salary smallint,
	FOREIGN KEY (job_id) REFERENCES jobs(job_id) ON DELETE NO ACTION ON UPDATE NO ACTION
)

## restricting and sorting
#1
SELECT first_name, last_name, salary FROM employees WHERE salary BETWEEN 10000 AND 15000

#2 (These departments dont exist so kind of a weird exercise)
SELECT first_name, last_name, department_id FROM employees 
WHERE department_id = 30 OR department_id = 100
ORDER BY department_id ASC

#3
SELECT first_name, last_name, salary FROM employees 
WHERE (department_id = 30 OR department_id = 100) AND salary between 10000 AND 15000
ORDER BY department_id ASC

#4
SELECT first_name, last_name, hire_date FROM employees 
WHERE hire_date BETWEEN '1987-01-01' and '1987-12-31'

#5
SELECT first_name FROM employees 
WHERE first_name ILIKE '%c%e%' 

#6
SELECT last_name, job_title, salary FROM employees JOIN jobs ON employees.job_id = jobs.job_id
WHERE job_title != 'Programmer' and job_title != 'Shipping Clerk' 
AND salary != 4500 AND salary != 10000 AND salary != 15000

#7
SELECT last_name FROM employees 
WHERE LENGTH(last_name) = 6

#8
SELECT last_name FROM employees 
WHERE last_name LIKE '__e%'

#9
SELECT DISTINCT job_title FROM employees JOIN jobs ON jobs.job_id = employees.job_id

#10
SELECT first_name, last_name, salary, (salary*0.15) AS PF FROM employees

#11
SELECT * FROM employees WHERE last_name IN ('Jones', 'Blake', 'Scott', 'King', 'Ford')