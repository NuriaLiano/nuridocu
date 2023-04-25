---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# SUBCONSULTAS

Las subconsultas son consultas o instrucciones SQL que se anidan dentro de otra consulta más grande. Estas subconsultas se utilizan para extraer datos específicos de una tabla y se pueden utilizar en diferentes cláusulas de SQL, como WHERE, HAVING, FROM y SELECT.

Por ejemplo, imagina que tienes dos tablas, una de "clientes" y otra de "órdenes". Quieres encontrar el nombre de todos los clientes que hayan realizado una compra. En este caso, podrías utilizar una subconsulta en la cláusula WHERE para obtener el resultado deseado:

~~~sql
SELECT nombre
FROM clientes
WHERE id IN (SELECT id_cliente FROM ordenes)
~~~

La subconsulta "SELECT id_cliente FROM ordenes" se ejecuta primero para obtener una lista de todos los clientes que han realizado una orden, y luego esa lista se utiliza en la cláusula WHERE de la consulta principal para filtrar los nombres de los clientes que se desean.

Las subconsultas también se utilizan para realizar operaciones complejas y consultas más avanzadas. Por ejemplo, se pueden utilizar para hacer consultas sobre varias tablas, agregar o unir resultados de múltiples consultas, y realizar cálculos complejos.

En resumen, las subconsultas son consultas o instrucciones SQL anidadas dentro de otra consulta más grande, que se utilizan para extraer datos específicos de una tabla y para realizar operaciones más complejas en una base de datos.

## Tipos de subconsultas

### Subconsultas correlacionadas

Son subconsultas que se ejecutan para cada fila de la consulta principal. La subconsulta se basa en valores de la fila actual de la consulta principal, lo que la hace "correlacionada". Las subconsultas correlacionadas se utilizan comúnmente en la cláusula WHERE para filtrar los resultados según ciertos criterios.

~~~sql
SELECT * FROM pedidos WHERE fecha > (SELECT fecha FROM clientes WHERE id_cliente = pedidos.id_cliente);
~~~

En este ejemplo, la subconsulta se ejecuta para cada fila de la tabla "pedidos" y utiliza el valor "id_cliente" de la fila actual para buscar la fecha correspondiente en la tabla "clientes".

### Subconsultas escalares

Son subconsultas que devuelven un solo valor, que se utiliza en la consulta principal. Las subconsultas escalares se utilizan comúnmente en la cláusula SELECT para agregar o modificar los resultados de la consulta.

~~~sql
SELECT nombre, (SELECT COUNT(*) FROM pedidos WHERE id_cliente = clientes.id_cliente) AS cantidad_pedidos FROM clientes;
~~~

En este ejemplo, la subconsulta se utiliza en la cláusula SELECT para contar el número de pedidos que ha realizado cada cliente y devolver el resultado como una columna adicional llamada "cantidad_pedidos".

### Subconsultas anidadas

Son subconsultas que se anidan dentro de otras subconsultas. Las subconsultas anidadas se utilizan para realizar operaciones más complejas y para extraer datos de múltiples tablas.

~~~sql
SELECT * FROM clientes WHERE id_cliente IN (SELECT id_cliente FROM pedidos WHERE id_producto IN (SELECT id_producto FROM productos WHERE categoria = 'Electrónica'));
~~~

En este ejemplo, la subconsulta más interna se utiliza para buscar todos los productos en la categoría "Electrónica". La subconsulta intermedia se utiliza para encontrar los pedidos que contienen uno o más de estos productos. La subconsulta externa se utiliza para encontrar los clientes que han realizado estos pedidos.

### Subconsultas con múltiples columnas

Son subconsultas que devuelven más de una columna de datos. Estas subconsultas se utilizan comúnmente para unir o combinar resultados de varias tablas.

~~~sql
SELECT * FROM productos WHERE (id_producto, nombre) IN (SELECT id_producto, nombre FROM productos_ventas WHERE ventas > 100);
~~~

En este ejemplo, la subconsulta se utiliza para buscar los productos que han registrado más de 100 ventas en la tabla "productos_ventas". La subconsulta devuelve dos columnas: "id_producto" y "nombre", que se comparan con las columnas correspondientes en la tabla "productos".

