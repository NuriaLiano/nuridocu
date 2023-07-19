---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Estructuras de control

- [Estructuras de control](#estructuras-de-control)
  - [IF, ELSE IF, ELSE](#if-else-if-else)
    - [Ternarios](#ternarios)
  - [WHILE / DO - WHILE](#while--do---while)
    - [While](#while)
    - [Do - while](#do---while)
  - [SWITCH](#switch)
  - [FOR / FOREACH](#for--foreach)
    - [For](#for)
    - [Foreach](#foreach)

## IF, ELSE IF, ELSE

~~~php
if (condición) {
    // Código a ejecutar si la condición es verdadera
} elseif (otra_condición) {
    // Código a ejecutar si la primera condición es falsa y la otra_condición es verdadera
} else {
    // Código a ejecutar si ninguna de las condiciones anteriores es verdadera
}
~~~

### Ternarios

El operador ternario es una forma abreviada de escribir una estructura if...else cuando solo necesitas asignar un valor a una variable o expresión según una condición.

~~~php
condición ? valor_si_verdadero : valor_si_falso;
~~~

## WHILE / DO - WHILE

### While

Esta estructura evalúa la condición antes de cada iteración.

~~~php
while (condición) {
    // Código a ejecutar mientras la condición sea verdadera
}
~~~

### Do - while

El bloque de código dentro del do se ejecutará al menos una vez, independientemente de si la condición es verdadera o falsa.

~~~php
do {
    // Código a ejecutar al menos una vez
    // Código a ejecutar mientras la condición sea verdadera
} while (condición);
~~~

## SWITCH

Se evalúa el valor de la variable $variable.

- Si $variable coincide con alguno de los valor_x dentro de los case, se ejecutará el código correspondiente a ese caso.
- Si $variable no coincide con ningún valor_x, se ejecutará el código dentro del default (opcional), que se utiliza cuando no hay coincidencia con ningún caso.

~~~php
switch ($variable) {
    case valor_1:
        // Código a ejecutar si la variable es igual a valor_1
        break;
    case valor_2:
        // Código a ejecutar si la variable es igual a valor_2
        break;
    // Puedes agregar más casos según sea necesario
    default:
        // Código a ejecutar si la variable no coincide con ningún caso anterior
        break;
}
~~~

## FOR / FOREACH

### For

- `inicialización` es una expresión que se evalúa una vez antes de comenzar el bucle.
- `condición` es una expresión que se evalúa antes de cada iteración. Si la condición es verdadera, el bucle continúa; si es falsa, el bucle se detiene.
- `incremento/decremento` se ejecuta después de cada iteración y generalmente se utiliza para aumentar o disminuir el valor de la variable de control del bucle.

~~~php
for (inicialización; condición; incremento/decremento) {
    // Código a ejecutar mientras se cumpla la condición
}
~~~

### Foreach

- `$array` es el array que se va a recorrer con el bucle foreach.
- `$valor` es una variable que tomará el valor de cada elemento del array en cada iteración del bucle.
- El bucle foreach se ejecuta para cada elemento del array.

~~~php
foreach ($array as $valor) {
    // Código a ejecutar para cada valor del array
}
~~~
