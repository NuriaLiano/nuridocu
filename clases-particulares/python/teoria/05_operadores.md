---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Operadores

- [Operadores](#operadores)
  - [Aritméticos](#aritméticos)
  - [Asignación](#asignación)
  - [Comparación](#comparación)
  - [Incremento / Decremento](#incremento--decremento)
  - [Lógicos](#lógicos)
  - [de Identidad](#de-identidad)
  - [de Pertenencia](#de-pertenencia)
  - [Bitwise](#bitwise)

Los operadores en PHP son herramientas clave que nos permiten manipular y realizar diversas operaciones en nuestros programas. Son caracteres especiales que indican al intérprete de PHP qué tipo de operación debe realizar entre los operandos.

## Aritméticos

Estos operadores aritméticos nos permiten realizar diversas operaciones matemáticas en PHP. Puedes utilizar estos operadores junto con variables o valores numéricos para realizar cálculos y asignar los resultados a variables.

| Operador  | Nombre          | Ejemplo     |
|-----------|-----------------|-------------|
| +         | Adición         | x + y       |
| -         | Sustracción     | x - y       |
| *         | Multiplicación  | x * y       |
| /         | División        | x / y       |
| %         | Módulo          | x % y       |
| **        | Exponenciación  | x ** y      |
| //        | División entera | x // y      |

## Asignación

Los operadores de asignación nos permiten asignar y modificar valores en variables de manera más eficiente.

| Operador | Descripción                     | Ejemplo      |
|----------|---------------------------------|--------------|
| =        | Asignación                      | x = 5        |
| +=       | Suma y asignación               | x += 3       |
| -=       | Resta y asignación              | x -= 3       |
| *=       | Multiplicación y asignación     | x *= 3       |
| /=       | División y asignación           | x /= 3       |
| %=       | Módulo y asignación             | x %= 3       |
| //=      | División entera y asignación    | x //= 3      |
| **=      | Exponenciación y asignación     | x **= 3      |
| &=       | AND bit a bit y asignación      | x &= 3       |
| \|=      | OR bit a bit y asignación       | x \|= 3      |
| ^=       | XOR bit a bit y asignación      | x ^= 3       |
| >>=      | Desplazamiento a la derecha y asignación | x >>= 3 |
| <<=      | Desplazamiento a la izquierda y asignación | x <<= 3 |

## Comparación

Los operadores de comparación nos permiten evaluar y comparar valores en PHP. Puedes utilizar estos operadores en combinación con variables y valores para realizar comparaciones y tomar decisiones basadas en el resultado.

| Operador | Descripción                 | Ejemplo     |
|----------|-----------------------------|-------------|
| ==       | Igual                       | x == y      |
| !=       | No igual                    | x != y      |
| >        | Mayor que                   | x > y       |
| <        | Menor que                   | x < y       |
| >=       | Mayor o igual que           | x >= y      |
| <=       | Menor o igual que           | x <= y      |

## Incremento / Decremento

En Python, no existen operadores de preincremento ni predecremento como en algunos otros lenguajes de programación. Sin embargo, podemos lograr el mismo resultado utilizando los operadores de incremento (+=) y decremento (-=).

| Operador | Descripción                    | Ejemplo           |
|----------|--------------------------------|-------------------|
| `+=`       | Postincremento (Incremento)    | `a += 1` o `a = a + 1`             |
| `-`       | Decremento (Resta en asignación)    | `a -= 1` o `a = a - 1`             |

## Lógicos

Estos operadores lógicos se utilizan para combinar y evaluar condiciones lógicas en expresiones condicionales. Puedes utilizar estos operadores lógicos para construir expresiones más complejas y realizar evaluaciones condicionales en tu código PHP.

| Operador | Nombre                         | Ejemplo                            |
|----------|--------------------------------|------------------------------------|
| and      | Y lógico                       | x < 5 and x < 10                   |
| or       | O lógico                       | x < 5 or x < 4                     |
| not      | Negación                       | not (x < 5 and x < 10)             |

## de Identidad

| Operador | Descripción                                    | Ejemplo             |
|----------|-----------------------------------------------|----------------------|
| is       | Devuelve True si ambas variables son el mismo objeto   | x is y      |
| is not   | Devuelve True si ambas variables no son el mismo objeto | x is not y |

## de Pertenencia

| Operador | Descripción                                    | Ejemplo                 |
|----------|-----------------------------------------------|-------------------------|
| in       | Retorna True si una secuencia con el valor especificado está presente en el objeto   | x in y                  |
| not in   | Retorna True si una secuencia con el valor especificado no está presente en el objeto | x not in y              |

## Bitwise

Los operadores bitwise se utilizan para realizar operaciones bit a bit en números binarios.

| Operador | Nombre  | Descripción                                               | Ejemplo   |
|----------|---------|----------------------------------------------------------|-----------|
| &        | AND     | Establece cada bit en 1 si ambos bits son 1             | x & y     |
| \|       | OR      | Establece cada bit en 1 si al menos uno de los dos bits es 1  | x \| y    |
| ^        | XOR     | Establece cada bit en 1 si solo uno de los dos bits es 1  | x ^ y     |
| ~        | NOT     | Invierte todos los bits                                  | ~x        |
| <<       | Desplazamiento a la izquierda con relleno de ceros     | Desplaza a la izquierda agregando ceros desde la derecha y deja que los bits más a la izquierda caigan   | x << 2    |
| >>       | Desplazamiento a la derecha con signo                 | Desplaza a la derecha empujando copias del bit más a la izquierda desde la izquierda, y deja que los bits más a la derecha caigan | x >> 2    |