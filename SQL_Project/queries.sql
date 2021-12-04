/*
1. Create a query that lists each movie, the film category it is classified in, 
and the number of times it has been rented out.
*/
--Q1
SELECT table_1.category_name category_name, 
SUM(table_1.count_of_rentals) AS number_of_movies
FROM
	(SELECT film.title AS film_title, 
		category.name AS category_name, 
		COUNT(rental.rental_id) AS count_of_rentals
		FROM category
		JOIN film_category 
			ON category.category_id = film_category.category_id
		AND category.name 
			IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
		JOIN film 
			ON film.film_id = film_category.film_id
		JOIN inventory 
			ON inventory.film_id = film.film_id
		JOIN rental 
			ON rental.inventory_id = inventory.inventory_id
	GROUP BY  film_title, category_name
	ORDER BY  film_title) AS table_1
GROUP BY  category_name
ORDER BY category_name ASC;

/*
2. Can you provide a table with the movie titles and divide them
into 4 levels (first_quarter, second_quarter, third_quarter, and final_quarter)
based on the quartiles (25%, 50%, 75%) of the rental duration for 
movies across all categories?
*/
-- Q2
SELECT table_1.category AS category, 
	table_1.rent_duration AS rent_duration,
	COUNT(table_1.movie_title) AS count_movies
	FROM
	(SELECT film.title AS movie_title, category.name AS category,
		film.rental_duration AS rent_duration,
		NTILE(4) OVER (ORDER BY film.rental_duration) AS standard_quartile
		FROM film_category
			JOIN category
				ON category.category_id = film_category.category_id
			JOIN film
				ON film.film_id = film_category.film_id
	WHERE category.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
	GROUP BY movie_title,category, rent_duration) AS table_1
GROUP BY category, rent_duration
ORDER BY category,rent_duration ASC;
	
/*
Question 3
	Provide a table with the family-friendly film category, 
	each of the quartiles, and the corresponding count of movies within 
	each combination of film category for each corresponding rental duration category. 
*/
-- Q3
SELECT name, standard_quartile, COUNT(*)
	FROM 
		(SELECT film.title AS title, 
			category.name AS name, 
			film.rental_duration AS rent_duration, 
			NTILE(4) OVER (ORDER BY film.rental_duration) AS standard_quartile
		FROM film_category
		JOIN category
			ON category.category_id = film_category.category_id
		JOIN film
			ON film.film_id = film_category.film_id
		WHERE category.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
		) AS table_1
GROUP BY name, standard_quartile
ORDER BY name, standard_quartile;

/*
Question 4
Can you write a query to capture the customer name, 
month and year of payment, and total payment amount for each month by these top 10 paying customers?
*/
/* I WILL USE payment TABLE, customer TABLE */
-- Q4
/*QUERY 1 - query used for first insight */
SELECT (customer.first_name || ' ' || customer.last_name) AS customer_full_name,
	DATE_TRUNC('month',payment.payment_date) AS payment_month,
	COUNT(payment.amount) AS pay_countpermon,
	sum(payment.amount) AS amount
	FROM customer
	JOIN payment
		ON payment.customer_id = customer.customer_id
	WHERE (customer.first_name || ' ' || customer.last_name) IN
		/*QUERY 2 - query used for second insight */
		(SELECT customer_full_name
			FROM
			(SELECT (customer.first_name || ' ' || customer.last_name) AS customer_full_name, 
				SUM(payment.amount) as total_amount
				FROM customer
				JOIN payment
					ON payment.customer_id = customer.customer_id
				GROUP BY customer_full_name
				ORDER BY total_amount DESC
				LIMIT 10
			) AS first_table
		) 
GROUP BY customer_full_name, payment_month
ORDER BY customer_full_name, payment_month,  pay_countpermon;
	