# Ejercicio disparadores, funciones, joins, consultas, subconsultas

## Crear base de datos y tablas

~~~sql
CREATE DATABASE motos;
\c motos;

CREATE TABLE marcas (
    id SERIAL,
    nombre VARCHAR(100)
);

CREATE TABLE modelos (
    id SERIAL,
    nombre VARCHAR(100),
    marca_id INTEGER,
    año INTEGER,
    cilindrada INTEGER
);

CREATE TABLE motos (
    id SERIAL,
    modelo_id INTEGER,
    color VARCHAR(50),
    precio NUMERIC(8, 2)
);
~~~

## Añadir información a las tablas

~~~sql
-- Añadir marcas
INSERT INTO marcas (nombre) VALUES ('Honda'), ('Yamaha'), ('Suzuki'), ('Kawasaki');

-- Añadir modelos
INSERT INTO modelos (nombre, marca_id, año, cilindrada) VALUES
    ('CBR500R', 1, 2022, 500),
    ('YZF-R6', 2, 2021, 600),
    ('GSX-R750', 3, 2020, 750),
    ('Ninja ZX-10R', 4, 2023, 1000);

-- Añadir motos
INSERT INTO motos (modelo_id, color, precio) VALUES
    (1, 'Rojo', 8000),
    (2, 'Azul', 9000),
    (3, 'Negro', 11000),
    (4, 'Verde', 12000);
~~~

## Ejercicio 1. Asegurate de que el precio de las motos siempre sea mayor que 0 ¿Tienes que utilizar constraint o triggers?

~~~sql
ALTER TABLE motos
ADD CONSTRAINT chk_precio_positivo CHECK (precio > 0);
~~~

### Ejercicio 1.2. Comprueba que las tablas están bien relacionadas

~~~sql
-- Añadir primary key a la tabla marcas
ALTER TABLE marcas
ADD CONSTRAINT pk_marcas PRIMARY KEY (id);

-- Añadir primary key a la tabla modelos
ALTER TABLE modelos
ADD CONSTRAINT pk_modelos PRIMARY KEY (id);

-- Añadir foreign key a la tabla modelos (referencia a la tabla marcas)
ALTER TABLE modelos
ADD CONSTRAINT fk_modelos_marcas FOREIGN KEY (marca_id)
REFERENCES marcas(id);

-- Añadir primary key a la tabla motos
ALTER TABLE motos
ADD CONSTRAINT pk_motos PRIMARY KEY (id);

-- Añadir foreign key a la tabla motos (referencia a la tabla modelos)
ALTER TABLE motos
ADD CONSTRAINT fk_motos_modelos FOREIGN KEY (modelo_id)
REFERENCES modelos(id);
~~~

## Ejercicio 2. Muestra el nombre de la marca y el modelo de las motos que sean de color rojo y tengan un precio inferior a 10000 (select con multitablas)

~~~sql
SELECT m.nombre AS marca, mod.nombre AS modelo
FROM marcas m, modelos mod, motos mo
WHERE mod.marca_id = m.id
  AND mo.modelo_id = mod.id
  AND mo.color = 'Rojo'
  AND mo.precio < 10000;
~~~

## Ejercicio 3. Mostrar los nombres de los modelos que estén disponibles en color rojo pero no en color azul (except)

~~~sql
SELECT nombre
FROM modelos
WHERE color = 'Rojo'

EXCEPT

SELECT nombre
FROM modelos
WHERE color = 'Azul';

-- sin except
SELECT nombre
FROM modelos
WHERE color = 'rojo'
  AND nombre NOT IN (SELECT nombre FROM modelos WHERE color = 'azul');
~~~

## Ejercicio 4. Obtener la cantidad total de motos vendidas para cada modelo, junto con el precio promedio de las motos vendidas para cada modelo (subconsultas con group by)

~~~sql
SELECT modelos.nombre AS modelo,
       COUNT(*) AS total_ventas,
       AVG(motos.precio) AS precio_promedio
FROM modelos
JOIN motos ON modelos.id = motos.modelo_id
GROUP BY modelos.nombre;
~~~

## Ejercicio 5. Obtener los IDs de las motos cuyos modelos tienen el precio máximo en la tabla "motos" (subconsultas nivel medio)

~~~sql
SELECT m.id
FROM motos AS m
WHERE m.modelo_id IN (
    SELECT modelo_id
    FROM motos
    WHERE precio = (
        SELECT MAX(precio)
        FROM motos
    )
);
~~~

## Ejercicio 6. Obtener los modelos de motos de la marca "Honda" que tienen un precio superior al precio máximo de las motos de la marca "Yamaha" (subconsultas nivel extremo)

