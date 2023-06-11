<?php
session_start();

$resultados = isset($_SESSION['resultados']) ? $_SESSION['resultados'] : array();

// if (isset($_SESSION['resultados'])) {
//     $resultados = $_SESSION['resultados'];
// } else {
//     $resultados = array();
// }

if (empty($resultados)) {
    echo "<p>No se encontraron series.</p>";
} else {
    //print_r($resultados);
    echo "<table>";
    echo "<tr><th>Título</th><th>Género</th><th>Año</th></tr>";
    foreach ($resultados as $serie) {
        echo "<tr>";
        echo "<td>".$serie['nombre']."</td>";
        echo "<td>".$serie['genero']."</td>";
        echo "<td>".$serie['anio_lanzamiento']."</td>";
        echo "</tr>";
    }
    echo "</table>";
}

unset($_SESSION['resultados']);
?>