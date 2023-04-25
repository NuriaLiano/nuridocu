---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---
# COMANDOS CMD

## Moverse por los directorios

>:pencil:**NOTA** las rutas pueden ser absolutas (indicando todas las carpetas por las que va a pasar desde raiz) o relativas (las carpetas por las que hay que pasar desde el directorio activo)
>:pencil:**NOTA** el directorio padre del directorio activo se representa mediante '..'

### CD

"Change Directory" (Cambiar Directorio) en CMD, y se utiliza para cambiar el directorio actual en el que se está trabajando.

~~~cmd
--ruta relativa 
cd Documentos

-- ruta absoluta
cd C:\Users\Usuario\Documentos
~~~

### DIR

"Directory" (Directorio) en CMD, y se utiliza para listar los archivos y carpetas en el directorio actual.

~~~cmd
dir C:\Users\Usuario\Documentos
~~~

#### Opciones

- '/A': permite restringir la lista a los elementos que tengan los atributos indicados (o mostrar todos si no se indica nada, incluidos los ocultos).
- '/B': muestra únicamente los nombres.
- '/O': permite especificar el orden en que se mostrarán los archivos.
- '/P': pausa la muestra cada vez que se visualiza una pantalla completa.
- '/S': también muestra el contenido de los subdirectorios.
- '/T': para indicar qué fecha se mostrará.

### TREE

Muestra una vista en forma de árbol de la estructura de carpetas y subcarpetas en el directorio actual, lo que puede ayudar a visualizar la jerarquía de archivos y carpetas de un directorio.

~~~cmd
tree C:\Users\Usuario\Documentos
~~~

## Operaciones básicas sobre carpetas

### MD

"Make Directory" (Crear Directorio) en CMD, y se utiliza para crear una nueva carpeta en el directorio actual o en una ubicación específica.

>:pencil:**NOTA** también crea las carpetas intermedias indicadas en la ruta si no existen

~~~cmd
md C:\Users\Usuario\Documentos\nueva_carpeta
~~~

#### Opciones

- '/V': Muestra información detallada sobre el proceso de creación de la carpeta
- '/P': Crea el directorio padre si este no existe

### RM

No es un comando nativo de CMD, sino que es un alias para el comando "del" (Delete) que se utiliza para eliminar archivos o carpetas en el directorio actual o en una ubicación específica.

~~~cmd
rm C:\Users\Usuario\Documentos\carpeta_borrador
~~~

#### Opciones

- '/q': Elimina el directorio sin pedir confirmación.
- '/s': Elimina el directorio y su contenido (subcarpetas y archivos).
- '/v': Muestra información detallada sobre el proceso de eliminación de la carpeta

### PUSHD

Se utiliza para cambiar la ubicación actual del directorio y para guardar la ruta actual en una pila.

~~~cmd
PUSHD C:\Windows
~~~

### POPD

se utiliza para cambiar la ubicación actual del directorio a la última ruta guardada en la pila.

~~~cmd
POPD
~~~

## Operaciones básicas sobre archivos

### REN

"Rename" (renombrar) en CMD, y se utiliza para cambiar el nombre de un archivo o carpeta en el directorio actual o en una ubicación específica.

~~~cmd
ren C:\Users\Usuario\Documentos\ficherito.txt C:\Users\Usuario\Documentos\ficheritos_renombrado.txt 
~~~

#### Opciones

- '/V': Muestra información detallada sobre el proceso de copia.
- '/y': No pide confirmación para sobrescribir un archivo existente con el mismo nombre.

### COPY

Se utiliza para copiar archivos de una ubicación a otra, ya sea en la misma unidad de disco o en una unidad de disco diferente.

>:pencil:**NOTA** si se copia una capeta, solo se copia el contenido de esta, no la carpeta en sí

~~~cmd
copy C:\Users\Usuario\Documentos\fich.txt C:\Users\Usuario\Escritorio\fich.txt 
~~~

#### Opciones

