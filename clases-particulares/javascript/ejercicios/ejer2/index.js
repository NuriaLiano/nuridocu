
addEventListener('load', main, false);
// Ejercicio: Calculadora básica

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
if (opcion === 1) {
  var suma = numero1 + numero2;
  console.log("El resultado de la suma es: " + suma);
} else if (opcion === 2) {
  var resta = numero1 - numero2;
  console.log("El resultado de la resta es: " + resta);
} else if (opcion === 3) {
  var multiplicacion = numero1 * numero2;
  console.log("El resultado de la multiplicación es: " + multiplicacion);
} else if (opcion === 4) {
  // Verificar si el segundo número es cero para evitar división entre cero
  if (numero2 === 0) {
    console.log("Error: No se puede dividir entre cero.");
  } else {
    var division = numero1 / numero2;
    console.log("El resultado de la división es: " + division);
  }
} else {
  console.log("Opción inválida. Por favor, selecciona una opción válida.");
}