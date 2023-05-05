# EXAMEN ISO Tema 4

## Instrucciones

- Escribe las ordenes necesarias para realizar las tareas en Bash
- Debes escribir una orden en cada caso, a no ser que se indique lo contrario
- Añade un disco duro virtual de 1GB a tu máquina

## Ejercicios

1. Crea un directorio llamado **EXAMEN** en tu directorio **/home/usuario** y hazlo tu directorio activo.
**Desde este momento ese será tu directorio activo y no te moverás en ningún otro momento**

>:warning:**ADVERTENCIA** Comprueba que estás en el directorio raíz de tu usuario (/home/usuario). En caso de no estar en tu $HOME tendras que ejecutar ``cd ~`` para moverte y facilitar el resto de instrucciones. 

~~~bash
#1. Crear el directorio
mkdir examen
#2. Cambiar al directorio
cd examen
~~~

>:pencil: **NOTA** para visualizar cual es la ruta del home de tu usuario puedes imprimir la variable global $HOME: ``echo $HOME``
>:pencil: **NOTA** si quieres ver la ruta absoluta del directorio en el que estás, puedes ejecutar este comando ``pwd``

2. Crea el siguiente árbol de directorios (Puedes escribir más de una orden)

- examen
  - dir1
    - electro
      - admini
  - dir2

~~~bash
mkdir -p ./dir1/electro/admini ./dir2
~~~

>:pencil: **NOTA** al indicar al principio ``./`` y después el resto de la ruta,
indica que comienza o actua sobre el directorio actual.
>:pencil: **NOTA** Es una buena práctica (en Windows lo añade por defecto) añadir el ``./`` delante de la ruta si quieres trabajar desde el directorio actual

3. Crea un archivo vacío llamado **archivo.txt** en el directorio **ADMINI**

~~~bash
touch ./dir1/electro/admini/archivo.txt
~~~

4. Crea un archivo denominado **CyL.txt** en **DIR2** con el siguiente contenido

   ~~~bash
    Soria 39112 Leon 124772 Burgos 175921 
    Segovia 51683 Zamora 61827 Valladolid 298866 
    Avila 57657 Salamanca 143978 Palencia 78629 
   ~~~

~~~bash
nano ./dir2/cyl.txt
~~~

>:pencil: **NOTA** puedes utilizar otros editores de texto como VI: ``vi ./dir2/cyl.txt``

5. Intenta ver el listado de ficheros y directorios de un directorio llamado **DIR3** que sería el hermano de **DIR1** y **DIR2**. Vuelca los errores en un archivo llamado **errores.log** en el directorio **ADMINI**
  
~~~bash
ls ./dir3 > ./dir1/electro/admini/errores.log
~~~

6. Ordena el contenido del archivo **cyl.txt** por orden alfabético, vuelca el resultado en un archivo denominado **cyl_az.txt** en **DIR2**
  
~~~bash
cat ./dir2/cyl.txt | sort > ./dir2/cyl_az.txt
~~~

>:pencil: **NOTA** Ayuda con los comandos --help o -h ejemplo: sort --help

7. Copia el archivo **cyl_az.txt** en el directorio **ELECTRO** con el nombre **datos.txt**
  
~~~bash
cp ./dir2/cyl_az.txt ./dir1/electro/datos.txt
~~~

>:pencil: **NOTA** El comando cp tiene el parámetro -r para poder copiar directorios completos

8. Ordena el contenido del archivo **cyl.txt** de forma numérica de menor a mayor población. Vuelca el resultado en un archivo denominado **poblacion.txt** en **DIR2**
  
~~~bash
cat ./dir2/cyl.txt | sort -n > ./dir2/poblacion.txt
~~~

>:pencil: **NOTA** Si quieres ordenar al revés, de mayor a menor, tienes que añadir el parámetro -r ``cat ./dir2/cyl.txt | sort -nr > ./dir2/poblacion.txt``

9.  Mediante el archivo **cyl.txt** muestra por pantalla la población de Salamanca. Solo debe aparecer el número, no el nombre de la provincia.
  
~~~bash
cat ./dir2/cyl.txt | cut -d "" -f 2
~~~

