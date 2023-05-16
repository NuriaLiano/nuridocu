
# Ejercicio con objetos, sesiones, conexión a base de datos, consultas y subconsultas

Has sido contratado como desarrollador web para crear un sistema de consulta de series de televisión. Deberás implementar un formulario básico y una página de resultados utilizando PHP y sesiones.

Instrucciones:

1. Crea un archivo llamado index.html que contenga un formulario HTML con los siguientes elementos:

- Un campo de texto para ingresar el género de la serie.
- Dos botones de tipo submit: "Consultar" y "Mostrar Serie Aleatoria".

2. Crea un archivo llamado consultar_series.php que será responsable de realizar la conexión a la base de datos y procesar los datos del formulario.

- Utiliza la clase conexionDB para establecer la conexión con la base de datos.
- Valida y sanitiza los datos ingresados en el formulario.
- Si se presiona el botón "Consultar", ejecuta una consulta SQL para obtener todas las series del género especificado y almacena los resultados en una variable de sesión.
- Si se presiona el botón "Mostrar Serie Aleatoria", ejecuta una consulta SQL para obtener una serie aleatoria y almacena el resultado en una variable de sesión.

3. Crea un archivo llamado resultados.php que mostrará los resultados de la consulta realizada.

- Muestra los resultados dependiendo del género introducido en el index.html.
- Si no se encontraron resultados, muestra un mensaje indicando que no se encontraron series.

1. Crea un archivo llamado serie_aleatoria.php que mostrará una serie aleatoria.

- Recupera la serie aleatoria almacenada en la variable de sesión y muestra sus detalles en una tabla.

Recuerda utilizar sesiones para mantener la información de los resultados y la serie aleatoria entre las diferentes páginas. Puedes utilizar las funciones y métodos proporcionados por la extensión PDO para realizar consultas a la base de datos.

Nota: Asegúrate de que todos los archivos necesarios estén en la misma ubicación y de que la configuración de la base de datos sea correcta.

## Base de datos necesaria

~~~sql
-- Crear la base de datos
CREATE DATABASE series_tv;

-- Conectarse a la base de datos
USE series_tv;

-- Crear tablas
CREATE TABLE Series (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    genero VARCHAR(100),
    anio_lanzamiento INT
);
CREATE TABLE Temporadas (
    id INT PRIMARY KEY,
    serie_id INT,
    numero INT,
    episodios INT,
    FOREIGN KEY (serie_id) REFERENCES Series(id)
);

-- Insertar datos
INSERT INTO Series (id, nombre, genero, anio_lanzamiento)
VALUES
    (1, 'Friends', 'Comedia', 1994),
    (2, 'Breaking Bad', 'Drama', 2008),
    (3, 'Stranger Things', 'Ciencia ficción', 2016),
    (4, 'Game of Thrones', 'Fantasía', 2011);

INSERT INTO Temporadas (id, serie_id, numero, episodios)
VALUES
    (1, 1, 1, 24),
    (2, 1, 2, 24),
    (3, 2, 1, 7),
    (4, 2, 2, 13),
    (5, 3, 1, 8),
    (6, 3, 2, 9),
    (7, 4, 1, 10),
    (8, 4, 2, 9),
    (9, 4, 3, 10);
~~~
