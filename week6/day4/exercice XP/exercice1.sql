-- COUP MONTÉ
-- Téléchargez cettebase de données.
-- Cliquez sur « View raw » pour le télécharger.
-- Restaurez la base de données dans pgadmin.


-- Pour restaurer la base de données ; Suivez ces instructions

-- Accédez à pgAdmin4 et accédez à Bases de données dans le panneau de gauche.
-- Cliquez avec le bouton droit > Créer > base de données.
-- Saisissez le nom de la nouvelle base de données :hr.backup, puis cliquez sur Enregistrer. Attendez quelques instants.
-- Faites un clic droit surhr.backupsous Bases de données dans le panneau de gauche.
-- Cliquez sur Restaurer.
-- À côté de Nom de fichier, vous devriez voir un bouton avec 3 points dessus. Cliquez sur le bouton.
-- Recherchez votre fichier dans la fenêtre (vous devrez peut-être cocher Afficher les fichiers et dossiers cachés), puis cliquez sur le bouton Sélectionner.


-- Si les instructions ci-dessus ne fonctionnent pas

-- Créez votre base de données avec pgAdmin ou le terminal.
-- Téléchargezce référentiel Github.
-- Ouvrez le shell ou le terminal.
-- cd vers le bureau ou à l’emplacement du fichier de base de données.
-- Entrez la commande suivante :oupsql -d hr -f hr.sqlpsql -d hr -f nameOfTheFile.extension


-- 🌟 Instruction De Sélection De Base
-- Écrivez une requête pour afficher les noms (first_name, last_name) à l’aide d’un nom d’alias « First », « Last » de la table employee.

-- Écrivez une requête pour obtenir l’ID de service unique de la table des employés (c’est-à-dire sans doublons).

-- Écrivez une requête pour obtenir les détails de tous les employés à partir de la table employee, faites-le par ordre décroissant par prénom.

-- Écrivez une requête pour obtenir les noms (first_name, last_name), le salaire et 15% du salaire en tant que PF (alias) pour tous les employés.

-- Écrivez une requête pour obtenir les identifiants des employés, les noms (first_name, last_name) et le salaire par ordre croissant en fonction de leur salaire.

-- Écrivez une requête pour obtenir la somme totale de tous les salaires versés aux employés.

-- Écrivez une requête pour obtenir les salaires maximum et minimum versés aux employés.

-- Écrivez une requête pour obtenir le salaire moyen versé aux employés.

-- Écrivez une requête pour obtenir le nombre d’employés travaillant dans l’entreprise.

-- Écrivez une requête pour obtenir tous les prénoms de la table employees en majuscules.

-- Écrivez une requête pour obtenir les trois premiers caractères de chaque prénom de tous les employés de la table employees.

-- Écrivez une requête pour obtenir les noms complets de tous les employés de la table employees. Vous devez inclure le prénom et le nom de famille.

-- Écrivez une requête pour obtenir le prénom, le nom et la longueur du nom complet de tous les employés de la table employees.

-- Écrivez une requête pour vérifier si la colonne first_name de la table employees contient des nombres.

-- Écrivez une requête pour sélectionner les dix premiers enregistrements d’une table.


-- 🌟 Restriction Et Tri
-- Écrivez une requête pour afficher le first_name, le last_name et le salaire de tous les employés dont le salaire se situe entre 10 000 $ et 15 000 $.

-- Écrivez une requête pour afficher le first_name, le last_name et la date d’embauche de tous les employés embauchés en 1987.

-- Écrivez une requête pour obtenir tous les employés dont le first_name a à la fois les lettres « c » et « e ».

-- Écrivez une requête pour afficher le last_name, le travail et le salaire de tous les employés qui ne travaillent pas comme programmeurs ou commis à l’expédition, et qui ne reçoivent pas un salaire égal à 4 500 $, 10 000 $ ou 15 000 $.

-- Écrivez une requête pour afficher les noms de famille de tous les employés dont le nom de famille contient exactement six caractères.

-- Écrivez une requête pour afficher le nom de famille de tous les employés qui ont la lettre « e » comme troisième caractère dans le nom.

-- Écrivez une requête pour afficher le titre des emplois apparaissant dans la table employees.

-- Écrivez une requête pour sélectionner toutes les informations des employés dont le nom de famille est « JONES » ou « BLAKE » ou « SCOTT » ou « KING » ou « FORD ».

--1
select  first_name as first , last_name as last from employees 

--2
select distinct (department_id) from employees

--3
select * from employees  order by  first_name desc

--4
select first_name as first, last_name as last, salary as salaire ,(salary*0,15) as salaire_quart  from employees 

--5
select employee_id ,first_name , last_name  from employees  order by salary asc

--6
select SUM (salary )from employees

--7
select  max(salary ),min (salary)from employees

--8
select avg  (salary )from employees

--9
select count (first_name) from employees

--10
SELECT upper(first_name)   from employees

--11
 select SUBSTRING(first_name for 3) from employees;

--12
select (first_name, last_name) as nom_complet from employees

--13
SELECT first_name, last_name, CHAR_LENGTH(first_name)+CHAR_LENGTH(last_name) as longuer_des_mot_complet FROM employees;

--14
select first_name from employees where first_name ~ '^[0-9]$';

--15 
SELECT * FROM employees LIMIT 10;


