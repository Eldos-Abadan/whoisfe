from django.shortcuts import render, redirect
import datetime
import hashlib
from django.contrib import messages
from whoisfe.settings import *

def mandakhHash(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def registerViews(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        passw = mandakhHash(password)
        confirm_password = request.POST.get('confirm_password')
        date_joined = datetime.date.today()

        if password != confirm_password:
            error_message = 'Нууц үгээ зөв давтан оруулна уу.'
            messages.error(request, error_message)
            context['error_message'] = error_message
            return render(request, 'register/register.html', context)

        if emailExists(email):
            context = {}
            error_message = 'Email already exists'
            context['error_message'] = error_message
            return render(request, 'register/register.html', context)

        if userNameExists(user_name):
            context = {}
            error_message = 'Username already exists'
            context['error_message'] = error_message
            return render(request, 'register/register.html', context)

        myCon = connectDB()
        userCursor = myCon.cursor()
        userCursor.execute('INSERT INTO "user" ("firstName", "lastName", "email", "pass", "userName", "date")'
                           'VALUES (%s, %s, %s, %s, %s, %s)',
                           (first_name, last_name, email, passw, user_name, date_joined))
        myCon.commit()
        userCursor.close()
        disconnectDB(myCon)

        return redirect('homeViews')

    return render(request, 'register/register.html')
