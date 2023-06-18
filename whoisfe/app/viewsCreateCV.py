from django.shortcuts import render

def createCVViews(request):
    return render(request, "createCV/createCV.html")