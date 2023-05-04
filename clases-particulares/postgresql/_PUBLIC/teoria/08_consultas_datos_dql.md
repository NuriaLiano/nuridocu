---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Definición de datos 'DQL'

DQL significa "Data Query Language" (Lenguaje de Consulta de Datos) en SQL. Se utiliza para consultar datos de una o varias tablas y recuperar datos de la base de datos sin modificarlos. Puede especificar las columnas que desea recuperar, aplicar filtros, ordenar los resultados y realizar cálculos y agregaciones.

## Comandos comunes de DQL

- **SELECT**: se utiliza para consultar datos de una o varias tablas en una base de datos. Puede especificar las columnas que desea recuperar, aplicar filtros, ordenar los resultados y realizar cálculos y agregaciones.
  - **DISTINCT**: se utiliza para seleccionar valores distintos de una columna en una tabla.
  - **FROM**: se utiliza para especificar la tabla o tablas de las que se van a recuperar los datos.
  - **WHERE**: se utiliza para filtrar los datos que se van a recuperar según una o varias condiciones.
  - **GROUP BY**: se utiliza para agrupar los resultados según una o varias columnas.
  - **HAVING**: se utiliza para filtrar los grupos resultantes según una o varias condiciones.
  - **ORDER BY**: se utiliza para ordenar los resultados según una o varias columnas.
  - **LIMIT**: se utiliza para limitar el número de filas que se recuperan.

### Ejemplo SELECT

Por ejemplo, si quieres recuperar todos los datos de una tabla:

~~~sql
SELECT * FROM nombre_tabla;
~~~

Por ejemplo, si quieres recuperar sólo algunas columnas de una tabla:

~~~sql
SELECT columna1, columna2 FROM nombre_tabla;
~~~

Por ejemplo, si quieres realizar cálculos en una consulta:

~~~sql
SELECT columna1, columna2, columna1 + columna2 AS sum FROM nombre_tabla;
~~~

### Ejemplo SELECT DISTINCT

Por ejemplo, si quieres seleccionar valores distintos de una columna

~~~sql
SELECT DISTINCT columna1 FROM nombre_tabla;
~~~

### Ejemplo SELECT FROM

Por ejemplo, si quieres especificar la tabla o tablas de las que se van a recuperar los datos.

~~~sql
SELECT * FROM tabla1, tabla2 WHERE tabla1.columna1 = tabla2.columna2;
~~~

### Ejemplo SELECT WHERE

Por ejemplo, si quieres filtrar los datos que se van a recuperar según una o varias condiciones.

~~~sql
SELECT * FROM nombre_tabla WHERE columna1 > 100;
~~~

### Ejemplo SELECT GROUP BY

Por ejemplo, si quieres agrupar los resultados según una o varias columnas.

~~~sql
SELECT columna1, AVG(columna2) FROM nombre_tabla GROUP BY columna1;
~~~

### Ejemplo SELECT HAVING

Por ejemplo, si quieres filtrar los grupos resultantes según una o varias condiciones.

~~~sql
SELECT columna1, AVG(columna2) FROM nombre_tabla GROUP BY columna1 HAVING AVG(columna2) > 50;
~~~

### Ejemplo SELECT ORDER BY

Por ejemplo, si quieres ordenar los resultados según una o varias columnas.

~~~sql
SELECT * FROM nombre_tabla ORDER BY columna1 ASC, columna2 DESC;
~~~

### Ejemplo SELECT LIMIT

Por ejemplo, si quieres limitar el número de filas que se recuperan.

~~~sql
SELECT * FROM nombre_tabla LIMIT 10;
~~~
