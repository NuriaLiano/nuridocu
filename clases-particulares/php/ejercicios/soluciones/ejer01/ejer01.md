
# Ejercicio 1. Objetos, sesiones, conexiones a la base de datos, consultas sencillas. 

Has sido contratado como desarrollador web para crear un sistema de consulta de series de televisión. Deberás implementar un formulario básico y una página de resultados utilizando PHP y sesiones.

Instrucciones:

1. Crea un archivo llamado index.html que contenga un formulario HTML con los siguientes elementos:

- Un campo de texto para ingresar el género de la serie.
- Dos botones de tipo submit: "Consultar" y "Mostrar Serie Aleatoria".

2. Crea un archivo llamado consultar_series.php que será responsable de realizar la conexión a la base de datos y procesar los datos del formulario.

- Utiliza la clase conexionDB para establecer la conexión con la base de datos.
- Valida y sanitiza los datos ingresados en el formulario.
- Si se presiona el botón "Consultar", ejecuta una consulta SQL para obtener todas las series del género especificado y almacena los resultados en una variable de sesión.
- Si se presiona el botón "Mostrar Serie Aleatoria", ejecuta una consulta SQL para obtener una serie aleatoria y almacena el resultado en una variable de sesión.

3. Crea un archivo llamado resultados.php que mostrará los resultados de la consulta realizada.

- Recupera los resultados almacenados en la variable de sesión y muéstralos en una tabla.
- Si no se encontraron resultados, muestra un mensaje indicando que no se encontraron series.

4. Crea un archivo llamado serie_aleatoria.php que mostrará una serie aleatoria.

- Recupera la serie aleatoria almacenada en la variable de sesión y muestra sus detalles en una tabla.

Recuerda utilizar sesiones para mantener la información de los resultados y la serie aleatoria entre las diferentes páginas. Puedes utilizar las funciones y métodos proporcionados por la extensión PDO para realizar consultas a la base de datos.

Nota: Asegúrate de que todos los archivos necesarios estén en la misma ubicación y de que la configuración de la base de datos sea correcta.

## Base de datos necesaria

~~~sql
-- Crear la base de datos
CREATE DATABASE series_tv;

-- Conectarse a la base de datos
USE series_tv;

-- Crear tablas
CREATE TABLE Series (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    genero VARCHAR(100),
    anio_lanzamiento INT
);
CREATE TABLE Temporadas (
    id INT PRIMARY KEY,
    serie_id INT,
    numero INT,
    episodios INT,
    FOREIGN KEY (serie_id) REFERENCES Series(id)
);

-- Insertar datos
INSERT INTO Series (id, nombre, genero, anio_lanzamiento)
VALUES
    (1, 'Friends', 'Comedia', 1994),
    (2, 'Breaking Bad', 'Drama', 2008),
    (3, 'Stranger Things', 'Ciencia ficción', 2016),
    (4, 'Game of Thrones', 'Fantasía', 2011);

INSERT INTO Temporadas (id, serie_id, numero, episodios)
VALUES
    (1, 1, 1, 24),
    (2, 1, 2, 24),
    (3, 2, 1, 7),
    (4, 2, 2, 13),
    (5, 3, 1, 8),
    (6, 3, 2, 9),
    (7, 4, 1, 10),
    (8, 4, 2, 9),
    (9, 4, 3, 10);
~~~

## Crea un formulario básico en html

### ¿Qué método tienes que usar para enviar el formulario?

El método GET se utiliza principalmente para solicitar y recuperar información del servidor. Los datos se envían como parte de la URL y son visibles en la barra de direcciones del navegador. Este método es adecuado cuando se trata de consultas o búsquedas donde se espera obtener resultados basados en parámetros proporcionados. Además, los formularios que utilizan el método GET son más fáciles de guardar y compartir, ya que la información se incluye en la URL.

El método POST, por otro lado, se utiliza principalmente para enviar datos al servidor para su procesamiento. Los datos se envían en el cuerpo de la solicitud HTTP y no son visibles en la URL. Este método es más adecuado cuando se trata de enviar datos sensibles o confidenciales, como contraseñas o información personal, ya que no se muestran en la barra de direcciones del navegador.

En el caso de un formulario de consulta de series de televisión, el uso del método GET es apropiado, ya que se está solicitando información del servidor (series de un género específico). **Los parámetros de búsqueda se envían como parte de la URL y no se maneja información confidencial. Sin embargo, si hubiera una acción que realizara modificaciones en la base de datos (por ejemplo, agregar una nueva serie), sería más apropiado utilizar el método POST para enviar los datos de manera segura al servidor.**

### Archivo INDEX.HTML

~~~html
<!DOCTYPE html>
<html>
<head>
    <title>Consulta de Series</title>
