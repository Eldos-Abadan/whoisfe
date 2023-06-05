from django.shortcuts import render

# Create your views here.

def homeView(request):
    return render(request,"home/mycv.html")


def week1View(request):
    return render(request,"week1/tm1.html")

def magnai(request):
    return render(request,"week1/Magnai/index.html")

def Eldos(request):
    return render(request,"week1/Eldos/index.html")

def HaTuguldur(request):
    return render(request,"week1/HaTuguldur/web cv.html")