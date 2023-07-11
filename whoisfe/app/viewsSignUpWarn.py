from django.shortcuts import render,redirect
from django.urls import reverse

def signUpWarnViews(request):
    if request.method == 'POST':

        return redirect(reverse('loginViews'))
    else:
        return render(request, "register/signUpwarning.html")