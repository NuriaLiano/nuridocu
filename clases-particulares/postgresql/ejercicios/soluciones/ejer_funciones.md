# Ejercicios de funciones con lenguaje PLPGSQL

Crearemos una base de datos ficticia para una tienda de música y crearemos una función que calculará el precio total de una compra de discos.

~~~sql
CREATE DATABASE tienda_musica;

\c tienda_musica;

CREATE TABLE discos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    artista VARCHAR(100),
    precio NUMERIC(8,2)
);

CREATE TABLE compras (
    id SERIAL PRIMARY KEY,
    fecha DATE,
    disco_id INTEGER,
    cantidad INTEGER,
    FOREIGN KEY (disco_id) REFERENCES discos (id)
);
~~~

~~~sql
INSERT INTO compras (fecha, disco_id, cantidad) VALUES
    ('2023-05-01', 1, 2),
    ('2023-05-02', 2, 3),
    ('2023-05-03', 3, 1);
INSERT INTO discos (nombre, artista, precio) VALUES
    ('Album A', 'Artista 1', 12.99),
    ('Album B', 'Artista 2', 9.99),
    ('Album C', 'Artista 3', 14.99);
~~~

## Ejercicio 1. Crearemos una función que calculará el precio total de una compra de discos

~~~sql
CREATE OR REPLACE FUNCTION calcular_precio_total(compra_id INTEGER)
    RETURNS NUMERIC(8,2)
    AS $$
    DECLARE
        total NUMERIC(8,2);
        cantidad INTEGER;
        precio NUMERIC(8,2);
    BEGIN
        SELECT cantidad, discos.precio INTO cantidad, precio
        FROM compras
        INNER JOIN discos ON compras.disco_id = discos.id
        WHERE compras.id = compra_id;
        
        total := cantidad * precio;
        
        RETURN total;
    END;
    $$
    LANGUAGE plpgsql;

-- opcion 2
CREATE OR REPLACE FUNCTION calcular_precio_total(p_compra_id INTEGER)
  RETURNS DECIMAL AS
$$
DECLARE
  total DECIMAL := 0;
  precio DECIMAL;
  cantidad INTEGER;
BEGIN
  SELECT COUNT(*) INTO cantidad FROM compras WHERE id = p_compra_id;
  
  IF cantidad = 0 THEN
    RAISE EXCEPTION 'No se encontró una compra con el ID proporcionado';
  END IF;
  
  SELECT d.precio INTO precio
  FROM discos d
  INNER JOIN compras c ON c.disco_id = d.id
  WHERE c.id = p_compra_id;
  
  total := precio * cantidad;
  
  RETURN total;
END;
$$
LANGUAGE plpgsql;
~~~

~~~sql
SELECT calcular_precio_total(1);
~~~

## Ejercicio 2. Calculará el monto total gastado por un cliente en sus compras

>:black_joker: **PISTA** es necesario crear una columna  'id_cliente' y asignale el id de un cliente para poder pasarlo como parámetro

~~~sql

-- agregar columna id_cliente

ALTER TABLE compras
ADD COLUMN cliente_id INTEGER;

-- actualizar los datos asignando un valor de 1. Supongamos que todos los registros pertenecen al cliente con cliente_id igual a 1

UPDATE compras
SET cliente_id = 1;

-- funcion

CREATE OR REPLACE FUNCTION calcular_monto_total(p_cliente_id INTEGER)
    RETURNS NUMERIC(8,2)
    AS $$
    DECLARE
        total NUMERIC(8,2) := 0;
    BEGIN
        SELECT SUM(discos.precio * compras.cantidad)
        INTO total
        FROM compras
        INNER JOIN discos ON compras.disco_id = discos.id
        WHERE compras.cliente_id = p_cliente_id;
        
        RETURN total;
    END;
    $$
    LANGUAGE plpgsql;
~~~

La función calcular_monto_total recibe como parámetro el cliente_id y utiliza una variable total para almacenar la suma total del monto gastado por el cliente en todas sus compras. Realiza una consulta que combina las tablas compras y discos mediante una unión (INNER JOIN) y utiliza la cláusula WHERE para filtrar por el cliente_id. Luego, multiplica el precio de cada disco por la cantidad comprada y realiza la suma total.

Finalmente, la función retorna el valor de total, que representa el monto total gastado por el cliente.

Puedes llamar a esta función pasando como argumento el cliente_id correspondiente para obtener el monto total gastado por ese cliente en todas sus compras.

## Ejercicio 3. Crearemos un disparador (trigger) en la tabla compras que se active después de insertar nuevos registros. El disparador actualizará automáticamente el campo fecha de la compra con la fecha actual

~~~sql
-- Crear el disparador
CREATE OR REPLACE FUNCTION actualizar_fecha_compra()
    RETURNS TRIGGER AS $$
BEGIN
    NEW.fecha := CURRENT_DATE;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER despues_insertar_compra
AFTER INSERT ON compras
FOR EACH ROW
EXECUTE FUNCTION actualizar_fecha_compra();
~~~

En este caso, hemos creado una función actualizar_fecha_compra() que se ejecutará como un disparador después de insertar un nuevo registro en la tabla compras. La función establece el campo fecha de la nueva fila con la fecha actual utilizando CURRENT_DATE. Luego, el disparador devuelve la nueva fila modificada.

**PARA PROBAR**

~~~sql
INSERT INTO compras (disco_id, cantidad, cliente_id) VALUES (1, 2, 1);
~~~
