function validateForm() {
    var name = document.forms["contactForm"]["fullname"].value;
    var email = document.forms["contactForm"]["email"].value;
    var phone = document.forms["contactForm"]["phone"].value;
    var affair = document.forms["contactForm"]["affair"].value;
    var message = document.forms["contactForm"]["message"].value;
  
    if (name == "") {
      alert("Por favor, ingrese su nombre.");
      return false;
    }
  
    if (email == "") {
      alert("Por favor, ingrese su correo electrónico.");
      return false;
    } else if (!email.includes("@")) {
      alert("Por favor, ingrese un correo electrónico válido.");
      return false;
    }
  
    if (phone == "") {
      alert("Por favor, ingrese su número de teléfono.");
      return false;
    }
  
    if (affair == "") {
      alert("Por favor, ingrese el asunto de su mensaje.");
      return false;
    }
  
    if (message == "") {
      alert("Por favor, ingrese su mensaje.");
      return false;
    }
  
    event.preventDefault();
    return false;
  }
  