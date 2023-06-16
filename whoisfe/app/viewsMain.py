from django.shortcuts import render,redirect
from whoisfe.settings import *
import json

    

def homeLogoutView(request): 
    checkSession(request)    
    request.session['beegii'] = 0
    return redirect("homeView")
#   homeLogoutView

def homeView(request):    
    checkSession(request)    
    if request.session['beegii'] != 0:
        return redirect("perinfoViews")
    zahia = {}
    aldaaniiMedegdel = ""
    # хэрвээ форм.пост бол:
    #     үр дүн  = нэвтрэх сервис(нэр, нууц үг)
    #     хэрвээ үр дүн.responseCode == 200
    #         request.session['beegii'] = 1
    #         return redirect("perinfoViews")
    #     else:
    #         aldaaniiMedegdel = "нэр нууц үг буруу"
    if(request.method == "POST"):
        myName = request.POST["myName"]
        myPass = request.POST["myPass"]
        requestJSON = {}
        requestJSON["name"] = myName
        requestJSON["pass"] = myPass

        r = requests.get("http://whoisb.mandakh.org/userLogin/",
                            data=json.dumps(requestJSON),
                            headers={'Content-Type': 'application/json'} )
        # print(r.json())
        resultCode = r.json()['responseCode']
        resultMessage = r.json()['responseText']
        if(resultCode == 200):
            request.session['beegii'] = 1
            return redirect("perinfoViews")
        else:
            aldaaniiMedegdel = resultMessage        

    zahia["aldaaniiMedegdel"] = aldaaniiMedegdel

    return render(request, "home/mycv.html",zahia)