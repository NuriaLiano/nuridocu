# EJERCICIOS DE ARRAYS

## EJERCICIO 1

Crea un script en Bash que le solicite al usuario cinco nombres y los almacene en un array. Luego, el script debe imprimir en la pantalla el número total de elementos en el array y el contenido del array.

~~~bash
    #!/bin/bash

    # Creamos un array vacío
    nombres=()

    # Le pedimos al usuario que ingrese cinco nombres y los almacenamos en el array
    echo "Ingresa cinco nombres:"
    read nombres[0] nombres[1] nombres[2] nombres[3] nombres[4]

    # Imprimimos en pantalla el número total de elementos en el array
    echo "El número total de elementos en el array es: ${#nombres[@]}"

    # Imprimimos en pantalla el contenido del array
    echo "El contenido del array es:"
    echo "${nombres[@]}"

~~~

## EJERCICIO 2

Crea un script en Bash que solicite al usuario una lista de números separados por comas y los guarde en un array. Luego, el script debe imprimir en la pantalla los números ingresados ordenados de forma ascendente.

~~~bash
    #!/bin/bash

    # Solicitamos al usuario que ingrese una lista de números separados por comas y los guardamos en un array
    echo "Ingresa una lista de números separados por comas:"
    read numeros_string
    IFS=',' read -a numeros <<< "$numeros_string"

    # Ordenamos los números ingresados de forma ascendente
    IFS=$'\n' numeros_ordenados=($(sort -n <<< "${numeros[*]}"))

    # Imprimimos los números ordenados
    echo "Los números ingresados ordenados de forma ascendente son:"
    echo "${numeros_ordenados[*]}"
~~~

## EJERCICIO 3

Crea un script en Bash que cree dos arrays, uno con los nombres de los meses del año y otro con los días que tiene cada mes. Luego, el script debe imprimir en la pantalla los nombres de los meses y la cantidad de días que tiene cada uno.

~~~bash
    #!/bin/bash

    # Creamos dos arrays, uno con los nombres de los meses y otro con la cantidad de días que tiene cada mes
    meses=(Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre)
    dias=(31 28 31 30 31 30 31 31 30 31 30 31)

    # Imprimimos los nombres de los meses y la cantidad de días que tiene cada uno
    for i in "${!meses[@]}"
    do
        echo "${meses[$i]} tiene ${dias[$i]} días"
    done
~~~

## EJERCICIO 4

Crea un script en Bash que genere un array de 10 números aleatorios entre 1 y 100. Luego, el script debe imprimir en la pantalla los números del array en orden inverso.

~~~bash
    #!/bin/bash

    # Generamos un array con 10 números aleatorios entre 1 y 100
    for ((i=0; i<10; i++))
    do
        numeros[$i]=$((RANDOM%100+1))
    done

    # Imprimimos los números del array en orden inverso
    for ((i=${#numeros[@]}-1; i>=0; i--))
    do
        echo ${numeros[i]}
    done
~~~
