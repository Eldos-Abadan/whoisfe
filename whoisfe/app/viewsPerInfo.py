from django.shortcuts import render,redirect
from whoisfe.settings import *

def perinfoViews(request):
    checkSession(request)  
    if request.session['beegii'] ==0:        
        return redirect("homeView")
    return render(request, "Profile/1.html")