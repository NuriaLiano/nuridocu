# Solución al examen del TEMA 5

**Realiza capturas en cada uno de los puntos siguientes nombrándolas con el nº del punto y número de secuencia dentro de él. Por ejemplo, en la pregunta 1 se realizarán capturas con nombre 1-1.png, 1-2.png… Recuerda que las capturas han de ser las suficientes para demostrar qué se ha hecho, cómo se ha hecho y que funciona lo que se haya hecho. Incluye las explicaciones oportunas para aclarar las acciones llevadas a cabo.**

## 1. En la Máquina Virtual para el examen añade 5 discos duros VDI de 10 GiB dinámicos. Utiliza los siguientes nombres: ex1.vdi, ex2.vdi, ex3.vdi, ex4.vdi y ex5.vdi

#### a. Utilizando fdisk y mkfs realiza las siguientes particiones en el primer disco

1. Ver los discos que tenemos para saber el path
   ``sudo fdisk -l``

- Una partición primaria de 3 GiB con formato EXT4.
  1. Crear la particion

    ~~~~
    sudo fdisk /dev/sdb
    n
    p
    Enter
    +3G
    ~~~~

  2. Dar formato a la partición

   ~~~~
   sudo mkfs.ext4 /dev/sdb1
   ~~~~
 
- Una partición primaria de 2 GiB con formato NTFS.
    1. Crear la particion

    ~~~~
    n
    p
    Enter
    +2G
    ~~~~

  2. Dar formato a la partición

   ~~~~
   sudo mkfs.ntfs /dev/sdb2
   ~~~~

**¡CUIDADO!** primero hay que crear una partición extendida para almacenar las particiones lógicas

~~~~
n
e
Enter
Enter
Enter (tamaño por defecto ya que solo quedan 5GB libres)
~~~~

- Una partición lógica de 2 GiB con formato FAT32.

    1. Crear la particion

    ~~~~
    n
    Enter
    +2G
    ~~~~

  1. Dar formato a la partición

   ~~~~
   sudo mkfs.vfat /dev/sdb5
   ~~~~

- Una partición lógica de 1 GiB con formato EXT3.
    1. Crear la particion

    ~~~~
    n
    Enter
    +1G
    ~~~~

  2. Dar formato a la partición

   ~~~~
   sudo mkfs.ext3 /dev/sdb6
   ~~~~

- Una partición lógica de 2 GiB con formato EXT4.
    1. Crear la particion

    ~~~~
    n
    Enter
    +2G
    ~~~~

  2. Dar formato a la partición

   ~~~~
   sudo mkfs.ext4 /dev/sdb7
   ~~~~

#### b. Una vez realizado el proceso realiza una captura de pantalla donde se muestre el resultado del particionamiento con gparted

#### c. Consulta los UUID de las particiones realizadas

``sudo blkid`` o ``ls /dev/disk/by-path``

#### d. Crea dos directorios en el directorio /home/usuario con nombres: DatosLinux y DatosWin. Monta la partición primaria de 3 GiB en el directorio DatosLinux y la partición primaria de 2 GiB en el directorio DatosWin. El montaje se realizará de forma automática al arrancar el equipo

1. Crear directorios
   ~~~~
   mkdir /home/usuario/DatosLinux
   mkdir /home/usuario/DatosWin
   ~~~~
   
2. Montaje automático
    ~~~~
    sudo nano /etc/fstab
    UUID=[UUID_de_la_partición_de_3_GiB] /home/usuario/DatosLinux ext4 defaults 0 2
    UUID=[UUID_de_la_partición_de_2_GiB] /home/usuario/DatosWin ntfs defaults 0 2
    ~~~~

#### e. Crea tres directorios en el directorio /home/usuario con nombres: temp1, temp2 y temp3. Monta temporalmente las particiones lógicas en dichos directorios

1. Crear directorios
   ~~~~
    mkdir /home/usuario/temp1
    mkdir /home/usuario/temp2
    mkdir /home/usuario/temp3
   ~~~~

2. Montar temporalmente (al reiniciar el equipo se desmonta)
   
   ~~~~
    sudo mount /dev/sdb6 /home/usuario/temp1
    sudo mount /dev/sdb5 /home/usuario/temp2
    sudo mount /dev/sdb7 /home/usuario/temp3
   ~~~~

#### f.Utilizando gdisk y mkfs realiza las siguientes particiones

- Una partición de 5 GiB con formato EXT4.
- Una partición de 5 GiB con formato NTFS.
  
