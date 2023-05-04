---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# SELECT

El comando "SELECT" se utiliza para seleccionar información de una o varias tablas en una base de datos. Al utilizar este comando, se pueden utilizar las siguientes opciones:

- **all/DISTINCT**: "all" significa que se seleccionarán todos los registros que cumplan con los criterios establecidos, mientras que "DISTINCT" significa que se seleccionarán solo los registros únicos.
- **WHERE**: se utiliza para establecer condiciones específicas que deben cumplir los registros para ser seleccionados
- **OPERADORES**: son herramientas utilizadas para comparar y evaluar datos. Hay varios tipos de operadores, entre ellos
  - **COMPARACION**: se utilizan para comparar dos valores y determinar si son iguales, diferentes, mayores o menores.
  - **LOGICOS**: se utilizan para evaluar si dos o más condiciones son verdaderas o falsas.
  - **ARITMETICOS**: se utilizan para realizar operaciones matemáticas.
  - **IS NULL/IS NOT NULL**: se utilizan para evaluar si un valor es nulo o no
  - **CONCATENACIÓN DE CADENAS**: PostgreSQL permite el uso de operadores de concatenación de cadenas (||) y de unión de arrays (+), que no están disponibles en otros lenguajes de bases de datos
- **LIMIT**: se utiliza para limitar la cantidad de registros que se seleccionarán.
- **COPY**: se utiliza para escribir los resultados de una consulta en un archivo externo
- **GROUP BY**: se utiliza para agrupar los registros en función de un campo o conjunto de campos
  - **ASC/DESC**: se utiliza para ordenar los resultados en orden ascendente o descendente
  - **NULLS FIRST/NULLS LAST**: se utiliza para determinar si los valores nulos se mostrarán primero o último en los resultados ordenados.
- **HAVING**: se utiliza para establecer condiciones adicionales después de agrupar los registros.
  >:pencil: **NOTA** en PostgreSQL se puede usar una cláusula "FILTER" en las funciones de agregación para establecer condiciones adicionales después de agrupar los registros. "HAVING" aún se admite en PostgreSQL, pero "FILTER" es una forma más flexible de lograr el mismo resultado.
- **ORDER BY**: se utiliza para ordenar los resultados en función de un campo o conjunto de campos.

## Ejemplo

~~~sql
-- Crear la base de datos 'mi_basedatos'
CREATE DATABASE mi_basedatos;

-- Conectar a la base de datos 'mi_basedatos'
\c mi_basedatos

-- Crear una tabla llamada 'productos' con tres columnas: 'id', 'nombre' y 'categoria'
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    categoria VARCHAR(50)
);

-- Insertar algunos datos en la tabla 'productos'
INSERT INTO productos (nombre, categoria)
VALUES
    ('Laptop Dell', 'Electrónica'),
    ('Smartphone Samsung', 'Electrónica'),
    ('Televisor LG', 'Electrónica'),
    ('Camiseta Nike', 'Ropa'),
    ('Zapatillas Adidas', 'Calzado'),
    ('Pantalón Levis', 'Ropa');

--Consulta con las dististintas claúsulas
SELECT DISTINCT nombre, COUNT(*) AS cantidad 
FROM productos 
WHERE categoria = 'Electrónica' 
GROUP BY nombre 
HAVING COUNT(*) > 1 
ORDER BY cantidad DESC 
LIMIT 10

--Copiar base de datos a un fichero CSV
COPY productos FROM '/ruta/al/archivo.csv' WITH (FORMAT CSV, HEADER);
--Copiar algunas columnas a un fichero CSV
COPY productos(id, nombre) FROM '/ruta/al/archivo.csv' WITH (FORMAT CSV, HEADER);
~~~

### Explicación

En este ejemplo, estamos seleccionando de la tabla productos, utilizando la cláusula DISTINCT para asegurarnos de que cada nombre de producto solo aparezca una vez. Luego, usamos la cláusula WHERE para filtrar los resultados y solo seleccionar productos de la categoría 'Electrónica'.

Dentro de la cláusula WHERE, utilizamos diferentes operadores, como = para comparar valores y AND para combinar condiciones. También podemos utilizar operadores aritméticos, como +, -, \* y /, para realizar cálculos en nuestras consultas.

Después de filtrar los resultados, utilizamos la cláusula GROUP BY para agrupar los productos por nombre y contar cuántos hay en cada grupo. Podemos ordenar los resultados utilizando la cláusula ORDER BY, utilizando el orden ascendente (ASC) o descendente (DESC).

Si queremos filtrar los resultados aún más, podemos utilizar la cláusula HAVING para especificar una condición para los grupos. En este ejemplo, estamos seleccionando solo aquellos grupos con más de un producto.

Finalmente, utilizamos la cláusula LIMIT para limitar el número de resultados a 10 y el comando COPY para guardar los resultados en un archivo llamado archivo.csv.
