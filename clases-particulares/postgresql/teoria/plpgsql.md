# PL/PGSQL

PL/pgSQL (Procedural Language/PostgreSQL) es un lenguaje de programación procedural que extiende el lenguaje SQL en PostgreSQL. Está diseñado específicamente para escribir funciones y procedimientos almacenados dentro de la base de datos. Aquí tienes una explicación de las características y elementos clave del lenguaje PL/pgSQL:

1. Estructura de bloque: Las funciones PL/pgSQL están compuestas por bloques de código delimitados por las palabras clave "BEGIN" y "END". Pueden contener declaraciones, sentencias SQL y otras construcciones de programación.

un bloque de código se delimita utilizando las palabras clave "BEGIN" y "END", y todas las declaraciones y sentencias se encuentran dentro de este bloque. Aquí tienes un ejemplo para ilustrar esto:

~~~sql
CREATE FUNCTION calcular_promedio(a integer, b integer)
RETURNS integer AS $$
DECLARE
    resultado integer;
BEGIN
    resultado := (a + b) / 2;
    RETURN resultado;
END;
$$ LANGUAGE plpgsql;
~~~

En el ejemplo anterior, se crea una función llamada "calcular_promedio" que acepta dos parámetros enteros y devuelve un entero. El bloque de código se encuentra entre las palabras clave "BEGIN" y "END". Dentro del bloque, se declaran variables y se realiza el cálculo para obtener el promedio de los dos parámetros. Finalmente, se asigna el resultado a la variable "resultado" y se devuelve.
Dentro del bloque, también puedes incluir declaraciones adicionales, como sentencias de control y consultas SQL. Por ejemplo:

~~~sql
CREATE FUNCTION obtener_datos(id integer)
RETURNS table (nombre text, edad integer) AS $$
DECLARE
    registro record;
BEGIN
    FOR registro IN SELECT nombre, edad FROM usuarios WHERE id = id LOOP
        RETURN NEXT registro;
    END LOOP;
    RETURN;
END;
$$ LANGUAGE plpgsql;
~~~

En este ejemplo, la función "obtener_datos" devuelve un conjunto de resultados (tabla) con columnas "nombre" y "edad". Dentro del bloque, se utiliza un bucle FOR para iterar sobre los registros seleccionados de la tabla "usuarios" que coinciden con el parámetro "id". Cada registro se agrega al conjunto de resultados utilizando la sentencia "RETURN NEXT". Al final del bloque, se utiliza "RETURN" sin argumentos para finalizar la función y devolver el conjunto de resultados.

En resumen, la estructura de bloque en PL/pgSQL delimita un bloque de código con las palabras clave "BEGIN" y "END". Dentro de este bloque, puedes incluir declaraciones de variables, sentencias de control, consultas SQL y otras construcciones de programación para implementar la lógica deseada en las funciones PL/pgSQL.

2. Declaraciones de variables: PL/pgSQL permite declarar variables con tipos de datos específicos, como enteros, cadenas, fechas, booleanos, entre otros. Las variables se utilizan para almacenar y manipular valores dentro de la función.

Las variables son objetos utilizados para almacenar y manipular valores en el lenguaje PL/pgSQL. Aquí tienes más detalles y ejemplos sobre las declaraciones de variables:

~~~sql
DECLARE nombre_variable tipo_de_dato;
~~~

Donde "nombre_variable" es el nombre que le asignas a la variable y "tipo_de_dato" es el tipo de dato que puede ser integer, text, boolean, date, entre otros.

Aquí tienes un ejemplo que muestra cómo declarar y utilizar variables en una función PL/pgSQL:

~~~sql
CREATE FUNCTION calcular_promedio(a integer, b integer)
RETURNS integer AS $$
DECLARE
    resultado integer;
BEGIN
    resultado := (a + b) / 2;
    RETURN resultado;
END;
$$ LANGUAGE plpgsql;
~~~

En este ejemplo, se declara una variable llamada "resultado" de tipo integer. Luego, se asigna el resultado del cálculo (la suma de "a" y "b" dividida por 2) a la variable "resultado". Finalmente, se utiliza la sentencia "RETURN" para devolver el valor almacenado en la variable.

Además de las variables simples, PL/pgSQL también admite variables de tipo registro que pueden contener múltiples campos. Aquí tienes un ejemplo:

~~~sql
CREATE FUNCTION obtener_datos(id integer)
RETURNS table (nombre text, edad integer) AS $$
DECLARE
    registro record;
