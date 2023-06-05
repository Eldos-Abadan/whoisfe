from django.shortcuts import render

def homeView(request):
    return render(request,"home/mycv.html")


def week1View(request):
    return render(request,"week1/tm1.html")

def magnai(request):
    return render(request,"week1/Magnai/index.html")
def tuugii(request):
    return render(request,"week1/HaTuguldur/webcv.html")
def odke(request):
    return render(request,"week1/odontungalag/odkeCV.html")