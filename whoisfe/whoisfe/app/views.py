from django.shortcuts import render

# Create your views here.

def loggedViews(request):
    return render(request,"home/mycv.html")


def week1View(request):
    return render(request,"week1/tm1.html")

def registerViews(request):
    return render(request,"register/register.html")
