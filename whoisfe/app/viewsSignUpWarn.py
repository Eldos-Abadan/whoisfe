from django.shortcuts import render

def signUpWarnViews(request):
    return render(request, "register/signUpwarning.html")