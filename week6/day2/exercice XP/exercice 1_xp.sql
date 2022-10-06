-- Database: public

-- DROP DATABASE IF EXISTS public;

-- CREATE DATABASE public
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'French_France.1252'
--     LC_CTYPE = 'French_France.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- Exercice 1 : Articles Et Clients
-- Instructions
-- Nous allons travailler sur la base de donnees publique que nous avons cree hier.

-- Utilisez SQL pour obtenir les elements suivants a partir de la base de donnees :
-- Tous les articles, classes par prix (du plus bas au plus eleve).
-- Articles dont le prix est superieur a 80 (80 inclus), commandes par prix (du plus eleve au plus bas).
-- Les 3 premiers clients dans l ordre alphabetique du prenom (A-Z) – excluent la colonne de cle primaire des resultats.
-- Tous les noms de famille (pas d autres colonnes!), dans l ordre alphabetique inverse (Z-A)


SELECT * FROM items GROUP BY items_id ORDER BY prix ASC
SELECT * FROM items  WHERE prix >80 GROUP BY items_id ORDER BY prix DESC
SELECT * FROM customers   ORDER BY customers_id ASC LIMIT 3
SELECT last_name FROM CUSTOMERS ORDER BY last_name DESC





-- Exercice 2 : Base De Données Dvdrental
-- Instructions
-- Coup Monté
-- Nous allons installer un nouvel exemple de base de données sur nos serveurs PostgreSQL.
-- Télécharger cet exemple de fichier de base de données

-- Il y a un seul fichier appelé dvdrental.tar à l’intérieur du zip. Extrayez-le dans votre répertoire local.
-- Astuce : Si vous utilisez Mac, après avoir extrait le fichier zip, vous obtiendrez un dossier appelé dvdrental

-- Accédez à pgAdmin4 et accédez à Bases de données dans le panneau de gauche.

-- Cliquez avec le bouton droit de la souris > Créer une base de données >...

-- Tapez le nom de la nouvelle base de données : dvdrental, puis cliquez sur Enregistrer. Attendez quelques instants.

-- Faites un clic droit sur dvdrental sous Bases de données dans le panneau de gauche.

-- Cliquez sur Restaurer....

-- Pour les utilisateurs de PC, choisissez le format suivant Personnalisé ou goudron. Pour les utilisateurs Mac, choisissez le format suivant Répertoire.

-- À côté de Nom de fichier, vous devriez voir un bouton avec 3 points dessus. Cliquez sur le bouton.

-- Pour les utilisateurs de PC : « Trouvez votre fichier dans la fenêtre ». Pour les utilisateurs Max : « Trouvez votre dossier dans la fenêtre ». (vous devrez peut-être cocher Afficher les fichiers et dossiers cachés ?), puis cliquez sur le bouton Sélectionner.

-- Si vous recevez une erreur « Utilitaire introuvable », vous devez modifier le chemin binaire pgadmin. Regardez cette vidéo

-- Si vous voyez des messages d’erreur, enregistrez-les et obtenez de l’aide. Sinon, vous devriez avoir une nouvelle base de données chargée sur votre serveur!

-- Voici un diagramme des tables du serveur. Jetez-y un coup d’œil et découvrez les tables, leurs colonnes et les relations entre les différentes tables.
-- Si vous rencontrez un problème lors de l’importation de la base de données, voici les instructions DEFAULT
--     Nous utiliserons la base de données dvdrental nouvellement installée.

-- Dans la base de données dvdrental, écrivez une requête pour sélectionner toutes les colonnes de la table « customer ».

-- Écrivez une requête pour afficher les noms (first_name, last_name) à l’aide d’un alias nommé « full_name ».

-- Permet d’obtenir toutes les dates auxquelles les comptes ont été créés. Écrivez une requête pour sélectionner tous les create_date dans la table « customer » (il ne doit pas y avoir de doublons).

