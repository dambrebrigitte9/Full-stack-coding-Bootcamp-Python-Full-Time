-- Exercice 1 : Location De DVD
-- Instructions
-- Obtenez une liste de toutes les langues du film.

-- Obtenez une liste de tous les films joints avec leurs langues - sélectionnez les détails suivants : titre du film, description et nom de la langue. Essayez votre requête avec différentes jointures :
-- Obtenez tous les films, même s’ils n’ont pas de langues.
-- Obtenez toutes les langues, même s’il n’y a pas de films dans ces langues.

-- Créez une nouvelle table appelée new_film avec les colonnes suivantes : id, name. Ajoutez de nouveaux films à la table.

-- Créez un nouveau tableau appelé customer_review, qui contiendra les critiques de films que les clients feront.
-- Pensez à la contrainte DELETE : si un film est supprimé, sa critique doit être automatiquement supprimée.
-- Il doit comporter les colonnes suivantes :
-- review_id – une clé primaire, non null, incrémentation automatique.
-- film_id – fait référence au tableau new_film. Le film qui est en cours de révision.
-- language_id – fait référence à la table des langues. Dans quelle langue se trouve l’examen.
-- title – le titre de la revue.
-- score – la note de l’avis (1-10).
-- review_text – le texte de la revue. Aucune limite de longueur.
-- last_update – date de la dernière mise à jour de l’avis.

-- Ajoutez 2 critiques de films. Assurez-vous de les lier à des objets valides dans les autres tables.

-- Supprimer un film qui a une critique du tableau new_film, qu’advient-il du tableau customer_review ?

SELECT * FROM public.language
select title,description,language.name from film INNER JOIN language ON film.film_id =language.language_id

CREATE TABLE new_film(
     new_film_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
    
)

INSERT INTO new_film(name)
VALUES
('Attaque de titant'),
('trois femme un village'),
('le griot du village'),
('Terresa');

CREATE TABLE customer_review(
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER NOT NULL,
	language_id INTEGER NOT NULL,
	title VARCHAR(50) NOT NULL,
    score DECIMAL NOT NULL,
	review_text TEXT NOT NULL,
	last_update DECIMAL NOT NULL,
	FOREIGN KEY (review_id) REFERENCES new_film(new_film_id) ON DELETE CASCADE
);      -- formule de usage de FOREIGN : FOREIGN KEY(parent_id) REFERENCES parent_table(parent_id) ON DELETE CASCADE

insert into customer_review(film_id, language_id, titre, note, review_text, last_update) VALUES(1, 1, 'film pas bon', 2, 'texte de revue', '23-08-2022'), (1, 1, 'film pas bon', 2, 'texte de revue', '23-08-2022'),(1, 1, 'film pas bon', 2, 'texte de revue', '23-08-2022'),(1, 1, 'film pas bon', 2, 'texte de revue', '23-08-2022')
delete from new_film where name='le griot du village'
