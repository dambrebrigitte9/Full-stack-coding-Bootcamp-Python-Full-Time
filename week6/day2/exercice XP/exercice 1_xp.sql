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