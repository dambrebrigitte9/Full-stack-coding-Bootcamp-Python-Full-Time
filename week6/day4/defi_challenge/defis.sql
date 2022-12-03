-- Instructions
-- Créez une table appelée et une table appelée. Vous décidez quels champs doivent figurer dans chaque table, mais assurez-vous que la table comporte une colonne appelée price.product_ordersitemsitems

-- Il devrait y avoir une relation un à plusieurs entre la table et la table. Une commande peut avoir plusieurs articles, mais un article ne peut appartenir qu’à une seule commande.product_ordersitems

-- Créez une fonction qui renvoie le prix total pour une commande donnée.

-- Bonus :
-- Créez une table appelée.users
-- Il devrait y avoir une relation un à plusieurs entre la table et la table.usersproduct_orders
-- Créez une fonction qui renvoie le prix total pour une commande donnée d’un utilisateur donné.


CREATE TABLE items(
     items_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL ,
	price numeric not null
	
    
);


CREATE TABLE product_orders(
     product_orders_id SERIAL PRIMARY KEY,
	items_id INTEGER NOT NULL,
    first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL ,
	 FOREIGN KEY (product_orders_id) REFERENCES items(items_id) ON DELETE CASCADE ON UPDATE CASCADE

);

CREATE TABLE users(
     users_id SERIAL PRIMARY KEY,
	 product_orders_id INTEGER NOT NULL,
    first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL ,
	 FOREIGN KEY (users_id) REFERENCES product_orders(product_orders_id) ON DELETE CASCADE ON UPDATE CASCADE

);