#1
UPDATE film SET language_id = 2 WHERE film_id = 23 OR film_id = 432 OR film_id = 300; 
#2
INSERT INTO address(address, district, city_id, postal_code, phone, last_update) VALUES ('5370 SW 34TH TERRACE', 'broward', 4, 33312, 3211321, CURRENT_TIMESTAMP)
INSERT INTO customer (store_id, first_name, last_name,email, activebool, create_date, last_update, active, address_id) 
VALUES (1, 'Nava', 'Gross', 'myemail@email.com', true, '2020-07-28', CURRENT_TIMESTAMP, 1, (SELECT address_id FROM address WHERE address = '5370 SW 34TH TERRACE')), 
(2, 'Nonny', 'Gross', 'myemail@email.com', true, '2020-07-28', CURRENT_TIMESTAMP, 1, (SELECT address_id FROM address WHERE address = '5370 SW 34TH TERRACE')),
(1, 'Sarah', 'Gross', 'myemail@email.com', true, '2020-07-28', CURRENT_TIMESTAMP, 1, (SELECT address_id FROM address WHERE address = '5370 SW 34TH TERRACE'));
///Was there a better way to do this? (#2)

#3
INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, last_update, special_features)
VALUES ('Bad Moms', 'Moms who stop trying', 2016, 1, 5, 4.99, 120, 20.99, 'PG-13', CURRENT_TIMESTAMP, '{Trailers}'), ('Bad Moms 2', 'Moms who stop trying, number 2', 2018, 1, 5, 4.99, 120, 20.99, 'PG-13', CURRENT_TIMESTAMP, '{Trailers}'), ('Were the millers', 'Family Drug Smuggling', 2016, 1, 5, 4.99, 120, 20.99, 'R', CURRENT_TIMESTAMP, '{Trailers}');

#4
DROP TABLE IF EXISTS customer_review;

#5
SELECT title FROM film INNER JOIN film_actor ON film.film_id = film_actor.film_id 
INNER JOIN actor on actor.actor_id = film_actor.actor_id WHERE description ILIKE '%sumo%' and first_name = 'Penelope' and last_name = 'Monroe'

SELECT title FROM film WHERE length < 60 AND rating = 'R' AND description ILIKE '%documentary%'

SELECT title FROM film INNER JOIN rental ON film.film_id = rental.inventory_id
INNER JOIN customer ON rental.customer_id = customer.customer_id
WHERE first_name = 'Matthew' AND last_name = 'Mahan' AND rental_rate > 4.00 AND return_date BETWEEN '2005-07-28' AND '2005-08-01'

SELECT title FROM film INNER JOIN rental ON film.film_id = rental.inventory_id
INNER JOIN customer ON rental.customer_id = customer.customer_id
WHERE first_name = 'Matthew' AND last_name = 'Mahan' AND (title ILIKE '%boat%' OR description ILIKE '%boat%')
