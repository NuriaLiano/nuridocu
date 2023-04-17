---
autor: @nurialiano
licence: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---

# BORRAR

Aunque no es siempre necesario utilizar la palabra clave ALTER antes de DROP, es importante tener en cuenta que, en algunos casos, puede ser necesario para realizar modificaciones en la estructura de la tabla antes de eliminar un objeto.

## BORRAR RESTRICCIONES

### SINTAXIS

~~~sql
ALTER TABLE table_name
DROP CONSTRAINT constraint_name;
~~~

### ASPECTOS A TENER EN CUENTA

Es importante tener en cuenta que las restricciones pueden ser de diferentes tipos, como restricciones de clave primaria, restricciones de clave foránea, restricciones de valores únicos, entre otros. Es necesario identificar primero el tipo de restricción que deseas eliminar para poder utilizar la instrucción SQL correcta.

## BORRAR RELACIONES (FOREIGN KEY)

### SINTAXIS

~~~sql
ALTER TABLE table_name
DROP FOREIGN KEY constraint_name;
~~~

### ASPECTOS A TENER EN CUENTA

Es importante tener en cuenta que al eliminar una relación entre dos tablas, también se pueden eliminar los datos asociados con la relación. Por lo tanto, debes asegurarte de que no se eliminarán datos importantes antes de eliminar la relación. También es posible que debas actualizar las restricciones y relaciones de otras tablas que dependen de la relación que deseas eliminar.

## BORRAR COLUMNAS

### SINTAXIS

~~~sql
ALTER TABLE table_name
DROP COLUMN column_name;
~~~

Si deseas eliminar varias columnas de una tabla, puedes especificar varios nombres de columna separados por comas después de la cláusula "DROP COLUMN".

~~~sql
ALTER TABLE table_name
DROP COLUMN column_name1, column_name2;
~~~

### ASPECTOS A TENER EN CUENTA

Es importante tener en cuenta que si la columna que deseas eliminar contiene datos, todos los datos asociados con la columna también se eliminarán. También debes asegurarte de que la eliminación de la columna no afecte la integridad de los datos en la tabla o cualquier restricción o relación que tenga la tabla. Si la columna que deseas eliminar es una clave foránea, por ejemplo, deberás eliminar cualquier restricción de clave foránea que tenga la tabla antes de eliminar la columna.

## BORRAR TABLAS

La instrucción SQL "DROP TABLE" se utiliza para eliminar una tabla de una base de datos.

### SINTAXIS

~~~sql
DROP TABLE [IF EXISTS] table_name;
~~~

### ASPECTOS A TENER EN CUENTA

- **IF EXISTS**: cláusula opcional que evita que se produzca un error si la tabla no existe en la base de datos. Si se utiliza esta cláusula y la tabla no existe, no se realizará ninguna acción.
- Tener en cuenta si la tabla contiene datos, ya que serán borrados de forma permanente
- Tener en cuenta las relaciones y restricciones con otras tablas. Es probable que primero haya que eliminar las relaciones y luego la tabla que queriamos borrar.

### ELIMINAR TABLAS CON RESTRICCIONES O RELACIONES CON OTRAS TABLAS

1. Identificar todas las restricciones o relaciones.
2. Elimina todas las restricciones y relaciones que tenga la tabla. Esto puede implicar la eliminación de restricciones de clave foránea (FOREIGN KEY), índices (INDEX), desencadenadores (TRIGGER), etc.
3. Utiliza la instrucción "DROP TABLE" para eliminar la tabla.

**Es importante tener cuidado al eliminar tablas que tienen relaciones o restricciones con otras tablas, ya que eliminar una tabla que tiene restricciones o relaciones puede provocar errores en otras partes de la base de datos. Es recomendable realizar una copia de seguridad de la base de datos antes de realizar cualquier acción de eliminación de tablas o datos.**
