# EJERCICIOS SUBCONSULTAS

~~~sql
CREATE DATABASE ventas3;

CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    id_cliente INT,
    fecha DATE,
    cantidad DECIMAL(8, 2)
);

INSERT INTO pedidos VALUES
    (1, 1, '2022-01-01', 100.00),
    (2, 2, '2022-01-02', 200.00),
    (3, 1, '2022-01-03', 150.00),
    (4, 3, '2022-01-04', 300.00);

CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nombre VARCHAR(50)
);

INSERT INTO clientes VALUES
    (1, 'Juan'),
    (2, 'María'),
    (3, 'Pedro'); 
~~~

# EJERCICIO 1

Obtener los nombres de los clientes que han realizado algún pedido

~~~sql
SELECT nombre
FROM clientes
WHERE id IN (SELECT id_cliente FROM pedidos);
~~~

En este ejemplo, la subconsulta se encuentra en la cláusula WHERE de la consulta principal. La subconsulta devuelve una lista de valores, los identificadores de los clientes que han realizado algún pedido, que se utilizan en la cláusula WHERE para filtrar los resultados de la consulta principal. La consulta principal devuelve los nombres de los clientes que coinciden con los identificadores obtenidos en la subconsulta.

## RESULTADO

| nombre |
|--------|
| Juan   |
| María  |
| Pedro  |

En este caso, los nombres de los tres clientes aparecen en la tabla de resultados porque cada uno ha realizado al menos un pedido en la tabla "pedidos".

# EJERCICIO 2 - DEVOLVIENDO VALOR y FUNCIONES

Supongamos que queremos obtener la cantidad total de dinero que se ha gastado en pedidos por el cliente con el identificador "1".

~~~sql
SELECT SUM(cantidad) AS total_gastado
FROM pedidos
WHERE id_cliente = (
    SELECT id
    FROM clientes
    WHERE nombre = 'Juan'
);
~~~

En este ejemplo, la subconsulta se utiliza en la cláusula WHERE de la consulta principal para filtrar los registros de la tabla "pedidos" que corresponden al cliente "Juan". La subconsulta devuelve un solo valor, el identificador del cliente "Juan", que se utiliza en la cláusula WHERE de la consulta principal para filtrar los registros de la tabla "pedidos". La consulta principal devuelve la suma de las cantidades de los pedidos realizados por el cliente "Juan".

## RESULTADO

| total_gastado |
|---------------|
|         250.00 |

En este caso, el cliente "Juan" ha realizado dos pedidos por un total de 250.00 unidades monetarias. La subconsulta devuelve el identificador del cliente "Juan", que se utiliza para filtrar los registros de la tabla "pedidos", y la consulta principal devuelve la suma de las cantidades de los pedidos correspondientes al cliente "Juan".

# EJERCICIO 3 - DEVOLVIENDO MÁS DE UNA COLUMNA e INNER JOIN

Utilizar una subconsulta para obtener el número de pedidos realizados por cada cliente, junto con su nombre.

~~~sql
SELECT clientes.nombre, pedidos.num_pedidos
FROM clientes
INNER JOIN (
    SELECT id_cliente, COUNT(*) AS num_pedidos
    FROM pedidos
    GROUP BY id_cliente
) AS pedidos
ON clientes.id = pedidos.id_cliente;
~~~

En este ejemplo, la subconsulta se encuentra en la cláusula FROM de la consulta principal, dentro de una cláusula JOIN. La subconsulta devuelve dos columnas: el identificador del cliente y el número de pedidos realizados por ese cliente. La consulta principal une esta información con los nombres de los clientes mediante un INNER JOIN, utilizando el identificador del cliente como clave de unión.

## RESULTADO

| nombre | num_pedidos |
|--------|-------------|
| Juan   |           2 |
| María  |           1 |
| Pedro  |           1 |

En este caso, la consulta devuelve una fila para cada cliente que tiene pedidos en la tabla "pedidos", mostrando su nombre y el número de pedidos que ha realizado.

# EJERCICIO 4 - 

Supongamos que queremos obtener la cantidad total de dinero que se ha gastado en pedidos por el cliente con el identificador "1".

~~~sql
SELECT SUM(cantidad) AS total_gastado
FROM pedidos
WHERE id_cliente = (
    SELECT id
    FROM clientes
    WHERE nombre = 'Juan'
);
~~~

En este ejemplo, la subconsulta se utiliza en la cláusula WHERE de la consulta principal para filtrar los registros de la tabla "pedidos" que corresponden al cliente "Juan". La subconsulta devuelve un solo valor, el identificador del cliente "Juan", que se utiliza en la cláusula WHERE de la consulta principal para filtrar los registros de la tabla "pedidos". La consulta principal devuelve la suma de las cantidades de los pedidos realizados por el cliente "Juan".

## RESULTADO

| total_gastado |
|---------------|
|         250.00 |

En este caso, el cliente "Juan" ha realizado dos pedidos por un total de 250.00 unidades monetarias. La subconsulta devuelve el identificador del cliente "Juan", que se utiliza para filtrar los registros de la tabla "pedidos", y la consulta principal devuelve la suma de las cantidades de los pedidos correspondientes al cliente "Juan".

# EJERCICIO 5 - DEVOLVIENDO CUALQUIER NÚMERO DE FILAS Y COLUMNAS

Supongamos que quieres obtener los detalles de cada pedido (identificador del pedido, fecha y cantidad) junto con el nombre del cliente que realizó el pedido y su número de teléfono. Para ello, necesitas obtener la información de los pedidos y unirla con la información de los clientes, que incluye su nombre y número de teléfono, mediante una subconsulta.

~~~sql
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    telefono VARCHAR(15)
);

INSERT INTO clientes VALUES
    (1, 'Juan', '1234567890'),
    (2, 'María', '2345678901'),
    (3, 'Pedro', '3456789012');

CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    id_cliente INT,
    fecha DATE,
    cantidad DECIMAL(8, 2)
);

INSERT INTO pedidos VALUES
    (1, 1, '2022-01-01', 100.00),
    (2, 2, '2022-01-02', 200.00),
    (3, 1, '2022-01-03', 150.00),
    (4, 3, '2022-01-04', 300.00);

SELECT pedidos.id, pedidos.fecha, pedidos.cantidad, clientes.nombre, clientes.telefono
FROM pedidos
INNER JOIN (
    SELECT id, nombre, telefono
    FROM clientes
) AS clientes
ON pedidos.id_cliente = clientes.id;
~~~

En este ejemplo, la subconsulta se encuentra en la cláusula FROM de la consulta principal, dentro de una cláusula JOIN. La subconsulta devuelve tres columnas: el identificador del cliente, su nombre y su número de teléfono. La consulta principal une esta información con los detalles de cada pedido mediante un INNER JOIN, utilizando el identificador del cliente como clave de unión.

## RESULTADO

| id | fecha       | cantidad | nombre | telefono    |
|----|-------------|----------|--------|-------------|
| 1  | 2022-01-01 | 100.00   | Juan   | 1234567890  |
| 2  | 2022-01-02 | 200.00   | María  | 2345678901  |
| 3  | 2022-01-03 | 150.00   | Juan   | 1234567890  |
| 4  | 2022-01-04 | 300.00   | Pedro  | 3456789012  |

En este caso, la consulta devuelve una fila para cada pedido en la tabla "pedidos", mostrando su identificador, fecha y cantidad, junto con el nombre y número de teléfono del cliente que realizó el pedido.
