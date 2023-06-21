from django.shortcuts import render

def myCVViews(request):
    return render(request, "myCV/myCV.html")