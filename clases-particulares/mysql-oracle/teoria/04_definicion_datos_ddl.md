---
author: @nurialiano
license: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---

# Definición de datos 'DDL'

DDL significa "Data Definition Language" (Lenguaje de Definición de Datos) en SQL. Se utiliza para definir y modificar la estructura de las bases de datos y sus objetos relacionados, como tablas, índices, vistas y restricciones.

## Comandos comunes de DDL

- **CREATE**: se utiliza para crear nuevos objetos en la base de datos, como tablas, vistas, índices, etc.
- **ALTER**: se utiliza para agregar, modificar o eliminar columnas de una tabla existente.
- **DROP**: se utiliza para eliminar objetos de la base de datos, como tablas, vistas, índices, etc.
- **TRUNCATE**: se utiliza para eliminar todos los datos de una tabla sin eliminar la estructura de la tabla en sí.
- **RENAME**: se utiliza para cambiar el nombre de los objetos en la base de datos, como tablas o columnas de tabla.

### ¿Es lo mismo 'modify' que 'alter'?

No. La diferencia principal entre "MODIFY" y "ALTER" es que "MODIFY" se utiliza específicamente para cambiar la definición de una columna en una tabla existente, mientras que "ALTER" se utiliza para modificar la estructura general de los objetos de la base de datos.

#### Ejemplo ALTER

Por ejemplo, si desea cambiar el tipo de datos de una columna existente en una tabla, utilizaría "MODIFY".

~~~sql
ALTER TABLE table_name MODIFY column_name new_data_type;
~~~

#### Ejemplo MODIFY

En cambio, si desea modificar la estructura general de una tabla, como agregar o eliminar columnas, cambiar el nombre de la tabla o modificar una restricción de clave externa, utilizaría "ALTER".

~~~sql
ALTER TABLE table_name ADD column_name data_type;
~~~
