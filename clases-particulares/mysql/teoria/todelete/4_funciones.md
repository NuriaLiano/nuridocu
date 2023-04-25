# FUNCIONES

Es un lenguaje de programación utilizado para manejar y manipular bases de datos relacionales. Las funciones SQL son comandos o instrucciones utilizadas para realizar tareas específicas en una base de datos.

Tipos de funciones:

* **Númericas**
* **Aritméticas**
* **Caracteres**
* **Fecha**
* **Conversión fechas**
* **Comparación**
* **Otras**

## NÚMERICAS Y ARITMÉTICAS

* **ABS**: Esta función devuelve el valor absoluto de un número, es decir, su valor sin signo.
* **CEIL**: Esta función devuelve el número entero más pequeño que es mayor o igual a un número dado.
* **FLOOR**: Esta función devuelve el número entero más grande que es menor o igual a un número dado.
* **EXP**: Esta función devuelve el valor de la constante matemática "e" elevado a un número dado.
* **LN**: Esta función devuelve el logaritmo natural (base "e") de un número dado.
* **LOG**: Esta función devuelve el logaritmo de un número dado en una base dada.
* **MOD**: Esta función devuelve el resto de la división de dos números dados.
* **PI**: Esta función devuelve el valor de la constante matemática "pi".
* **POWER**: Esta función devuelve un número elevado a una potencia dada.
* **RAND**: Esta función devuelve un número aleatorio entre 0 y 1.
* **ROUND**: Esta función redondea un número dado a un número entero o decimal determinado.
* **SIGN**: Esta función devuelve el signo de un número dado (1 si es positivo, -1 si es negativo, 0 si es cero).
* **SQRT**: Esta función devuelve la raíz cuadrada de un número dado.
* **TRUNCATE**: Esta función trunca un número dado a un número entero o decimal determinado.

## CARACTERES

* **ASCII**: Esta función devuelve el valor ASCII de un carácter específico.
* **CHAR**: Esta función devuelve el carácter correspondiente a un valor ASCII específico.
* **CONCAT**: Esta función concatena dos o más valores de caracteres en una sola cadena.
* **INSERT**: Esta función inserta una cadena de caracteres en otra cadena en una posición específica.
* **LENGTH**: Esta función devuelve la longitud de una cadena de caracteres.
* **LOCATE**: Esta función devuelve la posición de la primera ocurrencia de una subcadena dentro de una cadena más grande.
* **LOWER**: Esta función convierte una cadena de caracteres en minúsculas.
* **LPAD**: Esta función agrega caracteres a la izquierda de una cadena de caracteres hasta que la cadena tenga una longitud específica.
* **LTRIM**: Esta función elimina los espacios en blanco a la izquierda de una cadena de caracteres.
* **REPLACE**: Esta función reemplaza todas las ocurrencias de una subcadena en una cadena con otra subcadena.
* **RPAD**: Esta función agrega caracteres a la derecha de una cadena de caracteres hasta que la cadena tenga una longitud específica.
* **RTRIM**: Esta función elimina los espacios en blanco a la derecha de una cadena de caracteres.
* **SUBSTR**: Esta función devuelve una subcadena de una cadena más grande.
* **UPPER**: Esta función convierte una cadena de caracteres en mayúsculas.

## FECHA

* **ADDDATE** y **DATE\_ADD**: Estas funciones se utilizan para agregar una cantidad específica de tiempo a una fecha o valor de fecha y hora. La sintaxis de ambas funciones es similar, y permiten especificar la cantidad de tiempo a agregar (en días, horas, minutos, etc.) y el tipo de unidad de tiempo a utilizar.
* **SUBDATE** y **DATE\_SUB**: Estas funciones se utilizan para sustraer una cantidad específica de tiempo de una fecha o valor de fecha y hora. Al igual que ADDDATE y DATE\_ADD, la sintaxis de ambas funciones es similar y permiten especificar la cantidad de tiempo a sustraer y el tipo de unidad de tiempo a utilizar.
* **DATEDIFF**: Esta función se utiliza para calcular la diferencia entre dos valores de fecha o hora. La función devuelve el número de días entre las dos fechas especificadas.
* **DAYNAME**: Esta función se utiliza para devolver el nombre del día de la semana de una fecha específica. Por ejemplo, si se especifica una fecha del lunes, la función devolverá "Monday".
* **DAYOFMONTH**, **DAYOFWEEK** y **DAYOFYEAR**: Estas funciones se utilizan para devolver el día del mes, día de la semana y día del año, respectivamente, de una fecha específica.
* **WEEKOFYEAR**: Esta función se utiliza para devolver el número de semana del año de una fecha específica.
* **MONTH** y **YEAR**: Estas funciones se utilizan para devolver el mes y el año de una fecha específica.
* **HOUR**, **MINUTE** y **SECOND**: Estas funciones se utilizan para devolver la hora, los minutos y los segundos de un valor de fecha y hora específico.
* **CURDATE**, **CURTIME** y **SYSDATE**: Estas funciones se utilizan para devolver la fecha y hora actuales del sistema en diferentes formatos.

