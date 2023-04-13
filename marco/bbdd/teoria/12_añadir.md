---
autor: @nurialiano
licence: [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode)
---

# AÑADIR

Aunque no es siempre necesario utilizar la palabra clave ALTER antes de ADD, es importante tener en cuenta que, en algunos casos, puede ser necesario para realizar modificaciones en la estructura de la tabla antes de añadir un objeto.

## AÑADIR RESTRICCIONES

### SINTAXIS

~~~sql
ALTER TABLE table_name
ADD CONSTRAINT constraint_name PRIMARY KEY (column_name);
~~~

## AÑADIR RESTRICCIONES (FOREING KEY)

### SINTAXIS

~~~sql
ALTER TABLE table_name
ADD CONSTRAINT constraint_name FOREIGN KEY (column_name) REFERENCES other_table_name(other_column_name);
~~~

- table_name es el nombre de la tabla a la que deseas añadir la restricción.
- constraint_name es el nombre que deseas asignar a la restricción.
- column_name es el nombre de la columna que deseas utilizar como clave foránea en la tabla actual.
- other_table_name es el nombre de la tabla que contiene la columna a la que la clave foránea hace referencia.
- other_column_name es el nombre de la columna a la que la clave foránea hace referencia en la tabla especificada.

### ASPECTOS A TENER EN CUENTA

Es importante tener en cuenta que para añadir una restricción de clave foránea, la columna a la que hace referencia la clave foránea debe existir en la tabla especificada. Además, la tabla a la que se hace referencia debe tener una clave primaria o una clave única definida en la columna referenciada.

## AÑADIR RELACIONES

En la tabla que actúa como tabla secundaria (la que tiene la clave foránea), se debe crear una columna que haga referencia a la clave primaria de la tabla principal. Esta columna debe tener el mismo tipo de datos que la clave primaria de la tabla principal.

### SINTAXIS

~~~sql
ALTER TABLE nombre_tabla_secundaria
ADD FOREIGN KEY (nombre_columna_foranea) REFERENCES nombre_tabla_principal(nombre_columna_primaria);
~~~

### ASPECTOS A TENER EN CUENTA

Es importante asegurarse de que los nombres de las tablas y columnas sean escritos correctamente y coincidan con los nombres reales de la base de datos.

## AÑADIR COLUMNAS

### SINTAXIS

~~~sql
ALTER TABLE table_name
ADD COLUMN nombre_columna tipo_de_datos
~~~

- (OPCIONAL) Especificar la posición de la columna

~~~sql
ALTER TABLE table_name
ADD COLUMN nombre_columna tipo_de_datos
AFTER nombre_columna_anterior
~~~

- Especificar restricciones

~~~sql
ALTER TABLE nombre_tabla 
ADD COLUMN nombre_columna tipo_de_datos 
CONSTRAINT nombre_restriccion restriccion;
~~~

- Especificar relaciones

~~~sql
-- Añadir la columna a la tabla existente
ALTER TABLE orders
ADD COLUMN customer_id INT;

-- Crear la relación entre las dos tablas
ALTER TABLE orders
ADD CONSTRAINT fk_customer
FOREIGN KEY (customer_id) REFERENCES customers(id);
~~~

### ASPECTOS A TENER EN CUENTA

En algunos sistemas de gestión de bases de datos (como MySQL o PostgreSQL) se permite omitir la palabra clave ADD en la cláusula ADD CONSTRAINT. Sin embargo, es importante tener en cuenta que esto no es estándar de SQL y que otros sistemas de gestión de bases de datos podrían requerir que se utilice la palabra clave ADD en la cláusula ADD CONSTRAINT.

~~~sql
ALTER TABLE orders
ADD COLUMN customer_id INT CONSTRAINT fk_customer
FOREIGN KEY (customer_id) REFERENCES customers(id);
~~~

## AÑADIR TABLAS (con restricciones)

La instrucción SQL "DROP TABLE" se utiliza para eliminar una tabla de una base de datos.

### SINTAXIS

~~~sql
CREATE TABLE nombre_tabla (
  columna1 tipo_de_datos1 CONSTRAINT nombre_restriccion1 restriccion1,
  columna2 tipo_de_datos2 CONSTRAINT nombre_restriccion2 restriccion2,
  columna3 tipo_de_datos3 CONSTRAINT nombre_restriccion3 restriccion3,
  ...
  PRIMARY KEY (columna1, columna2),
  FOREIGN KEY (columna3) REFERENCES otra_tabla (columna_referencia)
);
~~~
