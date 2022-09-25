CREATE TABLE items(
    items_id SERIAL PRIMARY KEY,
    liste_des_outils VARCHAR(100) NOT NULL,
    prix DECIMAL NOT NULL
)
SELECT* FROM items
INSERT INTO actors (liste_des_outils, prix)
VALUES('Petit bureau','100');
INSERT INTO actors (liste_des_outils, prix)
VALUES('Grand bureau','300');
INSERT INTO actors (liste_des_outils, prix)
VALUES('Ventilateur','80');

CREATE TABLE customers(
    customers_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL
)
SELECT* FROM customers
INSERT INTO customers(first_name,last_name)
VALUES('Greg','Jones');
INSERT INTO customers(first_name,last_name)
VALUES('Sandra','Jones');
INSERT INTO customers(first_name,last_name)
VALUES('Scott','Scott');
INSERT INTO customers(first_name,last_name)
VALUES('Trevor','Vert');
INSERT INTO customers(first_name,last_name)
VALUES('Melanie','Johnson');

SELECT * FROM items
SELECT * FROM items WHERE prix>80
SELECT * FROM items WHERE prix<300

SELECT * FROM customers
SELECT * FROM customers WHERE first_name ='Smith'
  --il n'affiche rien car Smith n'existe pas--
SELECT * FROM customers WHERE first_name ='Jones'
  --il n'affiche rien car Jones n'existe pas dans la list de nom de famille--
SELECT * FROM customers WHERE last_name ='Scott'


