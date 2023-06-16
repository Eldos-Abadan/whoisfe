from django.shortcuts import render


def loginHomeLogViews(request):
    return render(request,"logged/homeLog.html")