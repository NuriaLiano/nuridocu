---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Ejercicios de repaso manejando bases de datos, tablas, vistas, relaciones, restricciones y datos

## 1. Crea la base de datos

~~~sql
CREATE DATABASE GTADB;
~~~

## 2. Conéctate a la base de datos

~~~sql
\c GTADB;
~~~

## 3. Crea la tabla 'PERSONAJES'

id_personaje (INTEGER PRIMARY KEY),
nombre (VARCHAR(50)),
apellido (VARCHAR(50)),
edad (INTEGER),
genero (VARCHAR(10)),
nacionalidad (VARCHAR(50)),
banda (VARCHAR(50))

~~~sql
CREATE TABLE personajes (
    id_personaje INTEGER PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    edad INTEGER,
    genero VARCHAR(10),
    nacionalidad VARCHAR(50),
    banda VARCHAR(50)
);
~~~

## 4. Inserta los siguientes registros en la tabla 'PERSONAJES'

(1, 'Carl', 'Johnson', 29, 'Masculino', 'Estados Unidos', 'Grove Street Families'),
(2, 'Franklin', 'Clinton', 25, 'Masculino', 'Estados Unidos', 'Los Santos'),
(3, 'Michael', 'De Santa', 45, 'Masculino', 'Estados Unidos', 'FIB'),
(4, 'Trevor', 'Philips', 48, 'Masculino', 'Canadá', 'Trevor Philips Enterprises')

~~~sql
INSERT INTO personajes (id_personaje, nombre, apellido, edad, genero, nacionalidad, banda)
VALUES (1, 'Carl', 'Johnson', 29, 'Masculino', 'Estados Unidos', 'Grove Street Families'),
       (2, 'Franklin', 'Clinton', 25, 'Masculino', 'Estados Unidos', 'Los Santos'),
       (3, 'Michael', 'De Santa', 45, 'Masculino', 'Estados Unidos', 'FIB'),
       (4, 'Trevor', 'Philips', 48, 'Masculino', 'Canadá', 'Trevor Philips Enterprises');
~~~

## 5. Crear la tabla 'JUEGOS'

id_juego (INTEGER PRIMARY KEY),
titulo (VARCHAR(50)),
fecha_lanzamiento (DATE),
plataforma (VARCHAR(20)),
desarrolladora (VARCHAR(50))

~~~sql
CREATE TABLE juegos (
    id_juego INTEGER PRIMARY KEY,
    titulo VARCHAR(50),
    fecha_lanzamiento DATE,
    plataforma VARCHAR(20),
    desarrolladora VARCHAR(50)
);
~~~

## 6. Inserta los siguientes registros en la tabla 'JUEGOS'

(1, 'Grand Theft Auto III', '2001-10-22', 'PlayStation 2', 'Rockstar North'),
(2, 'Grand Theft Auto: San Andreas', '2004-10-26', 'PlayStation 2', 'Rockstar North'),
(3, 'Grand Theft Auto IV', '2008-04-29', 'PlayStation 3', 'Rockstar North'),
(4, 'Grand Theft Auto V', '2013-09-17', 'PlayStation 4', 'Rockstar North');

~~~sql
INSERT INTO Juegos (id_juego, titulo, fecha_lanzamiento, plataforma, desarrolladora)
VALUES (1, 'Grand Theft Auto III', '2001-10-22', 'PlayStation 2', 'Rockstar North'),
       (2, 'Grand Theft Auto: San Andreas', '2004-10-26', 'PlayStation 2', 'Rockstar North'),
       (3, 'Grand Theft Auto IV', '2008-04-29', 'PlayStation 3', 'Rockstar North'),
       (4, 'Grand Theft Auto V', '2013-09-17', 'PlayStation 4', 'Rockstar North');
~~~

## 7. Añade la clave primaria donde creas que falta

~~~sql
ALTER TABLE juegos
ADD COLUMN id_juego SERIAL PRIMARY KEY;
~~~

## 8. Añade la clave foránea en la tabla 'PERSONAJES'

>:black_joker: **PISTA** La columna "banda" de la tabla "Personajes" hará referencia a la columna "titulo" de la tabla "Juegos", por lo que necesitamos agregar una clave foránea en la tabla "Personajes".

~~~sql
ALTER TABLE personajes
ADD COLUMN id_juego INTEGER REFERENCES juegos (id_juego);
~~~