- '/V': Muestra información detallada sobre el proceso de copia.
- '/y': No pide confirmación para sobrescribir un archivo existente con el mismo nombre.
- '/z': Copia archivos de manera asíncrona para una mejor recuperación en caso de fallo en la copia.
- '/r': Copia archivos de forma recursiva, incluyendo subdirectorios y archivos ocultos.
- '/a': Copia archivos con atributos de sólo lectura, ocultos y de sistema.

### MOVE

Se utiliza para mover archivos o carpetas de una ubicación a otra, ya sea en la misma unidad de disco o en una unidad de disco diferente.

~~~cmd
move C:\Users\Usuario\Documentos\fich_mover.txt C:\Users\Usuario\fich_mover.txt
~~~

#### Opciones

- /y: No pide confirmación para sobrescribir un archivo existente con el mismo nombre.
- /v: Muestra información detallada sobre el proceso de movimiento.
- /z: Mueve archivos de manera asíncrona para una mejor recuperación en caso de fallo en el movimiento.
- /u: Mueve sólo los archivos que sean más nuevos que los archivos existentes en la ubicación destino.

### ATTRIB

se utiliza para visualizar o modificar los atributos de un archivo o carpeta, como su estado de sólo lectura, oculto, de sistema, entre otros.

~~~cmd
md C:\Users\Usuario\Documentos\nueva_carpeta
~~~

#### Opciones

- +h: Atribuye el atributo de "oculto" a un archivo o carpeta.
- -h: Quita el atributo de "oculto" a un archivo o carpeta.
- +s: Atribuye el atributo de "sistema" a un archivo o carpeta.
- -s: Quita el atributo de "sistema" a un archivo o carpeta.
- +r: Atribuye el atributo de "sólo lectura" a un archivo o carpeta.
- -r: Quita el atributo de "sólo lectura" a un archivo o carpeta.
- /d: Procesa las carpetas también, no sólo los archivos.
- /s: Procesa los archivos y subcarpetas en modo recursivo.
- /l: Muestra la información en forma de lista, en lugar de mostrar en formato tabla.

### DEL

Delete" (eliminar) en CMD, y se utiliza para eliminar uno o más archivos en el directorio actual o en una ubicación específica.

~~~cmd
del C:\Users\Usuario\Documentos\nueva_carpeta
~~~

#### Opciones

- /p: Pide confirmación antes de eliminar cada archivo.
- /q: Suprime los mensajes de confirmación antes de eliminar cada archivo.
- /s: Elimina archivos de manera recursiva en el directorio actual y todos sus subdirectorios.
- /f: Fuerza la eliminación de los archivos sin solicitar confirmación.
  
### TYPE

Se utiliza para mostrar el contenido de un archivo de texto en la pantalla.

~~~cmd
type C:\Users\Usuario\Documentos\fich.txt
~~~

#### Opciones

- /a: Utiliza el formato ASCII en lugar del formato ANSI para mostrar el contenido del archivo.
- /e: Imprime el carácter de fin de archivo (EOF) después de mostrar el contenido del archivo.
- /n: Muestra el número de línea antes de cada línea de texto.

### ASSOC

se utiliza para mostrar o cambiar la asociación de tipos de archivo con las extensiones de archivo correspondientes.

~~~cmd
assoc .txt
~~~

### FC

se utiliza para comparar el contenido de dos archivos.

~~~cmd
fc archivo1.txt archivo2.txt
~~~

### FTYPE

se utiliza para establecer qué programa se abrirá para un tipo de archivo en particular.

~~~cmd
ftype txtfile=%SystemRoot%\system32\NOTEPAD.EXE %1
~~~

los archivos ".txt" se abran con el Bloc de notas

### MKLINK

se utiliza para crear enlaces simbólicos a archivos o directorios.

~~~cmd
mklink /D C:\Users\Juan\Documentos D:\Documentos
~~~

### OPENFILES

se utiliza para mostrar los archivos que están abiertos en una estación de trabajo.

- /local <on|off>: especifica si se deben mostrar los archivos abiertos en el equipo local.

