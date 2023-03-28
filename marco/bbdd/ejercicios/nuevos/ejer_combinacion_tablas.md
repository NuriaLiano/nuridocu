# EJERCICIOS COMBINACIÓN DE TABLAS

Las tres cláusulas de join son utilizadas para combinar información de dos o más tablas en una consulta en SQL, pero tienen diferentes comportamientos:

- **Inner Join**: devuelve solo las filas que tienen coincidencias en ambas tablas. Es decir, si una fila de una tabla no tiene una coincidencia en la otra tabla, esa fila no se incluirá en el resultado.
- **Left Join**: devuelve todas las filas de la tabla izquierda (la que aparece antes de la cláusula JOIN) y las filas de la tabla derecha (la que aparece después de la cláusula JOIN) que tengan coincidencias. Si una fila de la tabla izquierda no tiene una coincidencia en la tabla derecha, se incluirá en el resultado con valores NULL en las columnas de la tabla derecha.
- **Right Join**: es similar al Left Join, pero devuelve todas las filas de la tabla derecha y solo las filas de la tabla izquierda que tengan coincidencias. Si una fila de la tabla derecha no tiene una coincidencia en la tabla izquierda, se incluirá en el resultado con valores NULL en las columnas de la tabla izquierda.

En resumen, la diferencia principal entre Left Join y Right Join es qué tabla se incluye en su totalidad en el resultado, mientras que Inner Join solo muestra filas coincidentes en ambas tablas.

~~~sql
CREATE DATABASE mi_empresa;

USE mi_empresa;

CREATE TABLE departamentos (
    id INT PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    departamento_id INT,
    salario DECIMAL(10,2),
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

INSERT INTO departamentos (id, nombre) VALUES (1, 'Ventas');
INSERT INTO departamentos (id, nombre) VALUES (2, 'Marketing');
INSERT INTO departamentos (id, nombre) VALUES (3, 'Finanzas');

INSERT INTO empleados (id, nombre, apellido, departamento_id, salario) VALUES (1, 'Juan', 'Pérez', 1, 2000.00);
INSERT INTO empleados (id, nombre, apellido, departamento_id, salario) VALUES (2, 'María', 'González', 2, 2500.00);
INSERT INTO empleados (id, nombre, apellido, departamento_id, salario) VALUES (3, 'Pedro', 'Ramírez', 3, 3000.00);
INSERT INTO empleados (id, nombre, apellido, departamento_id, salario) VALUES (4, 'Laura', 'Fernández', 2, 2700.00);

~~~

## EJERCICIO 1 - INNER JOIN

Supongamos que queremos obtener un informe con el nombre de los empleados y sus respectivos departamentos, ordenados por el nombre del departamento

~~~sql
SELECT e.nombre AS nombre_empleado, d.nombre AS nombre_departamento
FROM empleados AS e
INNER JOIN departamentos AS d ON e.id_departamento = d.id
ORDER BY d.nombre;
~~~

Es importante tener en cuenta que la operación INNER JOIN sólo devuelve las filas que tienen una correspondencia en ambas tablas. Si algún registro no tiene una coincidencia en la tabla relacionada, no se mostrará en los resultados.

**RESULTADO**
+--------+----------+
| nombre | departamento|
+--------+----------+
| Juan   | Ventas      |
| María  | Marketing   |
| Pedro  | Finanzas    |
| Laura  | Marketing   |
+--------+----------+

## EJERCICIO 2 - LEFT JOIN

Devuelve una tabla con dos columnas, la primera columna es el nombre del empleado y la segunda columna es el nombre del departamento al que pertenece.
A diferencia del INNER JOIN que nos muestra solamente aquellos empleados que pertenecen a un departamento, este LEFT JOIN también nos muestra aquellos empleados que no tienen un departamento asignado.

~~~sql
SELECT empleados.nombre, departamentos.nombre as departamento
FROM empleados
LEFT JOIN departamentos
ON empleados.departamento_id = departamentos.id;
~~~

**RESULTADO**
nombre	departamento
Juan	Ventas
María	Marketing
Pedro	Finanzas
Laura	Marketing
NULL	NULL

Como puedes ver, el último registro muestra NULL en ambas columnas ya que representa a un empleado que no tiene un departamento asignado en la tabla departamentos.

## EJERCICIO 3 - RIGHT JOIN

Devuelve una tabla con dos columnas, la primera columna es el nombre del empleado y la segunda columna es el nombre del departamento al que pertenece. A diferencia del LEFT JOIN, este RIGHT JOIN nos muestra todos los departamentos, incluso aquellos que no tienen empleados asignados.

~~~sql
SELECT empleados.nombre, departamentos.nombre as departamento
FROM empleados
LEFT JOIN departamentos
ON empleados.departamento_id = departamentos.id;
~~~

**RESULTADO**
nombre	departamento
Juan	Ventas
María	Marketing
Pedro	Finanzas
Laura	Marketing
NULL	Recursos

Como puedes ver, el último registro muestra NULL en la columna de empleados ya que representa a un departamento que no tiene empleados asignados en la tabla empleados.

## EJERCICIO 4 - FULL OUTER JOIN

Devuelve una tabla con dos columnas, la primera columna es el nombre del empleado y la segunda columna es el nombre del departamento al que pertenece. A diferencia del INNER JOIN, el FULL OUTER JOIN nos muestra todos los registros de ambas tablas, incluso aquellos que no tienen coincidencias en la otra tabla.

~~~sql
SELECT empleados.nombre, departamentos.nombre as departamento
FROM empleados
FULL OUTER JOIN departamentos
ON empleados.departamento_id = departamentos.id;
~~~

**RESULTADO**
nombre	departamento
Juan	Ventas
María	Marketing
Pedro	Finanzas
Laura	Marketing
NULL	Recursos
NULL	Compras

Como puedes ver, los dos últimos registros muestran NULL en ambas columnas ya que representan a un departamento sin empleados y a un empleado sin departamento asignado en la tabla empleados.