## Tipos según resultado

### Subconsultas que devuelven un solo valor

Son subconsultas que devuelven un único valor, como una suma, un promedio, una fecha máxima o mínima, etc. Estas subconsultas se utilizan a menudo en la cláusula SELECT para recuperar un valor único que se utilizará en otra parte de la consulta.

~~~sql
SELECT nombre, (SELECT COUNT(*) FROM compras WHERE id_cliente = clientes.id) as num_compras
FROM clientes;
~~~

En este ejemplo, la subconsulta se utiliza en la cláusula SELECT para contar el número de compras que ha realizado cada cliente y devolver el resultado como una columna adicional llamada "num_compras".

### Subconsultas que devuelven múltiples valores

Son subconsultas que devuelven varias filas de datos, como una lista de nombres de clientes que han realizado una compra en un rango de fechas específico. Estas subconsultas se pueden utilizar en la cláusula WHERE o en otras partes de la consulta para filtrar o combinar datos.

~~~sql
SELECT nombre, direccion
FROM clientes
WHERE id IN (SELECT id_cliente FROM compras WHERE fecha BETWEEN '2022-01-01' AND '2022-12-31');
~~~

En este ejemplo, la subconsulta se utiliza en la cláusula WHERE para encontrar todos los clientes que han realizado compras en un rango de fechas específico.

### Subconsultas que se comparan con una lista de valores

Son subconsultas que se utilizan en la cláusula WHERE para comparar una columna de la tabla principal con una lista de valores de otra tabla. Por ejemplo, se podría utilizar una subconsulta para encontrar todos los clientes que han realizado una compra en un conjunto específico de fechas.

~~~sql
SELECT nombre, direccion
FROM clientes
WHERE id IN (SELECT id_cliente FROM compras WHERE id_producto IN (SELECT id FROM productos WHERE categoria = 'Electrónica'));
~~~

En este ejemplo, la subconsulta se utiliza en la cláusula WHERE para encontrar todos los clientes que han comprado productos de electrónica.

### Subconsultas que se comparan con un conjunto de valores

Son subconsultas que se utilizan para comparar una columna con un conjunto de valores, como los resultados de otra subconsulta. Estas subconsultas se pueden utilizar para filtrar o combinar resultados en la consulta principal.

~~~sql
SELECT nombre, direccion
FROM clientes
WHERE id IN (SELECT id_cliente FROM compras WHERE fecha BETWEEN '2022-01-01' AND '2022-12-31')
AND id NOT IN (SELECT id_cliente FROM compras WHERE fecha > '2022-12-31');
~~~

En este ejemplo, la subconsulta se utiliza en la cláusula WHERE para encontrar todos los clientes que han realizado compras en un rango de fechas específico pero no han realizado ninguna compra después de ese rango de fechas.

## ¿Es lo mismo las subconsultas que los joins?

Tanto las subconsultas como las cláusulas JOIN son formas de combinar datos de múltiples tablas en una consulta SQL. Sin embargo, hay algunas diferencias entre ellas:

1. Estructura de la consulta:

   - Las subconsultas se escriben dentro de la cláusula WHERE o HAVING de la consulta principal.
   - Las cláusulas JOIN se escriben al final de la consulta principal.

2. Tamaño del conjunto de resultados:

   - Las subconsultas suelen devolver un conjunto de resultados pequeño que se utiliza para filtrar los resultados de la consulta principal.
   - Las cláusulas JOIN unen varias tablas de datos y devuelven un conjunto de resultados más grande.

3. Rendimiento:

   - Las subconsultas pueden ser menos eficientes en términos de rendimiento que las cláusulas JOIN, especialmente cuando se utilizan para filtrar grandes conjuntos de datos.
   - Las subconsultas pueden ser menos eficientes en términos de rendimiento que las cláusulas JOIN, especialmente cuando se utilizan para filtrar grandes conjuntos de datos.

>:pencil: **NOTA** Se recomienda utilizar cláusulas JOIN para unir tablas de datos grandes, mientras que las subconsultas son útiles para filtrar datos en un conjunto de resultados más pequeño.