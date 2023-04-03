# EJERCICIO 1 (PRIMARY AND FOREIGN KEY)

1. Crea una base de datos llamada "Ejercicio1"
2. Crea dos tablas llamadas "clientes" y "pedidos"
3. La tabla "clientes" debe tener los siguientes campos: "id_cliente" (clave primaria), "nombre" y "apellidos"
4. La tabla "pedidos" debe tener los siguientes campos: "id_pedido" (clave primaria), "id_cliente" (clave foránea), "fecha_pedido" y "importe"
5. Define la integridad referencial para la clave foránea "id_cliente" en la tabla "pedidos"

## SOLUCIÓN

~~~sql
   -- Crear la base de datos
   CREATE DATABASE Ejercicio1;

   -- Usar la base de datos creada
   USE Ejercicio1;

   -- Crear la tabla "clientes"
   CREATE TABLE clientes (
      id_cliente INT PRIMARY KEY,
      nombre VARCHAR(50),
      apellidos VARCHAR(50)
   );

   -- Crear la tabla "pedidos"
   CREATE TABLE pedidos (
      id_pedido INT PRIMARY KEY,
      id_cliente INT,
      fecha_pedido DATE,
      importe DECIMAL(10,2),
      FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
   );
~~~

# EJERCICIO 2 (forzar error)

1. Crea la tabla "actores" con los siguientes campos: id_actor (clave primaria), nombre, fecha_nacimiento

~~~sql
   CREATE TABLE actores (
      id_actor INT PRIMARY KEY,
      nombre VARCHAR(50),
      fecha_nacimiento DATE
   );
~~~

2. Crea la tabla "peliculas" con los siguientes campos: id_pelicula (clave primaria), titulo, anio, id_actor (clave foránea de la tabla actores)

~~~sql
   CREATE TABLE peliculas (
      id_pelicula INT PRIMARY KEY,
      titulo VARCHAR(100),
      anio INT,
      id_actor INT,
      FOREIGN KEY (id_actor) REFERENCES actores(id_actor)
   );
~~~

1. Inserta algunos datos en ambas tablas

~~~sql
   INSERT INTO actores (id_actor, nombre, fecha_nacimiento)
   VALUES (1, 'Tom Hanks', '1956-07-09'),
      (2, 'Meryl Streep', '1949-06-22'),
      (3, 'Leonardo DiCaprio', '1974-11-11');

   INSERT INTO peliculas (id_pelicula, titulo, anio, id_actor)
   VALUES (1, 'Forrest Gump', 1994, 1),
      (2, 'The Post', 2017, 2),
      (3, 'The Revenant', 2015, 3);
~~~

1. Intenta insertar una película con un id_actor que no existe en la tabla actores
   *Esto dará como resultado un error de integridad referencial, ya que no existe ningún actor con id_actor igual a 4*

   ~~~sql
   INSERT INTO peliculas (id_pelicula, titulo, anio, id_actor) VALUES (4, 'Inception', 2010, 4);
   ~~~

# EJERCICIO 3 (UPDATE, DELETE y forzar error)

Supongamos que tenemos dos tablas en nuestra base de datos: "Clientes" y "Pedidos". Cada pedido pertenece a un cliente y un cliente puede tener muchos pedidos. Si eliminamos un cliente, queremos que todos sus pedidos también sean eliminados (ON CASCADE). Sin embargo, si un pedido aún no ha sido entregado, no queremos eliminarlo y en su lugar, estableceremos su cliente_id como NULL. Además, si hay algún pedido que hace referencia a un cliente que ya ha sido eliminado, queremos evitar que se elimine el cliente y en su lugar, restringir la eliminación de ese pedido.

~~~sql
CREATE TABLE Clientes (
    id INT PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE Pedidos (
    id INT PRIMARY KEY,
    cliente_id INT,
    producto VARCHAR(50),
    entregado BOOLEAN DEFAULT false,
    FOREIGN KEY (cliente_id)
        REFERENCES Clientes(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
~~~

**Explicación:** En este ejemplo, hemos establecido una clave externa en la tabla Pedidos que hace referencia a la columna id en la tabla Clientes. Hemos configurado la eliminación en cascada y la actualización en cascada, lo que significa que si eliminamos un cliente, todos sus pedidos también se eliminarán y si actualizamos el id de un cliente, ese cambio también se reflejará en los pedidos relacionados. También hemos establecido ON DELETE SET NULL para asegurarnos de que si un pedido hace referencia a un cliente eliminado, su cliente_id se establecerá como NULL en lugar de eliminarse.

#### PRUEBAS

1. insertar algunos datos de prueba:
 
~~~sql
    INSERT INTO Clientes (id, nombre) VALUES (1, 'Juan');
    INSERT INTO Pedidos (id, cliente_id, producto) VALUES (1, 1, 'Zapatos');
    INSERT INTO Pedidos (id, cliente_id, producto) VALUES (2, 1, 'Camisa');
~~~

2. Si eliminamos al cliente Juan, deberíamos ver que todos sus pedidos también se eliminan:
   ``DELETE FROM Clientes WHERE id = 1;``
3. Si consultamos la tabla Pedidos después de ejecutar esta eliminación, veremos que no hay ningún pedido en la tabla:

~~~sql
   SELECT * FROM Pedidos;
    -- resultado: no hay filas
~~~

4. Si actualizamos el id del cliente Juan a 2, deberíamos ver que los pedidos relacionados también se actualizan automáticamente

~~~sql
    UPDATE Clientes SET id = 2 WHERE id = 1;
    SELECT * FROM Pedidos;
    -- resultado: ambos pedidos ahora tienen cliente_id = 2
~~~

5. Finalmente, si intentamos eliminar un pedido que hace referencia a un cliente que ya ha sido eliminado, deberíamos ver que se produce un error debido a la restricción de eliminación

~~~sql
    DELETE FROM Pedidos WHERE id = 1;
    -- resultado: ERROR: update or delete on table "Clientes" violates foreign key constraint "pedidos_cliente_id_fkey" on table "Pedidos"
~~~
