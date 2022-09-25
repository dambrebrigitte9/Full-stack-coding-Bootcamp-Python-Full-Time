 Database: bootcamp

--  DROP DATABASE IF EXISTS bootcamp;

--  CREATE DATABASE bootcamp
--      WITH
--      OWNER = postgres
--      ENCODING = 'UTF8'
--      LC_COLLATE = 'French_France.1252'
--      LC_CTYPE = 'French_France.1252'
--      TABLESPACE = pg_default
--      CONNECTION LIMIT = -1
--      IS_TEMPLATE = False;

 CREATE TABLE etudiant(
 	etudiant_id SERIAL PRIMARY KEY,
 	first_name VARCHAR(50) NOT NULL,
 	last_name VARCHAR(100) NOT NULL,
 	birth_date DATE NOT NULL
 )
 SELECT * FROM etudiant
 INSERT INTO etudiant(first_name,last_name,birth_date)
 VALUES('Marc','Benichou','02/11/1998');
 INSERT INTO etudiant(first_name,last_name,birth_date)
 VALUES('Yoan','Cohen','03/12/2010');
 INSERT INTO etudiant(first_name,last_name,birth_date)
 VALUES('Lea','Benichou','27/07/1987');
 INSERT INTO etudiant(first_name,last_name,birth_date)
 VALUES('Amelia','Dux','07/04/1996');
 INSERT INTO etudiant(first_name,last_name,birth_date)
 VALUES('David','Grez','14/06/2003');
 INSERT INTO etudiant(first_name,last_name,birth_date)
 VALUES('Omer','Simpson','03/10/1980');
 SELECT * FROM etudiant
 SELECT first_name,last_name FROM etudiant
 SELECT * FROM etudiant WHERE etudiant_id=2
 SELECT * FROM etudiant WHERE first_name='Marc' AND last_name='Benichou'
 SELECT * FROM etudiant WHERE last_name='Benichou' OR first_name='Marc'
 SELECT * FROM etudiant WHERE first_name LIKE '%a%'
 SELECT * FROM etudiant WHERE first_name LIKE 'a%'
 SELECT * FROM etudiant WHERE first_name LIKE '%a'
 SELECT * FROM etudiant WHERE etudiant_id =1 OR etudiant_id =3
 SELECT * FROM etudiant WHERE birth_date >' 1/01/2000' 