from django.shortcuts import render, redirect
import datetime
import hashlib
from django.contrib import messages
from whoisfe.settings import *


def registerViews(request):
    if request.method == 'POST':
        try:
            jsons = request.POST.dict()
            required_fields = ["first_name", "last_name", "email", "user_name", "password", "confirm_password"]
            if not reqValidation(jsons, required_fields):
                error_message = 'Fields are missing or invalid'
                messages.error(request, error_message)

            first_name = jsons['first_name']
            last_name = jsons['last_name']
            email = jsons['email']
            user_name = jsons['user_name']
            password = jsons['password']
            passw = mandakhHash(password)
            confirm_password = jsons['confirm_password']
            date_joined = datetime.date.today()

            if password != confirm_password:
                error_message = 'Нууц үгээ зөв давтан оруулна уу.'
                messages.error(request, error_message)

            if emailExists(email):
                error_message = 'Email already exists'
                messages.error(request, error_message)

            if userNameExists(user_name):
                error_message = 'Username already exists'
                messages.error(request, error_message)

            # Perform email verification
            if not isEmailValid(email):
                error_message = 'Invalid email address'
                messages.error(request, error_message)

            if messages.get_messages(request):
                return render(request, 'register/register.html')

            myCon = connectDB()
            userCursor = myCon.cursor()
            userCursor.execute('INSERT INTO "f_user" ("firstName", "lastName", "email", "pass", "userName", "date")'
                               'VALUES (%s, %s, %s, %s, %s, %s)',
                               (first_name, last_name, email, passw, user_name, date_joined))
            myCon.commit()
            userCursor.close()
            disconnectDB(myCon)

            return redirect('loginViews')

        except Exception as e:
            error_message = 'Database error'
            messages.error(request, error_message)

    return render(request, 'register/register.html')
