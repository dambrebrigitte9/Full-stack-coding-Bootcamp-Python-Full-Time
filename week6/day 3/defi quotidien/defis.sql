-- Partie I

-- Créez 2 tableaux : Profil Client et Profil Client. Ils ont une relation un-à-un.

-- Un client ne peut avoir qu’un seul profil, et un profil appartient à un seul client
-- La table Customer doit comporter les colonnes : , , idfirst_namelast_name NOT NULL
-- La table de profil Customer doit comporter les colonnes : , (un booléen), (une référence à la table Customer)idisLoggedIn DEFAULT falsecustomer_id

-- Insérer ces clients

-- John, biche
-- Jérôme, Lalu
-- Léa, Rive

-- Insérer ces profils client, utiliser des sous-requêtes

-- John est connecté
-- Jérôme n’est pas connecté

-- Utilisez les types de jointures appropriés pour afficher :

-- La first_name des clients LoggedIn
-- Tous les clients first_name et les colonnes isLoggedIn - même les clients qui n’ont pas de profil.
-- Le nombre de clients qui ne sont pas connectés


-- Partie II :

-- Créez une table nommée Book, avec les colonnes : , , book_id SERIAL PRIMARY KEYtitle NOT NULLauthor NOT NULL

-- Insérez ces livres :
-- Alice au pays des merveilles, Lewis Carroll
-- Harry Potter, J.K Rowling
-- Pour tuer un oiseau moqueur, Harper Lee

-- Créez une table nommée Student, avec les colonnes : , , . Assurez-vous que l’âge n’est jamais supérieur à 15 ans (Trouver une méthode SQL) ;student_id SERIAL PRIMARY KEYname NOT NULL UNIQUEage

-- Insérez ces étudiants :
-- Jean, 12 ans
-- Lera, 11 ans
-- Patrick, 10 ans
-- Bob, 14 ans

-- Créez une table nommée Library, avec les colonnes :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
-- Cette table, est une table de jonction pour une relation Plusieurs à Plusieurs avec les tables Livre et Étudiant : Un étudiant peut emprunter de nombreux livres, et un livre peut être emprunté par de nombreux enfants
-- book_fk_id est une clé étrangère représentant la colonne de la table Livrebook_id
-- student_fk_id est une clé étrangère représentant la colonne de la table Studentstudent_id
-- La paire de clés étrangères est la clé primaire de la table de jonction

-- Ajoutez 4 enregistrements dans la table de jonction, utilisez des sous-requêtes.
-- l’étudiant nommé John, a emprunté le livre Alice au pays des merveilles le 15/02/2022
-- l’étudiant nommé Bob, a emprunté le livre Pour tuer un oiseau moqueur le 03/03/2021
-- l’étudiante nommée Lera, a emprunté le livre Alice au pays des merveilles le 23/05/2021
-- l’étudiant nommé Bob, a emprunté le livre Harry Potter le 12/08/2021

-- Afficher les données
-- Sélectionnez toutes les colonnes de la table de jonction
-- Sélectionnez le nom de l’élève et le titre des livres empruntés
-- Sélectionnez l’âge moyen des enfants qui ont emprunté le livre Alice au pays des merveilles
-- Supprimer un élève de la table Étudiant, que s’est-il passé dans la table de jonction ?

CREATE TABLE client(
     client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL
	
    
);
CREATE TABLE profil_Client(
    profil_Client_id SERIAL PRIMARY KEY,
    isLoggedIn  BOOLEAN DEFAULT false,
	FOREIGN KEY(profil_Client_id) REFERENCES client( client_id) ON DELETE CASCADE
    
);
INSERT INTO client(first_name,last_name)
 VALUES('John','biche'),
 		('Jérôme','Lalu'),
 		('Léa', 'Rive');

INSERT into profil_Client(profil_Client_id,isLoggedIn) VALUES 
((SELECT client_id FROM client where first_name = 'John'),(true)),
((SELECT client_id FROM client where first_name = 'Jérôme'),(false))

SELECT client.first_name
FROM client
FULL OUTER JOIN profil_Client
ON client.client_id =profil_Client.profil_Client_id;

SELECT client.first_name
FROM client
FULL OUTER JOIN profil_Client
ON client.client_id =profil_Client.profil_Client_id where profil_client.isLoggedIn=false;

--partie 2
CREATE TABLE books(
    books_id SERIAL PRIMARY KEY,
    title  VARCHAR(50) NOT NULL,
	author VARCHAR(50) NOT NULL
	
    
);

INSERT INTO books(title,author)
VALUES('Alice au pays des merveilles', 'Lewis Carroll'),
	  ('Harry Potter', 'J.K Rowling'),
	  ('Pour tuer un oiseau moqueur', 'Harper Lee');


CREATE TABLE Student(
     Student_id SERIAL PRIMARY KEY,
     name  VARCHAR(50) NOT NULL UNIQUE,
	   age DECIMAL NOT NULL CONSTRAINT age_contrainte CHECK(age<=15) 
 );

 INSERT INTO Student(name,age)
 VALUES('Jean', '12 '),
 		('Lera', '11'),
 		('Patrick', '10' ),
		('Bob', '14');


CREATE TABLE library(
    Student_id SERIAL,
    books_id INTEGER NOT NULL,
    borrowed_date date NOT NULL,
    PRIMARY KEY (books_id),
    FOREIGN KEY (Student_id) REFERENCES Student(Student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (books_id) REFERENCES books(books_id) ON DELETE CASCADE ON UPDATE CASCADE
 );


INSERT into library (Student_id,books_id, borrowed_date ) VALUES 
((SELECT Student_id FROM Student where name = 'John'),
 (SELECT books_id FROM books WHERE title='Alice au pays des merveilles'),'15/02/2022'),
 
 ((SELECT Student_id FROM Student WHERE name = 'Bob'),
 (SELECT books_id FROM books WHERE title=' Pour tuer un oiseau moqueur '),'03/03/2021'),
 
 ((SELECT Student_id FROM Student WHERE name = 'Lera'),
 (SELECT books_id FROM books WHERE title='Alice au pays des merveilles'),'23/05/2021'),
 
 ((SELECT Student_id FROM Student WHERE name = 'Bob'),
 (SELECT books_id FROM books WHERE title='Harry Potter'),'12/08/2021');
 

 SELECT * FROM library;