---
autor: @nurialiano
licence: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---
# EJERCICIOS SELECT

## EJERCICIO 1 - FUNCIONES Y AS

Supongamos que tienes una tabla **empleados** con las columnas **id**, **nombre**, **apellido**, **fecha_nacimiento** y **salario**. Escribe una consulta que **seleccione el nombre y el apellido de cada empleado**, y muestre una **columna adicional llamada nombre_completo** que contenga la **concatenación del nombre y el apellido**.

- id INT PRIMARY KEY,
- nombre VARCHAR(50),
- apellido VARCHAR(50),
- fecha_nacimiento DATE,
- salario DECIMAL(10,2)

- (1, 'Juan', 'Pérez', '1990-01-01', 2000.00),
- (2, 'María', 'García', '1985-05-10', 2500.00),
- (3, 'Pedro', 'Sánchez', '1988-12-15', 2200.00);

## EJERCICIO 2 - OPERACIONES Y AS

Supongamos que tienes una tabla **productos** con las columnas **id**, **nombre**, **precio** y **stock**. Escribe una consulta que **seleccione el nombre y el precio de cada producto**, y muestre una **columna adicional** llamada **precio_descuento** que **contenga el precio con un descuento del 10%**.

- id INT PRIMARY KEY,
- nombre VARCHAR(50),
- precio DECIMAL(10,2),
- stock INT

- (1, 'Camisa', 29.99, 10),
- (2, 'Pantalón', 39.99, 5),
- (3, 'Zapatos', 59.99, 2);

## EJERCICIO 3 - AS Y ORDER BY

- id SERIAL PRIMARY KEY,
- nombre VARCHAR(50),
- apellido VARCHAR(50),
- puesto VARCHAR(50)

- ('Juan', 'Pérez', 'Gerente'),
- ('María', 'González', 'Supervisor'),
- ('Pedro', 'López', 'Técnico'),
- ('Laura', 'Hernández', 'Asistente'),
- ('Luis', 'Martínez', 'Técnico'),
- ('Carla', 'Sánchez', 'Asistente'),
- ('Javier', 'García', 'Técnico');
