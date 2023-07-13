<?php
// Definir una función para obtener el promedio de un arreglo de números
function calcularPromedio($numeros) {
    $total = 0;
    $cantidad = count($numeros);

    for ($i = 0; $i < $cantidad; $i++) {
        $total += $numeros[$i];
    }

    $promedio = $total / $cantidad;
    return $promedio;
}

// Definir un arreglo de números
$notas = [85, 92, 78, 90, 88];

// Llamar a la función para calcular el promedio y mostrarlo en pantalla
$promedioNotas = calcularPromedio($notas);
echo "El promedio de las notas es: " . $promedioNotas;
?>
