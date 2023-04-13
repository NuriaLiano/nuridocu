---
autor: @nurialiano
licence: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---

# CONSULTAS CORRELACIONADAS

Las consultas correlacionadas en SQL son aquellas en las que una subconsulta depende de una columna de la consulta principal (consulta externa). En otras palabras, la subconsulta se ejecuta una vez para cada fila de la consulta principal, utilizando los valores de las columnas de esa fila en la subconsulta.

En una consulta correlacionada, la subconsulta se utiliza para filtrar los resultados de la consulta principal. La subconsulta se ejecuta una vez para cada fila de la tabla principal y los resultados de la subconsulta se utilizan para determinar si se debe incluir o excluir la fila de la consulta principal.

Es importante tener en cuenta que las consultas correlacionadas pueden ser menos eficientes que otras formas de consulta, ya que se ejecutan una vez para cada fila de la consulta principal. Por lo tanto, es importante usarlas con cuidado y considerar otras opciones de consulta si es posible

## EJEMPLO

~~~sql
SELECT * 
FROM orders o 
WHERE o.order_date > (SELECT MAX(order_date) 
                      FROM orders 
                      WHERE customer_id = o.customer_id);
~~~

En esta consulta, la subconsulta se utiliza para encontrar la fecha más reciente de un pedido para cada cliente. Luego, se utiliza esa fecha más reciente para filtrar los pedidos en la consulta principal, devolviendo solo los pedidos cuya fecha de pedido sea posterior a la fecha más reciente de ese cliente