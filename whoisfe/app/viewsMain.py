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


# balance kharakh
def walletView(request): 
  # Check session
  checkSession(request)
  if request.session['beegii'] == 0:
      return redirect("homeView")
  # getTransactionLog
  htmlRuu = {}
  htmlRuu["aldaa"] = ""
  serviceZam = "http://whoisb.mandakh.org/getTransactionLog/"
  id = request.session['userId']
  requestJSON = {
     "user_id" : str(id)
  }
  r = requests.get(serviceZam,
                            data=json.dumps(requestJSON),
                            headers={'Content-Type': 'application/json'} )
  data = r.json()
  htmlRuu["vldegdel"] = data["dansniiUldegdel"]
  return render(request, "wallet/wallet.html", htmlRuu)
##############################################################

# Gvilgee khiikhed
def wallet1View(request): 
    # Check session
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    htmlRuu = {}
    htmlRuu["aldaa"] = ""
    # makeTransaction
    if request.method == "POST":
        serviceZam = "http://whoisb.mandakh.org/makeTransaction/"
        utga = request.POST.get("utga")
        hend = request.POST.get("hend")
        amount = request.POST.get("amount")

        requestJSON = {
          "from": request.session['userId'],
          "target": hend,
          "amount": str(amount),
          "utga": utga
        }
        r = requests.post(serviceZam,
                                  data=json.dumps(requestJSON),
                                  headers={'Content-Type': 'application/json'} )
        data = r.json()
        if data["responseCode"] == 200:
            htmlRuu["responseText"] = data["responseText"]
        else:
            htmlRuu["aldaa"] = data["responseText"]
    #  end makeTransaction
    serviceZam = "http://whoisb.mandakh.org/getTransactionLog/"
    id = request.session['userId']
    requestJSON = {
      "user_id" : str(id)
    }
    r = requests.get(serviceZam,
                              data=json.dumps(requestJSON),
                              headers={'Content-Type': 'application/json'} )
    data = r.json()
    htmlRuu["vldegdel"] = data["dansniiUldegdel"]
    htmlRuu["userData"] = data["guilgee"]
    return render(request, "wallet/wallet1.html", htmlRuu)
##########################################################

def justCVViews(request): 
  return render(request, "templates/just.html")

def justNCViews(request): 
  return render(request, "templates/bc.html")

def odkeBcViews(request): 
  return render(request, "templates/odkeBc.html")

def odkeBcViews(request): 
  return render(request, "templates/odkeBc.html")

def mainNCViews(request): 
  return render(request, "templates/main.html")

def enkuCVViews(request): 
  return render(request, "templates/enku.html")

def enku2CVViews(request): 
  return render(request, "templates/enku2.html")