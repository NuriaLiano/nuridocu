<?php
class conexionDB {
    private $host = "localhost"; // Nombre del host de la base de datos (por ejemplo, localhost)
    private $usuario = "root"; // Nombre de usuario para acceder a la base de datos
    private $password = ""; // Contraseña para acceder a la base de datos
    private $nombreBD = "series_tv"; // Nombre de la base de datos

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
