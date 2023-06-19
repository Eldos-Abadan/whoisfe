from django.shortcuts import render

# Create your views here.

def loggedViews(request):
    return render(request,"home/mycv.html")


def week1View(request):
    return render(request,"week1/tm1.html")

def registerViews(request):
    return render(request,"register/register.html")

def dashboardViews(request):
    return render(request, "dashboard/dashboard.html")

def perinfoViews(request):
    return render(request,"Profile/1.html")

def myNCViews(request):
    return render(request,"myNC/myNC.html")

def createCVViews(request):
    return render(request,"createCV/createCV.html")

def guideViews(request):
    return render(request, "guide/guide.html")