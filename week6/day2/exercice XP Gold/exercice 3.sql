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
CREATE TABLE achats(
 	achat_id SERIAL PRIMARY KEY,
	customers_id DECIMAL NOT NULL,
	items_id DECIMAL NOT NULL,
 	quantity_purchased DECIMAL NOT NULL
 )