---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Primeros pasos con PHP

## Ejecutar PHP

## Sintaxis

Los script de PHP comienzan siempre con `<?php` y terminan con `?>`. Estos caracteres marcan que el código que se encuentre dentro de ellos será ejcutado como código PHP independientemente de si se encuentra en un fichero con otro tipo de código.

~~~php
<?php
    //código que queremos ejecutar
?>
~~~

Siempre que un fichero contenga código PHP deberá llevar la extensión de fichero `.php`. Por ejemplo, si tenemos un fichero `mipagina.html` que contiene código HTML y código PHP, ese fichero deberá llevar la extensión `.php` y no `.html`, quedaría como `mipagina.php`

Todas las intrucciones que acabemos en PHP tienen que estar cerradas con `;` si no el programa fallará por que no encontrará donde termina una intrucción

### Case sensitive

En PHP podemos escribir las palabras reservadas (if, switch, echo, etc) con mayúsculas, minúsculas o alternando, ya que reconoce que es una palabra reservada independientemente de como esté escrito.

Aunque no influya en el funcionamiento del programa es recomendable, siguiendo las buenas prácticas, escribir las palabras reservadas en minúsculas

> :woman_teacher: **EXPLICACIÓN** case sensitive 

~~~php
<?php
    echo "Hola Mundo"; //lo recomendado
    ECHO "Hola Mundo"; //es mejor que no lo hagas así ...
    EcHo "Hola Mundo"; //horrible!!
?>
~~~

## Comentarios

Los comentarios son líneas que no se ejecutan como parte del programa. Son un punto muy importante en todos los lenguajes de programación ya que nos ayuda a dejar notas sobre el funcionamiento de nuestro código y que, en el futuro, tanto nosotros como otros programadores entiendan más fácilmente que hace el código.

PHP permite establecer comentarios de línea y comentarios de bloque:

### Comentarios de línea

Estos comentarios solo se aplican a la línea en la que están declarados los caracteres `//` o `#`

~~~php
<?php
    // esto es un comentario de línea
    # otra forma de establecer comentarios de línea
?>
~~~

### Comentarios de bloque

Estos comentarios se aplican a todo lo que esté dentro del caracter de apertura `/*` y el caracter de cierre `*/`

También son útiles para comentar troxos de código dentro de una instrucción

~~~php
<?php
    /*
    todo este
    texto 
    va a ser 
    ignorado
    */

    echo (1 /*+ 2*/ + 3);
?>
~~~

## Imprimir

En todos los lenguajes de programación, en algún momento, necesitamos imprimir texto, variables, funciones, etc. PHP no iba a ser menos y, además, tenemos dos formas de imprimir.

`echo` y `print` son palabras que se usan para imprimir. Son casi lo mismo y podemos utilizar la que más nos guste pero hay que aclarar la única diferencia que tienen: `echo` no devuelve ningún valor pero `print` devuelve 1 por lo que se puede utilizar en expresiones.

Ambas pueden utilizarse con `()` al final para añadir parámetros o sin paréntesis. `echo` o `echo()` y `print` o `print()`

~~~php
<?php
    //ejemplos de echo y print

    echo "Imprimo con echo"
    echo ("Imprimo con echo")

    print "Imprimo con print"
    print ("Imprimo con print")

?>
~~~

## Primer programa con PHP

Una vez que conocemos lo básico sobre PHP ya estamos preparados para hacer nuestro primer programa 'Hola Mundo'.

Lo primero que vamos a hacer es crear un fichero `hola.php` y vamos a imprimir el mensaje `Hola Mundo` típico.

~~~php
<?php 
    //primer programa para aprender a imprimir texto
    echo "Hola Mundo"
?>
~~~

Ahora simplemente vamos a comprobar el resultado en el navegador

<div align="center">
  <img src="../" alt="imagen de la ejecucion hola mundo de php">
</div>

> :back: **PARA ENTRAR EN CONTEXTO** si no sabes como ejecutar PHP puedes echar un vistazo a la sección anterior donde vemos como configurar nuestro editor de código y navegador. [Instalación, configuración y ejecución de PHP](./03_tutorial_instalacion.md)

## Variables y constantes

EL uso de variables y constantes es una parte fundamental de los lenguajes de programación, nos permiten almacenar datos y utilizarlos en el código y también variar su valor en base a la ejecución.

PHP es un lenguaje de tipado débil por lo que no es necesario definir que tipo de dato establecemos en las variables

> :white_check_mark: **RECOMENDADO** echa un vistazo a la sección de [Lenguajes de programación: Tipados]()
> :white_check_mark: **RECOMENDADO** echa un vistazo a la sección de [Scope de las variables]()

### Variables

