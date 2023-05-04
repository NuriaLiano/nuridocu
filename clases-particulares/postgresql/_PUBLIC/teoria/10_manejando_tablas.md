---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Tablas

## Crear

Para crear una tabla en PostgreSQL, se utiliza la sentencia CREATE TABLE. Por ejemplo, si deseas crear una tabla de usuarios con los campos id, nombre, email y contraseña, puedes hacer lo siguiente

~~~sql
CREATE TABLE usuarios (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50),
  email VARCHAR(100),
  contraseña VARCHAR(255)
);
~~~

## Añadir columnas

Si deseas agregar una nueva columna a una tabla existente, puedes utilizar la sentencia ALTER TABLE. Por ejemplo, si deseas agregar una columna "telefono" a la tabla "usuarios", puedes hacer lo siguiente

~~~sql
ALTER TABLE usuarios ADD COLUMN telefono VARCHAR(20);
~~~

## Modificar

## Modificar columnas

Si deseas modificar una columna existente, puedes utilizar la sentencia ALTER TABLE y la cláusula ALTER TABLE con TYPE para establecer el tipo de dato. Por ejemplo, si deseas cambiar el tipo de datos de la columna "email" a VARCHAR(255), puedes hacer lo siguiente:

~~~sql
ALTER TABLE usuarios ALTER COLUMN email TYPE VARCHAR(255);
~~~

## Modificar el nombre de una tabla

~~~sql
ALTER TABLE clientes
RENAME TO clientes_nuevos;
~~~

## Modificar el nombre de una columna

~~~sql
ALTER TABLE usuarios RENAME COLUMN contraseña TO password;
~~~

## Eliminar columna

~~~sql
ALTER TABLE usuarios DROP COLUMN telefono;
~~~

## Eliminar tabla

~~~sql
DROP TABLE usuarios;
~~~

También existe la posibilidad de borrar la tabla en caso de que exista, para ello utilizamos la sentencia 'IF EXISTS'

~~~sql
DROP TABLE IF EXISTS usuarios;
~~~

>:pencil: **NOTA** la cláusula IF EXISTS es opcional pero útil para evitar errores en caso de que la tabla no exista. Si la tabla no existe, la sentencia simplemente se salta y no genera ningún error.

## Truncate

Si deseas eliminar todos los registros de una tabla sin eliminar la tabla en sí, puedes utilizar la sentencia TRUNCATE TABLE.

~~~sql
TRUNCATE TABLE usuarios;
~~~

## Copiar desde otra tabla

Es posible crear una nueva tabla a partir de los datos de una tabla existente utilizando la cláusula CREATE TABLE AS. Esta cláusula permite crear una nueva tabla y copiar los datos de la tabla original en la nueva tabla. También es posible definir que columnas se quieren copiar.

### Copiar todas las columnas

>:pencil: **NOTA** la nueva tabla tendrá el mismo nombre y tipo de datos de las columnas que la tabla existente.

~~~sql
CREATE TABLE nueva_tabla AS
SELECT * FROM tabla_existente;
~~~

### Seleccionar que columnas copiar

~~~sql
CREATE TABLE nueva_tabla (
  columna1 tipo_de_dato,
  columna2 tipo_de_dato,
  ...
) AS
SELECT columna1, columna2, ...
FROM tabla_existente;
~~~
