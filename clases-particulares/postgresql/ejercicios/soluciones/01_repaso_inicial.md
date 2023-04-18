---
autor: @nurialiano
licence: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---

# Repaso Inicial de nivel

## 1. Crear la base de datos 'videojuegos'

~~~sql
CREATE DATABASE videojuegos;
~~~

**CONECTARSE A LA BASE DE DATOS**

~~~sql
\c videojuegos
~~~

## 2. Crear tabla 'juegos' con los siguientes campos

- id SERIAL PRIMARY KEY,
- titulo VARCHAR(100) NOT NULL,
- plataforma VARCHAR (50) NOT NULL,
- lanzamiento DATE NOT NULL,
- desarrollador VARCHAR (100),
- rating FLOAT

~~~sql
CREATE TABLE juegos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    plataforma VARCHAR(50) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    lanzamiento DATE NOT NULL,
    desarrollador VARCHAR(100),
    rating FLOAT (2)
);
~~~

## 3. Insertar datos

- ('The Legend of Zelda: Breath of the Wild', 'Nintendo Switch', 'Acción-aventura', '2017-03-03', 'Nintendo EPD', 4.9),
- ('Super Mario Odyssey', 'Nintendo Switch', 'Plataformas', '2017-10-27', 'Nintendo EPD', 4.8),
- ('God of War', 'PlayStation 4', 'Acción-aventura', '2018-04-20', 'SIE Santa Monica Studio', 4.7),
- ('The Last of Us Part II', 'PlayStation 4', 'Acción-aventura', '2020-06-19', 'Naughty Dog', 4.6),
- ('Red Dead Redemption 2', 'PlayStation 4', 'Acción-aventura', '2018-10-26', 'Rockstar Studios', 4.5),
- ('Dark Souls III', 'PlayStation 4', 'Acción-RPG', '2016-04-12', 'FromSoftware', 4.4),
- ('Hades', 'PC', 'Roguelike', '2020-09-17', 'Supergiant Games', 4.9);

~~~sql
INSERT INTO juegos (titulo, plataforma, genero, lanzamiento, desarrollador, rating)
VALUES
    ('The Legend of Zelda: Breath of the Wild', 'Nintendo Switch', 'Acción-aventura', '2017-03-03', 'Nintendo EPD', 4.9),
    ('Super Mario Odyssey', 'Nintendo Switch', 'Plataformas', '2017-10-27', 'Nintendo EPD', 4.8),
    ('God of War', 'PlayStation 4', 'Acción-aventura', '2018-04-20', 'SIE Santa Monica Studio', 4.7),
    ('The Last of Us Part II', 'PlayStation 4', 'Acción-aventura', '2020-06-19', 'Naughty Dog', 4.6),
    ('Red Dead Redemption 2', 'PlayStation 4', 'Acción-aventura', '2018-10-26', 'Rockstar Studios', 4.5),
    ('Dark Souls III', 'PlayStation 4', 'Acción-RPG', '2016-04-12', 'FromSoftware', 4.4),
    ('Hades', 'PC', 'Roguelike', '2020-09-17', 'Supergiant Games', 4.9);
~~~

## 4. Añade una nueva columna llamada "precio" a la tabla "juegos" con el tipo de datos 'DECIMAL(10,2)'

~~~sql
ALTER TABLE juegos ADD COLUMN precio DECIMAL(10,2);
~~~

## 5. Crea una nueva tabla llamada "plataformas" con los siguientes campos

- id
- nombre
- fabricante

~~~sql
CREATE TABLE plataformas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    fabricante VARCHAR(100)
);
~~~

## 6. Inserta algunos datos en la tabla 'plataformas'

~~~sql
INSERT INTO plataformas (nombre, fabricante)
VALUES
    ('Nintendo Switch', 'Nintendo'),
    ('PlayStation 4', 'Sony Interactive Entertainment'),
    ('PC', NULL);
~~~

