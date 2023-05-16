# Ejercicios propuestos en clase de Dante

## Ejercicio 1. Crea una sencilla aplicación web y un formulario que permita hacer un tablero de ajedrez con las siguientes características

### El formulario debe solicitar el nombre de las columnas, filas o por el contrario ser aleatorio

### El formulario ha de detectar errores en las variables

### El tablero ha de ser entre 4 y 40

### Si las filas y las columnas introducidas son iguales: el color de las casillas ha de ser Blanco y Negro

### Si las filas introducidas son más que las columnas Rojo y Negro

### Si las columnas introducidas son más que las filas Verde y Blanco

### Si la creación es aleatorioa tanto las filas, las columnas y los colores han de ser aleatorios

### Una vez creado el tablero se deben poner 4 peones en 4 casillas pidiendo las coordenadas. Se deben poner de uno en uno demandando en cada petición las coordenadas para un peón (No se puede de repente). Mirar sesiones PHP

~~~php
<!DOCTYPE html>
<html>
<head>
    <title>Tablero de Ajedrez</title>
</head>
<body>
    <?php
    // Función para generar un color aleatorio
    function generarColorAleatorio() {
        $colores = array("Blanco", "Negro", "Rojo", "Verde");
        return $colores[array_rand($colores)];
    }

    // Obtener los valores del formulario
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $filas = $_POST["filas"];
        $columnas = $_POST["columnas"];
        $modoAleatorio = $_POST["aleatorio"];

        // Validar errores en las variables
        if (empty($filas) || empty($columnas)) {
            echo "Por favor, ingresa el número de filas y columnas.";
        } elseif (!is_numeric($filas) || !is_numeric($columnas)) {
            echo "Por favor, ingresa valores numéricos para filas y columnas.";
        } elseif ($filas < 4 || $filas > 40 || $columnas < 4 || $columnas > 40) {
            echo "El número de filas y columnas debe estar entre 4 y 40.";
        } else {
            // Crear el tablero de ajedrez
            echo "<table border='1'>";
            for ($i = 1; $i <= $filas; $i++) {
                echo "<tr>";
                for ($j = 1; $j <= $columnas; $j++) {
                    // Determinar el color de cada casilla
                    if ($modoAleatorio) {
                        $color = generarColorAleatorio();
                    } else {
                        if ($filas == $columnas) {
                            $color = ($i + $j) % 2 == 0 ? "Blanco" : "Negro";
                        } elseif ($filas > $columnas) {
                            $color = $i % 2 == 0 ? "Rojo" : "Negro";
                        } else {
                            $color = $j % 2 == 0 ? "Verde" : "Blanco";
                        }
                    }

                    echo "<td style='background-color: $color;'>($i, $j)</td>";
                }
                echo "</tr>";
            }
            echo "</table>";

            // Solicitar coordenadas para los peones
            echo "<h3>Coloca los peones:</h3>";
            for ($k = 1; $k <= 4; $k++) {
                echo "<form method='post' action=''>";
                echo "Coordenadas para el peón $k: ";
                echo "<input type='text' name='peon$k' required>";
                echo "<input type='submit' value='Guardar'>";
                echo "</form>";
            }
        }
    } else {
        // Mostrar formulario inicial
        echo "<h3>Configuración del tablero:</h3>";
        echo "<form method='post' action=''>";
        echo "Número de filas (4-40): ";
        echo "<input type='number' name='filas' min='4' max='40' required><br>";
        echo "Número de columnas (4-40): ";
        echo "<input type='number' name='columnas' min='4' max='40' required><br>";
        echo "Modo aleatorio: ";
        echo "<input type='checkbox' name='aleatorio'><br>";
        echo "<input type='submit' value='Crear tablero'>";
        echo "</form>";
    }
?>

</body>
</html>
~~~

## Ejercicio 2. Crea una sencilla web en PHP que permita a un usuario comprar un conjunto de frutas. El usuario se logueará y podrá ir comprando frutas hasta que se le agote el dinero o cierre sesion. Las frutas tienen un número de unidades limitado, así que cuando el contador de las frutas llega a 0 ya no se pueden comprar más. Solo el usuario administrator puede insertar usuarios y frutas

### Tabla usuario

- tipos = 0 por usuario
- tipos = 1 por administrador

|usuario|contraseña|dinero|tipo|
|-|-|-|-|

### Tabla frutas

|fruta|unidades|precio|
|-|-|-|

### Se valorará

- Gestión de la sesion (Sesión 'usuario' y 'password')
- Correcta gestion del envío de los parámetros (POST o GET)
- Uso correcto de la base de datos
- Estructuración del código y funciones
- Funcionalidad global

### Registra un hosting gratuito para enviar la aplicación

~~~php
<?php
session_start();

// Datos de conexión a la base de datos
$servername = "localhost";
$username = "tu_usuario";
$password = "tu_contraseña";
$dbname = "nombre_base_de_datos";

// Función para establecer la conexión a la base de datos
function conectarBD() {
    global $servername, $username, $password, $dbname;
    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        die("Error de conexión: " . $conn->connect_error);
    }
    return $conn;
}

// Función para iniciar sesión
function iniciarSesion($usuario, $contrasena) {
    $conn = conectarBD();
    $sql = "SELECT * FROM usuario WHERE usuario = '$usuario' AND contraseña = '$contrasena'";
    $result = $conn->query($sql);

    if ($result->num_rows == 1) {
        $row = $result->fetch_assoc();
        $_SESSION['usuario'] = $row['usuario'];
        $_SESSION['tipo'] = $row['tipo'];
        $_SESSION['dinero'] = $row['dinero'];
        return true;
    } else {
        return false;
    }
}

