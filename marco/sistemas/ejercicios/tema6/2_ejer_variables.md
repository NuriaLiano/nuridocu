# EJERCICIOS DE VARIABLES

## EJERCICIO 1

Crea un script en Bash que le solicite al usuario su nombre y su edad, calcule la cantidad de días que ha vivido, y luego imprima en la pantalla un mensaje que incluya su nombre, su edad y la cantidad de días que ha vivido

~~~bash
    #!/bin/bash

    # Solicitamos el nombre del usuario
    echo "Por favor, introduce tu nombre: "
    read nombre

    # Solicitamos la edad del usuario
    echo "Por favor, introduce tu edad: "
    read edad

    # Calculamos la cantidad de días que ha vivido el usuario
    dias=$((edad * 365))

    # Imprimimos un mensaje que incluye el nombre, la edad y la cantidad de días que ha vivido el usuario
    echo "Hola, $nombre! Tienes $edad años, lo que significa que has vivido aproximadamente $dias días. ¡Disfruta el presente!"
~~~

## EJERCICIO 2

Crea un script en Bash que le solicite al usuario su nombre y su comida favorita, y luego imprima en la pantalla un mensaje que incluya su nombre y su comida favorita en una oración.

~~~bash
    #!/bin/bash

    # Solicitamos el nombre del usuario
    echo "Por favor, introduce tu nombre: "
    read nombre

    # Solicitamos la comida favorita del usuario
    echo "Por favor, introduce tu comida favorita: "
    read comida

    # Creamos una variable que contiene la oración que incluye el nombre y la comida favorita del usuario
    mensaje="Hola, $nombre. Tu comida favorita es $comida. ¡Espero que esté deliciosa!"

    # Imprimimos el mensaje en la pantalla
    echo $mensaje
~~~

## EJERCICIO 3 - VARIABLES DE POSICIÓN

Crea un script en Bash que tome dos argumentos de línea de comandos: un número y una cadena de texto. El script debe imprimir en la pantalla y el segundo parámetro en mayúsculas.

~~~bash
    #!/bin/bash

    # Almacenamos el primer argumento en la variable "numero"
    numero=$1

    # Almacenamos el segundo argumento en la variable "cadena"
    cadena=$2

    # Convertimos la cadena de texto a mayúsculas
    mayusculas=$(echo $cadena | tr '[:lower:]' '[:upper:]')

    # Imprimimos el doble del número y la cadena de texto en mayúsculas
    echo "La cadena en mayúsculas es: $mayusculas"
~~~

## EJERCICIO 4 - VARIABLES DE POSICIÓN

Crea un script en Bash que le solicite al usuario un nombre de archivo y luego intente abrir el archivo usando el comando "cat". Si el archivo existe, se debe imprimir en la pantalla su contenido. Si el archivo no existe, se debe imprimir en la pantalla un mensaje de error y salir del script. Al finalizar, el script debe imprimir en la pantalla el valor de las variables "$*", "$@" y "$?".

~~~bash
    #!/bin/bash

    # Le pedimos al usuario que ingrese el nombre del archivo
    echo "Ingresa el nombre del archivo:"
    read archivo

    # Intentamos abrir el archivo usando el comando "cat"
    cat $archivo

    # Verificamos si el comando "cat" tuvo éxito o no
    if [ $? -ne 0 ]; then
    # Si el archivo no existe, imprimimos un mensaje de error y salimos del script
    echo "Error: el archivo '$archivo' no existe."
    exit 1
    fi

    # Imprimimos en pantalla el valor de las variables "$*", "$@" y "$?"
    echo "El valor de la variable \"\$*\" es: $*"
    echo "El valor de la variable \"\$@\" es: $@"
    echo "El valor de la variable \"\$?\" es: $?"
~~~
