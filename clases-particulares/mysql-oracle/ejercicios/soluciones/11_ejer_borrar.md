---
autor: @nurialiano
licence: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---

# EJERCICIOS BORRAR

~~~sql
CREATE DATABASE mi_basededatos;
USE mi_basededatos;
CREATE TABLE departamentos (
  id INT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL
);
CREATE TABLE empleados (
  id INT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  email VARCHAR(50) UNIQUE,
  departamento_id INT,
  FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);
INSERT INTO departamentos (id, nombre) VALUES
  (1, 'Ventas'),
  (2, 'Marketing'),
  (3, 'Recursos Humanos');
INSERT INTO empleados (id, nombre, email, departamento_id) VALUES
  (1, 'Juan', 'juan@gmail.com', 1),
  (2, 'María', 'maria@gmail.com', 2),
  (3, 'Pedro', 'pedro@gmail.com', 3);
~~~

**Forzar error al insertar**

~~~sql
INSERT INTO empleados (id, nombre, email, departamento_id) VALUES
  (4, NULL, 'juan@gmail.com', 4);
~~~

## BORRAR RESTRICCIONES

~~~sql
ALTER TABLE departamentos ALTER COLUMN nombre DROP NOT NULL;
~~~

También se puede hacer la siguiente sentencia para modificar la columna y quitar la restriccion

~~~sql
ALTER TABLE departamentos MODIFY COLUMN nombre VARCHAR(50);
~~~

## BORRAR RELACIONES (FOREIGN KEY)

1. Eliminar la clave foránea de la tabla "empleados":

~~~sql
ALTER TABLE empleados DROP FOREIGN KEY departamento_id;

~~~

2. Eliminar la columna "departamento_id" de la tabla "empleados":

~~~sql
ALTER TABLE empleados DROP COLUMN departamento_id;
~~~

## BORRAR TABLAS

~~~sql
DROP TABLE empleados;
~~~

Este comando eliminará completamente la tabla "empleados" y todos los datos que contenga. Es importante tener en cuenta que si hay relaciones o restricciones que dependan de esta tabla, deben ser eliminadas primero antes de ejecutar este comando.

### ELIMINAR TABLAS CON RESTRICCIONES O RELACIONES CON OTRAS TABLAS (ON DELETE CASCADE)

~~~sql
CREATE DATABASE tienda_virtual;
USE tienda_virtual;
CREATE TABLE productos (
  id INT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  precio DECIMAL(8, 2) NOT NULL,
  descripcion TEXT
);
CREATE TABLE categorias (
  id INT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL
);
CREATE TABLE productos_categorias (
  producto_id INT,
  categoria_id INT,
  PRIMARY KEY (producto_id, categoria_id),
  FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE CASCADE,
  FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE
);
INSERT INTO productos (id, nombre, precio, descripcion) VALUES
  (1, 'Camiseta', 19.99, 'Camiseta de algodón'),
  (2, 'Pantalón', 39.99, 'Pantalón vaquero'),
  (3, 'Zapatillas', 49.99, 'Zapatillas deportivas');
  
INSERT INTO categorias (id, nombre) VALUES
  (1, 'Ropa'),
  (2, 'Calzado');
  
INSERT INTO productos_categorias (producto_id, categoria_id) VALUES
  (1, 1),
  (2, 1),
  (3, 2);

ALTER TABLE productos ALTER COLUMN precio DROP NOT NULL;
DROP TABLE productos_categorias;
DROP TABLE categorias;
~~~

En este ejemplo, primero se borra la tabla "productos_categorias" y sus restricciones para que no haya problemas al borrar la tabla "categorias" que está relacionada con ella. Las claves foráneas que hacen referencia a la tabla "categorias" se eliminan automáticamente cuando se borra la tabla "productos_categorias" gracias a la cláusula "ON DELETE CASCADE" que se estableció al crear las restricciones.