## 9. Añade una restricción a la tabla 'JUEGOS' para que no se puedan insertar juegos con el mismo título

~~~sql
ALTER TABLE juegos
ADD CONSTRAINT unique_titulo UNIQUE (titulo);
~~~

## 10. Añade una restricción a la tabla 'PERSONAJES' para que sólo se puedan insertar edades mayores de 18 años

~~~sql
ALTER TABLE personajes
ADD CONSTRAINT check_edad CHECK (edad >= 18);
~~~

## 11. Añade una restricción a la tabla 'PERSONAJES' para que no se puedan insertar valores nulos

~~~sql
ALTER TABLE personajes
ALTER COLUMN nacionalidad SET NOT NULL;

--opcion menos restrictiva
ALTER TABLE personajes
ADD CONSTRAINT nombre_de_la_restriccion CHECK (nacionalidad IS NOT NULL);
~~~

## 12. Inserta estos valores en la tabla 'JUEGOS' y explica que ocurre

('Grand Theft Auto V', 'PC', '2013-09-17'),
('Grand Theft Auto IV', 'Xbox 360', '2008-04-29'),
('Grand Theft Auto V', 'PlayStation 3', '2013-09-17')

~~~sql
INSERT INTO juegos (titulo, plataforma, lanzamiento)
VALUES ('Grand Theft Auto V', 'PC', '2013-09-17'),
       ('Grand Theft Auto IV', 'Xbox 360', '2008-04-29'),
       ('Grand Theft Auto V', 'PlayStation 3', '2013-09-17');
~~~

Explicación:
Faltan los campos 'id_juego' y 'desarrolladora'.
El orden no es correcto.
La restricción UNIQUE que añadimos anteriormente a la tabla "Juegos" asegura que no se puedan insertar dos juegos con el mismo título. Por lo tanto, el tercer registro con el título "Grand Theft Auto V" y la plataforma "PlayStation 3" viola esta restricción y genera un error.

CORRECCIÓN:

~~~sql
INSERT INTO juegos (id_juego, titulo, fecha_lanzamiento, plataforma, desarrolladora)
VALUES (5, 'Grand Theft Auto VI', '2013-09-17', 'PC', ),
       (6, 'Grand Theft Auto VII', 'Xbox 360', '2008-04-29'),
       (7, 'Grand Theft Auto VIII', 'PlayStation 3', '2013-09-17');
~~~

## 13. Muestra los registros de la tabla 'PERSONAJES' que sean de la banda 'Grove Street Families' y la nacionalidad sea 'Estados Unidos'

~~~sql
SELECT * FROM personajes
WHERE banda = 'Grove Street Families' AND nacionalidad = 'Estados Unidos';
~~~

## 14. Muestra el número de personajes de cada banda

~~~sql
SELECT banda, COUNT(*) FROM personajes
GROUP BY banda;
~~~

## 15. Muestra las bandas con más de 2 personajes

~~~sql
SELECT banda, COUNT(*) FROM personajes
GROUP BY banda
HAVING COUNT(*) > 2;
~~~

## 16. Muestra el número de personajes en cada juego que son de nacionalidad estadounidense

~~~sql
SELECT juegos.titulo, COUNT(*) FROM personajes
JOIN juegos ON personajes.id_juego = juegos.id_juego
WHERE personajes.nacionalidad = 'Estados Unidos'
GROUP BY juegos.titulo;
~~~

## 17. Muestra los nombres de los personajes y el título del juego correspondiente en el que aparecen en una vista llamada 'personajes_juegos'

~~~sql
CREATE VIEW personajes_juegos AS
SELECT personajes.nombre, juegos.titulo
FROM personajes
JOIN juegos ON personajes.id_juego = juegos.id_juego;
~~~

## 18. Consulta la vista creada

~~~sql
SELECT * FROM personajes_juegos;
~~~

## 19. Actualiza el título del juego a 'Grand Theft Auto: San Andreas' en la vista 'personajes_juegos' para el personaje 'CJ'

~~~sql
UPDATE personajes_juegos
SET titulo = 'Grand Theft Auto: San Andreas'
WHERE nombre = 'CJ';
~~~

## 20. Elimina la vista 'personajes_juegos'

~~~sql
DROP VIEW personajes_juegos;
~~~

