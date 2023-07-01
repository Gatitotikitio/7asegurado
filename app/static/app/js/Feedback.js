document.getElementById('feedbackForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
  
    // Get form values
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;
  
    // Perform form validation
    if (name.trim() === '' || email.trim() === '' || message.trim() === '') {
      alert('Por favor, complete todos los campos.');
      return;
    }
  
    // Submit form data to server (AJAX request or other actions)
    // ...
  
    // Reset form after submission
    document.getElementById('feedbackForm').reset();
  
    alert('¡Gracias por tu feedback!');
  });
  