from   django.shortcuts import render,redirect
from   whoisfe.settings import *
import requests 
import json
import hashlib
    


    
def homeLogoutView(request): 
    checkSession(request)    
    request.session['beegii'] = 0
    return redirect("loginViews")

def loginViews(request):
    checkSession(request)
    if request.session.get('beegii') != 0:
        return redirect("dashboardViews")

    zahia = {}
    aldaaniiMedegdel = ""

    if request.method == "POST":
        myName = request.POST.get("myName")
        myPass = request.POST.get("myPass")
        passs = mandakhHash(myPass)

        requestJSON = {
            "name": myName,
            "pass": passs
        }
    
        required_fields = ["name", "pass"]
        if not reqValidation(requestJSON, required_fields):
            error_message = 'Fields are missing or invalid'
            zahia["error_message"] = error_message
            return render(request, 'login/login.html', zahia)

        try:
            r = requests.get("http://whoisb.mandakh.org/userLogin/",
                             data=json.dumps(requestJSON),
                             headers={'Content-Type': 'application/json'})
            response_json = r.json()
            resultCode = response_json.get('responseCode')
            resultMessage = response_json.get('responseText')
       
            if resultCode == 200:
                request.session['beegii'] = 1
                request.session['userId'] = response_json.get('userData')["id"]
                return redirect("dashboardViews")
            else:
                aldaaniiMedegdel = resultMessage

        except requests.exceptions.RequestException as e:
            aldaaniiMedegdel = str(e)

    zahia["aldaaniiMedegdel"] = aldaaniiMedegdel

    return render(request, "login/login.html", zahia)