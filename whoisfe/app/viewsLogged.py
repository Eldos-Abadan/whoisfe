from django.shortcuts import render


def loginViews(request):
    return render(request,"login/homelog.html")

def loginhome(request):
    return render(request,"login/homelog.html")