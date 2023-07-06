from django.shortcuts import render

def myCVViews(request):
    return render(request, "my/myCV.html")

def myNCViews(request):
    return render(request, "my/myNC.html")