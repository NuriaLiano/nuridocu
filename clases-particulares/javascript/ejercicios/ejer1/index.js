function sumar(a, b) {
    return a + b;
  }
  
  function restar(a, b) {
    return a - b;
  }
  
  function multiplicar(a, b) {
    return a * b;
  }
  
  function dividir(a, b) {
    return a / b;
  }
  
  function calcularPorcentaje(a, b) {
    return (a * 100) / b;
  }
  
  function validarNumeros(numero1, numero2) {
    if (isNaN(numero1) || isNaN(numero2)) {
      return false;
    }
    return true;
  }
  
  function calcular() {
    var numero1 = parseInt(document.getElementById("numero1").value);
    var numero2 = parseInt(document.getElementById("numero2").value);
    
    if (!validarNumeros(numero1, numero2)) {
      document.getElementById("resultado").innerHTML = "Por favor, ingresa números válidos.";
      return;
    }
    
    var suma = sumar(numero1, numero2);
    var resta = restar(numero1, numero2);
    var producto = multiplicar(numero1, numero2);
    var division = dividir(numero1, numero2);
    var porcentaje = calcularPorcentaje(numero1, numero2);
    
    mostrarResultado(suma, resta, producto, division, porcentaje);
  }
  
  function mostrarResultado(suma, resta, producto, division, porcentaje) {
    document.getElementById("resultado").innerHTML = "Suma: " + suma + "<br>"
                                                      + "Resta: " + resta + "<br>"
                                                      + "Producto: " + producto + "<br>"
                                                      + "División: " + division.toFixed(2) + "<br>"
                                                      + "Porcentaje: " + porcentaje.toFixed(2) + "%";
  }
  
  function realizarCalculos() {
    calcular();
  }