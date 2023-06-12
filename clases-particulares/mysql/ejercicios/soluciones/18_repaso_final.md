# Repaso general MYSQL

## FAQs inicial

### ¿Cuando uso subconsultas y cuando joins?

Las subconsultas son útiles para realizar cálculos, filtrar resultados y obtener un conjunto de datos más pequeño y específico.
Los joins son adecuados para combinar columnas y filas de múltiples tablas basándose en una condición de igualdad.
Las subconsultas son más simples de escribir y entender en consultas anidadas y para necesidades específicas.
Los joins son más eficientes y escalables para grandes volúmenes de datos y cuando necesitas acceder y combinar múltiples columnas de diferentes tablas.
La elección entre subconsultas y joins depende de la estructura de los datos, la complejidad de la consulta, el rendimiento requerido y la legibilidad del código. Puedes evaluar estos factores en cada caso específico.

### ¿Qué diferencias hay entre = o IN en las subconsultas?

El operador **"="** en una subconsulta se utiliza cuando **se espera que la subconsulta devuelva un solo valor para la comparación**, mientras que **"IN"** se utiliza cuando **se espera que la subconsulta devuelva múltiples valores y se desea comprobar si el valor de la consulta principal se encuentra entre esos valores devueltos por la subconsulta.**

Ejemplo: ``SELECT nombre FROM personas WHERE edad = (SELECT MAX(edad) FROM personas)``
Ejemplo: ``SELECT nombre FROM personas WHERE edad IN (SELECT edad FROM personas WHERE ciudad = 'Madrid')``

### ¿Para qué sirve AS?

Se utiliza para asignar alias a tablas, columnas, funciones o tablas derivadas en una consulta SQL. Esto puede mejorar la legibilidad y la claridad del código, permitiendo hacer referencia a esos elementos con nombres más descriptivos o abreviados.

### ¿Cuándo usar ALTER TABLE o UPDATE?

Utiliza ALTER TABLE cuando necesites realizar cambios en la estructura de una tabla, como agregar, modificar o eliminar columnas. Utiliza UPDATE cuando necesites modificar los valores de una o varias filas de una tabla. Recuerda que **ALTER TABLE afecta la estructura de la tabla, mientras que UPDATE modifica los datos en las filas existentes.**

## Base de datos, tablas y datos

~~~sql
-- Creación de la base de datos
CREATE DATABASE simpsons;

-- Selección de la base de datos
USE simpsons;

-- Creación de la tabla "personajes"
CREATE TABLE personajes (
  nombre VARCHAR(100),
  ocupacion VARCHAR(100),
  edad INTEGER
);

-- Inserción de datos en la tabla "personajes"
INSERT INTO personajes (nombre, ocupacion, edad) VALUES
  ('Homer Simpson', 'Empleado de la Planta Nuclear', 39),
  ('Marge Simpson', 'Ama de casa', 36),
  ('Bart Simpson', 'Estudiante', 10),
  ('Lisa Simpson', 'Estudiante', 8),
  ('Maggie Simpson', 'Bebé', 1);

-- Creación de la tabla "lugares"
CREATE TABLE lugares (
  nombre VARCHAR(100),
  tipo VARCHAR(100),
  direccion VARCHAR(100)
);

-- Inserción de datos en la tabla "lugares"
INSERT INTO lugares (nombre, tipo, direccion) VALUES
  ('Bar de Moe', 'Bar', 'Calle de la Amargura, Springfield'),
  ('Escuela Primaria de Springfield', 'Escuela', 'Avenida Principal, Springfield'),
  ('Casa de los Simpson', 'Residencia', 'Evergreen Terrace, Springfield'),
  ('Planta Nuclear de Springfield', 'Lugar de Trabajo', 'Avenida Principal, Springfield');
~~~

## RELACIONES DE LAS TABLAS

~~~sql
-- Añadir clave primaria a la tabla "personajes"
ALTER TABLE personajes
ADD COLUMN personaje_id INT AUTO_INCREMENT PRIMARY KEY;

-- Añadir clave primaria a la tabla "lugares"
ALTER TABLE lugares
ADD COLUMN lugar_id INT AUTO_INCREMENT PRIMARY KEY;

-- Añadir clave foránea a la tabla "personajes"
ALTER TABLE personajes
ADD COLUMN lugar_id INT,
ADD CONSTRAINT fk_lugar
FOREIGN KEY (lugar_id) REFERENCES lugares(lugar_id);

-- añadir informacion a personajes.lugar_id
UPDATE personajes
SET lugar_id = 1
WHERE nombre = 'Homer Simpson';

UPDATE personajes
SET lugar_id = 3
WHERE nombre = 'Marge Simpson';

UPDATE personajes
SET lugar_id = 2
WHERE nombre = 'Bart Simpson';

UPDATE personajes
SET lugar_id = 2
WHERE nombre = 'Lisa Simpson';

UPDATE personajes
SET lugar_id = 3
WHERE nombre = 'Marggie Simpson';
~~~

## 1. Muestra toda la información de los personajes cuya ocupación sea "Estudiante"

~~~sql
SELECT * FROM personajes WHERE ocupacion = "Estudiante";
~~~

## 2. Modifica el nombre de "Homer" por "Homero"

~~~sql
UPDATE personajes
SET nombre = 'Homero Simpson'
WHERE nombre = 'Homer Simpson';
~~~

## 3. Muestra una lista de los nombres de los personajes ordenados alfabéticamente

~~~sql
SELECT nombre, ocupacion
FROM personajes
ORDER BY nombre ASC;
~~~

## 4. Asegurate que la edad de los personajes siempre es mayor que 0

~~~sql
ALTER TABLE personajes
ADD CONSTRAINT check_edad_nonnegative CHECK (edad >= 0);
~~~

