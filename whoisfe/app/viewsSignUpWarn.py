from django.shortcuts import render

def signUpWarViews(request):
    return render(request, "register/signUpwarning.html")