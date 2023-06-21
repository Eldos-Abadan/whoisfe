from django.shortcuts import render



def forgetView(request):
    return render(request, "forget/Forget.html")


