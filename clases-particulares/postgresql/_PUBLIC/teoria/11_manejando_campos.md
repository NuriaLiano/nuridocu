---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Campos

## Añadir

Se refiere a la adición de nuevas columnas a una tabla existente.

~~~sql
ALTER TABLE clientes ADD COLUMN telefono VARCHAR(20);
~~~

## Modificar

Se refiere a la modificación de las propiedades de una columna existente en una tabla.

~~~sql
ALTER TABLE clientes ALTER COLUMN fecha_nacimiento TYPE TIMESTAMP;
~~~

## Eliminar

Se refiere a la adición de nuevas columnas a una tabla existente.

~~~sql
ALTER TABLE usuarios DROP COLUMN telefono;
~~~
