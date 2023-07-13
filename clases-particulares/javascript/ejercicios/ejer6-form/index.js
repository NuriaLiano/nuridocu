function collectFormData(event) {
    event.preventDefault();
  
    var nameInput = document.getElementById("name");
    var emailInput = document.getElementById("email");
    var messageInput = document.getElementById("message");
  
    var name = nameInput.value;
    var email = emailInput.value;
    var message = messageInput.value;
  
    console.log("Nombre:", name);
    console.log("Correo Electrónico:", email);
    console.log("Mensaje:", message);
  
    showConfirmation();
  }
  
  function showConfirmation() {
    window.alert("Datos enviados");
  }
  
  function setupEventListeners() {
    var contactForm = document.getElementById("contactForm");
    contactForm.addEventListener("submit", collectFormData);
  }
  
  window.addEventListener("load", setupEventListeners);