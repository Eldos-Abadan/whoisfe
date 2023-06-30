from django.shortcuts import render,redirect
from whoisfe.settings import *
import requests
import json

def homeLogoutView(request): 
    checkSession(request)    
    request.session['beegii'] = 0
    return redirect("homeView")
#   homeLogoutView

def homeView(request):    
    checkSession(request)    
    if request.session['beegii'] != 0:
        return redirect("dashboardViews")
    zahia = {}
    aldaaniiMedegdel = ""
    # хэрвээ форм.пост бол:
    #     үр дүн  = нэвтрэх сервис(нэр, нууц үг)
    #     хэрвээ үр дүн.responseCode == 200
    #         request.session['beegii'] = 1
    #         return redirect("profileMain")
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
            return redirect("profileMain")
        else:
            aldaaniiMedegdel = resultMessage        

    zahia["aldaaniiMedegdel"] = aldaaniiMedegdel

    return render(request, "home/home.html",zahia)


def walletView(request): 
  return render(request, "wallet/wallet.html")

def wallet1View(request): 
  return render(request, "wallet/wallet1.html")

def justCVViews(request): 
  return render(request, "templates/just.html")

def justNCViews(request): 
  return render(request, "templates/bc.html")

def odkeBcViews(request): 
  return render(request, "templates/odkeBc.html")
