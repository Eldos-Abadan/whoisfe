from django.shortcuts import render,redirect
from whoisfe.settings import *

def dashboardViews(request):
    checkSession  (request)  
    if request.session ['beegii'] ==0:        
        return redirect("homeViews")
    return render(request, "dashboard/dashboard.html")