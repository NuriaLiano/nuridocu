# EJERCICIOS DE UNIÓN, INTERSECCIÓN Y DIFERENCIA

~~~sql
CREATE DATABASE ventas4

CREATE TABLE clientes (
  id INT PRIMARY KEY,
  nombre VARCHAR(50)
);

INSERT INTO clientes (id, nombre)
VALUES (1, 'Juan'),
       (2, 'Maria'),
       (3, 'Pedro');

CREATE TABLE proveedores (
  id INT PRIMARY KEY,
  nombre VARCHAR(50)
);

INSERT INTO proveedores (id, nombre)
VALUES (2, 'Laura'),
       (3, 'Pedro'),
       (4, 'Ana');
~~~

## EJERCICIO 1 - UNION

Utilizar la unión para obtener todos los nombres de clientes y proveedores

~~~sql
SELECT nombre FROM clientes
UNION
SELECT nombre FROM proveedores;
~~~

### RESULTADO

| nombre|
|-------|
| Ana   |
| Juan  |
| Laura |
| Maria |
| Pedro |


## EJERCICIO 2 - UNION ALL

Utilizar UNION ALL para obtener todos los nombres de clientes y proveedores, incluyendo duplicados

~~~sql
SELECT nombre FROM clientes
UNION ALL
SELECT nombre FROM proveedores;
~~~

### RESULTADO

| nombre|
|-------|
| Juan  |
| Maria |
| Pedro |
| Laura |
| Pedro |
| Ana   |


## EJERCICIO 3 - INTERSECT

Utilizar la intersección para obtener los nombres que se encuentran en ambas tablas

~~~sql
SELECT nombre FROM clientes
INTERSECT
SELECT nombre FROM proveedores;
~~~

### RESULTADO

| nombre|
|-------|
| Pedro |

## EJERCICIO 4 - EXCEPT

Utilizar la diferencia para obtener los nombres de clientes que no son proveedores

~~~sql
SELECT nombre FROM clientes
EXCEPT
SELECT nombre FROM proveedores;
~~~

### RESULTADO

| nombre|
|-------|
| Juan  |
| Maria |
