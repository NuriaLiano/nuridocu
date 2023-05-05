# Prueba de examen 01

## Instrucciones

- Escribe las ordenes necesarias para realizar las tareas en Bash
- Debes escribir una orden en cada caso, a no ser que se indique lo contrario
- Añade un disco duro virtual de 10GB a tu máquina
- Añade 5 discos duros virtuales de 10GB a tu máquina. Se utilizarán para un raid
- Utiliza rutas relativas, a no ser que se indique lo contrario

## 1. Muestra el contenido de tu directorio activo

~~~bash
ls ./
~~~

## 2. Crea una directorio 'SCRIPTS_exa' en tu home

~~~bash
mkdir ~/SCRIPTS_exa
~~~

## 3. Utiliza el directorio que acabas de crear como directorio activo para el examen

~~~bash
cd ~/SCRIPTS_exa
~~~

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

~~~bash
#!/bin/bash

# Validar que se ha pasado el nombre de usuario como argumento
if [ $# -lt 1 ]; then
  echo "Debe indicar el nombre del usuario a crear."
  exit 1
fi

# Comprobar si el usuario existe
if id "$1" >/dev/null 2>&1; then
  echo "El usuario $1 ya existe."
  # Pedir el nombre del grupo
  read -p "Introduzca el nombre del grupo: " group_name
  # Comprobar si el grupo existe
  if ! getent group "$group_name" >/dev/null 2>&1; then
    echo "El grupo $group_name no existe."
    # Bucle para pedir el nombre del grupo hasta que exista
    while true; do
      read -p "Introduzca un grupo válido: " group_name
      if getent group "$group_name" >/dev/null 2>&1; then
        break
      fi
      echo "El grupo $group_name no existe."
    done
  else
    echo "El grupo $group_name existe."
  fi
else
  echo "El usuario $1 no existe."
  # Pedir los parámetros para crear la cuenta de usuario y grupo
  read -p "Introduzca el nombre del grupo: " group_name
  read -p "Introduzca el nombre completo del usuario: " full_name
  read -p "Introduzca la contraseña del usuario: " password
  # Crear el directorio home del usuario
  mkdir "/home/$1"
  # Crear el grupo
  groupadd "$group_name"
  # Crear el usuario
  useradd -c "$full_name" -m -g "$group_name" -s /bin/bash "$1"
  # Cambiar la contraseña del usuario
  echo -e "$password\n$password" | passwd "$1"
  # Añadir el usuario y la fecha de creación a un archivo usu_creados
  echo "$(date +%F) - $1" >> usu_creados.txt
  echo "La cuenta de usuario $1 ha sido creada correctamente."
  echo "La contraseña por defecto es $password. Deberá cambiarla en su primer inicio de sesión."
fi
~~~

## 5. Crea estas particiones y formatos en el primer disco extra

- primaria 3gb ext4
- primaria 2gb ntfs
- logica 2 gb fat32
- logica 1gb ext3
- logica 2 ext4

>:warning: **¡CUIDADO!** primero hay que crear una partición extendida para almacenar las particiones lógicas

~~~bash
#Ver los discos que tenemos para saber el path
sudo fdisk -l

#Una partición primaria de 3 GiB con formato EXT4.
  #Crear la particion
    sudo fdisk /dev/sdb
    n
    p
    Enter
    +3G

  #Dar formato a la partición
   sudo mkfs.ext4 /dev/sdb1
 
#Una partición primaria de 2 GiB con formato NTFS.
    #Crear la particion
    n
    p
    Enter
    +2G

  #Dar formato a la partición
  sudo mkfs.ntfs /dev/sdb2

#una particion extendida para contener las logicas
n
e
Enter
Enter
Enter (tamaño por defecto ya que solo quedan 5GB libres)

#Una partición lógica de 2 GiB con formato FAT32.

    #Crear la particion
    n
    Enter
    +2G

  #Dar formato a la partición
   sudo mkfs.vfat /dev/sdb5

#Una partición lógica de 1 GiB con formato EXT3.
    #Crear la particion
    n
    Enter
    +1G

  #Dar formato a la partición
   sudo mkfs.ext3 /dev/sdb6

#Una partición lógica de 2 GiB con formato EXT4.
    #Crear la particion
    n
    Enter
    +2G

  #Dar formato a la partición
   sudo mkfs.ext4 /dev/sdb7
~~~

## 6. Crea un directorio 'mnt_1' en tu home y monta, de forma automática usando UUID, la primera partición (3GB) del primer disco extra

~~~bash
#crear el directorio
mkdir ~/mnt_1

#montar de forma automática
sudo nano /etc/fstab
UUID=[UUID_de_la_partición_de_3_GiB] /home/usuario/mnt_1 ext4 defaults 0 2
~~~

## 7. Crea un enlace que haga referencia llamada 'enlace_documentos' a la ruta del directorio 'Documentos' al 'Escritorio' de tu usuario

~~~bash
ln -s ~/Documentos ~/Escritorio/enlace_documentos
~~~

### ¿Que tipo de enlace es?

Simbólico

## 8. Lanza un proceso en segundo plano usando el comando 'sleep'

~~~bash
sleep 300 &
~~~

## 9. Muestra el PID de ese proceso

~~~bash
ps aux
~~~

## 10. Si no ha terminado matale, si ha terminado muestra solo la instrucción que harias

~~~bash
kill <PID>
~~~

## 11. Crea un sistema RAID 5 con los 5 discos añadidos. 2 serán de reserva

~~~bash
#instalar mdadm
sudo apt-get install mdadm
#ver los discos
sudo fdisk -l
#crear raid5
sudo mdadm --create --verbose /dev/md0 --level=5 --raid-devices=5 /dev/sd[b-f]
#verificar el estado
cat /proc/mdstat
~~~

### Muestra el estado del RAID

~~~bash
cat /proc/mdstat
~~~

## 12. Crea una tarea programada que elimine el contenido del directorio 'Descargas' de tu usuario el día 1 de cada mes a las 23:00

~~~bash
0 23 1 * * rm -r /home/usuario/Descargas/*
~~~

## 13. Realiza un backup normal del directorio /home/usuario/DATOS. El backup debe realizarse los domingos a las 23:59 y debe guardarse en el directorio /home/usuario/Backups con el nombre CT_DATOS_ddmmaa.tar.bz2 (siendo dd día, mm mes y aa año)

>:pencil: **NOTA** los comandos están configurados para ejecutarse en el huso horario del sistema, por lo que asegúrate de verificar la configuración del huso horario si es necesario para evitar confusiones con la hora de ejecución de los comandos

~~~bash
59 23 * * 0 tar -cjf /home/usuario/Backups/CT_DATOS_$(date +\%d\%m\%y).tar.bz2 /home/usuario/DATOS
~~~

## 14. Realiza un backup diferencial del directorio /home/usuario/DATOS. El backup debe realizarse de lunes a viernes a las 23:59 y debe guardarse en el directorio /home/usuario/Backups con el nombre CI_DATOS_ddmmaa.tar.bz2

>:pencil: **NOTA** los comandos están configurados para ejecutarse en el huso horario del sistema, por lo que asegúrate de verificar la configuración del huso horario si es necesario para evitar confusiones con la hora de ejecución de los comandos

~~~bash
59 23 * * 1-5 tar -cjf /home/usuario/Backups/CI_DATOS_$(date +\%d\%m\%y).tar.bz2 -g /home/usuario/Backups/backup.snap /home/usuario/DATOS
~~~

## 15. Crea un script 'lanzador_de_videojuegos.sh' dentro del directorio 'SCRIPTS_exa' contendrá dos juegos que también realizarás en el propio script

~~~bash
#!/bin/bash

echo "Bienvenido al Lanzador de videojuegos"
echo "Elige un juego:"
echo "1. Adivinar el número"
echo "2. Piedra, papel o tijera"

read opcion

case $opcion in
  1)
    # Juego de adivinar el número
    echo "Adivina el número entre 1 y 100"
    numero=$((RANDOM%100+1))
    intentos=0
    while true
    do
      read guess
      if [[ $guess -eq $numero ]]
      then
        echo "¡Felicidades, adivinaste el número en $intentos intentos!"
        break
      elif [[ $guess -lt $numero ]]
      then
        echo "El número es más grande"
      else
        echo "El número es más pequeño"
      fi
      intentos=$((intentos+1))
    done
    ;;
  2)
    # Juego de piedra, papel o tijera
    echo "Elige una opción:"
    echo "1. Piedra"
    echo "2. Papel"
    echo "3. Tijera"

    read opcion_jugador_1

    if [[ $opcion_jugador_1 -lt 1 || $opcion_jugador_1 -gt 3 ]]
    then
      echo "Opción inválida"
      exit 1
    fi

    opcion_jugador_2=$((RANDOM%3+1))

    echo "El jugador 2 elige:"
    case $opcion_jugador_2 in
      1) echo "Piedra";;
      2) echo "Papel";;
      3) echo "Tijera";;
    esac

    echo "Resultado:"
    case $opcion_jugador_1 in
      1)
        case $opcion_jugador_2 in
          1) echo "Empate";;
          2) echo "Gana el jugador 2";;
          3) echo "Gana el jugador 1";;
        esac
        ;;
      2)
        case $opcion_jugador_2 in
          1) echo "Gana el jugador 1";;
          2) echo "Empate";;
          3) echo "Gana el jugador 2";;
        esac
        ;;
      3)
        case $opcion_jugador_2 in
          1) echo "Gana el jugador 2";;
          2) echo "Gana el jugador 1";;
          3) echo "Empate";;
        esac
        ;;
    esac
    ;;
  *)
    echo "Opción inválida"
    exit 1
    ;;
esac
~~~

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

~~~bash
#!/bin/bash

# Generar un número aleatorio entre 1 y 100
num=$((RANDOM % 100 + 1))

# Definir un contador para el número de intentos
count=0

# Pedir al usuario que adivine el número
echo "¡Bienvenido al juego de adivinanza! Adivina el número que estoy pensando entre 1 y 100"

# Leer la respuesta del usuario
read guess

# Mientras la respuesta del usuario sea incorrecta
while [[ $guess -ne $num ]]
do
    # Aumentar el contador de intentos
    count=$((count+1))

    # Si el número es demasiado alto
    if [[ $guess -gt $num ]]
    then
        echo "¡Muy alto! Intenta de nuevo"
    fi

    # Si el número es demasiado bajo
    if [[ $guess -lt $num ]]
    then
        echo "¡Muy bajo! Intenta de nuevo"
    fi

    # Leer la respuesta del usuario de nuevo
    read guess
done

# Si el usuario ha adivinado el número
echo "¡Felicidades! Adivinaste el número en $count intentos"
~~~

### Juego 2 'piedra, papel o tijera'

En este juego, el jugador 1 elige una opción (piedra, papel o tijera), y el jugador 2 es el ordenador, que elige aleatoriamente una opción. Luego se muestra el resultado del juego.

Requisitos:

- Función que muestra las opciones para que el usuario elija
- Función que muestra el resultado del juego
- Verificar que la opción del jugador 1 es válida
- Generar la opción del jugador 2
- Mostrar la opción del jugador 2
- Mostrar el resultado

~~~bash
#!/bin/bash

# Función que muestra las opciones para que el usuario elija
mostrar_opciones() {
  echo "Elige una opción:"
  echo "1. Piedra"
  echo "2. Papel"
  echo "3. Tijera"
}

# Función que muestra el resultado del juego
mostrar_resultado() {
  case $1 in
    1)
      case $2 in
        1) echo "Empate";;
        2) echo "Gana el jugador 2";;
        3) echo "Gana el jugador 1";;
      esac
      ;;
    2)
      case $2 in
        1) echo "Gana el jugador 1";;
        2) echo "Empate";;
        3) echo "Gana el jugador 2";;
      esac
      ;;
    3)
      case $2 in
        1) echo "Gana el jugador 2";;
        2) echo "Gana el jugador 1";;
        3) echo "Empate";;
      esac
      ;;
  esac
}

# Mostrar las opciones
mostrar_opciones

# Leer la opción del jugador 1
read opcion_jugador_1

# Verificar que la opción del jugador 1 es válida
if [[ $opcion_jugador_1 -lt 1 || $opcion_jugador_1 -gt 3 ]]
then
  echo "Opción inválida"
  exit 1
fi

# Generar la opción del jugador 2
opcion_jugador_2=$((RANDOM%3+1))

# Mostrar la opción del jugador 2
echo "El jugador 2 elige:"
case $opcion_jugador_2 in
  1) echo "Piedra";;
  2) echo "Papel";;
  3) echo "Tijera";;
esac

# Mostrar el resultado
echo "Resultado:"
mostrar_resultado $opcion_jugador_1 $opcion_jugador_2
~~~
