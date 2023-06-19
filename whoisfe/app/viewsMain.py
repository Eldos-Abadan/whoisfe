from django.shortcuts import render


def homeViews(request):
    return render(request,"home/home.html")