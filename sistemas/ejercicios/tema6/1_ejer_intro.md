# EJERCICIOS INTRODUCCIÓN

## EJERCICIO 1

Crea un script en Bash que le solicite al usuario su nombre y su edad, y luego imprima en la pantalla un mensaje de bienvenida que incluya su nombre y su edad.

~~~bash
    #!/bin/bash
    # Solicitamos el nombre del usuario
    echo "Por favor, introduce tu nombre: "
    read nombre

    # Solicitamos la edad del usuario
    echo "Por favor, introduce tu edad: "
    read edad

    # Imprimimos un mensaje de bienvenida que incluye el nombre y la edad del usuario
    echo "¡Bienvenido/a, $nombre! Veo que tienes $edad años. ¡Disfruta tu estancia!"
~~~

## EJERCICIO 2

Crea un script en Bash que le solicite al usuario dos números enteros, calcule la suma de los dos números, y luego imprima en la pantalla un mensaje que incluya los dos números y su suma.

~~~bash
    #!/bin/bash
    # Solicitamos el primer número
    echo "Por favor, introduce el primer número: "
    read num1

    # Solicitamos el segundo número
    echo "Por favor, introduce el segundo número: "
    read num2

    # Calculamos la suma de los dos números
    suma=$((num1 + num2))

    # Imprimimos un mensaje que incluye los dos números y su suma
    echo "La suma de $num1 y $num2 es igual a $suma."
~~~
