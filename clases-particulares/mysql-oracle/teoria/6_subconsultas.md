# SUBCONSULTAS

Las subconsultas en SQL son consultas anidadas dentro de otra consulta. Es decir, una subconsulta es una consulta que se realiza dentro de otra consulta más grande, con el fin de obtener un resultado específico.

Las subconsultas se utilizan para:

- Realizar consultas más complejas que no se pueden lograr mediante una sola consulta
- Filtrar los resultados de una consulta en función de los resultados de otra consulta
- Realizar cálculos con los resultados de otra consulta.

Las subconsultas pueden utilizarse en diferentes partes de una consulta, como en la cláusula WHERE, en la cláusula FROM o en la cláusula HAVING. En la mayoría de los casos, las subconsultas se utilizan en la cláusula WHERE para filtrar los resultados de la consulta principal.

Es importante tener en cuenta que las subconsultas pueden afectar el rendimiento de las consultas, especialmente si se utilizan en grandes conjuntos de datos. Por lo tanto, es recomendable utilizarlas con precaución y optimizarlas según sea necesario.

## EJEMPLO

~~~sql
SELECT nombre
FROM empleado
WHERE departamento = (
    SELECT id_departamento
    FROM departamento
    WHERE nombre = 'Ventas'
);
~~~

### TIPOS DE SUBCONSULTAS

1. **Subconsultas no correlacionadas**: Estas son subconsultas que no dependen de la consulta principal. Es decir, la subconsulta se ejecuta por sí sola y se utiliza para filtrar los datos de la consulta principal. Las subconsultas no correlacionadas son las más comunes y se utilizan para consultas simples.

   ~~~sql
    SELECT nombre, salario
    FROM empleados
    WHERE salario > (SELECT AVG(salario) FROM empleados);
   ~~~

En este ejemplo, la subconsulta no correlacionada se utiliza para obtener el salario promedio de todos los empleados y se utiliza para filtrar los resultados de la consulta principal para mostrar solo aquellos empleados que ganan más que el salario promedio.

2. **Subconsultas correlacionadas**: Estas son subconsultas que dependen de la consulta principal. Es decir, la subconsulta se ejecuta para cada fila de la consulta principal y se utiliza para filtrar los datos de esa fila. Las subconsultas correlacionadas son más complejas y se utilizan para consultas más avanzadas.

   ~~~sql
    SELECT nombre, salario
    FROM empleados e
    WHERE salario > (SELECT AVG(salario) FROM empleados WHERE departamento = e.departamento);
   ~~~

En este ejemplo, la subconsulta correlacionada se utiliza para obtener el salario promedio de los empleados que trabajan en el mismo departamento que la fila actual de la consulta principal. La subconsulta se ejecuta para cada fila de la consulta principal y se utiliza para filtrar los resultados de esa fila.

### TIPOS SEGÚN EL RESULTADO

1. **Subconsultas que devuelven un valor**: Estas subconsultas devuelven un solo valor que se utiliza en la consulta principal. Estas subconsultas se pueden utilizar para realizar cálculos y comparaciones. El operador puede ser cualquier operador relacional (<,>, =, <=, =>)

   ~~~sql
   SELECT nombre, salario
   FROM empleados
   WHERE salario > (SELECT AVG(salario) FROM empleados);
   ~~~

En este ejemplo, la subconsulta devuelve un solo valor, el salario promedio de todos los empleados, que se utiliza en la cláusula WHERE para filtrar los resultados de la consulta principal.

2. **Subconsultas que devuelven una lista de valores**: Estas subconsultas devuelven una lista de valores que se utilizan en la consulta principal. Estas subconsultas se pueden utilizar para hacer coincidir valores en la consulta principal.El operador puede ser un operador lógico de conjuntos (IN, ALL, ANY)

   ~~~sql
    SELECT nombre, salario
    FROM empleados
    WHERE departamento IN (SELECT departamento FROM departamentos WHERE region = 'Norte');
   ~~~

En este ejemplo, la subconsulta devuelve una lista de valores, los departamentos que están en la región Norte, que se utilizan en la cláusula WHERE para filtrar los resultados de la consulta principal.

3. **Subconsultas que devuelven más de una columna**: Estas subconsultas devuelven más de una columna que se utiliza en la consulta principal. Estas subconsultas se pueden utilizar para hacer coincidir valores en varias columnas en la consulta principal.

   ~~~sql
    SELECT nombre, salario
    FROM empleados
    WHERE (departamento, cargo) IN (SELECT departamento, cargo FROM empleados WHERE salario > 5000);
   ~~~

En este ejemplo, la subconsulta devuelve dos columnas, departamento y cargo, que se utilizan en la cláusula WHERE para filtrar los resultados de la consulta principal.

4. **Subconsultas que devuelven cualquier número de filas y columnas**: Estas subconsultas pueden devolver cualquier número de filas y columnas y se utilizan para realizar cálculos más complejos y procesar los datos de varias tablas.

   ~~~sql
    SELECT nombre, salario
    FROM empleados
    WHERE departamento = (SELECT departamento FROM departamentos WHERE region = 'Norte' ORDER BY RAND() LIMIT 1);
   ~~~

En este ejemplo, la subconsulta devuelve una fila aleatoria de la tabla departamentos que está en la región Norte y se utiliza en la cláusula WHERE para filtrar los resultados de la consulta principal.
