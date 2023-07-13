<?php
// Definir un arreglo multidimensional de estudiantes y sus calificaciones
$estudiantes = [
    ["nombre" => "Juan", "calificaciones" => [85, 92, 78, 90, 88]],
    ["nombre" => "María", "calificaciones" => [76, 82, 90, 88, 94]],
    ["nombre" => "Carlos", "calificaciones" => [89, 84, 79, 92, 87]],
    ["nombre" => "Ana", "calificaciones" => [91, 88, 82, 85, 90]]
];

// Calcular el promedio de cada estudiante y mostrarlo en pantalla
foreach ($estudiantes as $estudiante) {
    $nombre = $estudiante["nombre"];
    $calificaciones = $estudiante["calificaciones"];

    $total = 0;
    $cantidad = count($calificaciones);

    foreach ($calificaciones as $calificacion) {
        $total += $calificacion;
    }

    $promedio = $total / $cantidad;

    echo "El promedio de calificaciones de " . $nombre . " es: " . $promedio . "<br>";
}
?>
