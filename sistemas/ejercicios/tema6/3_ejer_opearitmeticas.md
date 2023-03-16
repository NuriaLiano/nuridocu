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

Crea un script en Bash que solicite al usuario que ingrese dos números enteros y guarde cada número en una variable. Luego, el script debe imprimir la suma, resta, multiplicación y división de los dos números.

~~~bash
    #!/bin/bash

    # Solicitamos al usuario que ingrese dos números enteros
    echo "Ingrese el primer número: "
    read num1
    echo "Ingrese el segundo número: "
    read num2

    # Realizamos las operaciones matemáticas y las almacenamos en variables
    suma=$((num1+num2))
    resta=$((num1-num2))
    multi=$((num1*num2))
    div=$((num1/num2))

    # Imprimimos los resultados
    echo "La suma de los números es: $suma"
    echo "La resta de los números es: $resta"
    echo "La multiplicación de los números es: $multi"
    echo "La división de los números es: $div"
~~~

## EJERCICIO 3

Crea un script en Bash que le solicite al usuario un número entero y luego calcule su cuadrado y su cubo. El script debe imprimir en la pantalla los resultados de cada operación.

~~~bash
    #!/bin/bash

    # Le pedimos al usuario que ingrese un número entero
    echo "Ingresa un número entero:"
    read num

    # Calculamos el cuadrado y el cubo del número
    cuadrado=$((num * num))
    cubo=$((num * num * num))

    # Imprimimos en pantalla los resultados de cada operación
    echo "El cuadrado de $num es: $cuadrado"
    echo "El cubo de $num es: $cubo"
~~~
