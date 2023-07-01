document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
  
    // Get form values
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;
  
    // Reset error messages
    var errorMessages = document.getElementsByClassName('error-message');
    for (var i = 0; i < errorMessages.length; i++) {
      errorMessages[i].textContent = '';
    }
  
    // Perform form validation
    if (password !== confirmPassword) {
      document.getElementById('confirmPasswordErrorMessage').textContent = 'Las contraseñas no coinciden';
    } else {
      // Form is valid, proceed with registration logic
      alert('Registro exitoso');
      // Add your registration logic here
    }
  });
  