# EJERCICIO 1

Supongamos que queremos relacionar dos tablas: "estudiantes" y "cursos". Cada estudiante puede estar inscrito en varios cursos y cada curso puede tener varios estudiantes inscritos. Para esto, necesitamos una tabla intermedia que vincule a cada estudiante con los cursos a los que está inscrito.

1. Crear la tabla "estudiantes":

~~~sql
  CREATE TABLE estudiantes (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(100)
  );
~~~

2. Crear la tabla "cursos":

~~~sql
  CREATE TABLE cursos (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    descripcion VARCHAR(100)
  );
~~~

3. Crear la tabla intermedia "inscripciones":

~~~sql
  CREATE TABLE inscripciones (
    id INT PRIMARY KEY,
    id_estudiante INT,
    id_curso INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id),
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
  );
~~~

En este ejemplo, la tabla "inscripciones" tiene dos claves foráneas que hacen referencia a las claves primarias en las tablas "estudiantes" y "cursos". Esta tabla intermedia se utiliza para relacionar los estudiantes con los cursos en los que están inscritos.

# EJERCICIO 2

Supongamos que queremos relacionar dos tablas: "clientes" y "pedidos". Cada cliente puede tener varios pedidos y cada pedido pertenece a un solo cliente. Para esto, necesitamos una clave foránea en la tabla "pedidos" que haga referencia a la clave primaria en la tabla "clientes".

1. Crear la tabla "clientes":

~~~sql
  CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    direccion VARCHAR(100),
    email VARCHAR(100)
  );
~~~

1. Crear la tabla "pedidos":

~~~sql
  CREATE TABLE pedidos (
    num_pedido INT PRIMARY KEY,
    fecha_pedido DATE,
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
  );
~~~

En este ejemplo, la tabla "pedidos" tiene una clave foránea "id_cliente" que hace referencia a la clave primaria en la tabla "clientes". Esto establece una relación uno a muchos entre los clientes y los pedidos.

# EJERCICIO 3

Supongamos que queremos relacionar dos tablas: "autores" y "libros". Cada autor puede escribir varios libros y cada libro puede tener varios autores. Para esto, necesitamos una tabla intermedia que vincule a cada autor con los libros que ha escrito.

1. Crear la tabla "autores":

~~~sql
  CREATE TABLE autores (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(100)
  );
~~~

2. Crear la tabla "libros":

~~~sql
  CREATE TABLE libros (
    id INT PRIMARY KEY,
    titulo VARCHAR(50),
    fecha_publicacion DATE
  );
~~~

3. Crear la tabla intermedia "escritos_por":

~~~sql
  CREATE TABLE escritos_por (
    id INT PRIMARY KEY,
    id_autor INT,
    id_libro INT,
    FOREIGN KEY (id_autor) REFERENCES autores(id),
    FOREIGN KEY (id_libro) REFERENCES libros(id)
  );
~~~

En este ejemplo, la tabla "escritos_por" tiene dos claves foráneas que hacen referencia a las claves primarias en las tablas "autores