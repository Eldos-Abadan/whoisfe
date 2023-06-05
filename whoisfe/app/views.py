from django.shortcuts import render



def homeView(request):
    return render(request,"week1/bumaa/cv.html")


# def week1View(request):
#     return render(request,"week1/Magnai/index.html")
def week1View(request):
    return render(request,"week1/Ha.Tuguldur/webcv.html")
