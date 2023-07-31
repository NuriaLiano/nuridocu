---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Tipos de datos y casting

- [Tipos de datos y casting](#tipos-de-datos-y-casting)
  - [Tipos de datos](#tipos-de-datos)
    - [Strings](#strings)
      - [Cortar cadenas](#cortar-cadenas)
        - [Índice positivo](#índice-positivo)
        - [Índice negativo](#índice-negativo)
        - [Corte con salto](#corte-con-salto)
      - [Modificar cadenas](#modificar-cadenas)
      - [Formatear](#formatear)
      - [Caracteres de escape](#caracteres-de-escape)
      - [Métodos](#métodos)
  - [Casting](#casting)

## Tipos de datos

Entender los tipos de datos en Python es fundamental para declarar variables, asignarles valores y utilizarlos correctamente en nuestras aplicaciones. Si bien ya hemos aprendido cómo declarar variables, asignarles valores e imprimirlos, es crucial comprender qué tipo de dato estamos estableciendo en cada variable y cuándo debemos utilizar cada uno de ellos.

| Clasificación General | Tipo de Dato     | Descripción                                | Ejemplo                         |
|----------------------|------------------|--------------------------------------------|-------------------------------|
| Tipo de Texto        | str              | Representa una cadena de caracteres.      | nombre = "Nuria"               |
| Tipos Numéricos      | int              | Representa un número entero.              | edad = 25                      |
|                      | float            | Representa un número decimal.             | precio = 19.99                 |
|                      | complex          | Representa un número complejo.            | numero_complejo = 2 + 3j       |
| Tipos de Secuencia   | list             | Representa una lista de elementos.        | numeros = [1, 2, 3, 4, 5]      |
|                      | tuple            | Representa una tupla inmutable.           | punto = (10, 20)               |
|                      | range            | Representa una secuencia de números.      | rango = range(1, 6)            |
| Tipo de Mapeo       | dict             | Representa un diccionario o mapa.         | persona = {"nombre": "Nuria", "edad": 25} |
| Tipos de Conjunto    | set              | Representa un conjunto de elementos únicos.| conjunto = {1, 2, 3, 4, 5}     |
|                      | frozenset        | Representa un conjunto inmutable.        | conjunto_inmutable = frozenset({1, 2, 3}) |
| Tipo Booleano        | bool             | Representa un valor verdadero o falso.    | conectado = True               |
| Tipos Binarios       | bytes            | Representa una secuencia de bytes.        | datos_binarios = b"Hello"       |
|                      | bytearray       | Representa una secuencia de bytes modificable.| datos_modificables = bytearray([65, 66, 67]) |
|                      | memoryview       | Representa una vista de memoria de un objeto.| vista_memoria = memoryview(b"Hello") |
| Tipo None           | NoneType         | Representa un valor nulo o la ausencia de valor.| dato = None                    |

### Strings

#### Cortar cadenas

En Python, el rebanado de cadenas, también conocido como "slicing", es una técnica que nos permite extraer una parte específica de una cadena de caracteres. Esto se logra mediante el uso de índices que indican el inicio y el final de la porción de la cadena que deseamos obtener. El rebanado no modifica la cadena original, sino que crea una nueva cadena con la porción extraída.

Sintaxis: `cadena[inicio:fin]`

##### Índice positivo

- Inicio:

~~~py
cadena = "Hola Mundo"
resultado = cadena[0:4]
print(resultado)  # Salida: "Hola"
~~~

- Fín:

~~~py
resultado2 = cadena[5:]
print(resultado2)  # Salida: "Mundo"
~~~

En este ejemplo, estamos obteniendo una porción de la cadena "Hola Mundo". El rebanado cadena[0:4] devuelve los caracteres desde el índice 0 hasta el índice 3 (el carácter en la posición 4 no está incluido). Esto nos da "Hola". Luego, el rebanado cadena[5:] devuelve los caracteres desde el índice 5 hasta el final de la cadena, lo que nos da "Mundo".

##### Índice negativo

También es posible utilizar índices negativos para contar desde el final de la cadena.

~~~py
cadena = "Hola Mundo"
resultado = cadena[-5:-1]
print(resultado)  # Salida: "Mund"

resultado2 = cadena[-5:]
print(resultado2)  # Salida: "Mundo"
~~~

En este ejemplo, estamos usando índices negativos para contar desde el final de la cadena. El rebanado cadena[-5:-1] devuelve los caracteres desde el quinto carácter desde el final hasta el segundo carácter desde el final (el carácter en la posición -1 no está incluido), lo que nos da "Mund". Luego, el rebanado cadena[-5:] devuelve los caracteres desde el quinto carácter desde el final hasta el final de la cadena, lo que nos da "Mundo".

##### Corte con salto

En caso de que queramos extraer dos partes de la cadena se puede realizar mediante el salto o "step".

~~~py
cadena = "abcdefghijklm"
resultado = cadena[1:10:2]
print(resultado)  # Salida: "bdfhj"

resultado2 = cadena[::3]
print(resultado2)  # Salida: "adgjm"
~~~

En este ejemplo, estamos usando un tercer parámetro para especificar el salto (step) entre los índices. El rebanado cadena[1:10:2] devuelve los caracteres desde el índice 1 hasta el índice 9 (el carácter en la posición 10 no está incluido) dando "bdfhj", saltando de dos en dos caracteres. Luego, el rebanado cadena[::3] devuelve todos los caracteres de la cadena, pero salta de tres en tres caracteres, lo que nos da "adgjm".

#### Modificar cadenas

En Python, las cadenas de caracteres son inmutables, lo que significa que una vez que se crea una cadena, no se puede modificar directamente. Sin embargo, hay varias formas de realizar modificaciones en una cadena y crear una nueva cadena con los cambios deseados.

- **Concatenación**: Se puede utilizar para unir dos o más cadenas y crear una nueva cadena que contenga el contenido combinado.

~~~py
cadena1 = "Hola"
cadena2 = "Mundo"
nueva_cadena = cadena1 + " " + cadena2
print(nueva_cadena)  # Salida: "Hola Mundo"
~~~

- **Repetición**: Se puede utilizar el operador de repetición * para repetir una cadena varias veces y crear una nueva cadena con la repetición.

~~~py
cadena = "Hola "
nueva_cadena = cadena * 3
print(nueva_cadena)  # Salida: "Hola Hola Hola "
~~~

- **Sustitución**: Reemplazar una subcadena con otra en una cadena.

~~~py
cadena = "Hola Mundo"
nueva_cadena = cadena.replace("Mundo", "Python")
print(nueva_cadena)  # Salida: "Hola Python"
~~~

- **Conversión mayúsculas y minúsculas**

~~~py
cadena = "Hola Mundo"
mayusculas = cadena.upper()
minusculas = cadena.lower()
print(mayusculas)  # Salida: "HOLA MUNDO"
print(minusculas)  # Salida: "hola mundo"
~~~

- **Eliminación de espacios en blanco**

~~~py
cadena = "   Hola Mundo   "
nueva_cadena = cadena.strip()
print(nueva_cadena)  # Salida: "Hola Mundo"
~~~

#### Formatear

En Python, el formateo de cadenas permite crear cadenas de texto dinámicas al incorporar valores de variables dentro de ellas. Esto facilita la presentación de información de manera legible y estructurada. Python ofrece varias formas de formatear cadenas, y una de las más utilizadas es mediante el método format().

El método format() permite insertar valores de variables dentro de una cadena utilizando marcadores de posición. Los marcadores de posición son llaves {} que indican dónde se colocarán los valores de las variables. Luego, mediante el método format(), podemos especificar qué valores se insertarán en esos marcadores.

~~~py
nombre = "Nuria"
edad = 25

 # Formato de cadena con marcadores de posición
cadena_formato = "Hola, mi nombre es {} y tengo {} años."

 # Utilizando el método format() para insertar los valores en los marcadores
cadena_resultado = cadena_formato.format(nombre, edad)

print(cadena_resultado)
 # Salida: "Hola, mi nombre es Nuria y tengo 25 años
~~~

Además de utilizar los índices de posición, también es posible especificar nombres para los marcadores de posición y utilizarlos en el método format() mediante argumentos con nombres.

~~~py
nombre = "Nuria"
edad = 25

 # Formato de cadena con marcadores de posición
cadena_formato = "Hola, mi nombre es {nombre} y tengo {edad} años."

 # Utilizando el método format() para insertar los valores en los marcadores
cadena_resultado = cadena_formato.format(nombre=nombre, edad=edad)

print(cadena_resultado)
 # Salida: "Hola, mi nombre es Nuria y tengo 25 años
~~~

#### Caracteres de escape

Los caracteres de escape se utilizan para representar caracteres especiales dentro de una cadena. Estos caracteres comienzan con el símbolo de barra invertida `\` seguido de un carácter que define la acción especial que se debe realizar.

- `\\`: Representa una barra invertida literal `\`.
- `\'`: Representa una comilla simple `'`.
- `\"`: Representa una comilla doble `"`.

Además de estos caracteres de escape, Python también admite otros caracteres de escape para representar caracteres especiales, como \n para nueva línea, \t para tabulación horizontal, etc.

~~~py
cadena_nueva_linea = "Primera línea\nSegunda línea"
print(cadena_nueva_linea)
 # Salida:
 # Primera línea
 # Segunda línea

cadena_tabulacion = "Nombre:\Nuria\tEdad:\25"
print(cadena_tabulacion)
 # Salida: "Nombre:	Nuria	Edad:	25"
~~~

| Caracter | Resultado          |
|--------  |--------------------|
| `\'`     | Comilla Simple     |
| `\\`     | Barra Invertida    |
| `\n`     | Nueva Línea        |
| `\r`     | Retorno de Carro   |
| `\t`     | Tabulación         |
| `\b`     | Retroceso          |
| `\f`     | Avance de Formato  |
| `\ooo`   | Valor Octal        |
| `\xhh`   | Valor Hexadecimal  |

#### Métodos

Los "métodos de cadena" son funciones incorporadas que se pueden utilizar para manipular y trabajar con cadenas de texto. Cada cadena en Python es un objeto y tiene asociado un conjunto de métodos que se pueden llamar para realizar diversas operaciones con la cadena.

| Método        | Descripción                                       |
|---------------|---------------------------------------------------|
| capitalize()  | Convierte el primer carácter a mayúscula         |
| casefold()    | Convierte la cadena en minúsculas                |
| center()      | Devuelve una cadena centrada                      |
| count()       | Devuelve el número de veces que ocurre un valor especificado en una cadena |
| encode()      | Devuelve una versión codificada de la cadena      |
| endswith()    | Devuelve verdadero si la cadena termina con el valor especificado |
| expandtabs()  | Establece el tamaño de la tabulación de la cadena |
| find()        | Busca un valor especificado en la cadena y devuelve la posición donde se encontró |
| format()      | Formatea valores especificados en una cadena      |
| format_map()  | Formatea valores especificados en una cadena      |
| index()       | Busca un valor especificado en la cadena y devuelve la posición donde se encontró |
| isalnum()     | Devuelve True si todos los caracteres de la cadena son alfanuméricos |
| isalpha()     | Devuelve True si todos los caracteres de la cadena están en el alfabeto |
| isascii()     | Devuelve True si todos los caracteres de la cadena son caracteres ascii |
| isdecimal()   | Devuelve True si todos los caracteres de la cadena son decimales |
| isdigit()     | Devuelve True si todos los caracteres de la cadena son dígitos |
| isidentifier() | Devuelve True si la cadena es un identificador |
| islower()     | Devuelve True si todos los caracteres de la cadena están en minúsculas |
| isnumeric()   | Devuelve True si todos los caracteres de la cadena son numéricos |
| isprintable() | Devuelve True si todos los caracteres de la cadena son imprimibles |
| isspace()     | Devuelve True si todos los caracteres de la cadena son espacios en blanco |
| istitle()     | Devuelve True si la cadena sigue las reglas de un título |
| isupper()     | Devuelve True si todos los caracteres de la cadena están en mayúsculas |
| join()        | Une los elementos de un iterable al final de la cadena |
| ljust()       | Devuelve una versión justificada a la izquierda de la cadena |
| lower()       | Convierte una cadena en minúsculas                |
| lstrip()      | Devuelve una versión de la cadena con recorte a la izquierda |
| maketrans()   | Devuelve una tabla de traducción que se utilizará en traducciones |
| partition()   | Devuelve una tupla donde la cadena se divide en tres partes |
| replace()     | Devuelve una cadena donde se reemplaza un valor especificado con otro valor especificado |
| rfind()       | Busca un valor especificado en la cadena y devuelve la última posición donde se encontró |
| rindex()      | Busca un valor especificado en la cadena y devuelve la última posición donde se encontró |
| rjust()       | Devuelve una versión justificada a la derecha de la cadena |
| rpartition()  | Devuelve una tupla donde la cadena se divide en tres partes |
| rsplit()      | Divide la cadena en el separador especificado y devuelve una lista |
| rstrip()      | Devuelve una versión de la cadena con recorte a la derecha |
| split()       | Divide la cadena en el separador especificado y devuelve una lista |
| splitlines()  | Divide la cadena en saltos de línea y devuelve una lista |
| startswith()  | Devuelve verdadero si la cadena comienza con el valor especificado |
| strip()       | Devuelve una versión recortada de la cadena |
| swapcase()    | Intercambia mayúsculas y minúsculas, mayúsculas se convierten en minúsculas y viceversa |
| title()       | Convierte el primer carácter de cada palabra en mayúscula |
| translate()   | Devuelve una cadena traducida |
| upper()       | Convierte una cadena en mayúsculas                |
| zfill()       | Rellena la cadena con un número especificado de valores 0 al principio |

## Casting

En ocasiones, es posible que desees especificar un tipo para una variable en Python. Esto se puede lograr mediante el proceso de conversión de tipos, también conocido como "casting". Python es un lenguaje orientado a objetos, y utiliza clases para definir tipos de datos, incluyendo sus tipos primitivos.

El casting en Python se realiza mediante funciones constructoras:

- `int()` - construye un número entero a partir de un literal entero, un literal de punto flotante (eliminando todas las decimales), o un literal de cadena (siempre que la cadena represente un número entero).

~~~py
 # Literal entero
numero_entero = int(10)
print(numero_entero)  # Salida: 10
~~~

- `float()` - construye un número de punto flotante a partir de un literal entero, un literal de punto flotante o un literal de cadena (siempre que la cadena represente un número de punto flotante o un número entero).

~~~py
 # Literal entero
numero_flotante = float(5)
print(numero_flotante)  # Salida: 5.0
~~~

- `str()` - construye una cadena de caracteres a partir de una amplia variedad de tipos de datos, incluyendo cadenas de caracteres, literales enteros y literales de punto flotante.

~~~py
 # Literal entero
cadena2 = str(123)
print(cadena2)  # Salida: "123"
~~~
