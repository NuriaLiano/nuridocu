<?php
// Obtener la fecha actual en formato "Y-m-d"
$fechaActual = date("Y-m-d");
echo "Fecha actual en formato Y-m-d: " . $fechaActual . "<br>";

// Obtener la fecha actual en formato "d/m/Y"
$fechaActualFormatoDMY = date("d/m/Y");
echo "Fecha actual en formato d/m/Y: " . $fechaActualFormatoDMY . "<br>";

// Obtener la fecha actual en formato "d F Y"
$fechaActualFormatoDFY = date("d F Y");
echo "Fecha actual en formato d F Y: " . $fechaActualFormatoDFY . "<br>";

// Obtener el día actual de la semana en formato "l" (nombre completo del día)
$diaSemana = date("l");
echo "Día de la semana: " . $diaSemana . "<br>";

// Obtener el número del día del mes actual en formato "j" (sin ceros iniciales)
$diaMes = date("j");
echo "Día del mes: " . $diaMes . "<br>";

// Obtener el número del mes actual en formato "n" (sin ceros iniciales)
$mes = date("n");
echo "Mes: " . $mes . "<br>";

// Obtener el nombre completo del mes actual en formato "F"
$nombreMes = date("F");
echo "Nombre del mes: " . $nombreMes . "<br>";

// Obtener el año actual en formato "Y"
$anio = date("Y");
echo "Año: " . $anio . "<br>";

// Obtener la hora actual en formato "H:i:s"
$horaActual = date("H:i:s");
echo "Hora actual en formato H:i:s: " . $horaActual . "<br>";

// Obtener la hora actual en formato "h:i:s A" (12 horas, con AM o PM)
$horaActualFormatoAMPM = date("h:i:s A");
echo "Hora actual en formato h:i:s A: " . $horaActualFormatoAMPM . "<br>";

// Obtener la zona horaria actual
$zonaHoraria = date_default_timezone_get();
echo "Zona horaria actual: " . $zonaHoraria . "<br>";

// Establecer una zona horaria diferente y mostrar la hora en esa zona horaria
date_default_timezone_set("America/New_York");
$horaNewYork = date("H:i:s");
echo "Hora en Nueva York: " . $horaNewYork . "<br>";
?>
