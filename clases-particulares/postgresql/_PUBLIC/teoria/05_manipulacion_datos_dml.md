---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Manipulación de datos 'DML'

DML significa "Data Manipulation Language" (Lenguaje de Manipulación de Datos) en SQL. Se utiliza para manipular los datos dentro de las tablas de una base de datos. Insertar nuevos datos, actualizar registros existentes y eliminar datos de las tablas.

## Comandos comunes de DDL

- **INSERT**: se utiliza para agregar nuevos registros a una tabla.
- **UPDATE**: se utiliza para actualizar registros existentes en una tabla.
- **DELETE**: se utiliza para eliminar registros existentes en una tabla.

>:pencil: **NOTA** También existen otros comandos menos comunes, como SELECT, que si bien técnicamente es una instrucción de DQL (Lenguaje de Consulta de Datos), a menudo se incluye junto con los comandos de DML ya que se utiliza para consultar datos de una tabla.

### Ejemplo INSERT

Por ejemplo, si quieres insertar un nuevo registro.

~~~sql
INSERT INTO nombre_tabla (campo1, campo2, campo3) VALUES (valor1, valor2, valor3);
~~~

### Ejemplo UPDATE

Por ejemplo, si quieres actualizar un campo filtrando por el valor de otro campo.

~~~sql
UPDATE nombre_tabla SET campo2 = valor2 WHERE campo1 = valor1;
~~~

### Ejemplo DELETE

Por ejemplo, si quieres eliminar el registro filtrando por otro campo.

~~~sql
DELETE FROM nombre_tabla WHERE campo1 = valor1;
~~~
