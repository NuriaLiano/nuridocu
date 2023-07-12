//secuencia de fibonacci
/*
La secuencia de Fibonacci es una serie de números en la que cada número es la suma de los dos números anteriores.
Comienza con los números 0 y 1, y a partir de ahí, cada número en la secuencia es la suma de los dos números anteriores.

La secuencia de Fibonacci se ve así: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Aquí tienes algunos ejemplos de los primeros números de la secuencia de Fibonacci:

El primer número es 0.
El segundo número es 1.
El tercer número es la suma del primer y segundo número, es decir, 0 + 1 = 1.
El cuarto número es la suma del segundo y tercer número, es decir, 1 + 1 = 2.
El quinto número es la suma del tercer y cuarto número, es decir, 1 + 2 = 3.
Y así sucesivamente.
La secuencia de Fibonacci es un patrón matemático que ha sido estudiado durante siglos debido a sus propiedades interesantes.
Aparece en diversas áreas de las matemáticas, la ciencia y la naturaleza, y tiene aplicaciones en problemas de optimización, análisis financiero, teoría de juegos, algoritmos y más.

*/

// Ejemplo utilizando do-while
let numeroLimite = parseInt(prompt("Ingrese un número límite para la secuencia de Fibonacci:"));
let fibonacci = [0, 1];
let indice = 2;

do {
  let siguienteNumero = fibonacci[indice - 1] + fibonacci[indice - 2];
  fibonacci.push(siguienteNumero);
  indice++;
} while (fibonacci[indice - 1] <= numeroLimite);

console.log("Secuencia de Fibonacci utilizando do-while:");
console.log(fibonacci);

// Ejemplo utilizando while
numeroLimite = parseInt(prompt("Ingrese un número límite para la secuencia de Fibonacci:"));
fibonacci = [0, 1];
indice = 2;

while (fibonacci[indice - 1] <= numeroLimite) {
  let siguienteNumero = fibonacci[indice - 1] + fibonacci[indice - 2];
  fibonacci.push(siguienteNumero);
  indice++;
}

console.log("Secuencia de Fibonacci utilizando while:");
console.log(fibonacci);