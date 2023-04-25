---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# EJERCICIOS DE REPASO

## Crear base de datos 'libreria'

~~~sql
CREATE DATABASE libreria;
~~~

## Crear dos tablas 'libros' y 'autores'

~~~sql
CREATE TABLE libros (
  id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(255) NOT NULL,
  anio_publicacion INT(11) NOT NULL
);

CREATE TABLE autores (
  id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  apellido VARCHAR(255) NOT NULL
);

~~~

## Insertar datos en las tablas

~~~sql
INSERT INTO libros (titulo, anio_publicacion) VALUES ('El amor en los tiempos del cólera', 1985);
INSERT INTO libros (titulo, anio_publicacion) VALUES ('Cien años de soledad', 1967);

INSERT INTO autores (nombre, apellido) VALUES ('Gabriel', 'García Márquez');

~~~

## Mostrar el contenido de la tabla 'libros' cuyo año de publicación sea 1985

~~~sql
SELECT * FROM libros WHERE anio_publicacion = 1985;
~~~

## Mostrar el contenido de la tabla 'autores' cuyo apellido sea 'Garcia Marquez'

~~~sql
SELECT * FROM autores WHERE apellido = 'García Márquez';
~~~

## Actualiza el año de publicación del libro 'cien años de soledad' a 1969

~~~sql
UPDATE libros SET anio_publicacion = 1969 WHERE titulo = 'Cien años de soledad';
~~~

## Mostrar el 'id', 'titulo' de la tabla 'libros' usando el alias 'l'

~~~sql
SELECT l.id, l.titulo, l.anio_publicacion FROM libros AS l;
~~~

## Mostrar el 'nombre' y 'apellido' de la tabla 'autores' usando el alias 'a'

~~~sql
SELECT a.id, a.nombre, a.apellido FROM autores AS a;
~~~

## Muestra el promedio de años de publicación de los libros

~~~sql
SELECT AVG(anio_publicacion) FROM libros;
~~~

## Añade una relación clave foránea entre la tabla 'libros' y la tabla 'autores'

>:diamond_shape_with_a_dot_inside: **PISTA** El campo 'id_autor' en la tabla 'libros' debe ser clave foránea referido al campo 'id' de la tabla 'autores'.

~~~sql
ALTER TABLE libros
ADD CONSTRAINT fk_libros_autores
FOREIGN KEY (id_autor)
REFERENCES autores(id)
ON DELETE CASCADE;
~~~

## Une las tablas 'libros' y 'autores' usando inner join, muéstralo en una columna llamada 'titulos_autores' y explica el resultado

~~~sql
SELECT libros.titulo, autores.nombre, autores.apellido
FROM libros
INNER JOIN autores
ON libros.id_autor = autores.id;

-- con CONCAT
SELECT CONCAT(libros.titulo, ' - ', autores.nombre, ' ', autores.apellido) AS titulos_autores
FROM libros
INNER JOIN autores
ON libros.id_autor = autores.id;
~~~

**Explicación**
La función CONCAT() permite unir diferentes cadenas de caracteres en una sola, utilizando los separadores o caracteres que deseemos. En este caso, se ha utilizado un guión y un espacio para separar el título del libro del nombre y apellido del autor.

La cláusula 'AS titulos_autores' al final de la consulta asigna el nombre 'titulos_autores' a la columna que contiene los resultados concatenados.

La consulta utiliza la cláusula "INNER JOIN" para unir los datos de ambas tablas en base a una condición específica. En este caso, la condición es que el valor de la columna "id_autor" en la tabla "libros" sea igual al valor de la columna "id" en la tabla "autores".

La sentencia selecciona las columnas "titulo" de la tabla "libros" y "nombre" y "apellido" de la tabla "autores". Esto significa que la consulta devolverá una lista de todos los títulos de libros junto con los nombres y apellidos de los autores correspondientes.

En resumen, esta consulta devuelve una lista de los títulos de los libros y los nombres y apellidos de los autores correspondientes que se encuentran almacenados en las tablas "libros" y "autores", respectivamente, unidas mediante la cláusula "INNER JOIN".
