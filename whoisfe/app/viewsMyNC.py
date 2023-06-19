from django.shortcuts import render

def myNCViews(request):
    return render(request, "myNC/myNC.html")