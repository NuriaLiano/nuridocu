# Prueba de examen 01

## Instrucciones

- Escribe las ordenes necesarias para realizar las tareas en Bash
- Debes escribir una orden en cada caso, a no ser que se indique lo contrario
- Añade un disco duro virtual de 10GB a tu máquina
- Añade 5 discos duros virtuales de 10GB a tu máquina. Se utilizarán para un raid
- Utiliza rutas relativas, a no ser que se indique lo contrario

## 1. Muestra el contenido de tu directorio activo

## 2. Crea una directorio 'SCRIPTS_exa' en tu home

## 3. Utiliza el directorio que acabas de crear como directorio activo para el examen

## 4. Crea un script 'auto_usuarios.sh' para automatizar la creación de cuenta de usuarios y grupos. El script tendra que validar si en el fichero de autenticación de fichero de Linux existe el usuario y tiene los parámetros correctos que recogerá por parámetro al ejecutar el script

- Si el usuario existe
  - pedir el grupo. NO existe
    - bucle de pedir grupo hasta acertar
      - mostrar mensaje
  - pedir grupo existe
    - mostrar mensaje
- Si el usuario no existe
  - pedir todos los parametros para crear home, grupo y usuario
  - crear mkdir home del usuario
  - crear grupo
  - crear usuario
  - añadir username y fecha de creacion a un fichero usu_creados
  - mensaje donde se vea el usuario, la contraseña por defecto y un aviso de que se va a pedir cambia al iniciar.

>:black_joker: **PISTA** deberás usar el comando useradd

## 5. Crea estas particiones y formatos en el primer disco extra

- primaria 3gb ext4
- primaria 2gb ntfs
- logica 2 gb fat32
- logica 1gb ext3
- logica 2 ext4

## 6. Crea un directorio 'mnt_1' en tu home y monta, de forma automática usando UUID, la primera partición (3GB) del primer disco extra

## 7. Crea un enlace que haga referencia llamada 'enlace_documentos' a la ruta del directorio 'Documentos' al 'Escritorio' de tu usuario

### ¿Que tipo de enlace es?

## 8. Lanza un proceso en segundo plano usando el comando 'sleep'

## 9. Muestra el PID de ese proceso

## 10. Si no ha terminado matale, si ha terminado muestra solo la instrucción que harias

## 11. Crea un sistema RAID 5 con los 5 discos añadidos. 2 serán de reserva

### Muestra el estado del RAID

## 12. Crea una tarea programada que elimine el contenido del directorio 'Descargas' de tu usuario el día 1 de cada mes a las 23:00

## 13. Realiza un backup normal del directorio /home/usuario/DATOS. El backup debe realizarse los domingos a las 23:59 y debe guardarse en el directorio /home/usuario/Backups con el nombre CT_DATOS_ddmmaa.tar.bz2 (siendo dd día, mm mes y aa año)

>:pencil: **NOTA** los comandos están configurados para ejecutarse en el huso horario del sistema, por lo que asegúrate de verificar la configuración del huso horario si es necesario para evitar confusiones con la hora de ejecución de los comandos

## 14. Realiza un backup diferencial del directorio /home/usuario/DATOS. El backup debe realizarse de lunes a viernes a las 23:59 y debe guardarse en el directorio /home/usuario/Backups con el nombre CI_DATOS_ddmmaa.tar.bz2

>:pencil: **NOTA** los comandos están configurados para ejecutarse en el huso horario del sistema, por lo que asegúrate de verificar la configuración del huso horario si es necesario para evitar confusiones con la hora de ejecución de los comandos

## 15. Crea un script 'lanzador_de_videojuegos.sh' dentro del directorio 'SCRIPTS_exa' contendrá dos juegos que también realizarás en el propio script

### Juego 1 'randomNumber'

La idea del juego es adivinar un número aleatorio que la computadora haya generado. Para ello, el usuario tendrá que ingresar un número y la computadora le dirá si es demasiado alto, demasiado bajo o correcto

Requisitos:

- Definir un contador de intentos
- Leer la respuesta por teclado
- Si el usuario acierta
  - mensaje '¡Felicidades! Adivinaste el número en [poner el numero de intentos] intentos'
- Si el usuario no acierta
  ejecutar en bucle hasta que el usuario acierte
  - Aumenta el contador
  - si el numero es más alto
    - mensaje '¡Muy alto! Intenta de nuevo'
  - si el numero es demasiado bajo
    - mensaje '¡Muy bajo! Intenta de nuevo'

### Juego 2 'piedra, papel o tijera'

En este juego, el jugador 1 elige una opción (piedra, papel o tijera), y el jugador 2 es el ordenador, que elige aleatoriamente una opción. Luego se muestra el resultado del juego.

Requisitos:

- Función que muestra las opciones para que el usuario elija
- Función que muestra el resultado del juego
- Verificar que la opción del jugador 1 es válida
- Generar la opción del jugador 2
- Mostrar la opción del jugador 2
- Mostrar el resultado