~~~sql
SELECT nombre
FROM modelos
WHERE marca_id = (
    SELECT id
    FROM marcas
    WHERE nombre = 'Honda'
) AND precio > (
    SELECT MAX(precio)
    FROM motos
    WHERE modelo_id IN (
        SELECT id
        FROM modelos
        WHERE marca_id = (
            SELECT id
            FROM marcas
            WHERE nombre = 'Yamaha'
        )
    )
);
~~~

## Ejercicio 7. Obtener una lista de todas las motos donde se muestre color, precio, año, cilindrada, nombre junto con el nombre de la marca correspondiente. Ordénalo de mayor a menor precio (join)

~~~sql
SELECT m.color, m.precio, mo.año, mo.cilindrada, mo.nombre AS modelo, ma.nombre AS marca
FROM motos m
JOIN modelos mo ON m.modelo_id = mo.id
JOIN marcas ma ON mo.marca_id = ma.id
ORDER BY m.precio DESC;
~~~

## Ejercicio 8. Mostrar el id de las motos, el nombre del modelo, la cilindrada, el año, el color y el precio de todas las motos de color negro (join)

~~~sql
SELECT m.id AS "ID de la moto", mo.nombre AS "Nombre del modelo", mo.cilindrada, mo.año, m.color, m.precio
FROM motos m
JOIN modelos mo ON m.modelo_id = mo.id
WHERE m.color = 'Negro';
~~~

## Ejercicio 9. Debemos asegurarnos de que el precio de una moto nunca sea inferior al precio mínimo registrado para ese modelo en la tabla "motos" (trigger con subconsultas)

~~~sql
CREATE OR REPLACE FUNCTION verificar_precio_minimo()
    RETURNS TRIGGER
    AS $$
    DECLARE
        precio_minimo NUMERIC(8, 2);
    BEGIN
        SELECT MIN(precio) INTO precio_minimo
        FROM motos
        WHERE modelo_id = NEW.modelo_id;

        IF NEW.precio < precio_minimo THEN
            RAISE EXCEPTION 'El precio de la moto no puede ser inferior al precio mínimo registrado para ese modelo';
        END IF;

        RETURN NEW;
    END;
    $$
    LANGUAGE plpgsql;

CREATE TRIGGER verificar_precio_minimo_trigger
    BEFORE INSERT OR UPDATE ON motos
    FOR EACH ROW
    EXECUTE FUNCTION verificar_precio_minimo();
~~~

## Ejercicio 10. Queremos mantener actualizado un contador en la tabla "modelos" que registre el número de motos asociadas a cada modelo.(trigger con join)

>:black_joker: **PISTA** : el contador es un campo de la tabla 'modelos'

~~~sql
ALTER TABLE modelos
ADD COLUMN contador_motos INTEGER DEFAULT 0;
~~~

~~~sql
CREATE OR REPLACE FUNCTION actualizar_contador_motos()
    RETURNS TRIGGER
    AS $$
    BEGIN
        -- Actualizar el contador de motos para el modelo afectado
        UPDATE modelos
        SET contador_motos = (
            SELECT COUNT(*)
            FROM motos
            JOIN modelos ON motos.modelo_id = modelos.id
            WHERE modelos.id = NEW.modelo_id
        )
        WHERE id = NEW.modelo_id;

        RETURN NULL;
    END;
    $$
    LANGUAGE plpgsql;

CREATE TRIGGER actualizar_contador_motos_trigger
    AFTER INSERT OR UPDATE OR DELETE ON motos
    FOR EACH ROW
    EXECUTE FUNCTION actualizar_contador_motos();

-- con subconsulta

CREATE OR REPLACE FUNCTION actualizar_contador_motos()
    RETURNS TRIGGER
    AS $$
    BEGIN
        -- Actualizar el contador de motos para el modelo afectado
        UPDATE modelos
        SET contador_motos = (
            SELECT COUNT(*)
            FROM motos
            WHERE motos.modelo_id = modelos.id
        )
        WHERE id = NEW.modelo_id;

        RETURN NULL;
    END;
    $$
    LANGUAGE plpgsql;

CREATE TRIGGER actualizar_contador_motos_trigger
    AFTER INSERT OR UPDATE OR DELETE ON motos
    FOR EACH ROW
    EXECUTE FUNCTION actualizar_contador_motos();
~~~

## Ejercicio 11. Necesitamos guardar el precio anterior de una moto cada vez que se actualice. El registro debe contener el ID de la moto, el precio anterior y la fecha de actualizacion(trigger con old y new)

