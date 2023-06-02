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

### Ejercicio 1.2. Comprueba que las tablas están bien relacionadas

## Ejercicio 2. Muestra el nombre de la marca y el modelo de las motos que sean de color rojo y tengan un precio inferior a 10000

## Ejercicio 3. Mostrar los nombres de los modelos que estén disponibles en color rojo pero no en color azul

## Ejercicio 4. Obtener la cantidad total de motos vendidas para cada modelo, junto con el precio promedio de las motos vendidas para cada modelo

## Ejercicio 5. Obtener los IDs de las motos cuyos modelos tienen el precio máximo en la tabla "motos"

## Ejercicio 6. Obtener los modelos de motos de la marca "Honda" que tienen un precio superior al precio máximo de las motos de la marca "Yamaha"

## Ejercicio 7. Obtener una lista de todas las motos donde se muestre color, precio, año, cilindrada, nombre junto con el nombre de la marca correspondiente. Ordénalo de mayor a menor precio

## Ejercicio 8. Mostrar el id de las motos, el nombre del modelo, la cilindrada, el año, el color y el precio de todas las motos de color negro

## Ejercicio 9. Debemos asegurarnos de que el precio de una moto nunca sea inferior al precio mínimo registrado para ese modelo en la tabla "motos"

## Ejercicio 10. Queremos mantener actualizado un contador en la tabla "modelos" que registre el número de motos asociadas a cada modelo

>:black_joker: **PISTA** : el contador es un campo de la tabla 'modelos'

## Ejercicio 11. Necesitamos guardar el precio anterior de una moto cada vez que se actualice. El registro debe contener el ID de la moto, el precio anterior y la fecha de actualizacion

>:black_joker: **PISTA** : hace falta una tabla para guardar los precios antiguos
>:black_joker: **PISTA** : para añadir la fecha de actualizacion puedes utilizar 'current_timestamp'
>:pencil: **NOTA** : 'current_timestamp' es una funcion que proporciona la fecha y la hora del momento en que se ejecuta.

### ¿Cuando usar OLD y NEW?

## Ejercicio 12. Cada vez que se actualice una moto, se registrará la actualización en la tabla "registros_actualizaciones"

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
        RETURN NEW;
    END;
    $$
    LANGUAGE plpgsql;

-- Crear trigger para la tabla motos
CREATE TRIGGER trigger_registrar_actualizacion
    AFTER UPDATE ON motos
    FOR EACH ROW
    EXECUTE FUNCTION registrar_actualizacion();
~~~

### ¿Cuándo usar 'RETURN OLD' y 'RETURN NEW'?

## Ejercicio 13. Obtén el id de la moto, el nombre de la marca, el nombre del modelo, el año y la cilindrada de las motos cuyo color es 'Negro

>:black_joker: **PISTA** : número de errores a corregir: 3

~~~sql
SELECT mt.id, m.nombre AS marca, modelo.nombre AS modelo, mo.año, mo.cilindrada
FROM marcas AS m
JOIN modelos AS mo ON mo.marca_id = m.id
JOIN motos AS mt ON mo.id = mt.modelo_id
WHERE mo.color = 'Negro';
~~~

## Ejercicio 14. Añade una restricción única a la tabla "marcas" llamada "uq_ide" que asegure que el campo "id" sea único

>:black_joker: **PISTA** : número de errores a corregir: 1

~~~sql
ALTER TABLE marcas
ADD CONSTRAINT uq_ide UNIQUE (id);
~~~

## Ejercicio 15. Obtén el color y precio de las motos del modelo "Ninja ZX-10R", ordenadas por precio de forma descendente

>:black_joker: **PISTA** : número de errores a corregir: 3

~~~sql
SELECT color, precio
FROM motos
WHERE modelo_id = (
    SELECT id
    FROM modelos
)
ORDER BY precio MIN
WHERE nombre = 'Ninja ZX-10R';

~~~

## ¿Diferencias entre subconsultas y joins?
