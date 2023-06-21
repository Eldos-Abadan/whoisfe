from django.shortcuts import render

def favoriteView(request):
    return render(request, "favoriteCV/favoriteCV.html")