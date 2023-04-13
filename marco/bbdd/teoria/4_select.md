---
autor: @nurialiano
licence: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
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
- **LIMIT**: se utiliza para limitar la cantidad de registros que se seleccionarán.
- **INTO OUTFILE**: se utiliza para escribir los resultados de una consulta en un archivo externo
- **GROUP BY**: se utiliza para agrupar los registros en función de un campo o conjunto de campos
  - **ASC/DESC**: se utiliza para ordenar los resultados en orden ascendente o descendente
- **HAVING**: se utiliza para establecer condiciones adicionales después de agrupar los registros.
- **ORDER BY**: se utiliza para ordenar los resultados en función de un campo o conjunto de campos.

### Ejemplo

~~~sql

-- Crear la base de datos 'mi_basedatos'
CREATE DATABASE mi_basedatos;
-- Usar la base de datos 'mi_basedatos'
USE mi_basedatos;
-- Crear una tabla llamada 'productos' con tres columnas: 'id', 'nombre' y 'categoria'
CREATE TABLE productos (
  id INT PRIMARY KEY,
  nombre VARCHAR(50),
  categoria VARCHAR(50)
);
-- Insertar algunos datos en la tabla 'productos'
INSERT INTO productos (id, nombre, categoria)
VALUES
  (1, 'Laptop Dell', 'Electrónica'),
  (2, 'Smartphone Samsung', 'Electrónica'),
  (3, 'Televisor LG', 'Electrónica'),
  (4, 'Camiseta Nike', 'Ropa'),
  (5, 'Zapatillas Adidas', 'Calzado'),
  (6, 'Pantalón Levis', 'Ropa');

SELECT DISTINCT nombre, COUNT(*) AS cantidad 
FROM productos 
WHERE categoria = 'Electrónica' 
GROUP BY nombre 
HAVING COUNT(*) > 1 
ORDER BY cantidad DESC 
LIMIT 10 
INTO OUTFILE 'resultados.csv';
~~~

### Explicación

En este ejemplo, estamos seleccionando de la tabla productos, utilizando la cláusula DISTINCT para asegurarnos de que cada nombre de producto solo aparezca una vez. Luego, usamos la cláusula WHERE para filtrar los resultados y solo seleccionar productos de la categoría 'Electrónica'.

Dentro de la cláusula WHERE, utilizamos diferentes operadores, como = para comparar valores y AND para combinar condiciones. También podemos utilizar operadores aritméticos, como +, -, * y /, para realizar cálculos en nuestras consultas.

Después de filtrar los resultados, utilizamos la cláusula GROUP BY para agrupar los productos por nombre y contar cuántos hay en cada grupo. Podemos ordenar los resultados utilizando la cláusula ORDER BY, utilizando el orden ascendente (ASC) o descendente (DESC).

Si queremos filtrar los resultados aún más, podemos utilizar la cláusula HAVING para especificar una condición para los grupos. En este ejemplo, estamos seleccionando solo aquellos grupos con más de un producto.

Finalmente, utilizamos la cláusula LIMIT para limitar el número de resultados a 10 y la cláusula INTO OUTFILE para guardar los resultados en un archivo llamado resultados.csv.
