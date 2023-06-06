from django.shortcuts import render


def homeView(request):
    return render(request, "home/mycv.html")


def week1View(request):
    return render(request, "week1/tm1.html")


def magnai(request):
    return render(request, "week1/Magnai/index.html")


def tuugii(request):
    return render(request, "week1/HaTuguldur/webcv.html")


def odke(request):
    return render(request, "week1/odontungalag/odkeCV.html")


def xuslen(request):
    return render(request, "week1/Xuslen/XuslnCV.html")


def sarnai(request):
    return render(request, "week1/Sarnai/index.html")


def enkhzul(request):
<<<<<<< Updated upstream
    return render(request, "week1/Enkhzul/index.html")

def zndra(request):
    return render(request, "week1/Zndra/cv.html")

def home(request):
    return render(request, "week1/home1.html")
=======
    return render(request,"week1/Enkhzul/index.html")
def Bayrbat(request):
    return render(request,"week1/Bayrbat/nuur.html")
>>>>>>> Stashed changes

def eldos(request):
    return render(request,"week1/Eldos/index.html")