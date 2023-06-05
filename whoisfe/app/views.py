from django.shortcuts import render

# Create your views here.

def homeView(request):
    return render(request,"week1/bumaa/cv.html")


def week1View(request):
    return render(request,"week1/bumaa/cv.html")

