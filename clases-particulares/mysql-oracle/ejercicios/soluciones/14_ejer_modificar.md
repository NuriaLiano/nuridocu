---
author: @nurialiano
license: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---

# EJERCICIOS MODIFICAR

~~~sql
-- Crear una base de datos
CREATE DATABASE tienda;
USE tienda;

-- Crear una tabla "productos"
CREATE TABLE productos (
  id INT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  precio DECIMAL(8,2) NOT NULL CHECK (precio >= 0),
  categoria_id VARCHAR(50) NOT NULL
);
CREATE TABLE categoria (
  id INT PRIMARY KEY,
  nombre varchar NOT NULL,
);

-- Insertar datos de ejemplo
INSERT INTO productos (id, nombre, precio, categoria) VALUES
  (1, 'Camiseta', 19.99, 'Ropa'),
  (2, 'Pantalón', 29.99, 'Ropa'),
  (3, 'Zapatos', 49.99, 'Calzado');
~~~

## MODIFICAR RESTRICCIONES

~~~sql
-- Modificar la restricción del campo "precio"
ALTER TABLE productos
MODIFY COLUMN precio DECIMAL(8,2) NOT NULL CHECK (precio >= 0 AND precio <= 1000);

-- Insertar más datos de ejemplo
INSERT INTO productos (id, nombre, precio, categoria) VALUES
  (4, 'Bufanda', 9.99, 'Ropa'),
  (5, 'Reloj', 199.99, 'Accesorios');
~~~

En este ejercicio creamos una base de datos llamada "tienda" y una tabla "productos" con campos para el ID, nombre, precio y categoría. Después insertamos algunos datos de ejemplo en la tabla.

A continuación, modificamos la restricción del campo "precio" para asegurarnos de que el valor esté entre 0 y 1000. Finalmente, insertamos más datos de ejemplo en la tabla "productos" para comprobar que la restricción ha sido modificada correctamente.

## MODIFICAR RELACIONES

No se ha definido una restricción de clave foránea para mantener la integridad referencial entre las tablas.

~~~sql
ALTER TABLE productos
ADD CONSTRAINT fk_productos_categoria
FOREIGN KEY (categoria_id)
REFERENCES categoria(id);
~~~

Esta sentencia agrega una restricción de clave foránea a la columna "categoria_id" de la tabla "productos" que hace referencia a la columna "id" de la tabla "categoria". La restricción se nombra "fk_productos_categoria". Ahora, cualquier registro en la tabla "productos" con un valor de "categoria_id" que no exista en la tabla "categoria" será rechazado.

## MODIFICAR COLUMNAS

~~~sql
ALTER TABLE productos
CHANGE COLUMN categoria categoria_producto VARCHAR(50) NOT NULL;
~~~

Este comando cambiará el nombre de la columna "categoria" a "categoria_producto" y mantendrá la misma definición de la columna (tipo de datos y restricciones).
SHOW COLUMNS FROM productos;

## MODIFICAR TABLAS

~~~sql
ALTER TABLE empleados RENAME TO trabajadores;
~~~

Esta sentencia cambia el nombre de la tabla "empleados" a "trabajadores". Asegúrate de actualizar todas las referencias a la tabla en tu código y consultas SQL después de ejecutar esta sentencia para que apunten a la nueva tabla "trabajadores".

## EJERCICIO 1

En este ejemplo, se crea una base de datos llamada "mi_basededatos" y se crea una tabla "empleados" con varias columnas. Luego, se modifica la restricción de la columna "email" para que sea única, se modifica la columna "nombre" para que tenga un máximo de 100 caracteres y se crea una tabla "departamentos". Después, se agrega una relación entre las tablas "empleados" y "departamentos" utilizando la columna "departamento_id". Por último, se insertan datos de ejemplo en ambas tablas.

~~~sql
-- Crear una base de datos
CREATE DATABASE mi_basededatos;
USE mi_basededatos;

-- Crear una tabla "empleados"
CREATE TABLE empleados (
  id INT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  fecha_nacimiento DATE NOT NULL,
  email VARCHAR(50) NOT NULL,
  salario DECIMAL(8,2) NOT NULL CHECK (salario >= 0),
  departamento_id INT NOT NULL
);

-- Modificar la restricción de la columna "email"
ALTER TABLE empleados MODIFY COLUMN email VARCHAR(50) NOT NULL UNIQUE;

-- Modificar la columna "nombre"
ALTER TABLE empleados MODIFY COLUMN nombre VARCHAR(100) NOT NULL;

-- Crear una tabla "departamentos"
CREATE TABLE departamentos (
  id INT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  ciudad VARCHAR(50) NOT NULL
);

-- Agregar una relación entre las tablas "empleados" y "departamentos"
ALTER TABLE empleados ADD FOREIGN KEY (departamento_id) REFERENCES departamentos(id);

-- Insertar datos de ejemplo
INSERT INTO departamentos (id, nombre, ciudad) VALUES
  (1, 'Ventas', 'Madrid'),
  (2, 'Marketing', 'Barcelona'),
  (3, 'Tecnología', 'Valencia');

INSERT INTO empleados (id, nombre, fecha_nacimiento, email, salario, departamento_id) VALUES
  (1, 'Juan Pérez', '1990-01-01', 'juan.perez@example.com', 2500.00, 1),
  (2, 'María Gómez', '1995-05-10', 'maria.gomez@example.com', 3000.00, 2),
  (3, 'Pedro Rodríguez', '1992-07-15', 'pedro.rodriguez@example.com', 4000.00, 3);
~~~