~~~cmd
openfiles /local on
~~~

### PRINT

Se utiliza para imprimir el contenido de un archivo.

~~~cmd
print documento.txt
~~~

### ROBOCOPY

Se utiliza para copiar el contenido de un directorio en otro, y solo copia los archivos que hayan sido modificados o añadidos.

- /E: copia directorios vacíos y subdirectorios, incluyendo los vacíos.
- /MIR: copia directorios vacíos y subdirector

~~~cmd
robocopy C:\Usuarios\ D:\nuevosUsuarios /E
~~~

### WHERE

es utilizado para buscar archivos en el sistema. Este comando busca el nombre de archivo especificado en los directorios del sistema y muestra la ubicación del archivo si es encontrado.

-/r: especifica el directorio raíz a partir del cual se realizará la búsqueda.

~~~cmd
where /r C:\Windows notepad.exe
~~~


## Operadores de redirección

### Redirección de la salida

">": Redirige la salida de un comando a un archivo. Si el archivo no existe, se crea; si existe, se sobrescribe.
">>": Añade la salida de un comando a un archivo existente. Si el archivo no existe, se crea.

>:pencil:**NOTA** si regirigimos la salida a NULL es para que aparezca el resultado por pantalla

~~~bash
dir > lista.txt
echo %date% >> registro.txt
~~~

Podemos indicar donde queremos almacenar los errores que genere un comando

~~~bash
mi_comando > salida.txt 2> errores.txt
~~~

### Redirección de la entrada

"<": Redirige la entrada de un comando desde un archivo.

Se suelen usar los siguientes comandos

- MORE: muestra un archivo por partes (pantalla a pantalla).
- SORT: ordena el contenido de un fichero.
- FIND: busca una cadena de texto en uno o varios archivos.

~~~bash
mi_comando < entrada.txt > salida.txt
~~~

>:warning:**ADVERTENCIA** La acción del comando sobre el fichero únicamente es mostrada en la pantalla, pero no guardada.
>:pencil:**NOTA** para guardarlo sería con COMANDO < origen > destino

### Redirección de comandos

"|": Redirige la salida de un comando a la entrada de otro comando.

~~~bash
dir | find "test"
~~~

## Caracteres comodín

Los caracteres comodín en CMD son símbolos que se utilizan para representar cualquier conjunto de caracteres en un nombre de archivo o directorio. Los dos caracteres comodín más comunes en CMD son el asterisco (*) y el signo de interrogación (?).

- El asterisco (*) se utiliza para representar cualquier conjunto de caracteres, incluyendo ningún carácter.

~~~bash
dir *.txt
~~~

- El signo de interrogación (?) se utiliza para representar cualquier carácter único.
  
~~~bash
dir ????????.???
~~~

Este comando buscará todos los archivos que tengan un nombre de cinco letras y una extensión de tres letras en el directorio actual.

- También es posible combinar los caracteres comodín en una sola expresión.

~~~bash
dir foto*.???
~~~

Este comando buscará todos los archivos que empiecen por "foto" y tengan una extensión de tres letras en el directorio actual.

## SHUTDOWN

### Apagar

~~~bash
shutdown /s /t 0
~~~

El 0 puede ser sustituido por los segundos que quieras de retardo, en este caso se apagara inmediatamente

### Reiniciar

~~~bash
shutdown /r /t 0
~~~

## Discos y particiones

### CHKDSK

Se utiliza para verificar la integridad del sistema de archivos y detectar cualquier error en el disco duro. El comando también puede tratar de reparar cualquier error que encuentre en el disco.

~~~bash
chkdsk C: /f /r /x
~~~

### CONVERT

se utiliza para convertir el sistema de archivos de una partición de FAT a NTFS.

~~~bash
convert D: /fs:ntfs
~~~

### DEFRAG

se utiliza para desfragmentar los archivos en una unidad de disco. La desfragmentación ayuda a mejorar el rendimiento de la unidad y a reducir el tiempo de acceso a los archivos.

