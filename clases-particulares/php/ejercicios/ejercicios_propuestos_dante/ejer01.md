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
