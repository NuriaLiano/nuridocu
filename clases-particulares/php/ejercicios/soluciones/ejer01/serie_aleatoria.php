<?php
session_start();

if (isset($_SESSION['serieAleatoria'])) {
    $serieAleatoria = $_SESSION['serieAleatoria'];

    if ($serieAleatoria) {
        echo "<h2>Serie Aleatoria:</h2>";
        echo "<table>";
        echo "<tr><th>ID</th><th>Nombre</th><th>Género</th><th>Año de lanzamiento</th></tr>";
        echo "<tr>";
        echo "<td>" . $serieAleatoria["id"] . "</td>";
        echo "<td>" . $serieAleatoria["nombre"] . "</td>";
        echo "<td>" . $serieAleatoria["genero"] . "</td>";
        echo "<td>" . $serieAleatoria["anio_lanzamiento"] . "</td>";
        echo "</tr>";
        echo "</table>";
    } else {
        echo "No se encontraron series.";
    }
} else {
    echo "No se encontró ninguna serie aleatoria.";
}
?>