#### g.Una vez realizado el proceso realiza una captura de pantalla donde se muestre el resultado del particionamiento con gparted

## 2. Creación de enlaces

#### a. Crea un enlace simbólico (blando) de nombre “enlace_a_etc” al directorio /etc dentro del directorio /home/usuario

``ln -s /etc /home/usuario/enlace_a_etc``

#### b. Crea un enlace duro de nombre passwd al archivo /etc/passwd dentro del directorio /home/usuario

``ln /etc/passwd /home/usuario/passwd``

#### c. Consulta los números de inodo de los enlaces y de los archivos y directorios originales. Explica cuáles son iguales y por qué

``ls -li /etc /home/usuario/enlace_a_etc /etc/passwd /home/usuario/passwd``

Explicación: Los números de inodo para los enlaces simbólicos (enlace_a_etc) y los enlaces duros (passwd) serán diferentes a los números de inodo de los archivos y directorios originales (/etc y /etc/passwd) ya que son diferentes archivos en el sistema de archivos, aunque apunten a los mismos contenidos.

## 3. Gestión de procesos

#### a. Consulta todos los procesos en ejecución en el sistema

``ps aux``

#### b. Lanza en segundo plano el proceso “sleep 300”

``sleep 300 &``

#### c. Consulta su PID y su PPID

PID (identificador de proceso) y el PPID (identificador de proceso padre)
``ps -p <PID> -o pid,ppid``

#### d. Detén el proceso

``kill <PID>``

#### e. Añade 5 puntos a la prioridad respecto a la prioridad que tenga ahora

``renice +5 <PID>``

#### f. Continua el proceso

El número de trabajo es el número que se muestra en corchetes cuando se detiene el proceso con Ctrl + Z.
``fg <job number>``

#### g. Termina el proceso

``kill <PID>``

## 4. Crea un sistema RAID 5 con los 5 discos añadidos a la Máquina Virtual. Dos de los discos se utilizarán de reserva

1. Instalar paquete mdadm
   ``sudo apt-get install mdadm``
2. Ver los discos
   ``sudo fdisk -l``
3. Crear RAID 5
   ``sudo mdadm --create --verbose /dev/md0 --level=5 --raid-devices=5 /dev/sd[b-f]``
   Esto creará un RAID 5 en el dispositivo /dev/md0 utilizando los discos /dev/sdb, /dev/sdc, /dev/sdd, /dev/sde y /dev/sdf.
4. Verificar estado del RAID
   ``cat /proc/mdstat``

#### a. Monta el array en el directorio /home/usuario/DATOS que debe ser creado. El sistema debe ser montado automáticamente al inicio del sistema

1. Crear directorio
   ``mkdir /home/usuario/DATOS``
2. Montar RAID en el directorio
   ``sudo mount /dev/md0 /home/usuario/DATOS``
3. Configurar automontaje del RAID en /etc/fstab
   ``/dev/md0 /home/usuario/DATOS ext4 defaults 0 0``

#### b. Incluye una captura del estado del RAID una vez creado

``sudo mdadm --detail /dev/md0``

## 5. Configura el archivo Crontab para que realice las siguientes tareas

**RECUERDA**: los comandos están configurados para ejecutarse en el huso horario del sistema, por lo que asegúrate de verificar la configuración del huso horario si es necesario para evitar confusiones con la hora de ejecución de los comandos.

1. Abrir crontab
   ``crontab -e``

#### a. Borrado de los archivos localizados en /home/usuario/Backup el día 1 de cada mes a las 23:00

``0 23 1 * * rm -r /home/usuario/Backup/*``

#### b. Realización de un backup normal del directorio /home/usuario/DATOS. El backup debe realizarse los domingos a las 23:59 y debe guardarse en el directorio /home/usuario/Backups con el nombre CT_DATOS_ddmmaa.tar.bz2 (siendo dd día, mm mes y aa año)

``59 23 * * 0 tar -cjf /home/usuario/Backups/CT_DATOS_$(date +\%d\%m\%y).tar.bz2 /home/usuario/DATOS``

#### c. Realización de un backup diferencial del directorio /home/usuario/DATOS. El backup debe realizarse de lunes a viernes a las 23:59 y debe guardarse en el directorio /home/usuario/Backups con el nombre CI_DATOS_ddmmaa.tar.bz2

``59 23 * * 1-5 tar -cjf /home/usuario/Backups/CI_DATOS_$(date +\%d\%m\%y).tar.bz2 -g /home/usuario/Backups/backup.snap /home/usuario/DATOS``
