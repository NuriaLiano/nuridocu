# Simulacro examen BASH

### 1. Escribe un script de Bash que reciba un nombre de archivo como argumento y compruebe si existe en el directorio actual. Si existe, debe imprimir un mensaje diciendo que el archivo existe y, de lo contrario, debe imprimir un mensaje diciendo que el archivo no existe. Utiliza la estructura de control if

~~~bash

    #!/bin/bash

    if [ -e $1 ]; then
        echo "El archivo $1 existe"
    else
        echo "El archivo $1 no existe"
    fi

~~~

### 2. Escribe un script de Bash que lea un archivo de texto y cuente el número de palabras que contiene. El script debe imprimir el número total de palabras al final. Utiliza la estructura de control while

~~~bash

    #!/bin/bash

    palabras=0

    while read linea; do
        palabras=$(($palabras+$(echo $linea | wc -w)))
    done < $1

    echo "El archivo $1 contiene $palabras palabras."

~~~

### 3. Escribe un script de Bash que reciba una cadena de texto como argumento y cuente el número de veces que aparece una palabra específica en ella. La palabra específica debe ser otro argumento del script. Utiliza la estructura de control for

~~~bash

    #!/bin/bash

    palabra=$2
    contador=0

    for palabra_en_linea in $(echo $1 | tr ' ' '\n'); do
        if [ $palabra_en_linea = $palabra ]; then
            contador=$(($contador+1))
        fi
    done

    echo "La palabra $palabra aparece $contador veces en la cadena de texto."

~~~

### 4. Escribe un script de Bash que solicite al usuario un número entero positivo y calcule la suma de todos los números enteros desde 1 hasta el número introducido por el usuario, e imprima el resultado en pantalla. Utiliza la estructura de control until

~~~bash

    #!/bin/bash

    echo "Introduce un número entero positivo: "
    read num

    # Comprueba que el número es positivo
    if [ $num -lt 1 ]; then
    echo "El número introducido no es válido."
    exit 1
    fi

    suma=0
    contador=1

    until [ $contador -gt $num ]
    do
    suma=$((suma + contador))
    contador=$((contador + 1))
    done

    echo "La suma de los números enteros desde 1 hasta $num es: $suma"

~~~

### 5. Escribe un script de Bash donde pidas por teclado al usuario dos numeros, realiza una funcion para sumar y otra que compase si es mayor, menor o igual e imprima por pantalla los dos resultados. 

~~~bash

    #!/bin/bash

    # Definición de una función que suma dos números
    sumar() {
    resultado=$(( $1 + $2 ))
    echo "La suma de $1 y $2 es: $resultado"
    }

    # Pedir al usuario que introduzca dos números
    echo "Introduce dos números:"
    read num1
    read num2

    # Llamar a la función sumar con los dos números introducidos
    sumar $num1 $num2

    # Comprobar si el primer número introducido es mayor o menor que el segundo
    if [ $num1 -gt $num2 ]; then
    echo "El número $num1 es mayor que $num2."
    elif [ $num1 -lt $num2 ]; then
    echo "El número $num1 es menor que $num2."
    else
    echo "Los números introducidos son iguales."
    fi

    # Mostrar los argumentos de la línea de comandos
    echo "Los argumentos introducidos son: $@"

~~~