Las variables son contenedores de valores que pueden cambiar su valor según definamos en la ejecución del código. En PHP se declaran utilizando el caracter `$` y seguido el nombre de la variable: `$variable`

> :white_check_mark: **RECOMENDADO** echa un vistazo a la sección de [Buenas prácticas de programación: variables y constantes]()

~~~php
<?php

    $variable1 = "Hola mundo";
    $var2 = 6;
    $v3 = "probando variables";
?>
~~~

### Constantes

Las contantes también son contenedores de valores pero, a diferencia de las variables, no cambian su valor durante la ejecución si no que se establece un valor y será el mismo durante todo el programa.

Se declaran utilizando `define()` y tenemos que indicar un nombre de constante, el valor y si queremos que sea 'case-insensitive' que por defecto es 'false'

Sintaxis: `define (nombre_constante, valor, case-insensitive)`

~~~php
// no es necesario establecer 'false' por que está establecido por defecto
define (primeraconstante, 'he desactivado case-insensitive') 
define (primeraconstante, 'he activado case-insensitive', true)
~~~

### Imprimir variables y constantes

~~~php
<?php
    echo $variable1 //resultado: Hola Mundo
    echo $var2 //resultado: 6
    echo $v3 //resultado: probando variables

    echo primeraconstante //case-insensitive deshabilitado  //resultado: he desactivado case-insensitive
    echo PRIMERACONSTANTE //case-insensitive habilitado     //resultado: he habilitado case-insensitive
?>
~~~

## Tipos de datos

Entender los tipos de datos en PHP es fundamental para declarar variables, asignarles valores y utilizarlos correctamente en nuestras aplicaciones. Si bien ya hemos aprendido cómo declarar variables, asignarles valores e imprimirlos, es crucial comprender qué tipo de dato estamos estableciendo en cada variable y cuándo debemos utilizar cada uno de ellos.

PHP proporciona una amplia gama de tipos de datos, pero en esta sección nos centraremos principalmente en los tipos de datos simples, destacados en color, dejando los tipos más complejos para futuras secciones.

| Tipo de dato  | Descripción                                 | Ejemplo                         |
| ------------- | ------------------------------------------- | ------------------------------- |
| boolean       | Representa un valor verdadero o falso.       | $activo = true;                 |
| integer       | Representa un número entero.                 | $edad = 25;                     |
| float         | Representa un número de punto flotante.      | $precio = 19.99;                |
| string        | Representa una cadena de caracteres.         | $nombre = "Nuria";              |
| array         | Representa una colección de elementos.       | $numeros = [1, 2, 3, 4, 5];     |
| object        | Representa una instancia de una clase.       | $usuario = new Usuario();       |
| null          | Representa un valor nulo.                    | $dato = null;                   |
| resource      | Representa un recurso externo.               | $archivo = fopen("archivo.txt"); |
| callable      | Representa un tipo de dato invocable.        | $funcion = function() {};       |
| iterable      | Representa una estructura iterativa.         | $lista = new ArrayIterator();   |

- **boolean**: Representa un valor verdadero o falso. Por ejemplo, podemos usarlo para indicar si un usuario ha iniciado sesión ($conectado = true;).
- **integer**: Representa un número entero. Podemos utilizarlo para almacenar edades, cantidades, entre otros ($edad = 25;).
- **float**: Representa un número decimal o de punto flotante. Es útil para valores que requieren precisión decimal, como precios o coordenadas ($precio = 19.99;).
- **string**: Representa una cadena de caracteres. Usamos este tipo de dato para almacenar texto, nombres, mensajes, entre otros ($nombre = "Nuria"; ).
- **null**: Representa un valor nulo o la ausencia de valor. Puede ser utilizado para indicar que una variable no tiene un valor asignado ($dato = null;).

## Operadores

os operadores en PHP son herramientas clave que nos permiten manipular y realizar diversas operaciones en nuestros programas. Son caracteres especiales que indican al intérprete de PHP qué tipo de operación debe realizar entre los operandos.

### Aritméticos

Estos operadores aritméticos nos permiten realizar diversas operaciones matemáticas en PHP. Puedes utilizar estos operadores junto con variables o valores numéricos para realizar cálculos y asignar los resultados a variables.

| Operador | Descripción              | Ejemplo              |
|----------|--------------------------|----------------------|
| `+`        | Suma                     | `$resultado = $a + $b;` |
| `-`        | Resta                    | `$resultado = $a - $b;` |
| `*`        | Multiplicación           | `$resultado = $a * $b;` |
| `/`        | División                 | `$resultado = $a / $b;` |
| `%`        | Módulo (resto de la división) | `$resultado = $a % $b;` |
| `**`       | Exponenciación           | `$resultado = $a ** $b;` |
| `++`       | Incremento               | `$a++;`                |
| `--`       | Decremento               | `$a--;`                |

