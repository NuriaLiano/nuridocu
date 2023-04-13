# EJERCICIOS AÑADIR

## AÑADIR RESTRICCIONES

~~~sql
CREATE DATABASE mi_basededatos;
USE mi_basededatos;

CREATE TABLE productos (
  id INT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  precio DECIMAL(8,2) NOT NULL,
  categoria_id INT NOT NULL,
  stock INT NOT NULL,
  fecha_registro DATE NOT NULL
);

-- Añadir restricción UNIQUE a la columna "nombre"
ALTER TABLE productos ADD CONSTRAINT unq_nombre UNIQUE (nombre);

-- Añadir restricción CHECK a la columna "stock"
ALTER TABLE productos ADD CONSTRAINT chk_stock CHECK (stock >= 0);

-- Insertar datos de ejemplo
INSERT INTO productos (id, nombre, precio, categoria_id, stock, fecha_registro) VALUES
  (1, 'Producto 1', 10.99, 1, 100, '2022-01-01'),
  (2, 'Producto 2', 25.99, 2, 50, '2022-01-02'),
  (3, 'Producto 3', 5.99, 1, 0, '2022-01-03');
~~~

En este ejemplo, se crea una tabla llamada "productos" con cinco columnas, y luego se agregan restricciones UNIQUE y CHECK a las columnas "nombre" y "stock", respectivamente, utilizando la sentencia ALTER TABLE. Luego se insertan algunos datos de ejemplo en la tabla. La restricción UNIQUE en la columna "nombre" asegura que no haya productos con el mismo nombre, mientras que la restricción CHECK en la columna "stock" asegura que el stock no sea un número negativo.

## AÑADIR COLUMNAS

~~~sql
-- Añadir columna "descuento"
ALTER TABLE productos
ADD COLUMN descuento DECIMAL(8,2) DEFAULT 0.00
CHECK (descuento >= 0 AND descuento <= 100);
~~~

Aquí, se están agregando dos nuevos registros a la tabla "productos", con los valores correspondientes para todas las columnas, incluyendo la nueva columna "descripcion". Nota que el orden de las columnas en la lista de valores debe corresponderse con el orden de las columnas en la definición de la tabla.

## AÑADIR TABLAS (con restricciones)

Primero debemos crear la tabla de categorías e insertar algunos datos de ejemplo

~~~sql
CREATE TABLE categorias (
  id INT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL
);

INSERT INTO categorias (id, nombre) VALUES
  (1, 'Electrónica'),
  (2, 'Hogar'),
  (3, 'Jardín');
~~~

Luego, podemos añadir la restricción de clave foránea en la columna categoria_id de la tabla productos para referenciar la columna id de la tabla categorias

~~~sql
ALTER TABLE productos
ADD CONSTRAINT fk_categoria
FOREIGN KEY (categoria_id) REFERENCES categorias(id);
~~~

De esta forma, se establece una relación entre las tablas productos y categorias, donde la columna categoria_id de la tabla productos referencia a la columna id de la tabla categorias. Ahora, cada vez que se inserten o actualicen datos en la tabla productos, se verificará que el valor de la columna categoria_id exista en la tabla categorias.

## EJERCICIO 2

~~~sql
-- Crear la base de datos
CREATE DATABASE tienda;
USE tienda;

-- Crear la tabla "clientes"
CREATE TABLE clientes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  apellidos VARCHAR(100) NOT NULL,
  direccion VARCHAR(200),
  telefono VARCHAR(15) NOT NULL UNIQUE
);

-- Crear la tabla "pedidos"
CREATE TABLE pedidos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  fecha DATE NOT NULL,
  cliente_id INT NOT NULL,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Crear la tabla "productos"
CREATE TABLE productos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  precio DECIMAL(8,2) NOT NULL CHECK (precio > 0),
  categoria_id INT NOT NULL,
  FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

-- Crear la tabla "categorias"
CREATE TABLE categorias (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL
);

-- Insertar datos en la tabla "clientes"
INSERT INTO clientes (id, nombre, apellidos, direccion, telefono) VALUES
  (1, 'Ana', 'García Pérez', 'Calle Mayor, 1', '123456789'),
  (2, 'Juan', 'Martínez Sánchez', 'Plaza del Ayuntamiento, 2', '987654321'),
  (3, 'Elena', 'González Ruiz', 'Avenida de la Constitución, 3', '111222333');

-- Insertar datos en la tabla "categorias"
INSERT INTO categorias (id, nombre) VALUES
  (1, 'Ropa'),
  (2, 'Calzado'),
  (3, 'Complementos');

-- Insertar datos en la tabla "productos"
INSERT INTO productos (id, nombre, precio, categoria_id) VALUES
  (1, 'Camiseta', 19.99, 1),
  (2, 'Pantalón', 29.99, 1),
  (3, 'Zapatos', 49.99, 2);
~~~

1. Añadir una columna llamada "email" a la tabla "clientes" que sea de tipo VARCHAR(100) y no nula

~~~sql
ALTER TABLE clientes
ADD COLUMN email VARCHAR(100) NOT NULL;
~~~

2. Añadir una restricción CHECK en la tabla "productos" para asegurarse de que el precio sea mayor que cero y menor que 100.

~~~sql
ALTER TABLE productos
ADD CONSTRAINT chk_precio CHECK (precio > 0 AND precio < 100);
~~~

3. Añadir una columna llamada "stock" a la tabla "productos" que sea de tipo INT y no nula.

~~~sql
ALTER TABLE productos
ADD COLUMN stock INT NOT NULL;
~~~

4. Añadir una restricción UNIQUE a la columna "nombre" de la tabla "categorias".

~~~sql
ALTER TABLE categorias
ADD CONSTRAINT uniq_nombre UNIQUE (nombre);
~~~

5. Añadir una columna llamada "nif" a la tabla "clientes" que sea de tipo VARCHAR(10) y no nula.

~~~sql
ALTER TABLE clientes
ADD COLUMN nif VARCHAR(10) NOT NULL;
~~~
