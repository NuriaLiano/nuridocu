# EJERCICIOS SELECT

~~~sql

CREATE TABLE empleados (
  id INT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  departamento VARCHAR(50) NOT NULL,
  salario DECIMAL(10, 2) NOT NULL
);

INSERT INTO empleados (id, nombre, departamento, salario) VALUES
  (1, 'Juan', 'Ventas', 5000.00),
  (2, 'Pedro', 'Marketing', 6000.00),
  (3, 'Maria', 'Finanzas', 7000.00),
  (4, 'Ana', 'Ventas', 4500.00),
  (5, 'Carlos', 'Marketing', 5500.00),
  (6, 'Luis', 'Finanzas', 8000.00);

~~~

## EJERCICIO 1 - SELECT ALL/DISTINCT 

1. Seleccionar todos los registros de la tabla empleados

   ~~~sql
   SELECT * FROM empleados;
   ~~~

2. Agregamos ORDER BY para ordenar los resultados por departamento

   ~~~sql
   SELECT * FROM empleados ORDER BY departamento;
   ~~~

3. Utilizamos SELECT DISTINCT para seleccionar los departamentos únicos en la tabla empleados

   ~~~sql
   SELECT DISTINCT departamento FROM empleados;
   ~~~

4. Utilizamos SELECT DISTINCT y WHERE para seleccionar los nombres únicos de los empleados que trabajan en el departamento de Finanzas.

   ~~~sql
   SELECT DISTINCT nombre FROM empleados WHERE departamento = 'Finanzas';
   ~~~

## EJERCICIO 2 - OPERADORES COMPARACION

Queremos seleccionar todos los empleados que ganan un salario mayor o igual a $6,000

   ~~~sql
   SELECT * FROM empleados WHERE salario >= 6000.00;
   ~~~

**RESULTADO**
| id | nombre | departamento | salario |
| ------ | --------- | -------- | ------- |
| 2   | Pedro     | Marketing | 6000.00 |
| 3   | Maria   | Finanzas | 7000.00 |
| 6  | Luis     | Finanzas | 8000.00 |

## EJERCICIO 3 - OPERADORES LÓGICOS

Supongamos que queremos seleccionar los empleados que trabajan en el departamento de Marketing o cuyo salario sea mayor a $7,000.

~~~sql
SELECT * FROM empleados WHERE departamento = 'Marketing' OR salario > 7000.00;
~~~

**RESULTADO**
+----+-------+-----------+---------+
| id | nombre| departamento | salario |
+----+-------+-----------+---------+
| 1  | Juan  | Ventas    | 5000.00 |
| 2  | Pedro | Marketing | 6000.00 |
| 3  | Maria | Finanzas  | 7000.00 |
| 4  | Ana   | Marketing | 7500.00 |
| 6  | Luis  | Finanzas  | 8000.00 |
+----+-------+-----------+---------+

En resumen, los operadores lógicos se utilizan para combinar condiciones en una consulta SQL y devolver registros que cumplan con todas o algunas de las condiciones especificadas.

## EJERCICIO 4 - OPERADORES ARITMÉTICOS CON FUNCIONES

Queremos calcular el salario promedio de todos los empleados en la tabla empleados

~~~sql
SELECT AVG(salario) AS salario_promedio FROM empleados;
~~~

**RESULTADO**
+-----------------+
| salario_promedio |
+-----------------+
| 6166.66666666667 |
+-----------------+

## EJERCICIO 4bis - OPERADORES ARITMÉTICOS SIN FUNCIONES

Queremos seleccionar los empleados cuyo salario **anual** sea mayor a $80,000.

~~~sql
SELECT * FROM empleados WHERE salario * 12 > 80000.00;
~~~

**RESULTADO**
+----+-------+-----------+---------+
| id | nombre| departamento | salario |
+----+-------+-----------+---------+
| 3  | Maria | Finanzas  | 7000.00 |
| 4  | Ana   | Marketing | 7500.00 |
| 6  | Luis  | Finanzas  | 8000.00 |
+----+-------+-----------+---------+

En resumen, los operadores aritméticos se utilizan para realizar operaciones matemáticas en los valores de las columnas de una tabla en una consulta SQL.

## EJERCICIO 5 - OPERADORES IS NULL/IS NOT NULL

Queremos seleccionar los empleados que no tienen asignado un número de teléfono en la tabla empleados

~~~sql
SELECT * FROM empleados WHERE telefono IS NULL;
SELECT * FROM empleados WHERE telefono IS NOT NULL;
~~~

