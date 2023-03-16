# EJERCICIOS DE FUNCIONES

## EJERCICIO 1 (nivel medio)

Crea una función en Bash que reciba como parámetro un directorio y un número entero n. La función debe imprimir en la pantalla los n archivos más grandes del directorio, ordenados de mayor a menor tamaño.

~~~bash
    #!/bin/bash

    # Definimos la función que recibe un directorio y un número entero n
    function archivos_mas_grandes() {
        directorio=$1
        n=$2

        # Obtenemos los n archivos más grandes del directorio
        archivos=($(ls -S $directorio | head -$n))

        # Imprimimos los n archivos más grandes del directorio, ordenados de mayor a menor tamaño
        echo "Los $n archivos más grandes del directorio $directorio son:"
        for archivo in "${archivos[@]}"
        do
            echo $archivo
        done
    }

    # Ejemplo de uso de la función
    archivos_mas_grandes "/home/usuario/documentos" 5
~~~

## EJERCICIO 2 (nivel medio)

Crea una función en Bash que reciba como parámetro un directorio y una extensión de archivo. La función debe buscar todos los archivos con esa extensión en el directorio y contar cuántos archivos hay. Luego, debe imprimir en la pantalla un mensaje indicando el número de archivos encontrados.

~~~bash
    #!/bin/bash

    # Definimos la función que recibe un directorio y una extensión de archivo
    function contar_archivos_por_extension() {
        directorio=$1
        extension=$2

        # Buscamos todos los archivos con la extensión dada en el directorio
        archivos=($(find $directorio -name "*.$extension"))

        # Contamos cuántos archivos se encontraron
        num_archivos=${#archivos[@]}

        # Imprimimos el número de archivos encontrados
        echo "Se encontraron $num_archivos archivos con la extensión .$extension en el directorio $directorio"
    }

    # Ejemplo de uso de la función
    contar_archivos_por_extension "/home/usuario/documentos" "pdf"

~~~

## EJERCICIO 3 (nivel fácil)

Crea una función en Bash que reciba como parámetros dos números y calcule la suma de ambos números. La función debe imprimir en la pantalla el resultado de la suma.

~~~bash
    #!/bin/bash

    # Definimos la función que recibe dos números y calcula su suma
    function sumar_numeros() {
        num1=$1
        num2=$2

        # Calculamos la suma de los dos números
        suma=$((num1 + num2))

        # Imprimimos el resultado de la suma
        echo "La suma de $num1 y $num2 es: $suma"
    }

    # Ejemplo de uso de la función
    sumar_numeros 10 20
~~~
