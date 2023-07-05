---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---
# Estructuras de control

- [Estructuras de control](#estructuras-de-control)
  - [1. Estructura if-else](#1-estructura-if-else)
  - [2. Estructura switch](#2-estructura-switch)
  - [3. Estructura while](#3-estructura-while)
  - [4. Estructura do-while](#4-estructura-do-while)
  - [5. Estructura for](#5-estructura-for)
  - [6. Estructura for...in](#6-estructura-forin)
  - [7. Estructura for...of](#7-estructura-forof)
  - [8. Estructura try-catch](#8-estructura-try-catch)
  - [9. Estructura try-catch-finally](#9-estructura-try-catch-finally)

## 1. Estructura if-else

La estructura if-else se utiliza para tomar decisiones basadas en una condición. Si la condición es verdadera, se ejecuta un bloque de código. De lo contrario, se ejecuta otro bloque de código.

~~~javascript
if (condicion) {
  // Bloque de código si la condición es verdadera
} else {
  // Bloque de código si la condición es falsa
}
~~~

## 2. Estructura switch

La estructura switch se utiliza para evaluar diferentes casos y ejecutar un bloque de código según el caso coincidente.

~~~javascript
switch (expresion) {
  case valor1:
    // Bloque de código si la expresión coincide con valor1
    break;
  case valor2:
    // Bloque de código si la expresión coincide con valor2
    break;
  default:
    // Bloque de código si la expresión no coincide con ningún caso
    break;
}
~~~

## 3. Estructura while

La estructura while se utiliza para repetir un bloque de código mientras se cumpla una condición.

~~~javascript
while (condicion) {
  // Bloque de código a repetir mientras la condición sea verdadera
}
~~~

## 4. Estructura do-while

La estructura do-while se utiliza para repetir un bloque de código al menos una vez y luego mientras se cumpla una condición.

~~~javascript
do {
  // Bloque de código a repetir
} while (condicion);
~~~

## 5. Estructura for

La estructura for se utiliza para repetir un bloque de código un número específico de veces.

~~~javascript
for (inicialización; condición; incremento/decremento) {
  // Bloque de código a repetir
}
~~~

## 6. Estructura for...in

La estructura for...in se utiliza para iterar sobre las propiedades de un objeto.

~~~javascript
for (variable in objeto) {
  // Bloque de código a ejecutar para cada propiedad del objeto
}
~~~

## 7. Estructura for...of

La estructura for...of se utiliza para iterar sobre los elementos de un iterable (como un array o una cadena).

~~~javascript
for (variable of iterable) {
  // Bloque de código a ejecutar para cada elemento del iterable
}
~~~

## 8. Estructura try-catch

La estructura try-catch se utiliza para manejar excepciones (errores) en el código.

~~~javascript
try {
  // Bloque de código que puede generar una excepción
} catch (error) {
  // Bloque de código para manejar la excepción
}
~~~

## 9. Estructura try-catch-finally

La estructura try-catch-finally se utiliza para manejar excepciones y ejecutar un bloque de código final, independientemente de si se produce una excepción o no.

~~~javascript
try {
  // Bloque de código que puede generar una excepción
} catch (error) {
  // Bloque de código para manejar la excepción
} finally {
  // Bloque de código que se ejecuta siempre, sin importar si se produjo una excepción o no
}
~~~