-- Écrivez une requête pour obtenir tous les détails du client à partir de la table client, elle doit être affichée dans l’ordre décroissant par leur prénom.

-- Écrivez une requête pour obtenir l’ID du film, le titre, la description, l’année de sortie et le taux de location dans l’ordre croissant en fonction de leur taux de location.

-- Écrivez une requête pour obtenir l’adresse, et le numéro de téléphone de tous les clients vivant dans le district du Texas, ces détails peuvent être trouvés dans le tableau « adresse ».

-- Écrivez une requête pour récupérer tous les détails du film dont l’ID de film est 15 ou 150.

-- Écrivez une requête qui devrait vérifier si votre film préféré existe dans la base de données. Demandez à votre requête d’obtenir l’ID du film, le titre, la description, la durée et le taux de location, ces détails peuvent être trouvés dans le tableau « film ».

-- Pas de chance de trouver votre film? Peut-être avez-vous fait une erreur d’orthographe du nom. Écrivez une requête pour obtenir l’ID du film, le titre, la description, la durée et le taux de location de tous les films en commençant par les deux premières lettres de votre film préféré.

-- Écrivez une requête qui trouvera les 10 films les moins chers.

-- Non satisfait des résultats. Écrivez une requête qui trouvera les 10 prochains films les moins chers.
-- Bonus : Essayez de ne pas utiliser LIMIT.

-- Écrivez une requête qui joindra les données de la table client et de la table de paiement. Vous souhaitez obtenir le montant et la date de chaque paiement effectué par un client, commandés par son identifiant (de 1 à...).

-- Vous devez vérifier votre inventaire. Écrivez une requête pour obtenir tous les films qui ne sont pas en inventaire.

-- Écrivez une requête pour savoir quelle ville se trouve dans quel pays.

-- Bonus Vous voulez être en mesure de voir comment vos vendeurs se sont comportés? Écrivez une requête pour obtenir l’identifiant du client, les noms (premier et dernier), le montant et la date de paiement ordonnés par l’identifiant du membre du personnel qui lui a vendu le dvd.


SELECT * FROM customer full_name
SELECT (first_name,last_name) as full_name FROM customer
SELECT DISTINCT  (create_date) FROM customer
SELECT * FROM customer ORDER BY first_name DESC
SELECT film_id,title,description,release_year,replacement_cost FROM film ORDER BY replacement_cost ASC
select address,phone,district from address  where district ='Texas';
SELECT * FROM film WHERE film_id=15 OR film_id=150
SELECT film_id,title,description,length,replacement_cost FROM film WHERE title = 'Agent Truman'
SELECT film_id,title,description,length,replacement_cost FROM film  WHERE title LIKE 'Ad%'
select title, replacement_cost from film order by replacement_cost limit 10;

    SELECT (first_name,last_name) as nom_prenom_de_customer, payment.amount, payment.payment_date FROM public.customer INNER JOIN public.payment ON customer.customer_id = payment.customer_id order by payment.customer_id
    --voila la formule utilise:      SELECT * FROM A INNER JOIN B ON A.key = B.key
select title,description  from public.film INNER JOIN public.inventory ON film.film_id = inventory.inventory_id

    SELECT title FROM public.film
    WHERE EXISTS (
    SELECT *
    FROM public.inventory
    WHERE inventory.inventory_id=film.film_id
  )
  -- voila la formule: SELECT nom_colonne1 FROM `table1` WHERE EXISTS (SELECT nom_colonne2 FROM `table2` WHERE nom_colonne3 = 10 )

 select city, country.country from city INNER JOIN country ON city.city_id=country.country_id 
 
SELECT (customer.first_name, customer.last_name) as nom_et_prenom, payment.amount, (staff.first_name, staff.last_name) as les_vendeurs FROM customer, payment, staff WHERE EXISTS (
SELECT * FROM payment, staff WHERE customer.customer_id = payment.customer_id and staff.staff_id = payment.staff_id
)


