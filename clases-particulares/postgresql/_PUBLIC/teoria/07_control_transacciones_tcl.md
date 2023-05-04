---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Definición de datos 'TCL'

TCL significa "Transaction Control Language" (Lenguaje de Control de Datos ) en SQL. Se utiliza para controlar las transacciones en una base de datos.

>:pencil: **NOTA** una transacción es una serie de operaciones que se realizan en una base de datos y que deben ser realizadas de manera atómica, es decir, que se deben completar todas o ninguna de ellas. La TCL se utiliza para asegurarse de que las transacciones se completen correctamente, y para deshacer las transacciones en caso de un error.

## Comandos comunes de TCL

- **COMMIT**: se utiliza para confirmar los cambios en una transacción y hacerlos permanentes en la base de datos
- **ROLLBACK**: se utiliza para deshacer los cambios realizados en una transacción y volver al estado anterior a la transacción.
- **SAVEPOINT**: se utiliza para establecer un punto de control dentro de una transacción, de modo que se pueda volver a ese punto si se produce un error.
- **RELEASE**: se utiliza para eliminar un punto de control establecido con SAVEPOINT.
- **ROLLBACK TO**: se utiliza para deshacer las operaciones realizadas desde un punto de control establecido con SAVEPOINT.

### Ejemplo COMMIT

Supongamos que queremos insertar un registro en la tabla clientes y confirmar la transacción. Primero, iniciamos la transacción con el comando BEGIN, luego insertamos el registro y finalmente confirmamos la transacción con COMMIT

~~~sql
BEGIN;
INSERT INTO clientes (nombre, apellido, edad) VALUES ('Juan', 'Pérez', 30);
COMMIT
~~~

### Ejemplo ROLLBACK

Supongamos que queremos actualizar un registro en la tabla clientes pero nos equivocamos en la cláusula WHERE y actualizamos todos los registros de la tabla.

~~~sql
BEGIN;
UPDATE clientes SET edad = 40 WHERE id = 1; -- ERROR en la cláusula WHERE
ROLLBACK;
~~~

### Ejemplo SAVEPOINT y ROLLBACK TO

Supongamos que queremos insertar varios registros en la tabla clientes, pero queremos tener la posibilidad de deshacer los cambios después del segundo registro.

~~~sql
BEGIN;
INSERT INTO clientes (nombre, apellido, edad) VALUES ('Juan', 'Pérez', 30);
SAVEPOINT segundo_registro;
INSERT INTO clientes (nombre, apellido, edad) VALUES ('María', 'González', 25);
INSERT INTO clientes (nombre, apellido, edad) VALUES ('Pedro', 'Rodríguez', 35);
ROLLBACK TO SAVEPOINT segundo_registro;
COMMIT;
~~~

En este ejemplo, creamos un punto de guardado después del primer registro con el comando SAVEPOINT segundo_registro. Luego insertamos dos registros más y finalmente, decidimos deshacer los cambios a partir del segundo registro con el comando ROLLBACK TO SAVEPOINT segundo_registro. Al final, confirmamos la transacción con COMMIT.

### Ejemplo RELEASE

Supongamos que hemos creado un punto de guardado (SAVEPOINT) llamado "sp1" y hemos realizado algunas operaciones de inserción y eliminación en la tabla. Si queremos hacer permanentes los cambios que hemos realizado desde el punto de guardado "sp1" y liberar el punto de guardado, podemos usar el comando RELEASE

~~~sql
SAVEPOINT sp1;
INSERT INTO tabla (columna1, columna2, columna3) VALUES (valor1, valor2, valor3);
DELETE FROM tabla WHERE columna1 = valor4;
RELEASE sp1;
~~~

Tambien podemos liberar el punto de guardado 'sp1' utilizando el commando commit. Después de ejecutar el comando COMMIT, los cambios se hacen permanentes y se libera automáticamente el punto de guardado "sp1".

~~~sql
SAVEPOINT sp1;
INSERT INTO tabla (columna1, columna2, columna3) VALUES (valor1, valor2, valor3);
DELETE FROM tabla WHERE columna1 = valor4;
COMMIT;
~~~

**¿Cuál de las dos formas es más correcta?**

Ambas formas son válidas y hacen prácticamente lo mismo. La diferencia principal es que **RELEASE** se utiliza para liberar un punto de guardado y continuar la transacción, mientras que **COMMIT** finaliza la transacción y hace que los cambios sean permanentes.
En general, se recomienda utilizar COMMIT al final de una transacción para hacer que los cambios sean permanentes. El uso de SAVEPOINT y ROLLBACK es útil cuando se quiere deshacer una parte de la transacción sin deshacer todo lo que se ha hecho hasta el momento.
