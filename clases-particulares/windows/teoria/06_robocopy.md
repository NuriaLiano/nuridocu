# ROBOCOPY

Es una herramienta de línea de comandos de Windows que permite copiar archivos y directorios de una ubicación a otra de manera eficiente y con muchas opciones avanzadas.

- Tolera las interrupciones en la copia de archivos ya sea por cortes de energía o en la conexión.
- Realiza reintentos automáticos si no se puede acceder a un archivo.
- Permite copiar grandes cantidades de archivos, imposible con XCOPY.
- Muestra indicador de progreso.
- Permite copiado multihilo.
- Copia correctamente toda la información como propiedades, atributos, datos del propietario, fechas, etc además mantiene inalterables los permisos del archivo.

## Ejemplos de uso

- **Copia recursiva de carpetas con subdirectorios vacíos**: el comando "ROBOCOPY ORIGEN DESTINO /E" copiará todos los archivos y subdirectorios del origen al destino, incluso si los subdirectorios están vacíos.
- **Copia recursiva de carpetas con subdirectorios pero no los vacíos**: el comando "ROBOCOPY ORIGEN DESTINO /S" copiará todos los archivos y subdirectorios del origen al destino, pero no los subdirectorios vacíos.
- **Modo espejo para copias de seguridad**: el comando "ROBOCOPY ORIGEN DESTINO /MIR" copiará todos los archivos y subdirectorios del origen al destino, eliminando cualquier archivo o subdirectorio del destino que no exista en el origen.
- **Copias multiproceso**: el comando "ROBOCOPY ORIGEN DESTINO /MT:n" permite que se realicen copias utilizando varios hilos, lo que puede acelerar la velocidad de la copia. El valor predeterminado es 8, pero se puede especificar cualquier valor entre 1 y 128.

## Opciones

- /R:n: Esta opción especifica el número de veces que se reintentará la copia de un archivo en caso de que se produzca un error. El valor predeterminado es 1 millón, pero puede ser ajustado por el usuario.
- /W:n: Esta opción especifica el tiempo de espera en segundos entre los reintentos de copia. El valor predeterminado es 30 segundos.
- /MT:n: Esta opción permite que la copia de archivos sea realizada en múltiples hilos simultáneamente. El valor n especifica el número de hilos y debe estar comprendido entre 1 y 128. El valor predeterminado es 8.
- /MOV: Esta opción mueve los archivos y los elimina del origen después de ser copiados.
- /MOVE: Esta opción mueve los archivos y carpetas y los elimina del origen después de ser copiados.
- /V: Esta opción muestra información detallada durante la copia.
- /L: Esta opción simula una copia y no realiza la operación de copia en sí.
- /FP: Esta opción incluye la ruta de acceso completa de los archivos en el resultado.
- /NJH: Esta opción no muestra el encabezado en la consola.
- /NJS: Esta opción no muestra el resumen final.
- /S: copia todos los subdirectorios (sin incluir vacíos).
- /E: copia todos los subdirectorios (incluso vacíos).
- /MIR: sincroniza los directorios de origen y destino, copiando solo los archivos que han cambiado o se han añadido en la fuente desde la última sincronización.
- /Z: copia los archivos en modo de reinicio, permitiendo reanudar la copia en caso de interrupción.
- /R: número de veces que se intentará copiar un archivo que ha fallado (por defecto es 1 millón).
- /W: tiempo de espera en segundos entre intentos de copia (por defecto es 30 segundos).
- /LOG: guarda un archivo de registro con todas las acciones realizadas.