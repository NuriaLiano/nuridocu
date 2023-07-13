<?php
// Definir función para asignar vuelos a pasajeros
function asignarVuelos($pasajeros) {
    $vuelosDisponibles = array("Vuelo 1", "Vuelo 2", "Vuelo 3", "Vuelo 4");
    $asignaciones = array();

    $numPasajeros = count($pasajeros);
    $numVuelos = count($vuelosDisponibles);
    $vueloIndex = 0;

    // Asignar vuelos a los pasajeros
    for ($i = 0; $i < $numPasajeros; $i++) {
        if ($vueloIndex >= $numVuelos) {
            $vueloIndex = 0;
        }

        $asignaciones[$pasajeros[$i]] = $vuelosDisponibles[$vueloIndex];
        $vueloIndex++;
    }

    return $asignaciones;
}

// Definir arreglo de pasajeros
$pasajeros = array("Juan", "María", "Carlos", "Ana", "Pedro", "Laura");

// Asignar vuelos a los pasajeros
$asignacionesVuelos = asignarVuelos($pasajeros);

// Mostrar las asignaciones de vuelos
foreach ($asignacionesVuelos as $pasajero => $vuelo) {
    echo $pasajero . " ha sido asignado al " . $vuelo . "<br>";
}

// Verificar si hay pasajeros sin vuelo asignado
$sinAsignacion = false;
foreach ($pasajeros as $pasajero) {
    if (!array_key_exists($pasajero, $asignacionesVuelos)) {
        $sinAsignacion = true;
        break;
    }
}

if ($sinAsignacion) {
    echo "Hay pasajeros sin vuelo asignado.<br>";
} else {
    echo "Todos los pasajeros tienen vuelo asignado.<br>";
}
?>