BEGIN
    SELECT nombre, edad INTO registro FROM usuarios WHERE id = id;
    RETURN NEXT registro;
    RETURN;
END;
$$ LANGUAGE plpgsql;
~~~

En este ejemplo, se declara una variable de tipo registro llamada "registro". Luego, se utiliza la sentencia "SELECT INTO" para asignar los valores de las columnas "nombre" y "edad" de la tabla "usuarios" a los campos correspondientes del registro. Posteriormente, el registro se agrega al conjunto de resultados utilizando la sentencia "RETURN NEXT".

En resumen, las declaraciones de variables en PL/pgSQL permiten almacenar y manipular valores en funciones y procedimientos. Las variables se declaran utilizando la sintaxis "DECLARE nombre_variable tipo_de_dato;" y se pueden utilizar para almacenar valores simples o conjuntos de campos en registros.

3. Estructuras de control: El lenguaje PL/pgSQL incluye estructuras de control, como condicionales (IF-THEN-ELSE), bucles (FOR, WHILE), bucles de cursor y bloques de manejo de excepciones. Estas estructuras permiten controlar el flujo de ejecución en función de condiciones específicas.

El punto tres se refiere a las estructuras de control en PL/pgSQL, que permiten controlar el flujo de ejecución de un programa en función de condiciones específicas. Aquí tienes más detalles y ejemplos sobre las estructuras de control en PL/pgSQL:

- Condicional IF-THEN-ELSE:
  La estructura IF-THEN-ELSE se utiliza para ejecutar un bloque de código si se cumple una condición y otro bloque de código si no se cumple. Aquí tienes un ejemplo:

~~~sql
CREATE FUNCTION evaluar_edad(edad integer)
RETURNS text AS $$
BEGIN
    IF edad >= 18 THEN
        RETURN 'Eres mayor de edad.';
    ELSE
        RETURN 'Eres menor de edad.';
    END IF;
END;
$$ LANGUAGE plpgsql;
~~~

En este ejemplo, la función "evaluar_edad" toma como argumento la edad y devuelve un texto que indica si es mayor de edad o menor de edad.

- Bucles:
  Los bucles permiten repetir un bloque de código hasta que se cumpla una condición determinada. En PL/pgSQL, se pueden usar bucles WHILE y FOR. Aquí tienes un ejemplo con un bucle FOR:

~~~sql

CREATE FUNCTION imprimir_numeros_hasta(n integer)
RETURNS void AS $$
DECLARE
    i integer;
BEGIN
    FOR i IN 1..n LOOP
        RAISE NOTICE 'Número: %', i;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
~~~

En este ejemplo, la función "imprimir_numeros_hasta" toma como argumento "n" y utiliza un bucle FOR para imprimir los números desde 1 hasta "n" utilizando la sentencia RAISE NOTICE.

- Manejo de excepciones:
  PL/pgSQL permite capturar y manejar excepciones que pueden ocurrir durante la ejecución de un bloque de código. Aquí tienes un ejemplo:

~~~sql

CREATE FUNCTION dividir_numeros(a integer, b integer)
RETURNS integer AS $$
DECLARE
    resultado integer;
BEGIN
    BEGIN
        resultado := a / b;
        EXCEPTION WHEN division_by_zero THEN
            resultado := 0;
    END;
    RETURN resultado;
END;
$$ LANGUAGE plpgsql;
~~~

En este ejemplo, la función "dividir_numeros" intenta dividir los números "a" y "b", pero si se produce una excepción de división por cero, captura la excepción y asigna un valor de 0 al resultado.

Estos son solo algunos ejemplos de las estructuras de control en PL/pgSQL. El lenguaje también ofrece otras construcciones, como CASE, LOOP, GOTO, entre otros, que permiten controlar el flujo de ejecución de manera más compleja y flexible.

4. Sentencias SQL: PL/pgSQL permite ejecutar sentencias SQL dentro de las funciones. Esto incluye consultas SELECT, INSERT, UPDATE, DELETE, entre otras. Las variables se pueden utilizar en las sentencias SQL para realizar operaciones basadas en los valores almacenados.

El punto cuatro se refiere a las funciones de ventana (window functions) en PL/pgSQL. Las funciones de ventana son una característica poderosa de PL/pgSQL que permiten realizar cálculos y operaciones en particiones de datos, es decir, en subconjuntos específicos de filas ordenadas. Aquí tienes más detalles y ejemplos sobre las funciones de ventana en PL/pgSQL:

