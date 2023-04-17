---
autor: @nurialiano
licence: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---

# EJERCICIO REPASO AÑADIR, MODIFICAR Y BORRAR

## Crea la base de datos 'videojuegos'

~~~sql
CREATE DATABASE videojuegos;
USE videojuegos;
~~~

## Crea una tabla 'titulos'

**Campos**

- id NOT NULL AUTO_INCREMENT PRIMARY KEY
- nombre NOT NULL
- plataforma NOT NULL,
- fecha_lanzamiento NOT NULL

~~~sql
CREATE TABLE titulos (
  id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  plataforma_id int NOT NULL,
  fecha_lanzamiento DATE NOT NULL
);
~~~

## Insertar datos

~~~sql
INSERT INTO titulos (nombre, plataforma_id, fecha_lanzamiento) VALUES
  ('The Legend of Zelda: Breath of the Wild', '3', '2017-03-03'),
  ('Red Dead Redemption 2', '1', '2018-10-26'),
  ('Horizon Zero Dawn', '1', '2017-02-28'),
  ('Fortnite', '2', '2017-07-25'),
  ('Minecraft', '2', '2011-11-18');
~~~

## Crea una tabla 'plataforma'

~~~sql
CREATE TABLE plataformas (
  id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  fabricante VARCHAR(255) NOT NULL
);
INSERT INTO plataformas (nombre, fabricante)
VALUES
  ('PlayStation 5', 'Sony'),
  ('Xbox Series X', 'Microsoft'),
  ('Nintendo Switch', 'Nintendo');
~~~

## Añadir la relación entre 'titulos' y 'plataformas'

~~~sql
-- op
ALTER TABLE titulos ADD CONSTRAINT fk_plataforma
FOREIGN KEY (plataforma_id) REFERENCES plataformas(id);

ALTER TABLE titulos ADD FOREIGN KEY (plataforma_id) REFERENCES plataformas(id);
~~~

## Cambiar la restricción de la columna 'nombre' de la tabla 'plataformas' a UNIQUE

~~~sql
ALTER TABLE plataformas MODIFY nombre VARCHAR(255) UNIQUE;
SHOW CREATE TABLE plataformas;
~~~

## Copiar una tabla 'titulos' a otra llamada 'titulos_copia'

~~~sql
CREATE TABLE titulos_copia AS
SELECT *
FROM titulos
WHERE 1=0;
~~~

>:pencil: **WHERE 1=0** se utiliza para indicar que no se seleccionará ninguna fila de la tabla "titulos", ya que solo se está interesado en la estructura de la tabla.
En caso de querer copiar la tabla con el contenido se elimina esa sentencia.

## Cambiar el nombre a la nueva tabla 'titulos_copia' por 'titulos_antiguos'

~~~sql
RENAME TABLE titulos_copia TO titulos_antiguos;
~~~

>:warning: **No es posible cambiar el nombre de una tabla utilizando el comando "MODIFY"**. Este comando se utiliza para modificar la estructura de una tabla, como cambiar el tipo de datos de una columna o agregar una restricción de clave foránea.

## Cambiar el tipo de dato por INT de la columna 'fabricante' de la tabla 'plataforma'

~~~sql
ALTER TABLE plataformas MODIFY fabricante INT;
~~~

>:warning: Ten en cuenta que, al cambiar el tipo de dato de una columna, **es posible que se pierda información si el tipo de dato original no se puede convertir al nuevo tipo de dato**. Asegúrate de tener copias de seguridad de tus datos antes de realizar cualquier cambio importante en la estructura de la tabla.

## Añadir una restriccion 'on delete cascade' a la clave foránea en la tabla 'titulos'

~~~sql
ALTER TABLE titulos
DROP FOREIGN KEY fk_plataforma;

ALTER TABLE titulos
ADD CONSTRAINT fk_plataforma
FOREIGN KEY (plataforma_id) REFERENCES plataformas(id)
ON DELETE CASCADE;
~~~

>:pencil: **ON DELETE CASCADE** es una restricción de integridad referencial que se utiliza en una base de datos para asegurarse de que cuando se borra una fila de una tabla, se borran automáticamente todas las filas relacionadas en otra tabla. Es una forma de mantener la integridad referencial y evitar datos huérfanos.
Cuando se establece una restricción "ON DELETE CASCADE" en una clave foránea, indica que si se borra una fila de la tabla principal, todas las filas relacionadas en la tabla secundaria también se eliminarán automáticamente, de forma que la integridad referencial se mantendrá.

## Eliminar la columna 'fecha_lanzamiento' de la tabla 'titulos_antiguos'

~~~sql
ALTER TABLE titulos
DROP COLUMN fecha_lanzamiento;
~~~

>:warning: Ten en cuenta que al eliminar una columna, también se eliminan todos los datos almacenados en ella.

## Eliminar la tabla 'titulos_antiguos'

~~~sql
DROP TABLE titulos_antiguos;
~~~

## Eliminar base de datos 'videojuegos'

~~~sql
DROP DATABASE videojuegos;
~~~
