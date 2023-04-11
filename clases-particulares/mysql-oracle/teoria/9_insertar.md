# INSERTAR VALORES

Para insertar valores en una tabla de SQL se utiliza la sentencia INSERT INTO seguida del nombre de la tabla y los valores a insertar. La sintaxis básica es la siguiente

~~~sql
INSERT INTO nombre_de_tabla (columna1, columna2, columna3, ...) 
VALUES (valor1, valor2, valor3, ...)
~~~

## EJEMPLO

Por ejemplo, si tenemos una tabla llamada usuarios con las columnas id, nombre y email, para insertar un nuevo registro con id=1, nombre="Juan" y email="juan@example.com", la sentencia sería la siguiente

~~~sql
INSERT INTO usuarios (id, nombre, email) 
VALUES (1, 'Juan', 'juan@example.com')
~~~

También es posible insertar varios registros en una sola sentencia, especificando múltiples conjuntos de valores separados por comas.

~~~sql
INSERT INTO usuarios (id, nombre, email) 
VALUES (1, 'Juan', 'juan@example.com'), 
       (2, 'María', 'maria@example.com'), 
       (3, 'Pedro', 'pedro@example.com')
~~~