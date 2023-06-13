from django.shortcuts import render

def registerViews(request):
    return render(request, "register/register.html")


