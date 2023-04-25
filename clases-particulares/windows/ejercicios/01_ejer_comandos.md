---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---
# Ejercicios comandos CMD

>:pencil:**NOTA** Cada vez que ejecutes un ejercicio tienes que limpiar la consola.

cd, dir, tree, mr, rm, push, popd, ren, copy, move, attrib, del, type, assoc, 
fc, ftype, mklink, openfiles, print, where, >, >>, <, | , *, ?, shutdown, chkdsk, convert, defrag, format, label, at, runas, start, taskkill, tasklist, driverquery, hostname, systeminfo, ver, date, time, logoff, query session, net user, net localgroup, whoami,  variables con set, cls, color, msg

# 1. Establece la fecha actual en una variable y crea una carpeta con esa variable como nombre

~~~bash
set fecha=%date:/=-%
md %fecha%

#otra opcion para eliminar los guiones de la fecha
set fecha=%date:/=-%
md %fecha%
ren %fecha% %fecha%
~~~

# 2. Buscar un archivo específico utilizando el comando where

~~~bash
where /R C:\ archivo.txt
~~~

# 3. Listar los procesos que están utilizando un archivo específico

~~~bash
where /R C:\ archivo.txt
~~~

# 4. Crear un archivo de texto en el escritorio llamado "nombres.txt" que contenga los nombres de todas las carpetas en la carpeta "Documentos".

~~~bash
cd C:\Users\Usuario\Documentos
dir /b /ad > C:\Users\Usuario\Escritorio\nombres.txt
~~~

Primero, cambia el directorio actual a la carpeta "Documentos" con el comando "cd" y luego usa el comando "dir /b /ad" para obtener una lista de todas las carpetas en esa carpeta en formato de una columna sin información adicional. A continuación, utiliza el operador ">" para guardar la salida del comando "dir" en un archivo de texto llamado "nombres.txt" en el escritorio.

# 5. Mover todos los archivos con extensión ".jpg" de la carpeta "Imágenes" a la carpeta "Backup".

~~~bash
cd C:\Users\Usuario\Imágenes
move *.jpg C:\Users\Usuario\Backup
~~~

Usa el comando "move" para mover todos los archivos con la extensión ".jpg" de la carpeta "Imágenes" a la carpeta "Backup". Puedes utilizar el comando "cd" para cambiar al directorio de la carpeta "Imágenes" y luego especificar la ruta completa de la carpeta "Backup" en el comando "move".

# 6. Cambiar el atributo "oculto" de todos los archivos en la carpeta "Documentos" y sus subcarpetas.

~~~bash
cd C:\Users\Usuario\Documentos
attrib +h /s *
~~~

Usa el comando "attrib" con el modificador "+h" para agregar el atributo "oculto" a todos los archivos en la carpeta "Documentos" y sus subcarpetas. Puedes utilizar el comando "cd" para cambiar al directorio de la carpeta "Documentos" y luego usar el modificador "/s" para aplicar el comando a todas las subcarpetas de forma recursiva.

# 7. Crear un directorio y un archivo dentro del directorio, luego copiar el archivo a otro directorio

~~~bash
mkdir C:\mi_directorio
echo "Este es un archivo de prueba" > C:\mi_directorio\archivo.txt
mkdir C:\otro_directorio
copy C:\mi_directorio\archivo.txt C:\otro_directorio\
~~~

# 8. Guarda la ruta del directorio actual usando pushd, Crea un nuevo directorio llamado "nuevo_directorio". y usa "popd" para volver a la ruta anterior y luego usa "dir" para verificar que estás en la ruta correcta.

~~~bash
pushd
md nuevo_directorio
popd
dir
~~~

# 9. Supongamos que queremos asociar la extensión ".txt" con el programa Notepad++.

~~~bash
assoc .txt=Notepad++.
~~~

>:pencil:**NOTA** para deshacer la asociacion se usa assoc .txt=

