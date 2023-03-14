# EJERCICIO 1 (básico)
Supongamos que deseas crear una base de datos para almacenar información de empleados. La base de datos tendrá una tabla llamada "empleados" que contendrá información sobre cada empleado, como su nombre, apellido, fecha de nacimiento y número de teléfono. Además, deseas agregar una nueva columna llamada "correo electrónico" a la tabla "empleados".
~~~
-- Crear la base de datos
CREATE DATABASE empleados_db;

-- Seleccionar la base de datos
USE empleados_db;

-- Crear la tabla
CREATE TABLE empleados (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL,
  fecha_de_nacimiento DATE NOT NULL,
  telefono VARCHAR(20) NOT NULL,
  PRIMARY KEY (id)
);

-- Agregar la columna de correo electrónico
ALTER TABLE empleados ADD correo_electronico VARCHAR(50);
~~~

# EJERCICIO 2 (básico con error)

Supongamos que tienes una base de datos llamada "ventas" que contiene una tabla llamada "productos". La tabla tiene las columnas "id" (clave primaria), "nombre" y "precio". Ahora deseas agregar una nueva columna llamada "cantidad" a la tabla "productos".
~~~
-- Crear la base de datos
CREATE DATABASE ventas;

-- Seleccionar la base de datos
USE ventas;

-- Crear la tabla
CREATE TABLE productos (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id)
);

-- Agregar la columna de cantidad (junto con el error)
ALTER TABLE productos ADD cantidad INT NOT NULL DEFAULT 0;
~~~

**EXPLICACIÓN:**     El comando "ALTER TABLE" intenta agregar una nueva columna llamada "cantidad" a la tabla "productos". Esta columna se define como un número entero que no puede ser nulo y que tiene un valor predeterminado de cero.
Sin embargo, este comando generará un error porque la tabla "productos" ya tiene datos en ella y la nueva columna no puede ser nula. Para solucionar este error, debes proporcionar un valor predeterminado o permitir valores nulos para la nueva columna

**SOLUCIÓN**
``ALTER TABLE productos ADD cantidad INT DEFAULT 0;``

# EJERCICIO 3 (con integridad ref ADD CONSTRAINT y UPDATE CASCADE)
Supongamos que tienes una base de datos llamada "tienda" que contiene dos tablas: "clientes" y "pedidos". La tabla "clientes" tiene las columnas "id" (clave primaria) y "nombre", mientras que la tabla "pedidos" tiene las columnas "id" (clave primaria), "cliente_id" (clave externa que hace referencia a la tabla "clientes") y "total".

Ahora deseas agregar una nueva tabla llamada "productos" que contendrá los detalles de cada producto. Esta tabla tendrá las columnas "id" (clave primaria), "nombre" y "precio", y se relacionará con la tabla "pedidos" a través de una tabla de unión llamada "pedido_producto".

~~~
-- Crear la base de datos
CREATE DATABASE tienda;

-- Seleccionar la base de datos
USE tienda;

-- Crear la tabla de clientes
CREATE TABLE clientes (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
);

-- Crear la tabla de pedidos
CREATE TABLE pedidos (
  id INT NOT NULL AUTO_INCREMENT,
  cliente_id INT NOT NULL,
  total DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON UPDATE CASCADE
);

-- Agregar la tabla de productos
CREATE TABLE productos (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id)
);

-- Agregar la tabla de unión
CREATE TABLE pedido_producto (
  pedido_id INT NOT NULL,
  producto_id INT NOT NULL,
  cantidad INT NOT NULL,
  PRIMARY KEY (pedido_id, producto_id),
  FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON UPDATE CASCADE,
  FOREIGN KEY (producto_id) REFERENCES productos(id) ON UPDATE CASCADE
);

-- Agregar un producto
INSERT INTO productos (nombre, precio) VALUES ('Producto 1', 10.00);

-- Agregar un cliente
INSERT INTO clientes (nombre) VALUES ('Cliente 1');

-- Agregar un pedido para el cliente 1 con el producto 1
INSERT INTO pedidos (cliente_id, total) VALUES (1, 10.00);
INSERT INTO pedido_producto (pedido_id, producto_id, cantidad) VALUES (1, 1, 1);

-- Agregar un segundo producto
INSERT INTO productos (nombre, precio) VALUES ('Producto 2', 20.00);

