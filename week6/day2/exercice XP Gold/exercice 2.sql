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
 
    SELECT * FROM etudiant   ORDER BY etudiant_id ASC
   SELECT * FROM etudiant
 UPDATE etudiant
 SET birth_date='02/11/1998'
 WHERE etudiant_id=1 AND etudiant_id=3
 UPDATE etudiant
 SET last_name='Guez'
 WHERE etudiant_id=5
  DELETE FROM etudiant WHERE etudiant_id=3
 SELECT COUNT (*) FROM etudiant WHERE birth_date >'1/01/2000'
 ALTER TABLE etudiant ADD COLUMN math_grade DECIMAL ;
 UPDATE etudiant
 SET math_grade='80'
 WHERE etudiant_id=1;
 UPDATE etudiant
 SET math_grade='90'
 WHERE etudiant_id=2 OR etudiant_id=4;
 UPDATE etudiant
 SET math_grade='40'
 WHERE etudiant_id=6
 SELECT COUNT (*) FROM etudiant WHERE math_grade>'83'
 INSERT INTO etudiant(first_name,last_name,birth_date,math_grade)
  VALUES('Omer','Simpson','03/10/1980','70');

 SELECT first_name,last_name , COUNT(*)  AS total_grade FROM etudiant GROUP BY first_name,last_name ;
 SELECT SUM( math_grade ) AS totalmoyenne FROM etudiant 
                    --   SELECT MAX( math_grade ) AS max FROM etudianT permet de calculer la note la plus elevee
                    --   SELECT AVG( math_grade ) AS moyenneclasse FROM etudiant permet de calculer la moyenne de la classe