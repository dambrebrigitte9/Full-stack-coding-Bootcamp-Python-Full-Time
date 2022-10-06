 Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

-- CREATE DATABASE bootcamp
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'French_France.1252'
--     LC_CTYPE = 'French_France.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- Exercice 1 : Bootcamp
-- Instructions
-- Poursuite de l’exercice XP

-- Choisir
-- Pour les questions suivantes, vous devez récupérer les first_names, les last_names et les birth_dates des étudiants.

-- Allez chercher les quatre premiers élèves. Vous devez classer les quatre étudiants par ordre alphabétique par last_name.
-- Récupérez les détails du plus jeune élève.
-- Aller chercher trois étudiants en sautant les deux premiers étudiants.



SELECT first_name,last_name,birth_date FROM etudiant
SELECT first_name,last_name,birth_date FROM etudiant LIMIT 4
SELECT * FROM etudiant  ORDER BY last_name ASC LIMIT 4
SELECT first_name,last_name,birth_date FROM etudiant WHERE birth_date ='2010-12-03'
SELECT first_name,last_name,birth_date FROM etudiant limit 3 OFFSET 2
