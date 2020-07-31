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
??????????????????????????????????????

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