## 5. Añade una columna "Género" a la tabla 'Personajes' y añade la siguiente información

nombre         | genero
---------------|----------
Homer Simpson  | masculino
Marge Simpson  | femenino
Bart Simpson   | masculino
Lisa Simpson   | femenino
Maggie Simpson | femenino

~~~sql
ALTER TABLE personajes
ADD COLUMN genero VARCHAR(20);

-- introducir datos
UPDATE personajes
SET genero = 'Masculino'
WHERE nombre = 'Homer Simpson';

UPDATE personajes
SET genero = 'Femenino'
WHERE nombre = 'Marge Simpson';

UPDATE personajes
SET genero = 'Masculino'
WHERE nombre = 'Bart Simpson';

UPDATE personajes
SET genero = 'Femenino'
WHERE nombre = 'Lisa Simpson';

UPDATE personajes
SET genero = 'Femenino'
WHERE nombre = 'Maggie Simpson';

~~~

## 6. Crea una tabla 'Episodios' donde el id sea auto incrementado y agrega la siguiente información

('El primer día de colegio', 1, 30),
('La boda de Apu', 3, 25),
('Homer en el espacio profundo', 5, 22),
('El especial de Noche de Brujas', 10, 20),
('La casita del horror XXIX', 30, 18)

~~~sql
CREATE TABLE episodios (
  id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(100),
  temporada INT,
  duracion INT
);
-- Inserción de datos en la tabla "episodios"
INSERT INTO episodios (titulo, temporada, duracion) VALUES
  ('El primer día de colegio', 1, 30),
  ('La boda de Apu', 3, 25),
  ('Homer en el espacio profundo', 5, 22),
  ('El especial de Noche de Brujas', 10, 20),
  ('La casita del horror XXIX', 30, 18);
~~~

## 7. Agrega una columna 'fecha_emision', después modifica el tipo de datos a INT y valor NULL. Acto seguido elimina la columna 'fecha_salida'

~~~sql
--crea la columna
ALTER TABLE episodios
ADD COLUMN fecha_emision DATE;

--modificar la columna
ALTER TABLE episodios
MODIFY COLUMN fecha_emision INT NULL;

-- eliminar la columna
ALTER TABLE episodios
DROP COLUMN fecha_emision;
~~~

## 8. Obtener la cantidad de personajes por ocupación y el promedio de edad de los personajes en cada ocupación

~~~sql
SELECT p.ocupacion, COUNT(*) AS cantidad_personajes, AVG(p.edad) AS promedio_edad
FROM personajes p
GROUP BY p.ocupacion;
~~~

## 9. Obtener el nombre de los personajes y el tipo de lugar para los personajes que trabajen en 'Empleado de la Planta Nuclear'

~~~sql
SELECT p.nombre, (
  SELECT l.tipo
  FROM lugares l
  WHERE l.lugar_id = p.lugar_id
) AS tipo_lugar
FROM personajes p
WHERE p.ocupacion = 'Empleado de la Planta Nuclear';

-- usando joins
SELECT p.nombre, l.tipo
FROM personajes p
JOIN lugares l ON p.lugar_id = l.lugar_id
WHERE p.ocupacion = 'Empleado de la Planta Nuclear';
~~~

## 10. Obtener el nombre del personaje y el nombre del lugar donde trabaja cada personaje

~~~sql
SELECT p.nombre, l.nombre
FROM personajes p
JOIN lugares l ON p.lugar_id = l.lugar_id;

--usando subconsultas
SELECT
  (SELECT nombre FROM personajes WHERE personaje_id = p.personaje_id) AS nombre_personaje,
  (SELECT nombre FROM lugares WHERE lugar_id = p.lugar_id) AS nombre_lugar
FROM personajes p;
~~~

## 11. Corrige los errores

~~~sql
SELECT nombre, ocupacion
FROM personajes
WHERE lugar_id = (
  SELECT id
  FROM lugares
  WHERE direccion = 'Casa de los Simpson'
  LIMIT 2
);
~~~

En esta consulta modificada, se ha cambiado el valor de LIMIT en la subconsulta a 2 en lugar de 1. Esto significa que la subconsulta puede devolver hasta dos filas en lugar de una.

El problema con esta modificación es que ahora estamos comparando la columna lugar_id en la tabla personajes con una subconsulta que puede devolver múltiples valores. Esto generará un error porque la comparación "=" solo puede utilizarse cuando se compara una columna con un único valor.

También hay un error en cuanto al SELECT id FROM lugares ya que debería ser lugar_id y con direccion = "Casa de los simpson" deberia ser tipo en vez de direccion

## 12. Elimina la ocupación de 'Homer'

~~~sql
UPDATE personajes
SET ocupacion = NULL
WHERE nombre = 'Homer Simpson';
~~~

## 13. Obtener una lista de nombres que estén presentes en ambas tablas y una lista de nombres que estén en la tabla1 pero no en la tabla2

~~~sql
-- Intersección de nombres presentes en ambas tablas
SELECT nombre FROM tabla1
INTERSECT
SELECT nombre FROM tabla2;

-- Diferencia de nombres entre tabla1 y tabla2
SELECT nombre FROM tabla1
EXCEPT
SELECT nombre FROM tabla2;
~~~

## 14. Elimina las tablas

~~~sql
-- Eliminar la clave foránea en la tabla "personajes"
ALTER TABLE personajes
DROP FOREIGN KEY fk_lugar;

-- Eliminar la tabla "personajes"
DROP TABLE personajes;

-- Eliminar la tabla "lugares"
DROP TABLE lugares;
~~~

## 15. Elimina la base de datos

~~~sql
-- Eliminar la base de datos
DROP DATABASE simpsons;
~~~
