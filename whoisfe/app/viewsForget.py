from django.shortcuts import render



def forgetView(request):
    return render(request, "login/Forget.html")


