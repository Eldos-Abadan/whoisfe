from django.shortcuts import render

def loggedViews(request):
    return render(request,"logged/homelog.html")

def createNCViews(request):
    return render(request,"createNC/createNC.html")

def createCVViews(request):
    return render(request,"createCV/createCV.html")

def dashboardViews(request):
    return render(request, "dashboard/dashboard.html")

def myNCViews(request):
    return render(request, "myNC/myNC.html")

# def myCVViews(request):
#     return render(request, "myCV/myCV.html")

# def walletViews(request):
#     return render(request, "wallet/wallet.html")

def guideViews(request):
    return render(request, "guide/guide.html")

# def favTemplatesViews(request):
#     return render(request, "favTemplates/favTemplates.html")

def profileViews(request):
    return render(request, "Profile/1.html")





