from django.shortcuts import render, redirect
import datetime
import json
import requests
from django.contrib import messages
from whoisfe.settings import *
from django.urls import reverse


def registerViews(request):
    if request.method == 'POST':
        try:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            user_name = request.POST.get('user_name')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            date_joined = datetime.date.today()

            # Perform any necessary validations or data processing

            if password != confirm_password:
                error_message = 'Passwords do not match'
                messages.error(request, error_message)
                return render(request, 'register/register.html')

            if emailExists(email):
                error_message = 'Email already exists'
                messages.error(request, error_message)
                return render(request, 'register/register.html')

            if userNameExists(user_name):
                error_message = 'Username already exists'
                messages.error(request, error_message)
                return render(request, 'register/register.html')

            # Perform email validation
            if not isEmailValid(email):
                error_message = 'Invalid email address'
                messages.error(request, error_message)
                return render(request, 'register/register.html')

            # Hash the password
            hashed_password =  mandakhHash(password) 
           
            # Prepare the request JSON data
            request_data = {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "pass": hashed_password,
                "userName": user_name
            }
            # Make the request to userRegisterView service
            response = requests.post("http://whoisb.mandakh.org/userRegister/",
                                     data=json.dumps(request_data),
                                     headers={'Content-Type': 'application/json'})

            if response.status_code == 200:
                # Registration success
                response_data = response.json()
                messages.success(request, response_data['responseText'])
                return redirect('loginViews')
            else:
                # Registration failed
                error_message = 'Registration failed: ' + response.content.decode()
                messages.error(request, error_message)
                return render(request, 'register/register.html')

        except Exception as e:
            error_message = 'Error occurred: ' + str(e)
            messages.error(request, error_message)
            return render(request, 'register/register.html')
    return render(request, 'register/register.html')
### email verify #########################################################
def EmailVerView(request, otp):
    try:
        response = requests.get(f"http://whoisb.mandakh.org/verifyEmail/{otp}/")
        if response.status_code == 200:
            response_data = response.json()
            messages.success(request, response_data['responseText'])
            # Render an additional template if needed
            return render(request, 'register/emailVerify.html')
        else:
            error_message = 'Email verification failed'
            messages.error(request, error_message)
            return redirect('loginViews')

    except Exception as e:
        error_message = 'Error occurred: ' + str(e)
        messages.error(request, error_message)
        return redirect('loginViews') 
#### sign up warning #####################################################
def signUpWarnViews(request):
    if request.method == 'POST':

        return redirect(reverse('loginViews'))
    else:
        return render(request, "register/signUpwarning.html")