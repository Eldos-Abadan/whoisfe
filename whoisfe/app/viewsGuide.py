from django.shortcuts import render

def guideViews(request):
    return render(request, "guide/guide.html")