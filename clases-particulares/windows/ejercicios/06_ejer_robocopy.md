# Ejercicios sobre ROBOCOPY

## 1. Copiar una carpeta y su contenido a otro directorio

~~~bash
robocopy C:\carpeta_origen C:\carpeta_destino /E /COPYALL
~~~

## 2. Supongamos que queremos copiar una carpeta, pero queremos excluir ciertos archivos específicos, como archivos temporales o de registro.

Podemos hacer esto utilizando el parámetro /XF, que especifica qué archivos excluir de la copia.

~~~bash
robocopy C:\carpeta_origen C:\carpeta_destino /E /COPYALL /XF *.tmp *.log
~~~

Este comando copia todos los archivos y subcarpetas en la carpeta de origen a la carpeta de destino, pero excluye cualquier archivo con la extensión .tmp o .log.

## 3. Supongamos que queremos copiar una carpeta de origen a un destino, pero también queremos sincronizar cualquier cambio que se haga en la carpeta de origen.

 Podemos hacer esto utilizando el parámetro /MIR, que sincroniza la carpeta de destino con la carpeta de origen

~~~bash
robocopy C:\carpeta_origen C:\carpeta_destino /MIR /COPYALL /DCOPY:T
~~~

Este comando copia todos los archivos y subcarpetas en la carpeta de origen a la carpeta de destino, y sincroniza cualquier cambio que se haga en la carpeta de origen. También incluye los atributos, tiempos de modificación y permisos de archivo, y copia cualquier carpeta vacía. El parámetro /DCOPY:T copia también la hora de creación de las carpetas.

## 4. Copiar archivos modificados en los últimos 7 días

 Podemos utilizar la opción /MAXAGE con el valor 7

~~~bash
ROBOCOPY C:\Origen D:\Destino /S /MAXAGE:7
~~~

## 5. Copiar archivos en paralelo

Si quieres acelerar el proceso de copia, puedes utilizar la opción /MT para copiar varios archivos en paralelo.

~~~bash
ROBOCOPY C:\Origen D:\Destino /S /MT:4
~~~
