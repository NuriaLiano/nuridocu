---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---
# Tareas programadas 

## SCHTASK

### Crear una tarea

~~~bash
schtasks /create /tn "My Task" /tr "C:\my_script.bat" /sc daily /st 12:00
~~~

### Modificar una tarea

~~~bash
schtasks /change /tn "My Task" /tr "C:\my_new_script.bat" /sd 01/01/2023
~~~

### Eliminar una tarea

~~~bash
schtasks /delete /tn "My Task"
~~~

### Mostrar una lista de las tareas programadas

~~~bash
schtasks /query
~~~

### Exportar una tarea programada a un archivo XML

~~~bash
schtasks /query /tn "My Task" /xml C:\my_task.xml
~~~

### Importar una tarea programada a un archivo XML

~~~bash
schtasks /create /xml C:\my_task.xml
~~~