## 7. Añade una nueva columna llamada 'plataforma_id' a la tabla de 'juegos' con el tipo de datos 'int'

~~~sql
ALTER TABLE juegos ADD COLUMN plataforma_id INT;
~~~

## 8. Actualiza la columna 'plataforma_id' con el id correspondiente de la tabla 'plataformas'

~~~sql
UPDATE juegos
SET plataforma_id = plataformas.id
FROM plataformas
WHERE juegos.plataforma = plataformas.nombre;

-- o con add constraint
ALTER TABLE juegos ADD CONSTRAINT fk_plataforma_id FOREIGN KEY (plataforma_id) REFERENCES plataformas (id);
~~~

>:pencil:**NOTA** como ver el nombre de la restriccion
> 

## 9. Cambia el campo 'rating' para que permita valores negativos

~~~sql
--opcion 1
ALTER TABLE juegos ALTER COLUMN rating TYPE FLOAT(2);
-- opcion 2
ALTER TABLE juegos DROP CONSTRAINT IF EXISTS juegos_rating_check;
ALTER TABLE juegos ADD CONSTRAINT juegos_rating_check CHECK (rating >= -5.0 AND rating <= 5.0);
~~~

## 10. Añade la clave foráea para crear la relación entre las tablas

~~~sql
ALTER TABLE juegos 
ADD CONSTRAINT fk_plataforma 
FOREIGN KEY (plataforma_id) 
REFERENCES plataformas (id);
~~~

## 11. Seleccionar todos los juegos con un rating mayor o igual a 4.5

~~~sql
SELECT *
FROM juegos
WHERE rating >= 4.5;
~~~

## 12. Seleccionar todos los titulos de juegos que se lanzaron antes de 2019

~~~sql
SELECT titulo
FROM juegos
WHERE lanzamiento < '2019-01-01';

SELECT titulo
FROM juegos
WHERE extract(year from lanzamiento) < 2019;
~~~

## 13. Seleccionar el promedio de rating de os juegos lanzados en Playstation 4

~~~sql
SELECT AVG(rating)
FROM juegos
WHERE plataforma = 'PlayStation 4';
~~~

## 14. Seleccionar el número de juegos por plataforma, solo incluyendo plataformas con  más de un juego

~~~sql
SELECT plataforma, COUNT(*) AS num_juegos
FROM juegos
GROUP BY plataforma
HAVING COUNT(*) > 1;
~~~

## 15. Seleccionar el desarrollador y el promedio de rating de los juegos que tienen un rating mayor o igula a 4.5, ordenados por rating promedio de forma descendente

~~~sql
SELECT desarrollador, AVG(rating) AS promedio_rating
FROM juegos
WHERE rating >= 4.5
GROUP BY desarrollador
ORDER BY promedio_rating DESC;
~~~

## 16. Selecciona los títulos de los juegos que se lanzaron en 2018 o después, limitado a 3 resultados

~~~sql
SELECT titulo
FROM juegos
WHERE lanzamiento >= '2018-01-01'
LIMIT 3;
~~~

## 17. Exportar los datos de la tabla 'juegos' a un archivo CSV sen el directorio 'home' del usuario actual

~~~sql
COPY juegos TO '/home/john/juegos.csv' DELIMITER ',' CSV HEADER;
~~~

## 18. Seleccionar todos los juegos junto con el nombre de la plataforma

~~~sql
SELECT juegos.*, plataformas.nombre AS nombre_plataforma
FROM juegos
JOIN plataformas ON juegos.plataforma = plataformas.nombre;
~~~

## 19. Seleccionar los nombres de los desarrolladores y la cantidad de juegos que han creado solo incluyendo desarrolladores con más de un juego

~~~sql
SELECT juegos.desarrollador, COUNT(*) AS num_juegos
FROM juegos
GROUP BY juegos.desarrollador
HAVING COUNT(*) > 1;
~~~

## 20. Seleccionar los títulos de los juegos lanzados por Playstation 4 que tienen un ratin mayor o igual a la media de rating de todos los juegos

