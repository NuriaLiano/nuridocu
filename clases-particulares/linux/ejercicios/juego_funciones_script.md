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
~~~
