---
author: @nurialiano
license: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---

# SUBCONSULTAS

~~~sql
CREATE DATABASE concesionario;
CREATE TABLE coches (
  id INTEGER PRIMARY KEY,
  marca TEXT,
  modelo TEXT,
  anio INTEGER,
  precio INTEGER
);

CREATE TABLE ventas (
  id INTEGER PRIMARY KEY,
  coche_id INTEGER,
  fecha_venta DATE,
  precio_venta INTEGER,
  FOREIGN KEY (coche_id) REFERENCES coches(id)
);
INSERT INTO coches (id, marca, modelo, anio, precio) VALUES
  (1, 'Ford', 'Mustang', 2022, 50000),
  (2, 'Chevrolet', 'Camaro', 2022, 55000),
  (3, 'Dodge', 'Challenger', 2022, 60000),
  (4, 'Porsche', '911', 2022, 100000),
  (5, 'Audi', 'R8', 2022, 150000);

INSERT INTO ventas (id, coche_id, fecha_venta, precio_venta) VALUES
  (1, 1, '2022-01-01', 45000),
  (2, 2, '2022-02-01', 50000),
  (3, 3, '2022-03-01', 55000),
  (4, 4, '2022-04-01', 95000),
  (5, 5, '2022-05-01', 140000),
  (6, 3, '2022-06-01', 58000),
  (7, 2, '2022-07-01', 52000),
  (8, 1, '2022-08-01', 48000),
  (9, 5, '2022-09-01', 145000),
  (10, 4, '2022-10-01', 98000);
~~~

## 1 - Devolver la marca y modelo del coche más vendido

~~~sql
SELECT marca, modelo
FROM coches
WHERE id = (
  SELECT coche_id
  FROM ventas
  GROUP BY coche_id
  ORDER BY SUM(precio_venta) DESC
  LIMIT 1
);
~~~

## 2 - Devolver una lista de todos los modelos de coches que hayan sido vendidos

~~~sql
SELECT DISTINCT modelo
FROM coches
WHERE id IN (
  SELECT coche_id
  FROM ventas
);
~~~

## 3 - Devolver el modelo del coche más caro vendido

~~~sql
SELECT modelo 
FROM coches 
WHERE id = (SELECT coche_id FROM ventas ORDER BY precio_venta DESC LIMIT 1);
~~~

<!-- ## 4 - Devolver la lista de modelos de coches vendidos en orden alfabético

~~~sql
SELECT modelo 
FROM coches 
WHERE id IN (SELECT coche_id FROM ventas) ORDER BY modelo ASC;
~~~ -->

## 5 - Devolver la marca y el modelo de los coches vendidos por encima del precio medio de venta

~~~sql
SELECT marca, modelo 
FROM coches 
WHERE id IN (SELECT coche_id FROM ventas WHERE precio_venta > (SELECT AVG(precio_venta) FROM ventas)) ORDER BY marca, modelo;
~~~
