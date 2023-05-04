---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Restricciones

## Crear

~~~sql
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    precio NUMERIC(10,2),
    descripcion TEXT,
    CONSTRAINT uk_nombre UNIQUE (nombre)
);
~~~

## Añadir

~~~sql
ALTER TABLE productos
ADD CONSTRAINT no_nulo_nombre
CHECK (nombre IS NOT NULL);
~~~

>:pencil: **NOTA** a diferencia de MySQL, en PostgreSQL se utiliza la cláusula "CHECK" en lugar de "NOT NULL" para definir restricciones de no nulidad.

## Modificar

~~~sql
ALTER TABLE clientes ALTER COLUMN email TYPE VARCHAR(255), 
ALTER COLUMN email SET NOT NULL;
~~~

## Eliminar

~~~sql
DROP INDEX clientes_email_idx;
~~~
