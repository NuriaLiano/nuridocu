<?php

// Define la cantidad de filas de la pirámide
$filas = 5;

// Bucle para imprimir las filas
for ($i = 1; $i <= $filas; $i++) {

  // Bucle para imprimir los espacios en blanco
  for ($espacio = 1; $espacio <= $filas - $i; $espacio++) {
    echo " ";
  } 

  // Bucle para imprimir los asteriscos
  for ($asterisco = 1; $asterisco <= (2 * $i - 1); $asterisco++) {
    echo "*";
  }

  // Imprime un salto de línea para pasar a la siguiente fila
  echo "\n";
}

?>