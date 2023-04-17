# UNIÓN, INTERSECCIÓN Y DIFERENCIA

(también conocido como MINUS o DIFERENCIA) son operadores que se utilizan para combinar o comparar los resultados de dos o más consultas

* **UNION**: combina los resultados de dos o más consultas en una sola tabla que incluye todas las filas de las consultas. Los resultados de cada consulta deben tener la misma cantidad de columnas y tipos de datos correspondientes. Las filas duplicadas se eliminan de la tabla resultante.
* **UNION ALL**: es similar al operador UNION, pero en lugar de eliminar filas duplicadas, devuelve todas las filas de todas las consultas, incluyendo las filas duplicadas. A diferencia del operador UNION, el operador UNION ALL no realiza ninguna operación de eliminación de duplicados y, por lo tanto, devuelve todas las filas de las consultas, incluso si hay duplicados. Por lo tanto, este operador puede ser útil cuando se requiere la devolución de todos los resultados de las consultas, incluidos los duplicados. Es importante mencionar que, como en el caso del operador UNION, las consultas que se combinan con UNION ALL deben tener la misma cantidad de columnas y tipos de datos correspondientes. Si las consultas difieren en alguna columna o tipo de dato, no se podrá utilizar este operador.
* **INTERSECT**: devuelve sólo las filas que aparecen en ambas consultas. De nuevo, las consultas deben tener la misma cantidad de columnas y tipos de datos correspondientes
* **EXCEPT** o **MINUS**: devuelve todas las filas de la primera consulta que no aparecen en la segunda consulta. Las consultas deben tener la misma cantidad de columnas y tipos de datos correspondientes.

Es importante mencionar que estos operadores solo funcionan con consultas que tengan las mismas columnas y tipos de datos correspondientes. Si las consultas difieren en alguna columna o tipo de dato, no se podrá utilizar estos operadores.

También es importante tener en cuenta que UNION, INTERSECT y EXCEPT son operaciones de conjunto, lo que significa que se utilizan para comparar o combinar conjuntos de datos. Los resultados devueltos por estos operadores no necesariamente conservan el orden original de las filas.

## REGLAS DE UTILIZACIÓN

1. Las tablas deben tener la misma cantidad de columnas y tipos de datos correspondientes para poder combinarlas con los operadores UNION, INTERSECT y MINUS.
2. El orden de las columnas debe ser el mismo en ambas tablas cuando se utilizan los operadores UNION, INTERSECT y MINUS.
3. Los operadores UNION y INTERSECT eliminan automáticamente las filas duplicadas en el conjunto de resultados combinado, mientras que el operador MINUS no lo hace.
4. El operador UNION ALL se puede utilizar en lugar de UNION para incluir todas las filas, incluso aquellas que aparecen en ambas tablas.
5. El operador INTERSECT devuelve solo las filas que se encuentran en ambas tablas, por lo que si una fila aparece en una tabla pero no en la otra, esa fila no se incluirá en el conjunto de resultados combinado.
6. El operador MINUS se utiliza para encontrar las filas que se encuentran en una tabla pero no en otra, y solo devuelve las filas de la primera tabla.
7. Las columnas de las dos consultas se relacionan en orden de izq a der
8. Los nombres de las columnas de la primera sentencia SELECT no tienen por qué ser los mismos que los nombres de la segunda.
9. Las SELECT necesitan tener el mismo número de columnas.
10. Los tipos de datos deben coincidir, aunque la longitud no tiene que ser la misma.
