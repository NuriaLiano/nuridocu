//CON MYSQLI
<?php
session_start();

// Realizar la conexión a la base de datos utilizando la clase conexionDB
require_once 'conexionDB.php';
$conexionDB = new conexionDB();
$conexion = $conexionDB->getConexion();

// Verificar si se ha enviado el formulario
if ($_SERVER["REQUEST_METHOD"] == "GET") {
    // Obtener el género seleccionado del formulario y validar
    $genero = $_GET["genero"];

    // Validar y sanitizar los datos del formulario si es necesario
    // En este caso, no realizaremos validación adicional ya que se introducirá el género manualmente

    // Verificar si se ha pulsado el botón "Consultar"
    if (isset($_GET["consulta"])) {
        // Construir y ejecutar la consulta SQL utilizando bind_param
        $sql = "SELECT * FROM Series";
        if (!empty($genero)) {
            $sql .= " WHERE genero = ?";
        }

        try {
            $consulta = $conexion->prepare($sql);

            if (!empty($genero)) {
                $consulta->bind_param("s", $genero);
            }

            $consulta->execute();
            $resultados = $consulta->get_result()->fetch_all(MYSQLI_ASSOC);

            // Almacenar los resultados en la sesión
            $_SESSION['resultados'] = $resultados;

            // Redirigir a la página de resultados
            header("Location: resultados.php");
            exit();
        } catch (Exception $e) {
            echo "Error en la consulta: " . $e->getMessage();
        }
    }

    // Verificar si se ha pulsado el botón "Mostrar Serie Aleatoria"
    if (isset($_GET["aleatoria"])) {
        try {
            $sql = "SELECT * FROM Series ORDER BY RAND() LIMIT 1";
            $consulta = $conexion->prepare($sql);
            $consulta->execute();
            $serieAleatoria = $consulta->get_result()->fetch_assoc();

            // Almacenar la serie aleatoria en la sesión
            $_SESSION['serieAleatoria'] = $serieAleatoria;

            // Redirigir a la página de serie aleatoria
            header("Location: serie_aleatoria.php");
            exit();
        } catch (Exception $e) {
            echo "Error en la consulta: " . $e->getMessage();
        }
    }
}
?>