>:black_joker: **PISTA** : hace falta una tabla para guardar los precios antiguos
>:black_joker: **PISTA** : para añadir la fecha de actualizacion puedes utilizar 'current_timestamp'
>:pencil: **NOTA** : 'current_timestamp' es una funcion que proporciona la fecha y la hora del momento en que se ejecuta.

~~~sql
-- Crear tabla de registros de precios antiguos
CREATE TABLE registros_precios (
    id SERIAL,
    moto_id INTEGER,
    precio_anterior NUMERIC(8, 2),
    fecha_actualizacion TIMESTAMP DEFAULT current_timestamp
);
~~~

~~~sql
-- Crear función para el trigger
CREATE OR REPLACE FUNCTION actualizar_precio_anterior()
    RETURNS TRIGGER
    AS $$
    BEGIN
        IF TG_OP = 'UPDATE' THEN
            INSERT INTO registros_precios (moto_id, precio_anterior)
            VALUES (NEW.id, OLD.precio);
        END IF;
        RETURN NEW;
    END;
    $$
    LANGUAGE plpgsql;

-- Crear trigger para la tabla motos
CREATE TRIGGER trigger_actualizar_precio_anterior
    AFTER UPDATE ON motos
    FOR EACH ROW
    EXECUTE FUNCTION actualizar_precio_anterior();
~~~

### ¿Cuando usar OLD y NEW?

Se utiliza OLD para acceder a los valores antiguos antes de la modificación y NEW para acceder a los valores nuevos después de la modificación. La elección de cuál utilizar depende del tipo de operación (INSERT, UPDATE o DELETE) y de qué valores se necesitan para realizar la lógica específica del trigger.

- OLD representa los valores antiguos de las filas afectadas antes de la modificación.
  - En un trigger AFTER INSERT, esta variable es nula, ya que no existen valores antiguos.
  - En un trigger AFTER DELETE, OLD contiene los valores de las filas eliminadas.
  - En un trigger AFTER UPDATE, OLD contiene los valores antiguos de las filas antes de la actualización.
- NEW representa los valores nuevos de las filas afectadas después de la modificación.
  - En un trigger AFTER INSERT, NEW contiene los valores de las filas recién insertadas.
  - En un trigger AFTER DELETE, esta variable es nula, ya que no existen filas nuevas.
  - QEn un trigger AFTER UPDATE, NEW contiene los valores actualizados de las filas.

## Ejercicio 12. Cada vez que se actualice una moto, se registrará la actualización en la tabla "registros_actualizaciones" (trigger mal hecho para corregir)

>:black_joker: **PISTA** : número de errores a corregir: 1

~~~sql
-- Crear tabla de registros de actualizaciones
CREATE TABLE registros_actualizaciones (
    id SERIAL,
    moto_id INTEGER,
    fecha_actualizacion TIMESTAMP DEFAULT current_timestamp
);

-- Crear función para el trigger
CREATE OR REPLACE FUNCTION registrar_actualizacion()
    RETURNS TRIGGER
    AS $$
    BEGIN
        INSERT INTO registros_actualizaciones (moto_id)
        VALUES (OLD.id);
        RETURN NEW; -- Error: Debería ser "RETURN OLD;"
    END;
    $$
    LANGUAGE plpgsql;

-- Crear trigger para la tabla motos
CREATE TRIGGER trigger_registrar_actualizacion
    AFTER UPDATE ON motos
    FOR EACH ROW
    EXECUTE FUNCTION registrar_actualizacion();
~~~

Error en la función registrar_actualizacion(): El trigger actualmente devuelve RETURN NEW;, pero debería devolver RETURN OLD;. Esto se debe a que se trata de un trigger AFTER UPDATE, por lo que el valor NEW contiene los datos actualizados y no los datos anteriores. Para registrar la actualización correctamente, debemos devolver los valores antiguos (OLD).

### ¿Cuándo usar 'RETURN OLD' y 'RETURN NEW'?

- **RETURN NEW**: Se utiliza en triggers AFTER INSERT, AFTER UPDATE, y AFTER DELETE. Permite devolver la fila modificada o insertada después de la operación realizada. Es decir, devuelve los nuevos valores de la fila después de la actualización o inserción.
- **RETURN OLD**: Se utiliza en triggers BEFORE UPDATE y BEFORE DELETE. Devuelve los valores antiguos de la fila antes de la modificación o eliminación.

En resumen, RETURN NEW se utiliza en triggers AFTER para obtener los valores actualizados o insertados, mientras que RETURN OLD se usa en triggers BEFORE para acceder a los valores originales antes de la modificación o eliminación.