### Asignación

Los operadores de asignación nos permiten asignar y modificar valores en variables de manera más eficiente.

| Operador | Descripción                       | Ejemplo                |
|----------|-----------------------------------|------------------------|
| `=`        | Asignación                        | `$a = 5;`               |
| `+=`       | Suma y asignación                 | `$a += 3; // Equivale a $a = $a + 3;` |
| `-=`       | Resta y asignación                | `$a -= 2; // Equivale a $a = $a - 2;` |
| `*=`       | Multiplicación y asignación       | `$a *= 4; // Equivale a $a = $a * 4;` |
| `/=`       | División y asignación             | `$a /= 2; // Equivale a $a = $a / 2;` |
| `%=`       | Módulo y asignación               | `$a %= 3; // Equivale a $a = $a % 3;` |
| `.=`       | Concatenación y asignación        | `$texto .= " mundo"; // Equivale a $texto = $texto . " mundo";` |
| `<<=`      | Desplazamiento a la izquierda y asignación | `$a <<= 2; // Equivale a $a = $a << 2;` |
| `>>=`      | Desplazamiento a la derecha y asignación | `$a >>= 1; // Equivale a $a = $a >> 1;` |
| `&=`       | AND a nivel de bits y asignación  | `$a &= $b; // Equivale a $a = $a & $b;` |
| `^=`       | XOR a nivel de bits y asignación  |`$a ^= $b; // Equivale a $a = $a ^ $b;` |
| `|=`       | OR a nivel de bits y asignación   | `$a |= $b; // Equivale a $a = $a | $b;` |

### Comparación

Los operadores de comparación nos permiten evaluar y comparar valores en PHP. Puedes utilizar estos operadores en combinación con variables y valores para realizar comparaciones y tomar decisiones basadas en el resultado.

| Operador | Descripción                | Ejemplo                    |
|----------|----------------------------|----------------------------|
| `==`       | Igual a                    | `$a == $b`                   |
| `!=`       | Diferente de               | `$a != $b`                   |
| `<`        | Menor que                  | `$a < $b`                    |
| `>`        | Mayor que                  | `$a > $b`                    |
| `<=`       | Menor o igual que          | `$a <= $b`                   |
| `>=`       | Mayor o igual que          | `$a >= $b`                   |
| `===`      | Identidad                  | `$a === $b`                  |
| `!==`      | No identidad               | `$a !== $b`                  |
| `<=>`      | Comparación combinada      | `$a <=> $b`                  |

### Incremento / Decremento

Los operadores de preincremento y predecremento se utilizan para incrementar o decrementar el valor de una variable en 1 antes de utilizarla en una expresión. Por otro lado, los operadores de postincremento y postdecremento incrementan o decrementan el valor de una variable en 1 después de utilizarla en una expresión.

| Operador | Descripción                    | Ejemplo           |
|----------|--------------------------------|-------------------|
| `++`       | Postincremento (Incremento)    | `$a++;`             |
| `--`       | Postdecremento (Decremento)    | `$a--;`             |
| `++`       | Preincremento (Incremento)     | `++$a;`             |
| `--`       | Predecremento (Decremento)     | `--$a;`             |

### Lógicos

Estos operadores lógicos se utilizan para combinar y evaluar condiciones lógicas en expresiones condicionales. Puedes utilizar estos operadores lógicos para construir expresiones más complejas y realizar evaluaciones condicionales en tu código PHP.

| Operador | Descripción                  | Ejemplo                          |
|----------|------------------------------|----------------------------------|
| &&       | AND lógico                   | $a && $b                         |
| \|\|     | OR lógico                    | $a \|\| $b                       |
| and      | AND lógico (alternativo)     | $a and $b                        |
| or       | OR lógico (alternativo)      | $a or $b                         |
| xor      | XOR lógico                   | $a xor $b                        |
| !        | NOT lógico                   | !$a                              |


### de String

| Operador | Descripción                | Ejemplo                    |
|----------|----------------------------|----------------------------|
| `.`       | Concatenación                    | `$a . $b`                   |
| `.=`       | Concatenación y asignación      | `$a .= $b`                   |

### de Array

### Condicionales


| Operador | Descripción                | Ejemplo                    |
|----------|----------------------------|----------------------------|
| `?:`       | Ternario true/false      | `$x = expresion1 ? expresion2 : expresion3` |
| `.=`       | Ternario is Null         | `$x = expresion1 ?? expresion2`  |

## Estructuras de control

### IF, ELSE IF, ELSE

#### Ternarios

### WHILE / DO - WHILE

### SWITCH

### FOR / FOREACH
