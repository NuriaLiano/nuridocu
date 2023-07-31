---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Funciones

- [Funciones](#funciones)
  - [Sintaxis](#sintaxis)
  - [Llamar a una función](#llamar-a-una-función)
  - [Parámetros y argumentos](#parámetros-y-argumentos)
  - [Argumentos arbitrarios](#argumentos-arbitrarios)
  - [Valores de retorno](#valores-de-retorno)
  - [Funciones recursivas](#funciones-recursivas)
  - [Ámbito de las variables (scope)](#ámbito-de-las-variables-scope)
  - [Funciones Lambda](#funciones-lambda)
  - [Funciones anidadas](#funciones-anidadas)

Las funciones en Python son bloques de código reutilizables que realizan una tarea específica. Se definen utilizando la palabra clave "def" seguida del nombre de la función y paréntesis que pueden contener parámetros. Las funciones pueden tener uno o más parámetros, y pueden o no devolver un valor.

## Sintaxis

~~~py
def nombre_de_funcion(parametro1, parametro2, ...):
    # Cuerpo de la función
    # Código que realiza la tarea de la función
    return resultado
~~~

## Llamar a una función

Una vez que una función está definida, se puede llamar para ejecutar su código y obtener su resultado (si devuelve un valor). Para llamar a una función, simplemente se escribe su nombre seguido de paréntesis y los argumentos necesarios (si los hay).

~~~py
def saludar(nombre):
    print("Hola, " + nombre + "!")

saludar("Nuria")
~~~

## Parámetros y argumentos

Los parámetros son variables que se utilizan para recibir datos en una función, mientras que los argumentos son los valores reales que se pasan a una función cuando es llamada.

## Argumentos arbitrarios

En Python, una función puede recibir un número arbitrario de argumentos utilizando `*args` y `**kwargs`. `*args` permite pasar un número variable de argumentos posicionales, mientras que `**kwargs` permite pasar un número variable de argumentos con nombre.

~~~py
def suma(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

total = suma(1, 2, 3, 4, 5)
print(total)
~~~

## Valores de retorno

Una función puede devolver un valor utilizando la declaración "return". Si una función no tiene una declaración "return", su valor de retorno será "None".

~~~py
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)
~~~

## Funciones recursivas

Una función recursiva es aquella que se llama a sí misma durante su ejecución. Se utilizan cuando es más conveniente resolver un problema dividiéndolo en casos más pequeños y similares.

~~~py
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

resultado = factorial(5)
print(resultado)
~~~

## Ámbito de las variables (scope)

El ámbito de una variable se refiere a la parte del programa donde la variable es accesible. En Python, las variables tienen alcance global o local. Las variables definidas dentro de una función tienen alcance local y solo pueden ser accedidas dentro de esa función, mientras que las variables definidas fuera de todas las funciones tienen alcance global y pueden ser accedidas en cualquier parte del programa.

~~~py
x = 10

def funcion():
    y = 5
    print("x dentro de la función:", x)
    print("y dentro de la función:", y)

funcion()
print("x fuera de la función:", x)
~~~

## Funciones Lambda

Las funciones lambda son funciones anónimas de una sola línea que pueden tener cualquier número de argumentos, pero solo pueden tener una expresión. Se definen utilizando la palabra clave "lambda" seguida de los parámetros y la expresión.

~~~py
doble = lambda x: x * 2
print(doble(5))
~~~

## Funciones anidadas

Es posible definir funciones dentro de otras funciones. Estas funciones se denominan funciones anidadas. Una función anidada puede acceder a las variables de la función que la contiene.

~~~py
def exterior(x):
    def interior(y):
        return x + y
    return interior

resultado = exterior(10)
print(resultado(5))
~~~
