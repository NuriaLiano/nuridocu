---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Estructuras de control

Las estructuras de control son utilizadas para tomar decisiones y controlar el flujo del programa.

- [Estructuras de control](#estructuras-de-control)
  - [IF, ELSE IF, ELSE](#if-else-if-else)
  - [WHILE / DO - WHILE](#while--do---while)
    - [While](#while)
    - [Do - while](#do---while)
  - [SWITCH](#switch)
  - [FOR / FOREACH](#for--foreach)
    - [For](#for)
    - [Foreach (List Comprehension)](#foreach-list-comprehension)

## IF, ELSE IF, ELSE

La estructura if, elif (else if) y else permite evaluar condiciones y ejecutar diferentes bloques de código dependiendo del resultado de esas condiciones.

~~~py
if condicion1:
    # código a ejecutar si condicion1 es verdadera
elif condicion2:
    # código a ejecutar si condicion2 es verdadera y condicion1 es falsa
else:
    # código a ejecutar si ninguna de las condiciones anteriores es verdadera
~~~

## WHILE / DO - WHILE

### While

Esta estructura evalúa la condición antes de cada iteración.

~~~py
while condicion:
    # código a repetir mientras se cumpla la condición
~~~

### Do - while

El bloque de código dentro del do se ejecutará al menos una vez, independientemente de si la condición es verdadera o falsa.
**Python no tiene una estructura de bucle do-while tradicional como en otros lenguajes, pero podemos lograr el mismo resultado usando un bucle while con una condición al final.**

~~~py
contador = 0
while True:
    print("Contador:", contador)
    contador += 1
    if contador >= 5:
        break
~~~

## SWITCH

Se evalúa el valor de la variable $variable.

- Si $variable coincide con alguno de los valor_x dentro de los case, se ejecutará el código correspondiente a ese caso.
- Si $variable no coincide con ningún valor_x, se ejecutará el código dentro del default (opcional), que se utiliza cuando no hay coincidencia con ningún caso.

**A diferencia de algunos otros lenguajes, Python no tiene una estructura de control switch. En su lugar, se utilizan múltiples declaraciones if-elif-else para realizar acciones dependiendo del valor de una variable.**

~~~py
opcion = 2
if opcion == 1:
    print("Seleccionaste la opción 1")
elif opcion == 2:
    print("Seleccionaste la opción 2")
elif opcion == 3:
    print("Seleccionaste la opción 3")
else:
    print("Opción inválida")
~~~

## FOR / FOREACH

### For

El bucle for se utiliza para iterar sobre una secuencia (como una lista o una cadena) y realizar una acción para cada elemento.

~~~py
for elemento in secuencia:
    # código a ejecutar para cada elemento en la secuencia

~~~

### Foreach (List Comprehension)

La comprensión de listas es una forma concisa y poderosa de crear listas en una sola línea. Permite aplicar una operación a cada elemento de una secuencia y crear una nueva lista con los resultados.

~~~py
numeros = [1, 2, 3, 4, 5]
cuadrados = [numero**2 for numero in numeros]
print(cuadrados)
~~~
