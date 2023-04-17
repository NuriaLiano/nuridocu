---
autor: @nurialiano
licence: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---

# EJERCICIOS SELECT

## EJERCICIO 1 - FUNCIONES Y AS

Supongamos que tienes una tabla **empleados** con las columnas **id**, **nombre**, **apellido**, **fecha_nacimiento** y **salario**. Escribe una consulta que **seleccione el nombre y el apellido de cada empleado**, y muestre una c**olumna adicional llamada nombre_completo** que contenga la **concatenación del nombre y el apellido**.

~~~sql
CREATE TABLE empleados (
  id INT PRIMARY KEY,
  nombre VARCHAR(50),
  apellido VARCHAR(50),
  fecha_nacimiento DATE,
  salario DECIMAL(10,2)
);

INSERT INTO empleados (id, nombre, apellido, fecha_nacimiento, salario) VALUES
  (1, 'Juan', 'Pérez', '1990-01-01', 2000.00),
  (2, 'María', 'García', '1985-05-10', 2500.00),
  (3, 'Pedro', 'Sánchez', '1988-12-15', 2200.00);

SELECT nombre, apellido, CONCAT(nombre, ' ', apellido) AS nombre_completo
FROM empleados;
~~~

### EXPLICACIÓN

Esta consulta selecciona el nombre y el apellido de cada empleado, y utiliza la función CONCAT() para unirlos en una sola cadena en la columna nombre_completo.

## EJERCICIO 2 - OPERACIONES Y AS

Supongamos que tienes una tabla **productos** con las columnas **id**, **nombre**, **precio** y **stock**. Escribe una consulta que **seleccione el nombre y el precio de cada producto**, y muestre una **columna adicional** llamada **precio_descuento** que **contenga el precio con un descuento del 10%**.

~~~sql
CREATE TABLE productos (
  id INT PRIMARY KEY,
  nombre VARCHAR(50),
  precio DECIMAL(10,2),
  stock INT
);

INSERT INTO productos (id, nombre, precio, stock) VALUES
  (1, 'Camisa', 29.99, 10),
  (2, 'Pantalón', 39.99, 5),
  (3, 'Zapatos', 59.99, 2);

SELECT nombre, precio, precio * 0.9 AS precio_descuento
FROM productos;
~~~

### EXPLICACIÓN

Esta consulta selecciona el nombre y el precio de cada producto, y multiplica el precio por 0.9 para obtener el precio con un descuento del 10% en la columna precio_descuento.

## EJERCICIO 3 - AS Y ORDER BY

~~~sql

  -- Crear la base de datos 'mi_basedatos2'
  CREATE DATABASE mi_basedatos2;
  -- Usar la base de datos 'mi_basedatos2'
  USE mi_ctido VARCHAR(50),
    puesto VARCHAR(50)
  );
  -- Insertar algunos datos en la tabla 'empleados'
  INSERT INTO empleados (id, nombre, apellido, puesto)
  VALUES
    (1, 'Juan', 'Pérez', 'Gerente'),
    (2, 'María', 'González', 'Supervisor'),
    (3, 'Pedro', 'López', 'Técnico'),
    (4, 'Laura', 'Hernández', 'Asistente'),
    (5, 'Luis', 'Martínez', 'Técnico'),
    (6, 'Carla', 'Sánchez', 'Asistente'),
    (7, 'Javier', 'García', 'Técnico');

  -- Realizar una consulta para obtener los nombres de los empleados con el puesto 'Técnico'
  SELECT nombre, apellido, puesto 
  FROM empleados 
  WHERE puesto = 'Técnico' 
  ORDER BY apellido ASC;

~~~

Este código crea una nueva base de datos llamada 'mi_basedatos2', crea una tabla llamada 'empleados' con cuatro columnas: 'id', 'nombre', 'apellido' y 'puesto', e inserta algunos datos en la tabla. Luego, realiza una consulta para obtener los nombres de los empleados con el puesto 'Técnico' y los ordena alfabéticamente por apellido.