# 10. Supongamos que tenemos dos archivos de texto, "archivo1.txt" y "archivo2.txt", y queremos compararlos para verificar si son idénticos. y guardar el resultado de la comparación en un archivo de texto

~~~bash
fc archivo1.txt archivo2.txt /c > diferencias.txt
~~~

# 11. Supongamos que tenemos una carpeta llamada "Documentos" en la unidad C: y queremos crear un enlace simbólico hacia esta carpeta en la unidad D: con el nombre "Mis documentos".

~~~bash
mklink /d D:\Mis documentos C:\Documentos
~~~

# 12. Supongamos que tenemos un archivo llamado "reporte.docx" en una carpeta compartida en la red y queremos saber qué usuarios tienen este archivo abierto en sus equipos.

~~~bash
openfiles /query /s <nombre_del_equipo> /fo list /v | find /i "reporte.docx"
~~~

Esto mostrará una lista de los usuarios que tienen el archivo "reporte.docx" abierto en el equipo remoto especificado por el parámetro /s. La opción /fo list indica que la salida se mostrará en formato de lista y la opción /v indica que se mostrará información detallada de los archivos abiertos. La salida se pasa al comando find para buscar el archivo específico en la lista de archivos abiertos.

# 12. Verifica o repara errores de la unidad C

~~~bash
chkdsk C:
~~~

# 13. Desfragmentar y cambiar nombre a disco

~~~bash
defrag E: /U /V
label E: "Nuevo Nombre"
~~~

# 14. Programar la ejecución de un archivo de comando "myscript.bat" para las 3:00 pm de hoy.

Donde "15:00" es la hora programada en formato de 24 horas y "/interactive" indica que la tarea se ejecutará en el escritorio interactivo.

>:warning:**ADVERTENCIA** Es importante tener en cuenta que el comando "at" solo funciona si el servicio "Programador de tareas" está en ejecución.

~~~bash
at 15:00 /interactive C:\ruta\del\archivo\myscript.bat
~~~

# 15. Queremos ejecutar el comando ipconfig con permisos de administrador en una cuenta de usuario que no tiene dichos permisos

~~~bash
runas /user:nombre_de_usuario "cmd /c ipconfig"
~~~

nombre_de_usuario" es el nombre de usuario de la cuenta con permisos de administrador. Al ejecutar este comando, se pedirá la contraseña de dicha cuenta de usuario y luego se ejecutará el comando ipconfig con los permisos de administrador correspondientes.


# 16. Supongamos que tienes un archivo de texto llamado "ejemplo.txt" en la carpeta "Documentos" de tu usuario en Windows. Quieres abrir este archivo con el Bloc de notas usando el comando "start". 

~~~bash
start notepad C:\Users\[tu usuario]\Documents\ejemplo.txt
~~~

# 17. Filtrar la lista de procesos para mostrar solo los procesos que coinciden con chrome.exe

~~~bash
tasklist /fi "IMAGENAME eq chrome.exe"
~~~

# 18. Cerrar la aplicación notepad.exe forzosamente

~~~bash
taskkill /IM notepad.exe /F
~~~

- /IM: Especifica el nombre de la imagen del proceso que queremos finalizar.
- /F: Especifica que el proceso se debe finalizar forzosamente.

# 19. Establece el fondo de la consola en negro y el texto en verde claro

~~~bash
color 0a
echo "Este texto es negro sobre fondo verde claro"
~~~

# 20. Supongamos que hay dos usuarios conectados a un mismo equipo, "Usuario1" y "Usuario2". El usuario1 desea enviar un mensaje al usuario2 que diga "Hola Usuario2, ¿cómo estás?".

>:warning:**ADVERTENCIA** sólo funciona si los dos usuarios están conectados a la misma red y si la función de mensajería está habilitada en ambos equipos.

~~~bash
MSG Usuario2 "Hola Usuario2, ¿cómo estás?"
~~~