## CONVERSIÓN DE FECHA

La función **DATE\_FORMAT** es una función de conversión de fechas en SQL que se utiliza para dar formato a una fecha o valor de tiempo en una cadena de caracteres. Esta función toma dos argumentos: la fecha o el valor de tiempo que se desea formatear y el formato en el que se desea mostrar la fecha. La función DATE\_FORMAT es muy útil cuando se necesita mostrar una fecha o un valor de tiempo en un formato específico, como en informes o exportaciones de datos. El formato es una cadena que especifica cómo se deben mostrar los componentes de la fecha, como el día, el mes y el año. Algunos de los formatos más comunes incluyen:

```
%Y: Año con cuatro dígitos
%y: Año con dos dígitos
%m: Mes con ceros iniciales (01 - 12)
%b: Abreviatura del mes (Jan - Dec)
%M: Nombre completo del mes (January - December)
%d: Día del mes con ceros iniciales (01 - 31)
%e: Día del mes sin ceros iniciales (1 - 31)
%H: Hora en formato de 24 horas (00 - 23)
%h: Hora en formato de 12 horas (01 - 12)
%i: Minutos con ceros iniciales (00 - 59)
%s: Segundos con ceros iniciales (00 - 59)
%p: AM o PM
```

### EJEMPLO

```sql
SELECT DATE_FORMAT(fecha, '%d/%m/%Y') AS fecha_formateada FROM pedidos;
```

Esta consulta seleccionará la columna "fecha" de la tabla "pedidos" y dará formato a la fecha en el formato "día/mes/año". La función "AS" se utiliza para renombrar la columna resultante como "fecha\_formateada".

## COMPARACIÓN

* **GREATEST**: Esta función devuelve el valor más grande de una lista de valores. Por ejemplo: SELECT GREATEST(5, 10, 15) devolverá 15.
* **LEAST**: Esta función devuelve el valor más pequeño de una lista de valores. Por ejemplo: SELECT LEAST(5, 10, 15) devolverá 5.
* **IFNULL**: Esta función devuelve el primer argumento si no es nulo, de lo contrario, devuelve el segundo argumento. Por ejemplo: SELECT IFNULL(nombre, 'Sin nombre') devolverá el nombre si no es nulo, de lo contrario, devolverá 'Sin nombre'.
* **ISNULL**: Esta función devuelve verdadero si el valor especificado es nulo, de lo contrario, devuelve falso. Por ejemplo: SELECT ISNULL(nombre) devolverá verdadero si el valor de la columna "nombre" es nulo.
* **STRCMP**: Esta función compara dos cadenas y devuelve un valor negativo, cero o positivo según si la primera cadena es menor, igual o mayor que la segunda cadena. Por ejemplo: SELECT STRCMP('manzana', 'naranja') devolverá un valor negativo porque 'manzana' es menor que 'naranja'.

## OTRAS

* **DATABASE**: Esta función devuelve el nombre de la base de datos actual. Por ejemplo: SELECT DATABASE() devolverá el nombre de la base de datos actual.
* **USER**: Esta función devuelve el nombre de usuario actual en la base de datos. Por ejemplo: SELECT USER() devolverá el nombre de usuario actual.
* **VERSION**: Esta función devuelve la versión del servidor de la base de datos. Por ejemplo: SELECT VERSION() devolverá la versión del servidor de la base de datos.
