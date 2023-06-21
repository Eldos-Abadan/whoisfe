from django.shortcuts import render

def createNCViews(request):
    return render(request, "createNC/createNC.html")