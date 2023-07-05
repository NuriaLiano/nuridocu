window.onload = function() {
  let numeroAleatorio;
  let intentos = 0;

  function reiniciarJuego() {
    numeroAleatorio = Math.floor(Math.random() * 100) + 1;
    intentos = 0;
    document.getElementById('mensaje').innerHTML = '';
    document.getElementById('intentos').innerHTML = '';
    document.getElementById('inputNumero').value = '';
    document.getElementById('botonAdivinar').disabled = false;
  }

  function adivinarNumero() {
    let inputNumero = document.getElementById('inputNumero');
    let mensajeElemento = document.getElementById('mensaje');
    let intentosElemento = document.getElementById('intentos');
    let numeroUsuario = parseInt(inputNumero.value);

    if (isNaN(numeroUsuario) || numeroUsuario < 1 || numeroUsuario > 100) {
      mensajeElemento.innerHTML = 'Ingresa un número válido entre 1 y 100.';
      return;
    }

    intentos++;
    intentosElemento.innerHTML = 'Intento ' + intentos + ': ';

    if (numeroUsuario === numeroAleatorio) {
      mensajeElemento.innerHTML = '¡Felicidades! ¡Has adivinado el número!';
      document.getElementById('botonAdivinar').disabled = true;
    } else if (numeroUsuario < numeroAleatorio) {
      mensajeElemento.innerHTML = 'El número que estás buscando es mayor.';
    } else {
      mensajeElemento.innerHTML = 'El número que estás buscando es menor.';
    }
  }

  // Asignar las funciones a los eventos de los botones
  document.getElementById('botonAdivinar').onclick = adivinarNumero;
  document.getElementById('botonReiniciar').onclick = reiniciarJuego;
};