~~~sql
SELECT juegos.titulo
FROM juegos
JOIN (
    SELECT AVG(rating) AS avg_rating, plataforma
    FROM juegos
    GROUP BY plataforma
) AS avg_rating_plataforma ON juegos.plataforma = avg_rating_plataforma.plataforma
WHERE juegos.plataforma = 'PlayStation 4' AND juegos.rating >= avg_rating_plataforma.avg_rating;
~~~

## 21. Seleccionar los nombres de las plataformas que tienen al menos un juego con un rating mayor o igual a 4.8 y lo snombres de los desarrolladores que han creado ese juego

~~~sql
SELECT DISTINCT plataformas.nombre, juegos.desarrollador
FROM juegos
JOIN plataformas ON juegos.plataforma = plataformas.nombre
WHERE juegos.rating >= 4.8;
~~~

## 22. Seleccionar los títulos de los juegos que se lanzaron en Playstation 4 y los titulos que se lanzaron en Nintendo Switch pero no en PC

~~~sql
(SELECT titulo FROM juegos WHERE plataforma = 'PlayStation 4')
UNION
(SELECT titulo FROM juegos WHERE plataforma = 'Nintendo Switch')
EXCEPT
(SELECT titulo FROM juegos WHERE plataforma = 'PC');
~~~

## 23. Inserta los juegos lanzados después del 2018 en una tabla llamada 'juegos_mas_nuevos' siguiendo la misma estructura de la tabla 'juegos'

~~~sql
-- Crear la tabla juegos_mas_nuevos
CREATE TABLE juegos_mas_nuevos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    plataforma VARCHAR(50) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    lanzamiento DATE NOT NULL,
    desarrollador VARCHAR(100),
    rating FLOAT (2)
);
-- Insertar los datos utilizando una subconsulta
INSERT INTO juegos_mas_nuevos (titulo, plataforma, genero, lanzamiento, desarrollador, rating)
SELECT titulo, plataforma, genero, lanzamiento, desarrollador, rating
FROM juegos
WHERE lanzamiento > '2018-01-01';
~~~

>:warning: **ADVERTENCIA** es importante tener en cuenta que la subconsulta debe seleccionar las mismas columnas y en el mismo orden que la tabla de destino (juegos_mas_nuevos en este caso) para que los datos se inserten correctamente

## 24. Cambia el desarrollador por 'Bandai Namco Entertainment' del juego 'Dark Souls III'

~~~sql
UPDATE juegos
SET desarrollador = 'Bandai Namco Entertainment'
WHERE titulo = 'Dark Souls III';
~~~

## 25. Actualizar el 'rating' de todos los juegos que hayan sido desarrollados por 'Nintendo EPD' y tengan un ratin menor a 4.8

~~~sql
UPDATE juegos
SET rating = 4.8
WHERE desarrollador = 'Nintendo EPD'
AND rating < (SELECT AVG(rating) FROM juegos);
~~~

## 26. Crea una vista que muestre información de los juegos desarrollados por 'Naughty Dog' y 'SIE Santa Monica Studio' junto con la información de la plataforma en la que estén disponibles

~~~sql
CREATE VIEW juegos_naughtydog_santamonica AS
SELECT juegos.titulo, juegos.plataforma, juegos.genero, juegos.lanzamiento, juegos.rating, plataformas.fabricante
FROM juegos
JOIN plataformas ON juegos.plataforma = plataformas.nombre
WHERE juegos.desarrollador IN ('Naughty Dog', 'SIE Santa Monica Studio');
~~~

## 27. Elimina la tabla 'plataformas

~~~sql
DROP TABLE plataformas;
~~~

## 28. Elimina el registro 'The Last of Us Part II'

~~~sql
DELETE FROM juegos
WHERE titulo = 'The Last of Us Part II';
~~~

## 29. Eliminar la base de datos 'videojuegos'

~~~sql
DROP DATABASE videojuegos;
~~~
