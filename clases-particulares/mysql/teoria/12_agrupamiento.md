---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# AGRUPAMIENTO

El agrupamiento en SQL es una técnica que se utiliza para agrupar filas de datos que comparten una o más columnas comunes y aplicar funciones de agregación a ellas, como SUM, COUNT, AVG, MAX o MIN.
La cláusula GROUP BY se utiliza para agrupar los datos en función de una o varias columnas y se coloca después de la cláusula WHERE en una consulta SQL.

Por ejemplo, si tienes una tabla de ventas con las columnas "producto", "vendedor" y "monto", puedes utilizar la cláusula GROUP BY para agrupar los datos por producto y obtener el monto total de ventas para cada uno de ellos.

~~~sql
SELECT producto, SUM(monto) as total_ventas
FROM ventas
GROUP BY producto;
~~~

Esta consulta agruparía los datos de la tabla "ventas" por el nombre del producto y calcularía la suma total de ventas para cada producto, mostrando los resultados en una tabla con dos columnas: "producto" y "total_ventas".
