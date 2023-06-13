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

## 1. Muestra toda la información de los personajes cuya ocupación sea "Estudiante"

## 2. Modifica el nombre de "Homer" por "Homero"

## 3. Muestra una lista de los nombres de los personajes ordenados alfabéticamente

## 4. Asegurate que la edad de los personajes siempre es mayor que 0

## 5. Añade una columna "Género" a la tabla 'Personajes' y añade la siguiente información

nombre         | genero
---------------|----------
Homer Simpson  | masculino
Marge Simpson  | femenino
Bart Simpson   | masculino
Lisa Simpson   | femenino
Maggie Simpson | femenino

## 6. Crea una tabla 'Episodios' donde el id sea auto incrementado y agrega la siguiente información

('El primer día de colegio', 1, 30),
('La boda de Apu', 3, 25),
('Homer en el espacio profundo', 5, 22),
('El especial de Noche de Brujas', 10, 20),
('La casita del horror XXIX', 30, 18)

## 7. Agrega una columna 'fecha_emision', después modifica el tipo de datos a INT y valor NULL. Acto seguido elimina la columna 'fecha_emision'

## 8. Obtener la cantidad de personajes por ocupación y el promedio de edad de los personajes en cada ocupación

## 9. Obtener el nombre de los personajes y el tipo de lugar para los personajes que trabajen en 'Empleado de la Planta Nuclear'

## 10. Obtener el nombre del personaje y el nombre del lugar donde trabaja cada personaje

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

## 12. Elimina la ocupación de 'Homer'

## 13. Obtener una lista de nombres que estén presentes en ambas tablas y una lista de nombres que estén en la tabla1 pero no en la tabla2

## 14. Elimina las tablas

## 15. Elimina la base de datos
