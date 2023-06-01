# Juego del ahorcado en BASH

Escribe un programa en Bash para jugar el juego del ahorcado.

- El programa mostrará un mensaje de bienvenida al usuario, indicando la fecha actual y preparando el juego del ahorcado.
- Seleccionará una palabra aleatoria del archivo de palabras.
- El jugador tendrá que adivinar la palabra ingresando letras una a una.
  - Si el jugador adivina todas las letras de la palabra antes de agotar los intentos, ganará el juego.
  - Si el jugador agota los intentos sin adivinar la palabra completa, perderá el juego.
- El programa mostrará el estado del ahorcado y las letras adivinadas después de cada intento.
- Al finalizar el juego, se registrará el resultado (si el jugador ganó o perdió), el número de intentos utilizados y la duración del juego en un archivo de registro.

Recuerda crear un archivo de texto llamado palabras.txt con una lista de palabras para el juego. Además, asegúrate de tener permisos de escritura en el directorio donde deseas crear el archivo partidas.log para el registro de las partidas.

~~~sh
#!/bin/bash

# Obtener el nombre de usuario actual
usuario=$(whoami)

# Obtener la fecha actual
fecha=$(date +%Y-%m-%d)

# Mostrar información del sistema antes de iniciar el juego
echo "Bienvenido, $usuario. Hoy es $fecha."
echo "Preparando el juego del ahorcado..."

# Archivo con palabras para adivinar
archivo_palabras="palabras.txt"

# Palabras para adivinar leídas desde el archivo
palabras=($(cat "$archivo_palabras"))

# Ruta del archivo de registro
ruta_log="partidas.log"

# Imágenes ASCII del ahorcado
ahorcado_imagenes=(
"
 +---+
 |   |
     |
     |
     |
     |
=========
"
"
 +---+
 |   |
 O   |
     |
     |
     |
=========
"
"
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
"
"
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
"
"
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
"
"
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
"
"
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
")

# Función para seleccionar una palabra aleatoria
function seleccionar_palabra {
    local index=$((RANDOM % ${#palabras[@]}))
    palabra_secreta=${palabras[$index]}
}

# Función para inicializar las variables del juego
function inicializar_juego {
    seleccionar_palabra
    letras_adivinadas=()
    intentos_restantes=6
    palabra_mostrada=$(printf '_%.0s' $(seq 1 ${#palabra_secreta}))
    inicio=$(date +%s)
}

# Función para imprimir el estado actual del juego
function imprimir_estado_juego {
    echo "Palabra secreta: $palabra_mostrada"
    echo "Letras adivinadas: ${letras_adivinadas[*]}"
    echo "Intentos restantes: $intentos_restantes"
    echo "${ahorcado_imagenes[$intentos_restantes]}"
}

# Función para procesar el intento del jugador
function procesar_intentos {
    local letra=$1
    letras_adivinadas+=($letra)
    if [[ ! "$palabra_secreta" =~ $letra ]]; then
        intentos_restantes=$((intentos_restantes - 1))
    else
        for i in $(seq 0 $((${#palabra_secreta} - 1))); do
            if [[ "${palabra_secreta:i:1}" == "$letra" ]]; then
                palabra_mostrada="${palabra_mostrada:0:i}$letra${palabra_mostrada:i+1}"
            fi
        done
    fi
}

# Función para registrar la partida en el archivo de registro
function registrar_partida {
    local fin=$(date +%s)
    local duracion=$((fin - inicio))
    local resultado=""
    if [[ "$palabra_secreta" == "$palabra_mostrada" ]]; then
        resultado="Ganador: Jugador"
    else
        resultado="Ganador: Máquina"
    fi
    echo "$(date) - $resultado - Intentos: $((6 - intentos_restantes)) - Duración: $duracion segundos" >> "$ruta_log"
}

# Función principal del juego
function jugar_ahorcado {
    inicializar_juego

    while true; do
        clear
        imprimir_estado_juego

        read -p "Ingresa una letra: " letra
        procesar_intentos $letra

        if [[ "$palabra_secreta" == "$palabra_mostrada" ]]; then
            echo "¡Felicidades! Has adivinado la palabra: $palabra_secreta"
            registrar_partida
            exit 0
        fi

        if [[ $intentos_restantes -eq 0 ]]; then
            echo "¡Oh no! Has perdido. La palabra secreta era: $palabra_secreta"
            registrar_partida
            exit 0
        fi
    done
}

# Iniciar el juego del ahorcado
jugar_ahorcado
~~~