Las funciones de ventana se utilizan en consultas SELECT para realizar cálculos y resúmenes en grupos de filas. Estas funciones se aplican a una ventana de filas definida por una cláusula OVER, que especifica la partición de filas y el orden en el que se deben realizar los cálculos.

Aquí tienes un ejemplo que muestra cómo utilizar una función de ventana para calcular un promedio móvil (rolling average) en una tabla de datos:

~~~sql
CREATE FUNCTION calcular_promedio_movil() RETURNS TABLE (fecha date, valor integer, promedio_movil numeric) AS $$
BEGIN
    RETURN QUERY
    SELECT fecha, valor, AVG(valor) OVER (ORDER BY fecha ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS promedio_movil
    FROM datos;
END;
$$ LANGUAGE plpgsql;
~~~

En este ejemplo, la función "calcular_promedio_movil" devuelve una tabla con las columnas "fecha", "valor" y "promedio_movil". La función de ventana AVG(valor) calcula el promedio de la columna "valor" en una ventana de tres filas que incluye la fila actual y las dos filas anteriores, ordenadas por la columna "fecha".

Al ejecutar esta función, obtendrás una tabla que muestra la fecha, el valor original y el promedio móvil correspondiente.

Las funciones de ventana en PL/pgSQL ofrecen una amplia variedad de operaciones y cálculos, como SUM, COUNT, MIN, MAX, RANK, DENSE_RANK, entre otros. Puedes utilizar cláusulas como PARTITION BY para dividir los datos en grupos más pequeños y ORDER BY para especificar el orden de los cálculos.

En resumen, las funciones de ventana en PL/pgSQL permiten realizar cálculos y operaciones en particiones de datos específicas en consultas SELECT. Estas funciones ofrecen flexibilidad y potencia para realizar análisis avanzados y resúmenes de datos en conjuntos de filas ordenadas.

5. Manipulación de registros: PL/pgSQL permite trabajar con registros (también conocidos como tuplas) que representan filas de tablas. Es posible asignar valores a variables de registro, acceder a los campos del registro y realizar operaciones de manipulación de registros, como inserción, actualización y eliminación.

El punto cinco se refiere a la manipulación de registros (también conocidos como tuplas) en PL/pgSQL. Los registros son estructuras de datos que representan filas de tablas en PostgreSQL. En PL/pgSQL, puedes trabajar con registros para acceder a los campos de una fila, asignar valores a variables de registro y realizar operaciones de manipulación de registros. Aquí tienes más detalles y ejemplos sobre la manipulación de registros en PL/pgSQL:

- Declaración y asignación de registros:

Puedes declarar una variable de tipo registro y asignar valores a los campos del registro utilizando la sintaxis:

~~~sql
DECLARE
    nombre_variable nombre_tabla%ROWTYPE;
~~~

Donde "nombre_variable" es el nombre que le asignas a la variable y "nombre_tabla" es el nombre de la tabla de la cual quieres obtener la estructura.

Aquí tienes un ejemplo:

~~~sql
DECLARE
    empleado registro_empleados%ROWTYPE;
BEGIN
    SELECT * INTO empleado FROM empleados WHERE id = 1;
    -- Acceder a los campos del registro
    RAISE NOTICE 'Nombre: %', empleado.nombre;
    RAISE NOTICE 'Edad: %', empleado.edad;
END;
~~~

En este ejemplo, se declara una variable de registro llamada "empleado" utilizando la estructura de la tabla "registro_empleados". Luego, se utiliza la sentencia SELECT INTO para asignar los valores de la fila con "id" igual a 1 de la tabla "empleados" al registro "empleado". Posteriormente, se accede a los campos del registro para imprimirlos utilizando la sentencia RAISE NOTICE.

- Manipulación de registros:
  
  PL/pgSQL permite realizar operaciones de manipulación de registros, como inserción, actualización y eliminación de filas. Aquí tienes un ejemplo:

~~~sql
DECLARE
    nuevo_empleado registro_empleados%ROWTYPE;
BEGIN
    -- Inserción de una nueva fila
    nuevo_empleado.nombre := 'John Doe';
    nuevo_empleado.edad := 30;
    INSERT INTO empleados VALUES nuevo_empleado;

    -- Actualización de una fila existente
    nuevo_empleado.edad := 31;
    UPDATE empleados SET nombre = nuevo_empleado.nombre, edad = nuevo_empleado.edad WHERE id = 1;

    -- Eliminación de una fila
    DELETE FROM empleados WHERE id = 1;
END;
~~~

En este ejemplo, se declara una variable de registro llamada "nuevo_empleado" y se asignan valores a sus campos. Luego, se utiliza la sentencia INSERT para insertar una nueva fila en la tabla "empleados" con los valores del registro. A continuación, se utiliza la sentencia UPDATE para actualizar una fila existente en la tabla, y la sentencia DELETE para eliminar una fila.

En resumen, la manipulación de registros en PL/pgSQL permite trabajar con filas de tablas utilizando variables de registro y realizar operaciones de inserción, actualización y eliminación. Esto brinda flexibilidad para manipular los datos almacenados en las tablas y realizar cambios en ellos dentro de las funciones y procedimientos PL/pgSQL.

6. Funciones de retorno: Las funciones PL/pgSQL pueden tener un valor de retorno definido. Pueden devolver un solo valor o conjuntos de resultados.

El punto seis se refiere a las transacciones en PL/pgSQL. Una transacción es una secuencia de operaciones que se ejecutan como una unidad lógica e indivisible. PL/pgSQL proporciona funcionalidades para controlar y manejar transacciones en el lenguaje de programación. Aquí tienes más detalles y ejemplos sobre las transacciones en PL/pgSQL:

    Inicio de una transacción:
    Puedes iniciar una transacción utilizando la sentencia BEGIN o BEGIN TRANSACTION. Esto marca el inicio de la secuencia de operaciones que formarán parte de la transacción. Aquí tienes un ejemplo:

plpgsql

BEGIN;
-- Secuencia de operaciones
...
COMMIT; -- o ROLLBACK;

En el ejemplo anterior, BEGIN inicia la transacción, seguida de una secuencia de operaciones que formarán parte de la transacción. Luego, se utiliza COMMIT para confirmar y guardar los cambios realizados en la transacción, o ROLLBACK para deshacer todos los cambios y cancelar la transacción.

    Control de transacciones:
    PL/pgSQL ofrece sentencias para controlar el comportamiento de las transacciones. Puedes utilizar SAVEPOINT para crear un punto de guardado dentro de una transacción y luego utilizar ROLLBACK TO SAVEPOINT para revertir los cambios realizados hasta ese punto específico. Aquí tienes un ejemplo:

plpgsql

BEGIN;
-- Secuencia de operaciones
SAVEPOINT punto_guardado;
-- Más operaciones
IF condicion THEN
    ROLLBACK TO SAVEPOINT punto_guardado;
ELSE
    -- Operaciones adicionales
END IF;
COMMIT;

En este ejemplo, se utiliza SAVEPOINT para crear un punto de guardado llamado "punto_guardado" dentro de la transacción. Luego, se ejecutan más operaciones y se evalúa una condición. Si la condición no se cumple, se continúa con las operaciones adicionales. Sin embargo, si la condición se cumple, se utiliza ROLLBACK TO SAVEPOINT para revertir los cambios hasta el punto de guardado, deshaciendo las operaciones realizadas después del SAVEPOINT.

    Manejo de errores y excepciones:
    Cuando se produce un error o excepción dentro de una transacción, PL/pgSQL permite capturar y manejar la excepción utilizando bloques de manejo de excepciones. Puedes utilizar los bloques EXCEPTION y EXIT para controlar el flujo de ejecución en caso de errores. Aquí tienes un ejemplo:

plpgsql

BEGIN;
-- Secuencia de operaciones
BEGIN
    -- Alguna operación que puede generar una excepción
    ...
EXCEPTION
    WHEN exception_type THEN
        -- Manejo de la excepción
        ...
    WHEN OTHERS THEN
        -- Manejo de otras excepciones
        ...
END;
COMMIT; -- o ROLLBACK;

En este ejemplo, se utiliza un bloque EXCEPTION para capturar excepciones específicas (definidas por "exception_type") y realizar el manejo correspondiente. También se utiliza un bloque WHEN OTHERS para capturar cualquier otra excepción no especificada previamente. Puedes utilizar comandos como RAISE para generar nuevas excepciones dentro del bloque de manejo.

En resumen, las transacciones en PL/pgSQL permiten agrupar operaciones en una unidad lógica e indivisible. Puedes controlar el inicio y finalización de las transacciones utilizando BEGIN, COMMIT y ROLLBACK. Además, PL/pgSQL ofrece funcionalidades para crear puntos de guardado con SAVE

En este ejemplo, se utiliza SAVEPOINT para crear un punto de guardado llamado "punto_guardado" dentro de la transacción. Luego, se ejecutan más operaciones y se evalúa una condición. Si la condición no se cumple, se continúa con las operaciones adicionales. Sin embargo, si la condición se cumple, se utiliza ROLLBACK TO SAVEPOINT para revertir los cambios hasta el punto de guardado, deshaciendo las operaciones realizadas después del SAVEPOINT.

1. Manejo de excepciones: El lenguaje PL/pgSQL proporciona mecanismos para manejar errores y excepciones que puedan ocurrir durante la ejecución de la función. Esto incluye capturar y procesar errores específicos y tomar acciones adecuadas.

El punto siete se refiere a los cursores en PL/pgSQL. Un cursor es una estructura que permite recorrer y manipular conjuntos de resultados obtenidos a partir de una consulta. PL/pgSQL proporciona funcionalidades para declarar, abrir, recorrer y cerrar cursores dentro de las funciones y procedimientos. Aquí tienes más detalles y ejemplos sobre el uso de cursores en PL/pgSQL:

    Declaración de cursores:
    Puedes declarar un cursor utilizando la sintaxis:

plpgsql

DECLARE nombre_cursor CURSOR FOR consulta;

Donde "nombre_cursor" es el nombre que le asignas al cursor y "consulta" es la consulta SQL que define el conjunto de resultados. Aquí tienes un ejemplo:

plpgsql

DECLARE empleado_cursor CURSOR FOR SELECT * FROM empleados;

En este ejemplo, se declara un cursor llamado "empleado_cursor" que recorrerá el conjunto de resultados de la consulta SELECT * FROM empleados.

    Apertura y recorrido del cursor:
    Para abrir un cursor y comenzar a recorrer los resultados, se utiliza la sentencia OPEN. Luego, puedes utilizar la sentencia FETCH para obtener los valores de las filas del cursor. Aquí tienes un ejemplo:

plpgsql

DECLARE
    empleado_cursor CURSOR FOR SELECT * FROM empleados;
    empleado registro_empleados%ROWTYPE;
BEGIN
    OPEN empleado_cursor;
    LOOP
        FETCH empleado_cursor INTO empleado;
        EXIT WHEN NOT FOUND; -- Salir del bucle cuando no hay más filas
        -- Operaciones con los valores del registro
        RAISE NOTICE 'Nombre: %', empleado.nombre;
        RAISE NOTICE 'Edad: %', empleado.edad;
    END LOOP;
    CLOSE empleado_cursor;
END;

En este ejemplo, se declara el cursor "empleado_cursor" y se abre con la sentencia OPEN. Luego, se utiliza un bucle LOOP para recorrer cada fila del cursor utilizando FETCH, que asigna los valores de la fila al registro "empleado". Dentro del bucle, puedes realizar operaciones con los valores del registro.

    Cierre del cursor:
    Después de recorrer los resultados y realizar las operaciones necesarias, es importante cerrar el cursor utilizando la sentencia CLOSE para liberar los recursos asociados. Aquí tienes un ejemplo:

plpgsql

DECLARE empleado_cursor CURSOR FOR SELECT * FROM empleados;
...
CLOSE empleado_cursor;

En este ejemplo, se cierra el cursor "empleado_cursor" utilizando la sentencia CLOSE.

Además de la apertura, recorrido y cierre básicos de cursores, PL/pgSQL también ofrece funcionalidades avanzadas para controlar el comportamiento de los cursores, como definir la posición inicial del cursor, desplazarse hacia adelante o hacia atrás en los resultados, filtrar filas y más.

En resumen, los cursores en PL/pgSQL permiten recorrer y manipular conjuntos de resultados obtenidos a partir de consultas. Puedes declarar, abrir, recorrer y cerrar cursores para acceder a los datos de manera más controlada y realizar operaciones específicas en cada fila del conjunto de resultados.

---

En resumen, PL/pgSQL es un lenguaje procedural que amplía el lenguaje SQL en PostgreSQL. Permite escribir funciones y procedimientos almacenados dentro de la base de datos, lo que proporciona flexibilidad y potencia para implementar lógica de programación compleja directamente en el motor de la base de datos.
