---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Primeros pasos con Python

- [Primeros pasos con Python](#primeros-pasos-con-python)
  - [Ejecutar Python](#ejecutar-python)
    - [Llamando al interprete](#llamando-al-interprete)
    - [Interactivo](#interactivo)
  - [Sintaxis](#sintaxis)
    - [Case sensitive](#case-sensitive)
  - [Comentarios](#comentarios)
    - [Comentarios de línea](#comentarios-de-línea)
    - [Comentarios de bloque](#comentarios-de-bloque)
  - [Imprimir](#imprimir)
  - [Primer programa con PHP](#primer-programa-con-php)
  - [Variables y constantes](#variables-y-constantes)
    - [Variables](#variables)
    - [Constantes](#constantes)
    - [Imprimir variables y constantes](#imprimir-variables-y-constantes)

## Ejecutar Python

Python ofrece varias formas de ejecución, tanto por línea de comandos llamando al ejecutable de python o en modo interactivo desde la consola.

### Llamando al interprete

PHP es un lenguaje de scripting que permite ejecutar código fuera de un servidor web.

1. Abre la consola o terminal de tu sistema operativo.
2. Navega hasta el directorio donde se encuentra el archivo Python que deseas ejecutar.
3. Una vez en el directorio correcto, puedes ejecutar el script Python usando el siguiente comando:

~~~php
python3 nombre_del_archivo.py
~~~

>:warning: **ADVERTENCIA** Es posible que al ejecutar python3 no encuentre el comando, ese error se debe a que la ruta donde está el interprete no está cargada en las variables del usuario.

### Interactivo

Python también ofrece un modo interactivo, donde puedes ejecutar líneas de código una a la vez.

1. Abre la terminal o consola de tu sistema operativo.
2. Ejecuta el siguiente comando

   ~~~py
   python3
   ~~~

3. Ahora estarás en el entorno interactivo de Python. Puedes ingresar líneas de código una a la vez y ver los resultados inmediatamente.

   ~~~py
   >>> print("Hola Mundo")
   Hola Mundo
   ~~~

> :pencil: **NOTA** Para salir del modo interactivo, puedes presionar Ctrl + D.

## Sintaxis

Los scripts en Python se escriben en archivos con extensión .py y no necesitan marcas de apertura o cierre como en PHP. El código dentro del archivo .py será ejecutado como código Python automáticamente.

~~~py
print("Hola Mundo")
~~~

Cuando creas un archivo con código Python, asegúrate de que tenga la extensión .py. Por ejemplo, si tienes un archivo llamado miarchivo.html que contiene código HTML y Python, debes cambiar su nombre a miarchivo.py.

En Python, el punto y coma no es necesario al final de cada instrucción. Python utiliza el salto de línea para determinar el final de una instrucción, por lo que puedes omitir el punto y coma en la mayoría de los casos.

### Case sensitive

En Python las palabras reservadas (if, switch, echo, etc) son case-sensitive, lo que significa que su escritura con mayúsculas y minúsculas afectará su reconocimiento. Es recomendable seguir una convención de escritura consistente para mantener el código legible y evitar posibles errores.

Aunque no influya en el funcionamiento del programa es recomendable, siguiendo las buenas prácticas, escribir las palabras reservadas en minúsculas

> :woman_teacher: **EXPLICACIÓN** case sensitive 

~~~py
print("Hola Mundo")  # lo recomendado
ECHO("Hola Mundo") # Esto dará un error, ya que Python distingue entre mayúsculas y minúsculas en las palabras clave.
EcHo("Hola Mundo") # Esto también dará un error por la misma razón.
~~~

## Comentarios

Los comentarios son líneas que no se ejecutan como parte del programa. Son fundamentales para agregar notas, explicaciones y aclaraciones dentro del código. Python permite establecer comentarios de línea y comentarios de bloque, pero se utilizan diferentes caracteres para cada uno.

### Comentarios de línea

Los comentarios de línea en Python comienzan con el carácter `#` y se aplican solo a la línea en la que se encuentran.

~~~py
    # Esto es un comentario de línea en Python
~~~

### Comentarios de bloque

En Python, no hay comentarios de bloque que abarquen varias líneas. Sin embargo, puedes usar el triple comilla doble `'''` o `"""` para crear comentarios de bloque, pero se utilizarán más comúnmente para escribir cadenas de texto multilinea o docstrings.

~~~py
'''
Todo este
texto
será
ignorado
'''

"""
Lo mismo ocurre
con estas
comillas triples
"""

~~~

## Imprimir

En todos los lenguajes de programación, en algún momento, necesitamos imprimir texto, variables, funciones, etc.

En Python, para imprimir texto y valores en la consola, utilizamos la función `print()` que puede recibir uno o más argumentos separados por comas y los imprimirá en la consola.

Recuerda que Python es un lenguaje muy versátil y ofrece muchas opciones para formatear y presentar datos en la consola utilizando print(). Por ejemplo, puedes usar formatos especiales o la función f-string para mostrar variables o expresiones dentro de una cadena de texto.

~~~py
print("Imprimo con print")  # Imprime el texto "Imprimo con print"
print("Imprimo", "con", "print")  # Imprime varios valores separados por espacio
print(1 + 2)  # Imprime el resultado de la expresión, que es 3
~~~

## Primer programa con PHP

En Python, hacer nuestro primer programa 'Hola Mundo' es muy sencillo. Solo necesitamos crear un archivo con extensión `.py` y utilizar la función `print()` para mostrar el mensaje

Lo primero que vamos a hacer es crear un fichero `hola.php` y vamos a imprimir el mensaje `Hola Mundo` típico.

~~~py
    # Primer programa para aprender a imprimir texto
print("Hola Mundo")
~~~

> :back: **PARA ENTRAR EN CONTEXTO** si no sabes como ejecutar Python puedes echar un vistazo a la sección anterior donde vemos como configurar nuestro editor de código y navegador. [Instalación, configuración y ejecución de Python](./02_instalacion.md)

## Variables y constantes

EL uso de variables y constantes es una parte fundamental de los lenguajes de programación, nos permiten almacenar datos y utilizarlos en el código y también variar su valor en base a la ejecución.

PHP es un lenguaje de tipado dinámico por lo que no es necesario definir que tipo de dato establecemos en las variables

> :white_check_mark: **RECOMENDADO** echa un vistazo a la sección de [Lenguajes de programación: Tipados]()
> :white_check_mark: **RECOMENDADO** echa un vistazo a la sección de [Scope de las variables]()

### Variables

Las variables son contenedores de valores que pueden cambiar su valor según definamos en la ejecución del código. En Python simplemente se crean asignando un valor a un nombre.

> :white_check_mark: **RECOMENDADO** echa un vistazo a la sección de [Buenas prácticas de programación: variables y constantes]()

~~~py
variable1 = "Hola mundo"
var2 = 6
v3 = "probando variables"
~~~

### Constantes

Aunque Python no tiene una construcción específica para constantes, se considera una buena práctica utilizar nombres en mayúsculas para indicar que una variable es una constante y que su valor no debe cambiar durante la ejecución del programa. Aunque el valor de estas variables puede modificarse, por convención, se considera que su valor es constante y no debería cambiar.

~~~py
PRIMERA_CONSTANTE = "he desactivado case-insensitive"
SEGUNDA_CONSTANTE = "he activado case-insensitive"
~~~

### Imprimir variables y constantes

En Python, para imprimir el valor de variables y constantes, utilizamos la función `print()` al igual que hemos visto previamente.

~~~py
    # Variables
variable1 = "Hola Mundo"
var2 = 6
v3 = "probando variables"

    # Constantes (convención en mayúsculas para indicar que son constantes)
PRIMERA_CONSTANTE = "he desactivado case-insensitive"
SEGUNDA_CONSTANTE = "he activado case-insensitive"

    # Imprimir variables y constantes
print(variable1)  # resultado: Hola Mundo
print(var2)       # resultado: 6
print(v3)         # resultado: probando variables

print(PRIMERA_CONSTANTE)  # resultado: he desactivado case-insensitive
print(SEGUNDA_CONSTANTE)  # resultado: he activado case-insensitive
~~~