// Función para obtener el listado de frutas disponibles
function obtenerFrutas() {
    $conn = conectarBD();
    $sql = "SELECT * FROM frutas WHERE unidades > 0";
    $result = $conn->query($sql);
    $frutas = array();

    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $frutas[] = $row;
        }
    }

    return $frutas;
}

// Función para comprar una fruta
function comprarFruta($fruta, $cantidad) {
    $conn = conectarBD();
    $sql = "SELECT * FROM frutas WHERE fruta = '$fruta'";
    $result = $conn->query($sql);

    if ($result->num_rows == 1) {
        $row = $result->fetch_assoc();
        $precio = $row['precio'];
        $unidadesDisponibles = $row['unidades'];

        if ($_SESSION['dinero'] >= $precio * $cantidad && $unidadesDisponibles >= $cantidad) {
            // Actualizar el saldo del usuario y las unidades de la fruta
            $usuario = $_SESSION['usuario'];
            $nuevoDinero = $_SESSION['dinero'] - $precio * $cantidad;
            $nuevasUnidades = $unidadesDisponibles - $cantidad;

            $sqlUsuario = "UPDATE usuario SET dinero = $nuevoDinero WHERE usuario = '$usuario'";
            $sqlFruta = "UPDATE frutas SET unidades = $nuevasUnidades WHERE fruta = '$fruta'";

            if ($conn->query($sqlUsuario) === TRUE && $conn->query($sqlFruta) === TRUE) {
                $_SESSION['dinero'] = $nuevoDinero;
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    } else {
        return false;
    }
}

// Comprobar si el usuario está logueado
function estaLogueado() {
    return isset($_SESSION['usuario']);
}

// Comprobar si el usuario es administrador
function esAdministrador() {
    return $_SESSION['tipo'] == 1;
}

// Comprobar si se ha enviado el formulario de inicio de sesión
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['login'])) {
    $usuario = $_POST['usuario'];
    $contrasena = $_POST['contrasena'];

    if (iniciarSesion($usuario, $contrasena)) {
        echo "Inicio de sesión exitoso.";
    } else {
        echo "Usuario o contraseña incorrectos.";
    }
}

// Comprobar si se ha enviado el formulario de compra de frutas
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['comprar'])) {
    $fruta = $_POST['fruta'];
    $cantidad = $_POST['cantidad'];

    if (comprarFruta($fruta, $cantidad)) {
        echo "Compra realizada con éxito.";
    } else {
        echo "No se pudo realizar la compra. Verifica tu saldo y la disponibilidad de la fruta.";
    }
}

// Mostrar el formulario de inicio de sesión si el usuario no está logueado
if (!estaLogueado()) {
    echo "<h3>Iniciar sesión:</h3>";
    echo "<form method='post' action=''>";
    echo "Usuario: <input type='text' name='usuario' required><br>";
    echo "Contraseña: <input type='password' name='contrasena' required><br>";
    echo "<input type='submit' name='login' value='Iniciar sesión'>";
    echo "</form>";
} else {
    // Mostrar el nombre de usuario y el saldo disponible
    echo "<p>Bienvenido, " . $_SESSION['usuario'] . "</p>";
    echo "<p>Saldo disponible: $" . $_SESSION['dinero'] . "</p>";

    if (esAdministrador()) {
        // Mostrar formulario para insertar frutas (solo para administradores)
        echo "<h3>Insertar fruta:</h3>";
        echo "<form method='post' action=''>";
        echo "Fruta: <input type='text' name='fruta' required><br>";
        echo "Unidades: <input type='number' name='unidades' required><br>";
        echo "Precio: $<input type='number' name='precio' required><br>";
        echo "<input type='submit' name='insertar_fruta' value='Insertar fruta'>";
        echo "</form>";
    }

    // Mostrar el listado de frutas disponibles y formulario para comprar
    $frutas = obtenerFrutas();

    if (!empty($frutas)) {
        echo "<h3>Listado de frutas disponibles:</h3>";
        echo "<table>";
        echo "<tr><th>Fruta</th><th>Unidades</th><th>Precio</th><th>Cantidad</th><th>Comprar</th></tr>";

        foreach ($frutas as $fruta) {
            echo "<form method='post' action=''>";
            echo "<tr>";
            echo "<td>" . $fruta['fruta'] . "</td>";
            echo "<td>" . $fruta['unidades'] . "</td>";
            echo "<td>$" . $fruta['precio'] . "</td>";
            echo "<td><input type='number' name='cantidad' min='1' max='" . $fruta['unidades'] . "'></td>";
            echo "<td><input type='submit' name='comprar' value='Comprar'></td>";
            echo "<input type='hidden' name='fruta' value='" . $fruta['fruta'] . "'>";
            echo "</tr>";
            echo "</form>";
        }
        echo "</table>";
    } else {
        echo "<p>No hay frutas disponibles.</p>";
    }

    // Botón de cierre de sesión
    echo "<br><form method='post' action=''>";
    echo "<input type='submit' name='logout' value='Cerrar sesión'>";
    echo "</form>";

    // Procesar el cierre de sesión
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['logout'])) {
        session_unset();
        session_destroy();
        header("Location: index.php");
        exit;
    }
}

?>
~~~