**RESULTADO IS NULL**
+----+-------+-----------+---------+
| id | nombre| departamento | salario |
+----+-------+-----------+---------+
| 5  | Pablo | Ventas    | 6500.00 |
+----+-------+-----------+---------+

**RESULTADO IS NOT NULL**
+----+-------+-----------+---------+--------------+
| id | nombre| departamento | salario | telefono    |
+----+-------+-----------+---------+--------------+
| 1  | Juan  | Ventas    | 5000.00 | 555-1234     |
| 2  | Pedro | Marketing | 6000.00 | 555-2345     |
| 3  | Maria | Finanzas  | 7000.00 |              |
| 4  | Ana   | Marketing | 7500.00 | 555-3456     |
| 6  | Luis  | Finanzas  | 8000.00 | 555-4567     |
+----+-------+-----------+---------+--------------+

En resumen, los operadores IS NULL e IS NOT NULL se utilizan para verificar si una columna de una tabla tiene valores nulos o no nulos en una consulta SQL.

## EJERCICIO 6 - ORDER BY

Queremos obtener los registros de la tabla empleados ordenados por salario de forma descendente.

~~~sql
SELECT * FROM empleados ORDER BY salario DESC;
~~~

**RESULTADO**
+----+-------+-----------+---------+--------------+
| id | nombre| departamento | salario | telefono    |
+----+-------+-----------+---------+--------------+
| 6  | Luis  | Finanzas  | 8000.00 | 555-4567     |
| 4  | Ana   | Marketing | 7500.00 | 555-3456     |
| 3  | Maria | Finanzas  | 7000.00 |              |
| 2  | Pedro | Marketing | 6000.00 | 555-2345     |
| 5  | Pablo | Ventas    | 6500.00 |              |
| 1  | Juan  | Ventas    | 5000.00 | 555-1234     |
+----+-------+-----------+---------+--------------+

En resumen, la cláusula ORDER BY se utiliza para ordenar los resultados de una consulta SQL según los valores de una o varias columnas en orden ascendente o descendente.

## EJERCICIO 7 - LIMIT

Queremos obtener los dos empleados con el salario más alto en la tabla empleados y limitar el el resultado a dos registros.

~~~sql
SELECT * FROM empleados ORDER BY salario DESC LIMIT 2;
~~~

**RESULTADO**
+----+------+-----------+---------+--------------+
| id | nombre| departamento | salario | telefono    |
+----+------+-----------+---------+--------------+
| 6  | Luis | Finanzas  | 8000.00 | 555-4567     |
| 4  | Ana  | Marketing | 7500.00 | 555-3456     |
+----+------+-----------+---------+--------------+

## EJERCICIO 8 - INTO OUTFILE

Queremos guardar los registros de la tabla empleados en un archivo llamado empleados.txt ubicado en la carpeta raíz del servidor MySQL.

~~~sql
-- Sobre escribe lo que este en el fichero
SELECT * INTO OUTFILE '/empleados.txt' FROM empleados;

-- Agrega al final sin sobreescribir
SELECT * INTO OUTFILE '/empleados.txt' FROM empleados APPEND;
~~~

## EJERCICIO 9 - GROUP BY (ASC/DESC)

Queremos obtener la suma total de los salarios por departamento en la tabla empleados

~~~sql
SELECT departamento, SUM(salario) as total_salario FROM empleados GROUP BY departamento;
~~~

**RESULTADO**
+-----------+---------------+
| departamento | total_salario |
+-----------+---------------+
| Ventas    | 11500.00      |
| Marketing | 13500.00      |
| Finanzas  | 15000.00      |
+-----------+---------------+

## EJERCICIO 10 - HAVING

Queremos obtener la cantidad de empleados por departamento, pero sólo nos interesan aquellos departamentos que tengan más de 1 empleado.

~~~sql
SELECT departamento, COUNT(*) AS cantidad_empleados 
FROM empleados 
GROUP BY departamento 
HAVING COUNT(*) > 1;
~~~

Esta consulta seleccionará todos los registros de la tabla empleados y los agrupará por departamento. Luego, contará la cantidad de empleados por cada departamento y devolverá sólo aquellos registros que tengan una cantidad mayor a 1. Es decir, sólo se incluirán los departamentos que tengan más de un empleado.

**RESULTADO**
+--------------+--------------------+
| departamento | cantidad_empleados |
+--------------+--------------------+
| Finanzas     |                  2 |
| Marketing    |                  2 |
+--------------+--------------------+

En resumen, la cláusula HAVING se utiliza para filtrar los resultados de una consulta SQL que han sido agrupados mediante la cláusula GROUP BY. De esta manera, se pueden aplicar condiciones sobre los valores que han sido agregados por cada grupo.
