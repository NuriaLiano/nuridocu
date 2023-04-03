# EJERCICIOS FUNCIONES

~~~sql
CREATE DATABASE ventas2

CREATE TABLE ventas (
  id INT PRIMARY KEY AUTO_INCREMENT,
  fecha DATE,
  cliente VARCHAR(50),
  producto VARCHAR(50),
  cantidad INT,
  precio_unitario DECIMAL(10,2)
);

INSERT INTO ventas (fecha, cliente, producto, cantidad, precio_unitario) 
VALUES 
('2022-01-01', 'Juan Perez', 'Producto 1', 2, 10.50), 
('2022-01-01', 'Maria Gomez', 'Producto 2', 1, 15.00), 
('2022-01-02', 'Pedro Sanchez', 'Producto 3', 3, 12.75), 
('2022-01-02', 'Ana Rodriguez', 'Producto 1', 5, 10.50), 
('2022-01-03', 'Juan Perez', 'Producto 2', 2, 15.00);

~~~

## EJERCICIO 1 - FUN. NUMÉRICAS

1. Calcular el total de ventas:

   ~~~sql
   SELECT SUM(cantidad * precio_unitario) AS total FROM ventas;
   ~~~

### RESULTADO
+--------+
| total  |
+--------+
| 147.75 |
+--------+


2. Calcular el promedio de ventas por día:

   ~~~sql
   SELECT AVG(cantidad * precio_unitario) AS promedio FROM ventas GROUP BY fecha;
   ~~~

### RESULTADO

+----------+
| promedio |
+----------+
| 21.0000  |
| 45.3750  |
| 30.0000  |
+----------+


3. Encontrar las ventas con un precio unitario superior a 15:

   ~~~sql
   SELECT * FROM ventas WHERE precio_unitario > 15;
   ~~~

### RESULTADO

+----+------------+--------------+-----------+----------+----------------+
| id | fecha      | cliente      | producto  | cantidad | precio_unitario |
+----+------------+--------------+-----------+----------+----------------+
|  2 | 2022-01-01 | Maria Gomez  | Producto 2|        1 |          15.00 |
|  5 | 2022-01-03 | Juan Perez   | Producto 2|        2 |          15.00 |
+----+------------+--------------+-----------+----------+----------------+

## EJERCICIO 2 - FUN. CARACTERES

1. Encontrar las ventas realizadas por el cliente "Juan Perez":

   ~~~sql
   SELECT * FROM ventas WHERE cliente = 'Juan Perez';
   ~~~

### RESULTADO

+----+------------+------------+-----------+----------+----------------+
| id | fecha      | cliente    | producto  | cantidad | precio_unitario |
+----+------------+------------+-----------+----------+----------------+
|  1 | 2022-01-01 | Juan Perez | Producto 1|        2 |          10.50 |
|  5 | 2022-01-03 | Juan Perez | Producto 2|        2 |          15.00 |
+----+------------+------------+-----------


2. Encontrar las ventas que incluyen el producto "Producto 1":

   ~~~sql
   SELECT * FROM ventas WHERE producto LIKE '%Producto 1%';
   ~~~

### RESULTADO

3. Convertir el nombre del cliente a mayúsculas:

   ~~~sql
   SELECT UPPER(cliente) AS cliente_mayusculas FROM ventas;
   ~~~

### RESULTADO

## EJERCICIO 3 - FUN. FECHAS

1. Encontrar las ventas realizadas en el mes de enero:

   ~~~sql
   SELECT * FROM ventas WHERE MONTH(fecha) = 1;
   ~~~

### RESULTADO

+----+------------+---------------+-----------+----------+----------------+
| id | fecha      | cliente       | producto  | cantidad | precio_unitario |
+----+------------+---------------+-----------+----------+----------------+
|  1 | 2022-01-01 | Juan Perez    | Producto 1|        2 |          10.50 |
|  2 | 2022-01-01 | Maria Gomez   | Producto 2|        1 |          15.00 |
|  3 | 2022-01-02 | Pedro Sanchez | Producto 3|        3 |          12.75 |
|  4 | 2022-01-02 | Ana Rodriguez | Producto 1|        5 |          10.50 |
|  5 | 2022-01-03 | Juan Perez    | Producto 2|        2 |          15.00 |
+----+------------+---------------+-----------+----------+----------------+


2. Encontrar las ventas realizadas el 2 de enero:

   ~~~sql
   SELECT * FROM ventas WHERE fecha = '2022-01-02';
   ~~~

### RESULTADO

3. Calcular el número de días entre la fecha de la primera venta y la fecha de la última venta:

   ~~~sql
   SELECT DATEDIFF(MAX(fecha), MIN(fecha)) AS dias_entre_ventas FROM ventas;
   ~~~

### RESULTADO

## EJERCICIO 3 - FUN. COMPARACIÓN

1. Encontrar las ventas con una cantidad mayor o igual a 3:

   ~~~sql
   SELECT * FROM ventas WHERE cantidad >= 3;
   ~~~

### RESULTADO

2. Encontrar las ventas con una cantidad entre 2 y 4:

   ~~~sql
   SELECT * FROM ventas WHERE cantidad BETWEEN 2 AND 4;
   ~~~

### RESULTADO

3. Encontrar las ventas con una cantidad menor que 2 o un precio unitario mayor que 15:

   ~~~sql
   SELECT * FROM ventas WHERE cantidad < 2 OR precio_unitario > 15;
   ~~~

### RESULTADO