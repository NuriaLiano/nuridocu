---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# REPASO FINAL MYSQL

subconsultas, 
add constraint, 
add foreign key, 
drop colum, 
update set,  
create table, 
create database, 
insert into, 
autoincremment, 
<!-- union, 
intersect, 
except,  -->
as, 
group by, 
having, 
count, 
concat, 
<!-- variables locales y globales, 
lock y unclock tables,
set transactino, -->
autocommit = 0,  
save point, 
rollback to savepoint 
y commit  
con tematica de juegos de gran theft auto

## Crea una base de datos llamada "petstore" que incluya una tabla "pets" con las siguientes columnas

    id: número entero, clave primaria, autoincrementable
    name: cadena de caracteres, no nula
    species: cadena de caracteres, no nula
    age: número entero, no nulo
    price: número decimal, no nulo

sql

CREATE DATABASE petstore;
USE petstore;

CREATE TABLE pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    species VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    price DECIMAL(6,2) NOT NULL,
);

    En la tabla pets hay un error de sintaxis en la última línea, se ha incluido una coma de más después de la última columna, lo que provoca un error al ejecutar la consulta.

Inserta 5 mascotas en la tabla "pets", utilizando el comando INSERT INTO

sql

INSERT INTO pets (name, species, age, price)
VALUES
    ('Luna', 'perro', 3, 70.50),
    ('Firulais', 'perro', 2, 55.75),
    ('Garfield', 'gato', 1, 45.90),
    ('Tom', 'gato', 5, 60.00),
    ('Tweety', 'pájaro', 2, 30.25;

    En la última línea del comando INSERT INTO falta cerrar el paréntesis que abre después de 30.25. Esto provoca un error al ejecutar la consulta.

Selecciona todas las mascotas que tengan un precio mayor a 50, utilizando el comando SELECT con una cláusula WHERE

sql

SELECT * FROM pets
WHERE price > 50;

    Esta consulta está bien formulada y no tiene errores.

Selecciona la especie y el promedio de edad de todas las mascotas, agrupadas por especie, utilizando el comando SELECT con la función AVG y la cláusula GROUP BY

sql

SELECT species, AVG(age) AS average_age
FROM pets
GROUP BY name;

    En la cláusula GROUP BY se está agrupando por la columna name, en lugar de la columna species. Esto provocará un error al ejecutar la consulta.

Selecciona el nombre de las mascotas y su precio, y renombra la columna "price" como "cost", utilizando la cláusula AS

sql

SELECT name, price AS cost
FORM pets;

    En la segunda línea, la palabra FORM está mal escrita, debería ser FROM. Esto provocará un error al ejecutar la consulta.

Actualiza el precio de todas las mascotas de la especie "gato" a $70, utilizando el comando UPDATE con la cláusula SET y la cláusula WHERE

sql

UPDATE pets
SET price = 70
WHERE species = 'gato';

    Esta consulta está bien formulada y no tiene errores.

Agrega una columna llamada "description" a la tabla "pets", que permita una cadena de caracteres de hasta 100 caracteres

sql

ALTER TABLE pets
ADD COLUMN description VARCHAR(100);

    Esta consulta está bien