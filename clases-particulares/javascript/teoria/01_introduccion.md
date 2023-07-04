---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Introducción a Javascript II

En la anterior sección [Introducción a Javascript I](./00_introduccion.md) veíamos los conceptos generales sobre los lenguajes de programación, nos introducíamos en la historia y los tipos de lenguajes y paradigmas de programación y veíamos unos conceptos sobre Javascript.

En este apartado, vamos a comenzar a tocar código viendo los tipos de datos, operadores, variables, como establecer comentarios, las distintas ubicaciones de Javascript, etc..

- [Variables y constantes](#variables-y-constantes)
  - [¿Qué son las constantes?](#qué-son-las-constantes)


## Variables y constantes

La primera toma de contacto son las variables. Las variables son contenedores que se utilizan para almacenar datos. Se declaran utilizando las palabras clave var, let o const.

>:pencil:**NOTA** Javascript también permite la declaración automatica de variables por lo que no es necesario el uso de var o let, aunque no es recomendable evitar el uso de let y var ya que perjudica la legibilidad del código.

- **var**: se utilizaba en versiones antiguas de JavaScript, concretamente desde 1995 a 2015

> :no_entry: **PROHIBIDO** no se recomienda el uso de **var** actualmente

~~~js
var nombre_variable = valor_variable
~~~

- **let**: nueva forma de declarar variables añadida en [ECMASscript6](#especificacion-ecmascript) a partir de 2015

~~~js
let nombre_variable = valor_variable
~~~

- **const**: forma de clarar constantes

~~~js
const NOMBRE_VARIABLE = valor_variable
~~~

### ¿Qué son las constantes?

Como ya hemos definido en el apartado anterior, las variables son contenedores de datos que pueden variar su valor según la ejecución del código pero hay veces que es necesario que una variable mantenga su valor durante toda la ejecución del código. Para esos casos es donde se utilizan las constantes, contenedores de datos que **NUNCA** modifican su valor, una vez asignado el valor le mantendrán durante toda la ejecución.

Es recomendable seguir unas guías de buenas prácticas cuando utilicemos constantes:

- **Mayusculas**: Convierte el nombre de las constantes en mayúsculas para resaltar que son constantes y no variables.
- **Inicialización al declarar**: Asegúrate de asignar un valor a la constante en el momento de su declaración. Esto evita confusiones y errores más adelante en el código. 
- **Evita reasignaciones**: No intentes cambiar el valor de una constante después de haberla declarado. Si necesitas un valor mutable, considera utilizar una variable en su lugar.
- **Alcance apropiado**: Declara tus constantes en el alcance más cercano posible a donde se utilizan. Esto ayuda a limitar su visibilidad y evitar colisiones de nombres con otras variables o constantes.
- **Documentación**: Si trabajas en un equipo o compartes tu código con otros desarrolladores, es una buena práctica proporcionar documentación clara sobre el propósito y uso de tus constantes. Esto facilita la comprensión del código y ayuda a otros desarrolladores a utilizar tus constantes de manera adecuada.

## Tipos de datos

Antes de asignar valor tenemos que ser conscientes de que tipos de datos existen, en esta tabla podemos ver todos los tipos de datos en Javascript

| Tipo de dato   | Descripción                                                      | Ejemplo                     |
| -------------- | ---------------------------------------------------------------- | --------------------------- |
| Number         | Representa valores numéricos, ya sean enteros o decimales.       | `42`, `3.14`                |
| BigInt         | Representa valores numéricos grandes.                            | `42`, `3.14`                |
| String         | Representa una secuencia de caracteres.                          | `'Hola'`, `"Mundo"`         |
| Boolean        | Representa un valor de verdadero (`true`) o falso (`false`).     | `true`, `false`             |
| Undefined      | Indica que una variable no tiene un valor asignado.              | `undefined`                 |
| Null           | Representa la ausencia intencional de cualquier objeto o valor.  | `null`                      |
| Array          | Representa una colección ordenada de elementos.                  | `[1, 2, 3]`                 |
| Objeto         | Representa una entidad con propiedades y valores asociados.      | `Symbol(1)`                 |
| Symbol         | Representa un valor único                                        | `[1, 2, 3]`                 |

En esta tabla puedes ver todos los tipos de datos que existen en Javascript, pero todos estos tipos de datos tienen una subclasificación que está representada por colores. 

- Tipos de datos primitivos: 
- Objetos
- Arrays
- Funciones
- Símbolos
- Fechas




### Tipos de datos primitivos

### ¿Es lo mismo `NULL` que `UNDEFINED`?

### ¿Cómo sé que tipo de dato tiene una variable?


Explicación de los diferentes tipos de datos en JavaScript: números, cadenas, booleanos, arrays, objetos, etc.
Cómo se utilizan los tipos de datos en la programación.

## Operadores

Descripción de los operadores aritméticos, lógicos y de comparación.
Cómo se usan los operadores para realizar operaciones matemáticas y lógicas.

## Comentarios

Cómo agregar comentarios en el código JavaScript para mejorar la legibilidad y explicar el código.

## Cómo enlazar o agregar código Javascript

### Vincular un archivo externo

### Insertar código directamente en HTML

## Como ejecutar Javascript

### Ejecutando en consola

Introducción a la consola del navegador y cómo usarla para depurar y probar el código JavaScript

### Ejecutando en navegador

## Especificacion ECMAScript

Explicación breve de qué es ECMAScript y cómo está relacionado con JavaScript.
