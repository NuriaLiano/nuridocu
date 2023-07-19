<?php
// Función para calcular el tiempo restante hasta una fecha específica
function calcularTiempoRestante($fechaObjetivo) {
    $fechaActual = new DateTime();
    $fechaObjetivo = new DateTime($fechaObjetivo);
    $diferencia = $fechaActual->diff($fechaObjetivo);

    $tiempoRestante = array(
        "anios" => $diferencia->y,
        "meses" => $diferencia->m,
        "dias" => $diferencia->d,
        "horas" => $diferencia->h,
        "minutos" => $diferencia->i,
        "segundos" => $diferencia->s
    );

    return $tiempoRestante;
}

// Fecha objetivo para el cálculo del tiempo restante (ejemplo: 31 de diciembre de 2023)
$fechaObjetivo = "2023-12-31";

// Calcular el tiempo restante hasta la fecha objetivo
$tiempoRestante = calcularTiempoRestante($fechaObjetivo);

// Mostrar el tiempo restante en pantalla
echo "Tiempo restante hasta el 31 de diciembre de 2023:<br>";
echo $tiempoRestante["anios"] . " años, ";
echo $tiempoRestante["meses"] . " meses, ";
echo $tiempoRestante["dias"] . " días, ";
echo $tiempoRestante["horas"] . " horas, ";
echo $tiempoRestante["minutos"] . " minutos, ";
echo $tiempoRestante["segundos"] . " segundos.";
?>