10. Cambia los permisos de ejecución del archivo **población.txt** de tal manera que el propietario tenga permisos de lectura, escritura y ejecución, el grupo tenga permiso de lectura y escritura y el resto sólo tenga permiso de lectura.
  
~~~bash
sudo chmod 764 ./dir2/poblacion.txt
~~~

>:pencil: **NOTA** orden de grupos OWNER | GROUP | OTHER
>:pencil: **NOTA** orden de permisos READ | WRITE | EXECUTE
>:pencil: **NOTA** peso de permisos READ = 4 | WRITE = 2 | EXECUTE = 1

11. Mueve el archivo **archivo.txt** al directorio **EXAMEN**
  
~~~bash
mv ./dir1/electro/admini/archivo.txt ./
~~~

>:pencil: **NOTA** Para mover al directorio EXAMEN solo es necesario poner ./ ya que es tu directorio actual y
del que no puedes moverte.
>:pencil: **NOTA** En caso de querer mover el fichero y darle otro nombre en la ruta de destino se añade en el segundo parámetro ejemplo: mv ./dir1/electro/admini/archivo.txt ./moviendoArchivo.txt

12. Cambia los permisos del fichero **archivo.txt** para que el propietario tenga permisos de ejecución. El resto de permisos no se deben modificar.
  
~~~bash
sudo chmod 164 ./archivo.txt
~~~

>:pencil: **NOTA** Solo tienes que modificar el permiso del propietario (owner), el resto de permisos copias los
que ya hay
>:pencil: **NOTA** Ver los permisos sobre directorios o ficheros ``ls -l ./ruta``

13. Empaqueta y comprime en formato **tar.gz** el directorio **EXAMEN** con todo su contenido en un archivo denominado **paquete.tar.gz**
  
~~~bash
tar -czvf ../paquete.tar.gz ./
~~~

14. Crea un grupo denominado **examen**
  
~~~bash
sudo groupadd examen
~~~

15. Crea un usuario que se llame **examen** que tenga como grupo principal **examen**, como directorio home **/home/examen** y por shell **/bin/bash**
  
~~~bash
#opción fácil
sudo useradd examen

#opción mas dificil
sudo adduser --home /home/examen --shell '/bin/bash' --group examen examen
~~~

16. Cambia el usuario propietario del archivo **datos.txt** al usuario **examen**
  
~~~bash
sudo chown examen ./dir1/electro/datos.txt
~~~

17.  Cambia el grupo propietario del archivo **datos.txt** al grupo **examen**
  
~~~bash
sudo chown :examen ./dir1/electro/datos.txt
~~~

>:pencil: **NOTA** El ejercicio 16 y 17 se puede hacer en una sola instrucción. Solo es necesario poner
usuario:grupo ``sudo chown examen:examen ./dir1/electro/datos.txt``

18. Del archivo **/etc/passwd** muesra sólo los nombres de los usuarios y las rutas de los directorios personales separadas por un espacio
  
~~~bash
sudo cut -d ":" -f1,6 /etc/passwd
~~~

>:pencil: **NOTA** Antes de realizar el cut se suele visualizar el contenido para poder contar que columnas
quieres mostrar

19. Cambia la contraseña del usuario **examen** a **123456**
  
~~~bash
sudo passwd examen
~~~

20. Cambia el nombre del usuario **examen** a **prueba**
  
~~~bash
sudo usermod -l prueba examen
~~~

21. Instala el programa **sudoku** localizado en los repositorios oficiales
  
~~~bash
sudo apt install sudoku
~~~

>:pencil: **NOTA** Si antes de instalar quieres comprobar si existe el paquete en los repositorios instalados: ``sudo apt search sudoku``

22. Elimina el programa **sudoku** junto con sus archivos de configuración
  
~~~bash
sudo apt purge sudoku
~~~

>:pencil: **NOTA** Comando para eliminar una aplicacion sin eliminar sus ficheros de configuración ``sudo apt remove sudoku``

23. Elimina el directorio **EXAMEN** y todo su contenido

>:warning: **ADVERTENCIA** Es necesario salirse del directorio que vas a eliminar

~~~bash
cd .. sudo rm -r ./examen/
~~~

24. Elimina el grupo examen
  
~~~bash
sudo groupdel examen
~~~

25. Elimina el usuario prueba.
  
~~~bash
sudo userdel prueba
~~~
