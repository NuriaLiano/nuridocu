# Solución examen BBDD

## Ejercicio 1

Qué requisitos debe cumplir un atributo para admitir la clausula AUTO_INCREMENT

Respuesta:

## Ejercicio 2

~~~sql
SET AUTOCOMMIT = 0
INSERT INTO tabla VALUES (1);

-- S1
SELECT * FROM tabla;
ROLLBACK

--S2
SELECT * FROM tabla;
INSERT INTO tabla VALUES (2);

--S3
SELECT * FROM tabla;
COMIT;

--S4
SELECT * FROM tabla;
SAVEPOINT UNO;
ROLLBACK;
INSERT INTO tabla VALUES (3);

--S5
SELECT * FROM tabla;
SET @X:=10;

--S6
SELECT @X X+@Y-10;
ROLLBACK TO SAVEPOINT UNO;

--S7
SELECT * FROM tabla;
ROLLBACK;
~~~

1. Corrige los errores sintácticos (4) en el siguiente código (aquellos que no permitan ejecutar las sentencia)

~~~sql
SET AUTOCOMMIT = 0
INSERT INTO tabla VALUES (1);

-- S1: Error de sintaxis en la consulta ROLLBACK, debe ser ROLLBACK WORK;
SELECT * FROM tabla;
ROLLBACK WORK;

-- S2: La consulta SELECT no se verá afectada por la consulta INSERT, debe ser COMMIT en lugar de COMIT.
INSERT INTO tabla VALUES (2);
SELECT * FROM tabla;
COMMIT;

-- S3: No hay una consulta previa para hacer commit, debe ser SELECT * FROM tabla; en lugar de SELECT * FROM table;
SELECT * FROM tabla;
COMMIT;

-- S4: Error de sintaxis en la consulta SAVEPOINT, debe ser SAVEPOINT UNO; en lugar de SAVEPOINT UNO;
SELECT * FROM tabla;
SAVEPOINT UNO;
ROLLBACK TO SAVEPOINT UNO;
INSERT INTO tabla VALUES (3);

--S5
SELECT * FROM tabla;
SET @X:=10;

-- S6: Error de sintaxis en la consulta SELECT, falta el operador de asignación, debe ser SELECT @X:=X+@Y-10;
SELECT @X:=X+@Y-10;
ROLLBACK TO SAVEPOINT UNO;

-- S7: Error de sintaxis en la consulta ROLLBACK, debe ser ROLLBACK WORK;
SELECT * FROM tabla;
ROLLBACK WORK;
~~~

>NOTAS
>
>1. **AUTOCOMMIT = 0** configuración que determina si una transacción se confirmará automáticamente o si se requiere una confirmación explícita (commit).
>2. **ROLLBACK WORK** se asegura que cualquier cambio realizado en la base de datos durante la transacción actual se deshaga y se restaure a su estado anterior.

1. Indica la información mostrada por cada una de ellas.

## Ejercicio 3

~~~sql
SELECT DISTINCT np
FROM ped
GROUP BY np
HAVING COUNT(DISTINCT na) (SELECT COUNT a FROM art);
~~~

1. Corrige los errores sintácticos (3) o de compilación del código del recuadro

**RESPUESTA**

~~~sql
SELECT DISTINCT np
FROM ped
GROUP BY np
HAVING COUNT(DISTINCT na) = (SELECT COUNT(*) FROM art);
~~~

2. Indica cuál sería el enunciado que define su funcionalidad

   **RESPUESTA**
    Busca todos los valores únicos en la columna "np" de la tabla "ped" que tienen un número de valores distintos en la columna "na" igual a la cantidad de filas en la tabla "art".
