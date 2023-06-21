from django.shortcuts import render,redirect
from whoisfe.settings import *

def profileViews(request):
    checkSession(request)  
    if request.session['beegii'] ==0:        
        return redirect("homeView")    
    htmlRuuDataDamjuulah = {}
    htmlRuuDataDamjuulah = request.session['userData']
    return render(request, "Profile/1.html",htmlRuuDataDamjuulah)