-- Agregar un pedido para el cliente 1 con el producto 1 y 2
INSERT INTO pedidos (cliente_id, total) VALUES (1, 30.00);
INSERT INTO pedido_producto (pedido_id, producto_id, cantidad) VALUES (2, 1, 1), (2, 2, 1);

-- Agregar una nueva columna a la tabla de productos
ALTER TABLE productos ADD descripcion VARCHAR(100) NULL;
~~~

**EXPLICACIÓN:**
El comando "CREATE DATABASE" crea una nueva base de datos llamada "tienda".

El comando "USE" selecciona la base de datos "tienda" para que todos los comandos posteriores se apliquen a esa base de datos.
El comando CREATE TABLE" se usa para crear las tablas "clientes", "pedidos", "productos" y "pedido_producto" con las columnas y restricciones necesarias.
El comando "INSERT INTO" se utiliza para agregar algunos datos de ejemplo a las tablas "clientes", "pedidos", "productos" y "pedido_producto".

El comando "ALTER TABLE" se usa para agregar una nueva columna llamada "descripcion" a la tabla "productos". Esta columna se define como NULLABLE, lo que significa que puede contener valores nulos.

La relación de integridad referencial se establece mediante el comando "FOREIGN KEY" en las tablas "pedidos" y "pedido_producto". En la tabla "pedidos", la columna "cliente_id" es una clave externa que hace referencia a la columna "id" de la tabla "clientes". En la tabla "pedido_producto", las columnas "pedido_id" y "producto_id" son claves externas que hacen referencia a las columnas "id" de las tablas "pedidos" y "productos", respectivamente. Además, se especifica la opción "ON UPDATE CASCADE" para que si se actualiza un valor en la tabla "clientes" o "productos", los valores correspondientes en las tablas "pedidos" y "pedido_producto" también se actualicen automáticament

# EJERCICIO 4 (con integridad ref)
Supongamos que tienes dos tablas: "libros" y "autores". La tabla "libros" tiene las columnas "id" (clave primaria), "titulo", "autor_id" (clave foránea a la tabla "autores") y "precio". La tabla "autores" tiene las columnas "id" (clave primaria) y "nombre".

Para agregar integridad referencial entre estas dos tablas, necesitarás definir una clave foránea en la tabla "libros" que haga referencia a la clave primaria en la tabla "autores". Aquí está el código SQL para crear estas dos tablas y agregar la integridad referencial:

~~~
-- Crear la base de datos
CREATE DATABASE biblioteca;

-- Seleccionar la base de datos
USE biblioteca;

-- Crear la tabla de autores
CREATE TABLE autores (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
);

-- Crear la tabla de libros
CREATE TABLE libros (
  id INT NOT NULL AUTO_INCREMENT,
  titulo VARCHAR(100) NOT NULL,
  autor_id INT NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (autor_id) REFERENCES autores(id)
);

-- Agregar un autor a la tabla de autores
INSERT INTO autores (nombre) VALUES ('Stephen King');

-- Agregar un libro a la tabla de libros
INSERT INTO libros (titulo, autor_id, precio) VALUES ('It', 1, 15.99);

-- Intentar agregar una restricción de clave foránea a la tabla de libros
ALTER TABLE libros ADD CONSTRAINT fk_libros_autores FOREIGN KEY (autor_id) REFERENCES autores(id) ON DELETE SET NULL;
~~~

**EXPLICACIÓN:**

El comando "CREATE DATABASE" crea una nueva base de datos llamada "biblioteca".

El comando "USE" selecciona la base de datos "biblioteca" para que todos los comandos posteriores se apliquen a esa base de datos.

El comando "CREATE TABLE" crea dos tablas: "autores" y "libros". La tabla "autores" tiene dos columnas: "id" (un número de identificación único para cada autor) y "nombre". La tabla "libros" tiene cuatro columnas: "id" (un número de identificación único para cada libro), "titulo", "autor_id" (un número de identificación para el autor del libro) y "precio".

El comando "FOREIGN KEY" en la tabla "libros" define una clave foránea que hace referencia a la clave primaria "id" en la tabla "autores". Esto garantiza que cualquier valor ingresado en la columna "autor_id" de la tabla "libros" tenga una correspondencia en la columna "id" de la tabla "autores".

