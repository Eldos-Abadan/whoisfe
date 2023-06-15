from django.shortcuts import render,redirect
from whoisfe.settings import *

    

def homeView(request):    
    checkSession(request)    
    if request.session['beegii'] != 0:
        return redirect("perinfoViews")
    
    return render(request, "home/mycv.html")