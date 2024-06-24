To create an ERD for a movie theater using Lucidchart and PostgreSQL, we'll consider entities such as Customers, Tickets, Concessions, and Movies. Here's a step-by-step guide including the ERD creation, SQL table creation scripts, and sample data insertion.

1. Entity-Relationship Diagram (ERD) in Lucidchart
Below is the ERD for the movie theater:

ERD Explanation and Relationships:

Customer Entity: Represents individuals who purchase tickets and concessions. Each customer has a unique ID (customer_id).

Movie Entity: Represents movies being shown at the theater. Each movie has a unique ID (movie_id).

Ticket Entity: Connects customers with movies, indicating which customer bought tickets for which movie. Includes attributes like ticket_id, customer_id, movie_id, and purchase_date.

Concession Entity: Represents the items sold at the concessions stand. Each concession item has a unique ID (concession_id).

Purchase Entity: Tracks purchases made by customers at the concessions stand. Connects customers with the concessions they purchased. Includes attributes like purchase_id, customer_id, concession_id, purchase_date, and quantity.

Reasoning for Relationships:

Customer - Ticket (): A customer can purchase multiple tickets (for different movies or multiple tickets for the same movie), but each ticket is purchased by only one customer.

Customer - Purchase (1
): A customer can make multiple purchases at the concessions stand, but each purchase is made by only one customer.

Ticket - Movie (M:1): Many tickets can be sold for the same movie, but each ticket corresponds to only one movie.

Purchase - Concession (M): A purchase can include multiple concession items, and each concession item can be purchased multiple times by different customers.

2. PostgreSQL Table Creation Scripts
Customers table
CREATE TABLE customers ( customer_id SERIAL PRIMARY KEY, customer_name VARCHAR(100) NOT NULL, email VARCHAR(100) UNIQUE);
Movies table
CREATE TABLE movies (movie_id SERIAL PRIMARY KEY,title VARCHAR(255) NOT NULL,release_date DATE,genre VARCHAR(100));
Tickets table
CREATE TABLE tickets (ticket_id SERIAL PRIMARY KEY, customer_id INT REFERENCES customers(customer_id),
    movie_id INT REFERENCES movies(movie_id),
    purchase_date DATE);
 Concessions table
CREATE TABLE concessions (concession_id SERIAL PRIMARY KEY,item_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL);
 Purchases table
CREATE TABLE purchases (
    purchase_id SERIAL PRIMARY KEY,customer_id INT REFERENCES customers(customer_id),
    concession_id INT REFERENCES concessions(concession_id),
    purchase_date DATE,quantity INT);
3. Sample Data Insertion
-- Inserting sample data into customers table
INSERT INTO customers (customer_name, email) VALUES
    ('Alice Johnson', 'alice@example.com'), ('Bob Smith', 'bob@example.com'), ('Charlie Brown', 'charlie@example.com');
Inserting sample data into movies table
INSERT INTO movies (title, release_date, genre) VALUES
    ('The Matrix', '1999-03-31', 'Sci-Fi'),
    ('Inception', '2010-07-16', 'Sci-Fi'),
    ('The Dark Knight', '2008-07-18', 'Action');
 Inserting sample data into tickets table
INSERT INTO tickets (customer_id, movie_id, purchase_date) VALUES
    (1, 1, '2024-06-24'),
    (2, 2, '2024-06-23'),
    (3, 3, '2024-06-22');
 Inserting sample data into concessions table
INSERT INTO concessions (item_name, price) VALUES
    ('Popcorn', 5.50),
    ('Soda', 3.00),
    ('Candy', 2.75);
 Inserting sample data into purchases table
INSERT INTO purchases (customer_id, concession_id, purchase_date, quantity) VALUES
    (1, 1, '2024-06-24', 2),
    (2, 2, '2024-06-23', 1),
    (3, 3, '2024-06-22', 3);