El comando "INSERT INTO" agrega un autor y un libro a sus respectivas tablas.

El comando "ALTER TABLE" intenta agregar una restricción de clave foránea adicional a la tabla de "libros". Sin embargo, esto generará un error porque la tabla ya tiene una clave foránea definida para la columna "autor_id". En lugar de agregar una nueva clave foránea, debes modificar la existente utilizando el comando ALTER TABLE. Por ejemplo, puedes cambiar el comando para lo siguiente:

**SOLUCIÓN:**
El comando "DROP FOREIGN KEY" elimina la restricción de clave foránea existente en la tabla de "libros".

El comando "ADD CONSTRAINT" agrega una nueva restricción de clave foránea a la tabla de "libros". La nueva restricción se llama "fk_libros_autores" y hace referencia a la columna "id" en la tabla de "autores". También se establece la opción "ON DELETE CASCADE", lo que significa que si un autor se elimina de la tabla de "autores", todos los libros relacionados con ese autor también se eliminarán automáticamente de la tabla de "libros".
~~~
-- Modificar la restricción de clave foránea existente en la tabla de libros
ALTER TABLE libros DROP FOREIGN KEY libros_ibfk_1;
ALTER TABLE libros ADD CONSTRAINT fk_libros_autores FOREIGN KEY (autor_id) REFERENCES autores(id) ON DELETE CASCADE;
~~~

# EJERCICIO 5 (difícil)
Supongamos que tenemos dos tablas: "usuarios" y "pedidos". La tabla "usuarios" tiene una clave primaria "id" y la tabla "pedidos" tiene una clave primaria compuesta por "id_usuario" y "num_pedido", donde "id_usuario" es una clave foránea que hace referencia a la tabla "usuarios". Ahora queremos modificar la tabla "usuarios" para que la clave primaria sea la columna "email" en lugar de la columna "id". Además, necesitamos actualizar la tabla "pedidos" para que la clave foránea "id_usuario" haga referencia a la columna "email" en lugar de la columna "id".

~~~
-- 1. Crear una nueva tabla de usuarios temporal con la clave primaria "email"
CREATE TABLE usuarios_temp (
  email VARCHAR(255) PRIMARY KEY,
  nombre VARCHAR(255),
  direccion VARCHAR(255)
);

-- 2. Copiar los datos de la tabla de usuarios a la nueva tabla de usuarios temporal
INSERT INTO usuarios_temp (email, nombre, direccion)
SELECT email, nombre, direccion
FROM usuarios;

-- 3. Eliminar la tabla de usuarios original
DROP TABLE usuarios;

-- 4. Renombrar la nueva tabla de usuarios temporal como la tabla de usuarios original
ALTER TABLE usuarios_temp RENAME TO usuarios;

-- 5. Modificar la tabla de pedidos para que la clave foránea "id_usuario" haga referencia a la nueva clave primaria "email"
ALTER TABLE pedidos DROP FOREIGN KEY fk_pedidos_usuarios;
ALTER TABLE pedidos DROP PRIMARY KEY;
ALTER TABLE pedidos ADD PRIMARY KEY (id_usuario, num_pedido);
ALTER TABLE pedidos ADD CONSTRAINT fk_pedidos_usuarios FOREIGN KEY (id_usuario) REFERENCES usuarios(email) ON DELETE CASCADE;
~~~

**EXPLICACIÓN:**     
Primero, creamos una nueva tabla "usuarios_temp" con la columna "email" como clave primaria.
Luego, copiamos los datos de la tabla "usuarios" original a la nueva tabla "usuarios_temp".
Después, eliminamos la tabla "usuarios" original.
A continuación, renombramos la nueva tabla "usuarios_temp" como la tabla "usuarios" original.
Finalmente, modificamos la tabla "pedidos" para que la clave foránea "id_usuario" haga referencia a la nueva clave primaria "email" en la tabla "usuarios". Para hacerlo, primero eliminamos la restricción de clave foránea existente, luego eliminamos la clave primaria compuesta existente en la tabla "pedidos", agregamos una nueva clave primaria compuesta con las columnas "id_usuario" y "num_pedido", y finalmente agregamos una nueva restricción de clave foránea que hace referencia a la columna "email" en la tabla "usuarios".