from django.shortcuts import render


def loginhomelogViews(request):
    return render(request,"login/homelog.html")