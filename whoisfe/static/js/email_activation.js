function sendActivationEmail(event) {
    event.preventDefault(); // Prevent form submission
  
    var email = document.getElementById('email').value;
  
    // Generate a unique activation code
    var activationCode = generateActivationCode();
  
    // Compose the activation email
    var subject = "Activate your account";
    var message = "Please click the following link to activate your account:\n\n";
    message += "http://example.com/activate.html?code=" + activationCode;
  
    // Use SendGrid API to send the activation email
    sendEmail(email, subject, message)
      .then(function () {
        alert("Activation link sent to your email address!");
      })
      .catch(function (error) {
        console.error("Error sending activation email:", error);
      });
  }
  
  function generateActivationCode() {
    // Generate a random activation code as per your requirements
    // For simplicity, we'll use a basic code generation method here
    var code = "";
    var characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    var codeLength = 10;
    for (var i = 0; i < codeLength; i++) {
      code += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return code;
  }
  
  function sendEmail(email, subject, message) {
    var sendGridAPIKey = "YOUR_SENDGRID_API_KEY";
    var sendGridURL = "https://api.sendgrid.com/v3/mail/send";
  
    var emailData = {
      personalizations: [
        {
          to: [{ email: email }],
          subject: subject
        }
      ],
      from: { email: "your@email.com" },
      content: [{ type: "text/plain", value: message }]
    };
  
    return axios.post(sendGridURL, emailData, {
      headers: {
        Authorization: "Bearer " + sendGridAPIKey,
        "Content-Type": "application/json"
      }
    });
  }
  