## 21. Elimina la vista 'personajes_juegos'

~~~sql
DROP VIEW personajes_juegos;
~~~

## 22. Devuelve los nombres de los personajes que pertenecen a las bandas "Ballers" o "Grove Street Families", y los nombres de los personajes que pertenecen a las bandas "Vagos" o "Aztecas". Los resultados de ambas consultas se combinan y se eliminan los duplicados

>:pencil: **NOTA** la consulta principal no necesita la cláusula DISTINCT ya que la operación UNION se encarga de eliminar los duplicados

~~~sql
SELECT nombre, banda FROM Personajes
WHERE banda = 'Ballers' OR banda = 'Grove Street Families'
UNION
SELECT nombre, banda FROM Personajes
WHERE banda = 'Vagos' OR banda = 'Aztecas';

-- alternativa usando OR
SELECT DISTINCT nombre, banda FROM Personajes
WHERE (banda = 'Ballers' OR banda = 'Grove Street Families')
  OR (banda = 'Vagos' OR banda = 'Aztecas');
~~~

## 23. Devuelve los nombres de los personajes que pertenecen a la banda "Ballers" y que son de nacionalidad mexicana

~~~sql
SELECT nombre, banda FROM Personajes
WHERE banda = 'Ballers'
INTERSECT
SELECT nombre, banda FROM Personajes
WHERE nacionalidad = 'México';

-- alternativa usando AND
SELECT nombre, banda FROM Personajes
WHERE banda = 'Ballers' AND nacionalidad = 'México';
~~~

## 24. Devuelve los nombres de los personajes que pertenecen a la banda "Grove Street Families" y que no son de nacionalidad estadounidense

~~~sql
SELECT nombre, banda FROM Personajes
WHERE banda = 'Grove Street Families'
EXCEPT
SELECT nombre, banda FROM Personajes
WHERE nacionalidad = 'Estados Unidos';

--alternativa usando AND NOT
SELECT nombre, banda FROM Personajes
WHERE banda = 'Grove Street Families' AND NOT nacionalidad = 'Estados Unidos';
~~~

>:pencil: **NOTA** la alternativa que usa AND NOT es correcta, pero se puede mejorar utilizando directamente la operación EXCEPT

## 25. Es lo mismo 'UNION', 'INTERSECT' y 'EXCEPT' que 'AND', 'OR' y 'NOT'?

No, 'UNION', 'INTERSECT' y 'EXCEPT' no son lo mismo que 'AND', 'OR' y 'NOT' en SQL. Son operadores diferentes que se utilizan para realizar diferentes tipos de operaciones en una base de datos relacional.

'UNION', 'INTERSECT' y 'EXCEPT' son operadores de conjunto en SQL que se utilizan para combinar o comparar resultados de dos o más consultas.

- **'UNION'** se utiliza para combinar los resultados de dos o más consultas en un solo conjunto de resultados, eliminando los duplicados.
- **'INTERSECT'** se utiliza para encontrar los registros que aparecen en ambas consultas.
- **'EXCEPT'** se utiliza para encontrar los registros que aparecen en la primera consulta pero no en la segunda.
Por otro lado, 'AND', 'OR' y 'NOT' son operadores lógicos en SQL que se utilizan para filtrar resultados dentro de una sola consulta.

- **'AND'** se utiliza para combinar múltiples condiciones en una sola consulta.
- **'OR'** se utiliza para filtrar resultados basados en una o más condiciones.
- **'NOT'** se utiliza para negar una condición.

## 26. Elimina la restricción para evitar que se puedan introducir títulos duplicados

~~~sql
ALTER TABLE juegos
DROP CONSTRAINT unique_titulo;
~~~

>:warning: **ADVENTENCIA** Recuerda que al eliminar una restricción se permitirá insertar registros que antes no estaban permitidos. Por lo tanto, debes evaluar cuidadosamente si la restricción es necesaria antes de eliminarla.

## 27. Elimina la restricción de edad

~~~sql
ALTER TABLE personajes
DROP CONSTRAINT check_edad;
~~~

>:warning: **ADVENTENCIA** Recuerda que al eliminar una restricción se permitirá insertar registros que antes no estaban permitidos. Por lo tanto, debes evaluar cuidadosamente si la restricción es necesaria antes de eliminarla.
