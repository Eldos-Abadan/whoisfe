from django.shortcuts import render


def loginViews(request):
    return render(request, "login/login.html")

def homeViews(request):
    return render(request, "home/home.html")

def registerViews(request):
    return render(request, "register/register.html")

def forgetViews(request):
    return render(request, "forget/forget.html")


