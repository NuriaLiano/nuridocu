# EJERCICIO DE CONSULTAS CORRELACIONADAS

## EJERCICIO 1

Utilizar una consulta correlacionada para obtener el total de ventas por cada cliente

~~~sql
CREATE TABLE clientes (
  id INT PRIMARY KEY,
  nombre VARCHAR(50)
);

INSERT INTO clientes (id, nombre)
VALUES (1, 'Juan'),
       (2, 'Maria'),
       (3, 'Pedro');

CREATE TABLE ventas (
  id INT PRIMARY KEY,
  cliente_id INT,
  fecha DATE,
  monto DECIMAL(10, 2)
);

INSERT INTO ventas (id, cliente_id, fecha, monto)
VALUES (1, 1, '2022-03-31', 100.00),
       (2, 2, '2022-04-01', 150.00),
       (3, 1, '2022-04-02', 75.00),
       (4, 3, '2022-04-03', 200.00),
       (5, 2, '2022-04-03', 50.00);

SELECT c.nombre, 
       (SELECT SUM(v.monto) FROM ventas v WHERE v.cliente_id = c.id) as total_ventas
FROM clientes c;
~~~

### RESULTADO

| nombre| total_ventas |
|-------|--------------|
| Juan  |       175.00 |
| Maria |       200.00 |
| Pedro |       200.00 |

En este ejemplo, la consulta interna (SELECT SUM(v.monto) FROM ventas v WHERE v.cliente_id = c.id) es una consulta correlacionada, ya que la condición del WHERE hace referencia a la tabla de la consulta externa (clientes). La consulta devuelve el nombre de cada cliente y el total de ventas que ha realizado.

## EJERCICIO 2

Queremos obtener la lista de clientes que han hecho un pedido por un monto mayor al promedio de los pedidos realizados por los clientes de la misma ciudad. 

~~~sql
CREATE DATABASE ventas5;

CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  city VARCHAR(50)
);

CREATE TABLE orders (
  id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  total DECIMAL(10,2)
);
INSERT INTO customers (id, name, city) VALUES
  (1, 'Juan', 'Madrid'),
  (2, 'Pedro', 'Barcelona'),
  (3, 'Ana', 'Valencia'),
  (4, 'Maria', 'Sevilla');

INSERT INTO orders (id, customer_id, order_date, total) VALUES
  (1, 1, '2022-01-01', 100.00),
  (2, 1, '2022-02-01', 200.00),
  (3, 2, '2022-03-01', 150.00),
  (4, 3, '2022-04-01', 300.00),
  (5, 4, '2022-05-01', 250.00),
  (6, 4, '2022-06-01', 200.00);

SELECT c.name, c.city, o.total
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id
WHERE o.total > (
  SELECT AVG(o2.total)
  FROM orders o2
  WHERE o2.customer_id IN (
    SELECT c2.id
    FROM customers c2
    WHERE c2.city = c.city
  )
)
ORDER BY c.name, o.total DESC;
~~~

### RESULTADO

| name  | city     | total  |
|-------|----------|--------|
| Ana   | Valencia | 300.00 |
| Juan  | Madrid   | 200.00 |
| Maria | Sevilla  | 250.00 |

En esta consulta, la subconsulta devuelve el promedio de los pedidos realizados por los clientes de la misma ciudad que el cliente actual de la consulta principal. Luego, la condición del WHERE compara el total del pedido del cliente actual con el promedio de los pedidos de los clientes de la misma ciudad.

Esto se debe a que Ana, Juan y Maria han realizado pedidos con un monto mayor al promedio de los pedidos realizados por los clientes de su misma ciudad.