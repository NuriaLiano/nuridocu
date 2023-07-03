// Función para realizar la suma
function sumar(num1, num2) {
    return num1 + num2;
  }
  
  // Función para realizar la resta
  function restar(num1, num2) {
    return num1 - num2;
  }
  
  // Función para realizar la multiplicación
  function multiplicar(num1, num2) {
    return num1 * num2;
  }
  
  // Función para realizar la división
  function dividir(num1, num2) {
    if (num2 === 0) {
      return "Error: No se puede dividir entre cero.";
    }
    return num1 / num2;
  }
  
  // Pedir al usuario que ingrese dos números
  var numero1 = parseInt(prompt("Ingresa el primer número:"));
  var numero2 = parseInt(prompt("Ingresa el segundo número:"));
  
  // Mostrar un menú de opciones
  console.log("Selecciona una operación:");
  console.log("1. Suma");
  console.log("2. Resta");
  console.log("3. Multiplicación");
  console.log("4. División");
  
  // Solicitar al usuario que elija una opción
  var opcion = parseInt(prompt("Ingresa el número de la operación que deseas realizar:"));
  
  // Realizar la operación según la opción seleccionada
  switch (opcion) {
    case 1:
      var resultado = sumar(numero1, numero2);
      console.log("El resultado de la suma es: " + resultado);
      break;
    case 2:
      var resultado = restar(numero1, numero2);
      console.log("El resultado de la resta es: " + resultado);
      break;
    case 3:
      var resultado = multiplicar(numero1, numero2);
      console.log("El resultado de la multiplicación es: " + resultado);
      break;
    case 4:
      var resultado = dividir(numero1, numero2);
      console.log("El resultado de la división es: " + resultado);
      break;
    default:
      console.log("Opción inválida. Por favor, selecciona una opción válida.");
      break;
  }