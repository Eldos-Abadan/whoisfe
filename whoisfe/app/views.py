from django.shortcuts import render



def homeView(request):
    return render(request, "home/mycv.html")


def week1View(request):
    return render(request, "week1/tm1.html")


def magnai(request):
    return render(request, "week1/Magnai/index.html")


def HaTuguldur(request):
    return render(request, "week1/HaTuguldur/webcv.html")


def odke(request):
    return render(request, "week1/odontungalag/odkeCV.html")


def xuslen(request):
    return render(request, "week1/Xuslen/XuslnCV.html")


def sarnai(request):
    return render(request, "week1/Sarnai/index.html")


def enkhzul(request):
    return render(request, "week1/Enkhzul/index.html")

def zndra(request):
    return render(request, "week1/Zndra/cv.html")

def Bayrbat(request):
    return render(request,"week1/Bayrbat/nuur.html")

def eldos(request):
    return render(request,"week1/Eldos/index.html")
def home(request):
    return render(request, "week1/home1.html")

def bilguun(request):
    return render(request, "week1/N.bilguun/cv.html")

def nomin(request):
    return render(request,"week1/Nomin-Erdene(2)/index.html")

def Odonkhuu(request):
    return render(request,"week1/Odonkhuu/index.html")
def Tudu(request):
    return render(request,"week1/Tudu/index.html")

def Nomio1(request):
    return render(request,"week1/Nomio1/cv.html")

def Tserenbaatar(request):
    return render(request,"week1/Tserenbaatr/index.html")

def bumaa(request):
    return render(request,"week1/bumaa/cv.html")

def olzii(request):
    return render(request,"week1/olzii/index.html")

