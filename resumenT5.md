# TEMA 5

**IMPORTANTE**
- Si tienes dudas con cualquier comando puedes ejecutar antes: ``comando --help``
    Ej: chown --help
- Intenta usar rutas absolutas, si no te dicen lo contrario, para que no pierdas el hilo de donde estas y a donde quieres ir. 
    Ej: nano /home/usuario/fichero
- Rutas absolutas: tienes que escribir la ruta completa desde raíz (/)
- Rutas relativas: escribes la ruta desde el directorio donde estás
- ~: indica el home del usuario, es lo mismo que poner /home/nombreusuario
- ./: el directorio en el que estás.
- PWD: comando para comprobar en que directorio estoy
- La ruta **/dev/sda/** siempre es la del disco donde está el sistema. NO TOCAR NADA

## Gestión de discos duros

- Path de los discos duros
  - SATA: ``/dev/sda``
  - NVME: ``/dev/nvme1``
- Path de las particiones 
  - SATA: ``/dev/sda1``
  - NVME: ``/dev/nvme0p1``
- Tablas de particiones:
  - MBR: bastante obsoleta
  - GPT: es la que se usa ahora, no tiene limitaciones
- Pasos a la hora de montar y particionar un disco
  - Introducir el disco 
  - Establecer la tabla de particiones GPT: ``fdisk /dev/sdb``
  - Particionar el disco
Estos pasos los podemos realizar con la herramienta **gparted** o bien de forma independiente. 

Todas las aplicaciones que puedes instalar en GNU/Linux están almacenadas en repositorios externos al Sistema Operativo. 
Estos repositorios se pueden agregar para disponer de las distintas aplicaciones que contienen. 

Una forma de instalar nuevos repositorios es: ``add-apt-repository urlrepo``

Manejo de aplicaciones en Debian y derivados: 
- Instalar: ``apt install nombrepaquete```
- Actualizar o reinstalar: ``apt upgrade nombrepaquete``
- Eliminar aplicacion **manteniendo archivos de configuracion y/o datos**: ``apt remove nombrepaquete``
- Desinstalar por completo **se borran todos los datos de la aplicación**: ``apt purge nombrepequete``

También existe la posibilidad de descargar los paquetes desde internet de igual forma que lo hacemos en Windows.
- Instalar: ``dpkg -i nombrepaquete.deb``
- Desinstalar: ``dpkg -P nombrepaquete.deb``

## Comprimir y descomprimir ficheros y directorios
**Importante**
Usa el mismo orden que aparece aqui para establecer los parámetros. Esto es por que cada parámetro sirve para una función distinta. Por ejemplo: el parámetro **-f** se usa para específicar el directorio o la ubicación del archivo, por ese motivo tiene que ir delante de la ruta. 
Parámetros:
    - c: crea un archivo con el nombre que has establecido para el paquete
    - z: representa la compresión **gzip**
    - v: verbose. muestra todo el proceso
    - f: ubicación del fichero
    - 9: mejor compresion
### .TAR.GZ
- Comprimir: ``tar -czvf nombrepaquete.tar.gz pathficheroacomprimir``
  - Ej: ``tar -czvf descargas_comprimido.tar.gz /home/usuario/Descargas``
- Descomprimir ``tar -xzvf nombrepaquete.tar.gz``
  - Ej: ``tar -xzvf descargas_comprimido.tar.gz``
### .TAR
- Comprimir: ``tar -cvf nombrepaquete.tar pathficheroacomprimir``
  - Ej: ``tar -cvf descargas_comprimido.tar /home/usuario/Descargas``
- Descomprimir ``tar -xvf nombrepaquete.tar``
  - Ej: ``tar -xvf descargas_comprimido.tar``
- Descomprimir en ruta específica: ``tar -xvf nombrepaquete.tar -C pathdestino``
  - Ej: ``tar -xvf descargas_comprimido.tar -C /home/usuario/destino/``
### .GZ
- Comprimir: ``gzip -9 pathficheroacomprimir``
  - Ej: ``gzip -9 /home/usuario/Descargas/ficherito``
- Descomprimir ``gzip -d nombrepaquete.gz``
  - Ej: ``gzip -d ficherito.gz``
### .ZIP
- Comprimir: ``zip nombrepaquete.zip pathficheroacomprimir``
  - Ej: ``zip descargas_comprimido.zip /home/usuario/Descargas/``
- Descomprimir ``unzip descargas_comprimido.zip``
  - Ej: ``unzip descargas_comprimido.zip``

## Gestión de usuarios y grupos

- Crear usuarios
  - **ADDUSER** Forma "sencilla"
    Con este comando se ejecutará un script el cual te irá preguntando datos para crear el usuario. Establece parámetros por defecto pero puedes editarlo si se lo indicas con parámetros
        - Creación simple: ``useradd usuariochuli``
        - Creación modificando parámetros: ``useradd --shell '/usr/bin/python3' usuariochuli``
        **RECUERDA** puedes consultar todos los parámetros que puedes modificar con: ``useradd --help``
    Una vez que has creado el usuario debes copiar el contenido del directorio ``/etc/skel/`` en el directorio del usuario creado y cambiar el propietario para que sea el usuario creado:
      - sudo cp /etc/skel/.bash* /home/usuariochuli/
      - sudo chown -R usuariochuli:usuariochuli /etc/usuariochuli/
  - **USERADD** Forma más compleja
    Con este comando tienes que establecer, mediante parámetros, toda la información obligatoria del usuario, como el directorio home, el grupo primario, el interprete de comando que utilizará, etc.. 
        ``useradd -d /home/usuariodos -m -g usuariodos -p contrasena123 -s '/bin/bash' ``
- Modificar usuario
    ``usermod -d '/home/nuevohome usuariochuli``
- Eliminar usuario
  De igual forma que para crear usuarios hay dos comandos similares, para eliminarlos también
  - **USERDEL** 
    Borra el usuario
    ``userdel usuariochuli``
  - **DELUSER**
    Elimina el usuario pero no el directorio personal, ni otros directorios del usuario
    ``deluser usuariochuli``
- Añadir grupo
    ``groupadd grupillo``
- Modificar grupo
  Puedes modificar las características como GID, password, nombre, etc. Recuerda mirar que parámetros puedes aplicar con **--help**
  ```groupmod -g 15000 grupillo``
- Eliminar grupo
  No puedes borrar un grupo que sea el grupo principal de un usuario, primero tienes que eliminar el usuario o asociarle a otro grupo
  ``groupdel grupillo``
- Contraseñas
  - Cambiar la contraseña de un usuario: ``passwd usuariodos``
  - Forzar que el usuario cambie la contraseña cuando inicie sesión: ``passwd -e usuariodos``
  - Desactivar la contraseña: ``passwd -d usuariodos`` 
  - Establecer limite de renovación de contraseña: ``passwd -n 31 usuariodos
- Cambiar grupo principal de usuarios y contraseñas
  ``gpasswd -a usuariodos grupillo``
- Cambiar el shell (interprete de comandos) asociado a un usuario
  ``chsh -s '/usr/bin/python3' usuario2
- Cambiar el grupo principal de un usuario de forma temporal
  ``newgrp nuevogrupotemp``

## Tuberías y redirecciones
**IMPORTANTE**
- '>': se usa para almacenar la información en otro fichero. SOBREESCRIBE LO QUE YA EXISTA EN EL FICHERO
- '>>': se usa para almacenar la información en otro fichero. AÑADE AL FINAL DEL FICHERO LO QUE INDIQUEMOS. NO SOBREESCRIBE

- Redireccionar salida y error
  Es útil para redireccionar la salida de otro comando. Por ejemplo: ``cat /etc/passwd > ficherousuarios``

  Redireccionar errores estandar: ``aplicacionaejecutar 2 > &1``
  - 2: error estandar
  - &1: salida estandar
- Redireccionar entradas
  Util cuando en una aplicación tenemos que pasar parámetros, de esta forma podemos almacenarlos en un fichero
  ``cat < fichero``
- Tuberías
  Permiten enviar la salida estandar de un comando como inicio de otro comando. Por ejemplo: mostrar los procesos y ordenarlos de mayor a menor
  ``ps -a | sort`` 
  - SORT: ordena a partir de unos critérios
    ``sort fichero``
  - GREP: imprime las lineas donde encuentra el patrón
    `` grep filtro fichero`` 
  - CUT: trocea una cadena
    ``cut -d " " -f2 fichero``
  - TR: sustituye caracteres o elimina los repetidos
    ``tr '/t' " "`` -> sustituye las tab por espacios
 
    





