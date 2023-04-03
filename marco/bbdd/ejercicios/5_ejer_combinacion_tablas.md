# EJERCICIOS COMBINACIÓN DE TABLAS

~~~sql
CREATE DATABASE empresa;

USE empresa;

CREATE TABLE empleado (
  id_empleado INT PRIMARY KEY,
  nombre VARCHAR(50),
  departamento INT
);

CREATE TABLE departamento (
  id_departamento INT PRIMARY KEY,
  nombre VARCHAR(50)
);

INSERT INTO departamento (id_departamento, nombre) 
VALUES 
(1, 'Ventas'), 
(2, 'Marketing'), 
(3, 'Recursos Humanos');

INSERT INTO empleado (id_empleado, nombre, departamento) 
VALUES 
(1, 'Juan Perez', 1), 
(2, 'Maria Gomez', 2), 
(3, 'Pedro Sanchez', 1), 
(4, 'Ana Rodriguez', 3), 
(5, 'Luisa Fernandez', 2);

~~~

## EJERCICIO 1 - INNER JOIN

Unir las tablas "empleado" y "departamento" y obtener el nombre del departamento de cada empleado

~~~sql
SELECT e.nombre AS empleado, d.nombre AS departamento
FROM empleado e
INNER JOIN departamento d ON e.departamento = d.id_departamento;
~~~

En esta consulta se seleccionan los nombres de los empleados y de los departamentos a los que pertenecen utilizando las tablas "empleado" y "departamento", y se unen mediante INNER JOIN a través de la columna "departamento" de la tabla "empleado" y la columna "id_departamento" de la tabla "departamento". De esta forma se obtiene una tabla que muestra el nombre de cada empleado junto con el nombre del departamento al que pertenece.

### RESULTADO

empleado	departamento
Juan Perez	Ventas
Maria Gomez	Marketing
Pedro Sanchez	Ventas
Ana Rodriguez	Recursos Humanos
Luisa Fernandez	Marketing

## EJERCICIO 2 - RIGHT JOIN

Unir las tablas "empleado" y "departamento" y obtener el nombre de todos los departamentos, incluso aquellos que no tienen empleados asignados:

~~~sql
SELECT d.nombre AS departamento, e.nombre AS empleado
FROM departamento d
RIGHT JOIN empleado e ON d.id_departamento = e.departamento;
~~~

En esta consulta se seleccionan los nombres de los departamentos y de los empleados utilizando las tablas "departamento" y "empleado", y se unen mediante RIGHT JOIN a través de la columna "id_departamento" de la tabla "departamento" y la columna "departamento" de la tabla "empleado". De esta forma se obtiene una tabla que muestra el nombre de cada departamento junto con el nombre de los empleados asignados a él, y también aquellos departamentos que no tienen empleados asignados, representados por el valor NULL en la columna "empleado".

### RESULTADO

departamento	empleado
Ventas	Juan Perez
Ventas	Pedro Sanchez
Marketing	Maria Gomez
Marketing	Luisa Fernandez
Recursos Humanos	Ana Rodriguez
Finanzas	NULL

## EJERCICIO 2 - LEFT JOIN

Unir las tablas "empleado" y "departamento" y obtener el nombre de todos los empleados, incluso aquellos que no están asignados a ningún departamento:

~~~sql
SELECT e.nombre AS empleado, d.nombre AS departamento
FROM empleado e
LEFT JOIN departamento d ON e.departamento = d.id_departamento;
~~~

En esta consulta se seleccionan los nombres de los empleados y de los departamentos utilizando las tablas "empleado" y "departamento", y se unen mediante LEFT JOIN a través de la columna "departamento" de la tabla "empleado" y la columna "id_departamento" de la tabla "departamento". De esta forma se obtiene una tabla que muestra el nombre de cada empleado junto con el nombre del departamento al que está asignado, y también aquellos empleados que no están asignados a ningún departamento, representados por el valor NULL en la columna "departamento".

### RESULTADO

empleado	departamento
Juan Perez	Ventas
Maria Gomez	Marketing
Pedro Sanchez	Ventas
Ana Rodriguez	Recursos Humanos
Luisa Fernandez	Marketing
Pepe Hernandez	NULL

## EJERCICIO 2 - FULL OUTER JOIN

Unir las tablas "empleado" y "departamento" y obtener todos los empleados y departamentos, incluyendo aquellos que no están asignados:

~~~sql
SELECT e.nombre AS empleado, d.nombre AS departamento
FROM empleado e
FULL OUTER JOIN departamento d ON e.departamento = d.id_departamento;
~~~

En esta consulta se seleccionan los nombres de los empleados y de los departamentos utilizando las tablas "empleado" y "departamento", y se unen mediante FULL OUTER JOIN a través de la columna "departamento" de la tabla "empleado" y la columna "id_departamento" de la tabla "departamento". De esta forma se obtiene una tabla que muestra el nombre de cada empleado junto con el nombre del departamento al que está asignado, y también aquellos empleados y departamentos que no tienen correspondencia en la otra tabla, representados por el valor NULL en las columnas correspondientes.

### RESULTADO

empleado	departamento
Juan Perez	Ventas
Pedro Sanchez	Ventas
Maria Gomez	Marketing
Luisa Fernandez	Marketing
Ana Rodriguez	Recursos Humanos
NULL	Finanzas
Pepe Hernandez	NULL