~~~bash
defrag C:
~~~

### FORMAT

se utiliza para formatear una unidad de disco en un sistema de archivos determinado.

~~~bash
format E: /fs:ntfs
~~~

### LABEL

se utiliza para cambiar el nombre de etiqueta de una unidad de disco.

~~~bash
label C: Windows
~~~

## Ejecución

### AT

Permite programar la ejecución de otro comando para una hora determinada.

- /INTERACTIVE: permite la interacción con el escritorio.
- /EVERY: programa la tarea para que se ejecute de forma periódica.
- /DELETE: elimina la tarea programada.

~~~bash
AT 15:00 C:\ruta\al\archivo\script.bat
~~~

### RUNAS

Permite ejecutar un programa con una cuenta diferente de usuario.

/USER: especifica el nombre de usuario y el dominio con el que se debe ejecutar el programa.

/SMARTCARD: utiliza una tarjeta inteligente para autenticar al usuario.

/NETONLY: especifica que la autenticación debe ocurrir en la red.

~~~bash
RUNAS /user:nombredeusuario "notepad.exe"
~~~

### START

Permite ejecutar aplicaciones en CMD

- /MAX: maximiza la ventana de la aplicación.
- /WAIT: espera a que la aplicación finalice antes de continuar.
- /B: ejecuta la aplicación sin abrir una nueva ventana de CMD.

~~~bash
START explorer.exe
~~~

### TASKKILL

Permite terminar un proceso.

- /F: fuerza el cierre del proceso.
- /PID: especifica el ID del proceso que se debe cerrar.
- /T: termina el proceso y todos sus subprocesos.

~~~bash
TASKKILL /IM notepad.exe
~~~

### TASKLIST

Permite listar los procesos en ejecución.

- /S: especifica el nombre o la dirección IP del equipo remoto.
- /U: especifica el nombre de usuario y la contraseña para la autenticación en el equipo remoto.
- /V: muestra información detallada sobre los procesos.

~~~bash
TASKLIST
~~~

## Información del sistema

### DRIVERQUERY

Permite mostrar la lista de controladores de dispositivos instalados en el sistema.

- /v: muestra información detallada sobre cada controlador.
- /si: muestra información adicional sobre el controlador, como la fecha de creación y la fecha de modificación.

~~~bash
driverquery
~~~

### HOSTNAME

Muestra el nombre del equipo en el que se está ejecutando.

~~~bash
hostname
~~~

### SYSTEMINFO

Muestra información detallada sobre la configuración del sistema, incluyendo información sobre la memoria, el procesador y los dispositivos de hardware. 

- /s [nombre de equipo]: muestra información sobre un equipo remoto en lugar del equipo local.
- /u [nombre de usuario]: utiliza un nombre de usuario diferente para conectarse al equipo remoto.
- /p [contraseña]: utiliza una contraseña diferente para conectarse al equipo remoto.

~~~bash
systeminfo
~~~

### VER

Muestra la versión del sistema operativo en el que se está ejecutando.

~~~bash
ver
~~~

## Tiempo

### DATE

Se utiliza para ver y establecer la fecha del sistema.

- /T : muestra solo la fecha actual, sin permitir establecer una nueva fecha.
- /D : permite establecer una nueva fecha. Debe ir seguido de la fecha en el formato "dd-mm-aa" o "dd/mm/aa".

#### Establecer fecha

~~~bash
date 20-04-23
~~~

#### Ver la fecha

~~~bash
date
~~~

### TIME

Se utiliza para ver y establecer la hora del sistema.

- /T : muestra solo la hora actual, sin permitir establecer una nueva hora.
- /D : permite establecer una nueva hora. Debe ir seguido de la hora en el formato "hh:mm:ss" y la letra "AM" o "PM".

#### Establecer hora

~~~bash
time 03:30:00 PM
~~~

#### Ver la hora

~~~bash
time
~~~

## Usuarios

### LOGOFF