</head>
<body>
    <h1>Consulta de Series</h1>
    <form action="consultar_series.php" method="GET">
        <label for="genero">Cúentame que género te apetece ver hoy:</label>
        <input type="text" name="genero" id="genero" required>
        <br><br>
        <input type="submit" name="consulta" value="Consultar series">
        <input type="submit" name="aleatoria" value="Mostrar Serie Aleatoria">
    </form>
</body>
</html>
~~~

### Crea un objeto llamado 'conexionDB' para conectarte a la base de datos

~~~php
<?php
// Usando MYSQLI
class conexionDB {
    private $host = "nombre_del_host"; // Nombre del host de la base de datos (por ejemplo, localhost)
    private $usuario = "nombre_de_usuario"; // Nombre de usuario para acceder a la base de datos
    private $password = "contraseña"; // Contraseña para acceder a la base de datos
    private $nombreBD = "nombre_de_la_base_de_datos"; // Nombre de la base de datos

    private $conexion;

    public function __construct() {
        $this->conexion = new mysqli($this->host, $this->usuario, $this->password, $this->nombreBD);
        if ($this->conexion->connect_error) {
            die("Error al conectar a la base de datos: " . $this->conexion->connect_error);
        }
    }

    public function getConexion() {
        return $this->conexion;
    }
}
?>

// Usando PDO
<?php
class conexionDB {
    private $host = "nombre_del_host"; // Nombre del host de la base de datos (por ejemplo, localhost)
    private $usuario = "nombre_de_usuario"; // Nombre de usuario para acceder a la base de datos
    private $password = "contraseña"; // Contraseña para acceder a la base de datos
    private $nombreBD = "nombre_de_la_base_de_datos"; // Nombre de la base de datos

    private $conexion;

    public function __construct() {
        try {
            $dsn = "mysql:host=$this->host;dbname=$this->nombreBD";
            $this->conexion = new PDO($dsn, $this->usuario, $this->password);
            $this->conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            die("Error al conectar a la base de datos: " . $e->getMessage());
        }
    }

    public function getConexion() {
        return $this->conexion;
    }
}
?>
~~~

Después en el código de 'consulta_series.php' tienes que llamar a este objeto

~~~php
<?php
$conexionDB = new conexionDB();
$conexion = $conexionDB->getConexion();

// A partir de aquí, puedes utilizar el objeto de conexión ($conexion) para realizar consultas y otras operaciones en la base de datos
?>
~~~

### Crea otro archivo llamado 'consultar_series.php' donde recibirás los valores introducidos en el formulario y realiza las consultas necesarias

~~~php

//CON PDO
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
        // Construir y ejecutar la consulta SQL utilizando bindParam
        $sql = "SELECT * FROM Series";
        if (!empty($genero)) {
            $sql .= " WHERE genero = :genero";
        }

        try {
            $consulta = $conexion->prepare($sql);

            if (!empty($genero)) {
                $consulta->bindParam(":genero", $genero);
            }

            $consulta->execute();
            $resultados = $consulta->fetchAll(PDO::FETCH_ASSOC);

            // Almacenar los resultados en la sesión
            $_SESSION['resultados'] = $resultados;

            // Redirigir a la página de resultados
            header("Location: resultados.php");
            exit();
        } catch (PDOException $e) {
            echo "Error en la consulta: " . $e->getMessage();
        }
    }

    // Verificar si se ha pulsado el botón "Mostrar Serie Aleatoria"
    if (isset($_GET["aleatoria"])) {
        try {
            $sql = "SELECT * FROM Series ORDER BY RAND() LIMIT 1";
            $consulta = $conexion->prepare($sql);
            $consulta->execute();
            $serieAleatoria = $consulta->fetch(PDO::FETCH_ASSOC);

            // Almacenar la serie aleatoria en la sesión
            $_SESSION['serieAleatoria'] = $serieAleatoria;

            // Redirigir a la página de serie aleatoria
            header("Location: serie_aleatoria.php");
            exit();
        } catch (PDOException $e) {
            echo "Error en la consulta: " . $e->getMessage();
        }
    }
}
?>

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
~~~

### Serie aleatoria

~~~php
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
~~~

### Preguntas

#### ¿Qué significa PDO::FETCH_ASSOC?

**PDO::FETCH_ASSOC** es una constante utilizada en PHP con la extensión PDO para obtener resultados de consultas SQL en forma de array asociativo. Cada fila del conjunto de resultados se devuelve como un array donde las claves son los nombres de las columnas y los valores son los valores de esas columnas en la fila correspondiente. Esto permite acceder fácilmente a los valores de las columnas utilizando las claves del array asociativo.

#### ¿Qué significa MYSQLI_ASSOC?

**mysqli_assoc()** es un método proporcionado por la extensión mysqli de PHP que se utiliza para obtener una fila de resultados de una consulta SQL en forma de un array asociativo. Cada fila de resultados se devuelve como un array asociativo donde las claves son los nombres de las columnas y los valores son los valores de esas columnas en la fila correspondiente. Esto permite acceder fácilmente a los valores de las columnas utilizando las claves del array asociativo.