## Ejercicio 13. Obtén el id de la moto, el nombre de la marca, el nombre del modelo, el año y la cilindrada de las motos cuyo color es 'Negro (join mal hecho para corregir)

~~~sql
-- Ejercicio con errores
SELECT mt.id, m.nombre AS marca, modelo.nombre AS modelo, mo.año, mo.cilindrada
FROM marcas AS m
JOIN modelos AS mo ON mo.marca_id = m.id
JOIN motos AS mt ON mo.id = mt.modelo_id
WHERE mo.color = 'Negro';
-- Consulta corregida
SELECT mt.id, m.nombre AS marca, mo.nombre AS modelo, mo.año, mo.cilindrada
FROM marcas AS m
JOIN modelos AS mo ON m.id = mo.marca_id
JOIN motos AS mt ON mo.id = mt.modelo_id
WHERE mt.color = 'Negro';
~~~

1. Error en la selección de columna de la tabla modelos: En la primera consulta, se utiliza el alias incorrecto modelo en lugar de mo al seleccionar la columna nombre
2. Error en la cláusula JOIN de la tabla modelos: En la primera consulta, se invierten las columnas en la condición de unión mo.marca_id = m.id
3. Error en la cláusula WHERE: En la primera consulta, se utiliza el alias incorrecto mo.color en lugar de mt.color para filtrar por el color 'Negro'

## Ejercicio 14. Añade una restricción única a la tabla "marcas" llamada "uq_ide" que asegure que el campo "id" sea único (constraint mal hecho para corregir)

~~~sql
ALTER TABLE marcas
ADD CONSTRAINT uq_ide UNIQUE (id);
~~~

El cambo id ya tiene implícito la restricción de 'unique' puesto que es de tipo 'SERIAL'

## Ejercicio 15. Obtén el color y precio de las motos del modelo "Ninja ZX-10R", ordenadas por precio de forma descendente. (subconsulta mal hecho para corregir)

~~~sql
-- Consulta con errores
SELECT color, precio
FROM motos
WHERE modelo_id = (
    SELECT id
    FROM modelos
)
ORDER BY precio MIN;  -- Error 1: Faltaba un punto y coma al final de la línea
WHERE nombre = 'Ninja ZX-10R'; -- Error 2: Se colocó una cláusula WHERE después de la cláusula ORDER BY

-- Consulta corregida
SELECT color, precio
FROM motos
WHERE modelo_id = (
    SELECT id
    FROM modelos
    WHERE nombre = 'Ninja ZX-10R'
)
ORDER BY precio DESC;
~~~

1. No se puede ordenar por MIN, tendria que ser por DESC
2. Se ha colocado una clausula WHERE después de ORDER BY.
3. La última cláusula WHERE debería ir dentro de la subconsulta.

## ¿Diferencias entre subconsultas y joins?

1. Sintaxis: Los joins se expresan utilizando las cláusulas JOIN, como INNER JOIN, LEFT JOIN, RIGHT JOIN, etc., que se utilizan para unir dos o más tablas en función de una condición de unión especificada. Las subconsultas, por otro lado, son consultas anidadas que se incluyen dentro de otra consulta.
2. Momento de evaluación: Los joins se evalúan como parte de la consulta principal y se unen las filas que cumplen con la condición de unión. Las subconsultas, por otro lado, se evalúan por separado y se utilizan como una fuente de datos para la consulta principal.
3. Rendimiento: En general, los joins suelen ser más eficientes en términos de rendimiento, especialmente cuando se trabaja con grandes conjuntos de datos, ya que permiten que el motor de base de datos optimice la consulta y utilice índices y estrategias de unión eficientes. Las subconsultas pueden ser menos eficientes en algunos casos, especialmente cuando se utilizan subconsultas correlacionadas que se ejecutan para cada fila de la consulta principal.
4. Legibilidad y mantenibilidad: Las subconsultas pueden ser más fáciles de entender y leer en algunas situaciones, ya que se pueden utilizar dentro de cláusulas como WHERE, FROM, SELECT, etc., lo que permite una lógica más concisa y legible. Los joins, especialmente cuando se utilizan en consultas complejas con múltiples tablas y condiciones de unión, pueden volverse más complejos y difíciles de seguir.

En resumen, los joins y las subconsultas son herramientas complementarias en PostgreSQL que se utilizan para combinar datos de diferentes tablas en una consulta. La elección entre ellos depende de los requisitos específicos de la consulta, la legibilidad del código y el rendimiento esperado. En general, se recomienda utilizar joins cuando sea posible y reservar las subconsultas para casos en los que sean más adecuadas y fáciles de entender.