Se utiliza para cerrar sesiones de usuario en un equipo local o remoto. Para utilizar este comando, primero es necesario conocer las sesiones activas en el equipo utilizando el comando "QUERY SESSION".

~~~bash
logoff 2
~~~

#### QUERY SESSION

Se utiliza para mostrar información sobre las sesiones de usuario activas en un servidor de Terminal Server o en un equipo local. Este comando muestra una lista de todas las sesiones de usuario activas, incluyendo el ID de sesión, el estado de la sesión, el nombre del usuario y la hora en que se inició la sesión.

~~~bash
query session
~~~

### NET

Se utiliza para administrar usuarios y grupos en un equipo local o remoto. Con este comando, se pueden crear, modificar y eliminar cuentas de usuario, así como asignar y revocar permisos y privilegios.

- USER: Permite administrar las cuentas de usuario en el equipo.
- GROUP: Permite administrar los grupos de usuario en el equipo.
- SHARE: Permite administrar los recursos compartidos en el equipo.

~~~bash
net user usuario1 123456 /add
~~~

### WHOAMI

Muestra el nombre de usuario y el dominio del usuario actualmente conectado al equipo. Este comando es útil para verificar la identidad del usuario antes de ejecutar ciertas tareas o comandos.

- USER: Muestra solo el nombre de usuario actual.
- GROUPS: Muestra los grupos de los que el usuario actual es miembro.

~~~bash
whoami
~~~

## Variables

### Establecer variables

~~~bash
set MI_DIRECTORIO=C:\Users\MiUsuario\Documentos
~~~

### Modificar variables

~~~bash
set MI_DIRECTORIO=C:\Users\MiUsuario
~~~

### Visualizar variables

~~~bash
set PATH
~~~

### Borrar variables

~~~bash
set MI_DIRECTORIO=
~~~

#### Opciones

- /a: permite realizar operaciones aritméticas con el valor de una variable.

~~~bash
set /A NUMERO=%NUMERO%+5
~~~

- /p: permite pedir al usuario que ingrese un valor para una variable.

~~~bash
set /P NOMBRE="Ingrese su nombre: "
~~~



## Visualización

### CLS

Se utiliza para limpiar la pantalla del símbolo del sistema en Windows.

~~~bash
cls
~~~

### COLOR

Se utiliza para cambiar los colores de la pantalla del símbolo del sistema en Windows. Su sintaxis incluye uno o dos parámetros que representan el color del texto y el fondo. Cada parámetro se compone de un número que representa el color en hexadecimal, seguido de una letra que indica si se trata del color del texto o del fondo.

COLORES

| CODIGO | COLOR |
| -       | -    |
|0 | Negro|
|1 | Azul|
|2 | Verde|
|3 | Aguamarina|
|4 | Rojo|
|5 | Púrpura|
|6 | Amarillo|
|7 | Blanco|
|8 | Gris|
|9 | Azul claro|
|A | Verde claro|
|B | Aguamarina claro|
|C | Rojo claro|
|D | Púrpura claro|
|E | Amarillo claro|
|F | Blanco brillante|

~~~bash
color 0A
~~~

En este ejemplo, "0" representa el color del fondo y "A" representa el color del texto. El número "0" indica el color negro y la letra "A" indica el color verde claro.

### MSG

Se utiliza para enviar mensajes a otros usuarios de la red en Windows. Su sintaxis incluye varios parámetros que permiten especificar el destinatario del mensaje, el título y el texto del mensaje. Es necesario tener privilegios de administrador para utilizar este comando.

~~~bash
msg /server:nombre_equipo usuario /time:10 "Hola, ¿cómo estás?"
~~~

En este ejemplo, "nombre_equipo" es el nombre del equipo en el que se encuentra el usuario al que queremos enviar el mensaje y "usuario" es el nombre de usuario del destinatario. El parámetro "/time:10" indica que el mensaje se mostrará durante 10 segundos antes de desaparecer automáticamente. El texto del mensaje es "Hola, ¿cómo estás?".