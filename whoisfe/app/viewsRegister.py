from django.shortcuts import render, redirect
import datetime
from whoisfe.settings import *


def registerViews(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        date_joined = datetime.date.today()

        if password != confirm_password:
            error_message = 'Нууц үгээ зөв давтан оруулна уу.'
            return render(request, 'register/register.html', {'error_message': error_message})

        myCon = connectDB()
        userCursor = myCon.cursor()
        userCursor.execute('INSERT INTO "user" ("firstName", "lastName", "email", "pass", "userName", "date")'
                       'VALUES (%s, %s, %s, %s, %s, %s)',
                       (first_name, last_name, email, password, user_name, date_joined))
        myCon.commit()
        userCursor.close()
        disconnectDB(myCon)

        return redirect('homeView')

    return render(request, 'register/register.html')
