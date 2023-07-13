addEventListener("load", setupEventListeners);

function calculateDiscount(event) {
    event.preventDefault();

/*La función event.preventDefault() se utiliza en JavaScript para detener el comportamiento predeterminado de un evento. 
Cuando se produce un evento, como hacer clic en un enlace o enviar un formulario, 
el navegador realiza una acción predeterminada asociada a ese evento, como seguir el enlace o recargar la página.

Al llamar a event.preventDefault(), se evita que el navegador realice la acción predeterminada asociada al evento. 
Esto es útil cuando deseas personalizar o controlar completamente el comportamiento de un evento sin que se realice la acción predeterminada.

Un ejemplo común de uso de preventDefault() es en formularios HTML. Por defecto, cuando se envía un formulario, el navegador recarga la página. 
Sin embargo, al llamar a preventDefault() en el evento submit del formulario, 
puedes evitar la recarga de la página y controlar el envío del formulario mediante JavaScript. 
Esto te permite realizar validaciones personalizadas, enviar datos mediante AJAX u otras acciones antes de que se produzca la recarga de la página. */


    var originalPriceInput = document.getElementById("originalPrice");
    var discountPercentageInput = document.getElementById("discountPercentage");
    var resultElement = document.getElementById("result");
  
    var originalPrice = parseFloat(originalPriceInput.value);
    var discountPercentage = parseFloat(discountPercentageInput.value);
  
    var discountAmount = originalPrice * (discountPercentage / 100);
    var finalPrice = originalPrice - discountAmount;
  
    resultElement.textContent = "Precio Final con Descuento: " + finalPrice.toFixed(2) + " €";
  }
  
  function setupEventListeners() {
    var discountForm = document.getElementById("discountForm");
    discountForm.addEventListener("submit", calculateDiscount);
  }
  