Create 3 different tables, each one with a different relationship.
Join them with all the types of PostgreSQL Joins



CREATE TABLE passports (
    passport_id INTEGER PRIMARY KEY,
    country_id INTEGER,
    expiry_date DATE
);

CREATE TABLE person (
    tz SERIAL PRIMARY KEY,
    passport_id INTEGER UNIQUE,
    f_name VARCHAR (50) NOT NULL,
    l_name VARCHAR (50) NOT NULL,
    birthdate DATE NOT NULL,
    FOREIGN KEY (passport_id) REFERENCES passports(passport_id)
);

CREATE TABLE passport_stamps(
    stamp_id SERIAL PRIMARY KEY,
    airport_id INTEGER NOT NULL,
    passport_id INTEGER NOT NULL,
    FOREIGN KEY (passport_id) REFERENCES passports (passport_id)
);

CREATE TABLE airports (
	airport_id SERIAL PRIMARY KEY,
	country_name VARCHAR (50)
);

CREATE TABLE people_visiting_airports(
    airport_id INTEGER,
    tz INTEGER,
    PRIMARY KEY (airport_id, tz),
    FOREIGN KEY (airport_id) REFERENCES airports(airport_id),
    FOREIGN KEY (tz) REFERENCES person(tz)
)

SELECT * FROM passports JOIN person ON passports.passport_id = person.passport_id;

SELECT * FROM passports LEFT JOIN person ON passports.passport_id = person.passport_id;

SELECT * FROM passports RIGHT JOIN person ON passports.passport_id = person.passport_id;

SELECT * FROM passports FULL JOIN person ON passports.passport_id = person.passport_id;


