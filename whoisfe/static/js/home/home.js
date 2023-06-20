function myFunction() {
    window.location.href="{% url 'login'%}";
  }
  function myFunctionSignup(){
      window.location.href="{% url 'register'%}";
  }