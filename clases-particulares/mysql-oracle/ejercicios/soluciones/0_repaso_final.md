# REPASO FINAL MYSQL

## Crea una base de datos llamada "petstore" que incluya una tabla "pets" con las siguientes columnas

- id: número entero, clave primaria, autoincrementable
- name: cadena de caracteres, no nula
- species: cadena de caracteres, no nula
- age: número entero, no nulo
- price: número decimal, no nulo

~~~sql
CREATE DATABASE petstore;
USE petstore;

CREATE TABLE pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    species VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    price DECIMAL(6,2) NOT NULL
);
~~~

## Inserta 5 mascotas en la tabla "pets", utilizando el comando INSERT INTO

~~~sql
INSERT INTO pets (name, species, age, price)
VALUES
    ('Luna', 'perro', 3, 70.50),
    ('Firulais', 'perro', 2, 55.75),
    ('Garfield', 'gato', 1, 45.90),
    ('Tom', 'gato', 5, 60.00),
    ('Tweety', 'pájaro', 2, 30.25);
~~~

## Selecciona todas las mascotas que tengan un precio mayor a 50, utilizando el comando SELECT con una cláusula WHERE

~~~sql
SELECT * FROM pets
WHERE price > 50;
~~~

## Selecciona la especie y el promedio de edad de todas las mascotas, agrupadas por especie, utilizando el comando SELECT con la función AVG y la cláusula GROUP BY

~~~sql
SELECT species, AVG(age) AS average_age
FROM pets
GROUP BY species;
~~~

## Selecciona el nombre de las mascotas y su precio, y renombra la columna "price" como "cost", utilizando la cláusula AS

~~~sql
SELECT name, price AS cost
FROM pets;
~~~

## Actualiza el precio de todas las mascotas de la especie "gato" a $70, utilizando el comando UPDATE con la cláusula SET y la cláusula WHERE

~~~sql
UPDATE pets
SET price = 70
WHERE species = 'gato';
~~~

## Agrega una columna llamada "description" a la tabla "pets", que permita una cadena de caracteres de hasta 100 caracteres

~~~sql
ALTER TABLE pets
ADD COLUMN description VARCHAR(100);
~~~

## Inserta una descripción para cada una de las 5 mascotas en la columna "description", utilizando el comando UPDATE con la cláusula SET y la cláusula WHERE

~~~sql
UPDATE pets
SET description = 'Mascota adorable'
WHERE id = 1;

UPDATE pets
SET description = 'Mascota juguetona'
WHERE id = 2;

UPDATE pets
SET description = 'Mascota dormilona'
WHERE id = 3;

UPDATE pets
SET description = 'Mascota curiosa'
WHERE id = 4;

UPDATE pets
SET description = 'Mascota traviesa'
WHERE id = 5;
~~~

## Selecciona el nombre de las mascotas y su precio, junto con el nombre de la tienda en la que se compraron, utilizando una consulta de INNER JOIN entre la tabla "pets" y la tabla "stores"

~~~sql
SELECT pets.name, pets.price, stores.name AS store_name
FROM pets
INNER JOIN stores
ON pets.store_id = stores.id;
~~~

## Selecciona el nombre de las mascotas y su precio, junto con la especie y edad de las mascotas que tienen un precio mayor a 50, utilizando una subconsulta

~~~sql
SELECT name, price, species, age
FROM pets
WHERE price > 50 AND (species, age) IN (
    SELECT species, age
    FROM pets
    WHERE price > 50
);
~~~

## Combina los resultados de dos consultas: la primera selecciona el nombre de las mascotas que son de la especie "perro", y la segunda selecciona el nombre de las mascotas que tienen un precio menor a 40, utilizando el comando UNION

~~~sql
SELECT name
FROM pets
WHERE species = 'perro'
UNION
SELECT name
FROM pets
WHERE price < 40;
~~~

## Selecciona el nombre de las mascotas que no sean de la especie "gato", utilizando el comando EXCEPT

~~~sql
SELECT name
FROM pets
EXCEPT
SELECT name
FROM pets
WHERE species = 'gato';
~~~

## Crea una variable de usuario llamada "discount" y asígnale un valor de 10

~~~sql
SET @discount = 10;
~~~

## Deshabilita el autocommit y comienza una transacción utilizando el comando START TRANSACTION

~~~sql
-- Deshabilita el autocommit
SET autocommit = 0;

-- Comienza la transacción
START TRANSACTION;
~~~

>:warning: acuerdate de que cuando queramos cerrar la transacción y aplicar los cambios tenemos que usar commit

## Actualiza el precio de todas las mascotas en la tabla "pets" multiplicándolo por el valor de la variable de usuario "discount", utilizando el comando UPDATE con la cláusula SET

~~~sql
UPDATE pets
SET price = price * @discount;
~~~

## Crea un punto de guardado llamado "savepoint1" utilizando el comando SAVEPOINT

~~~sql
SAVEPOINT savepoint1;
~~~

## Actualiza el precio de todas las mascotas de la especie "pájaro" a $20, utilizando el comando UPDATE con la cláusula SET y la cláusula WHERE

~~~sql
UPDATE pets
SET price = 20
WHERE species = 'pájaro';
~~~

## Utilizando el comando ROLLBACK TO SAVEPOINT, revierte todos los cambios hechos desde el punto de guardado "savepoint1"

~~~sql
ROLLBACK TO SAVEPOINT savepoint1;
~~~

## Crea una tabla llamada "stores" con las siguientes columnas

- id: número entero, clave primaria, autoincrementable
- name: cadena de caracteres, no nulo
- location: cadena de caracteres, no nula
- phone: cadena de caracteres, no nula

~~~sql
CREATE TABLE stores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL
);
~~~

## Agrega una restricción de clave foránea a la tabla "pets", que haga referencia a la columna "id" de la tabla "stores", utilizando el comando ALTER TABLE y la cláusula ADD CONSTRAINT

~~~sql
ALTER TABLE pets
ADD CONSTRAINT fk_stores_id
FOREIGN KEY (store_id) REFERENCES stores(id);
~~~

## Bloquea la tabla "pets" para que no se puedan hacer cambios en ella, utilizando el comando LOCK TABLES

~~~sql
LOCK TABLES pets WRITE;
~~~

## Selecciona el nombre de todas las mascotas que hay en la tabla "pets", utilizando la tabla bloqueada

~~~sql
SELECT name FROM pets;
~~~

## Cambia el campo 'age' a 10

~~~sql
UPDATE pets
SET age = 10
WHERE id = 2;
~~~

>:warning: **ADVERTENCIA** esta sentencia fallará debido a que la tabla "pets" está bloqueada por la sentencia anterior "LOCK TABLES pets WRITE".

## Desbloquea la tabla "pets", utilizando el comando UNLOCK TABLES

~~~sql
UNLOCK TABLES;
~~~

## Utiliza el comando SET TRANSACTION para establecer el nivel de aislamiento de la transacción actual en "SERIALIZABLE"

~~~sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
~~~

## Elimina la columna "description" de la tabla "pets"

~~~sql
ALTER TABLE pets
DROP COLUMN description;
~~~

## Borra las tablas y la base de datos

~~~sql
DROP TABLE stores;
DROP TABLE pets;
DROP DATABASE petstore;
~~~
