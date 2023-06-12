# Ejercicios de subconsultas y joins

```sql
-- Creación de la base de datos
CREATE DATABASE ejercicio_subconsultas;

-- Selección de la base de datos
USE ejercicio_subconsultas;

-- Creación de la tabla "clientes"
CREATE TABLE clientes (
  id INT PRIMARY KEY,
  nombre VARCHAR(100),
  ciudad VARCHAR(100)
);

-- Inserción de datos en la tabla "clientes"
INSERT INTO clientes (id, nombre, ciudad) VALUES
  (1, 'John Smith', 'Nueva York'),
  (2, 'Maria Garcia', 'Madrid'),
  (3, 'Robert Johnson', 'Chicago'),
  (4, 'Ana Torres', 'Barcelona'),
  (5, 'David Kim', 'Los Ángeles');

-- Creación de la tabla "pedidos"
CREATE TABLE pedidos (
  id INT PRIMARY KEY,
  cliente_id INT,
  producto VARCHAR(100),
  cantidad INT,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Inserción de datos en la tabla "pedidos"
INSERT INTO pedidos (id, cliente_id, producto, cantidad) VALUES
  (1, 1, 'Camisa', 3),
  (2, 2, 'Pantalón', 2),
  (3, 3, 'Zapatos', 1),
  (4, 1, 'Chaqueta', 1),
  (5, 4, 'Vestido', 2);

-- Ejercicio 1: Obtener los nombres de los clientes que han realizado pedidos
SELECT nombre
FROM clientes
WHERE id IN (
  SELECT DISTINCT cliente_id
  FROM pedidos
);

-- Ejercicio 2: Obtener los productos y las cantidades de los pedidos realizados por clientes de Madrid
SELECT producto, cantidad
FROM pedidos
WHERE cliente_id IN (
  SELECT id
  FROM clientes
  WHERE ciudad = 'Madrid'
);

-- Ejercicio 3: Obtener los nombres de los clientes que han realizado al menos 2 pedidos
SELECT nombre
FROM clientes
WHERE id IN (
  SELECT cliente_id
  FROM pedidos
  GROUP BY cliente_id
  HAVING COUNT(*) >= 2
);

-- Ejercicio 4: Obtener el total de pedidos realizados por cada cliente
SELECT c.nombre, COUNT(*) AS total_pedidos
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.nombre;

-- Obtener los nombres de los clientes que han realizado pedidos de productos diferentes al cliente con ID 1
SELECT nombre
FROM clientes
WHERE id <> 1 AND id IN (
  SELECT DISTINCT cliente_id
  FROM pedidos);

--Obtener los productos y las cantidades de los pedidos realizados por clientes de Madrid, excluyendo los pedidos de productos que contengan la palabra "Zapatos"
SELECT producto, cantidad
FROM pedidos
WHERE cliente_id IN (
  SELECT id
  FROM clientes
  WHERE ciudad = 'Madrid'
) AND producto NOT LIKE '%Zapatos%';

--Obtener los nombres de los clientes que han realizado al menos un pedido y su ciudad no coincide con la ciudad de ningún otro cliente
SELECT nombre
FROM clientes
WHERE id IN (
  SELECT DISTINCT cliente_id
  FROM pedidos
) AND ciudad NOT IN (
  SELECT DISTINCT ciudad
  FROM clientes
  WHERE id <> clientes.id
);

--Obtener el producto con la cantidad más alta entre todos los pedidos realizados
SELECT producto
FROM pedidos
WHERE cantidad = (
  SELECT MAX(cantidad)
  FROM pedidos
);

--Obtener los nombres de los clientes que han realizado pedidos de todos los productos disponibles
SELECT nombre
FROM clientes
WHERE (SELECT COUNT(DISTINCT producto)
       FROM pedidos) = (SELECT COUNT(DISTINCT producto)
                        FROM pedidos
                        WHERE cliente_id = clientes.id);

--Obtener el nombre del cliente que ha realizado el pedido con la cantidad más alta entre todos los pedidos realizados:
SELECT c.nombre
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id
WHERE p.cantidad = (
  SELECT MAX(cantidad)
  FROM pedidos
);

```
