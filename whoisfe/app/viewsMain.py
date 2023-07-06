from django.shortcuts import render,redirect
from whoisfe.settings import *
import requests
import json

## log out #########################################################
def homeLogoutView(request): 
    checkSession(request)    
    request.session['beegii'] = 0
    return redirect("homeView")
#####################################################################

## home #########################################################
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
############################################################

## wallet ##################################################

# balance kharakh # 
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
# end balance kharakh #
# Gvilgee khiikhed 3
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
    for i in range(0, len(htmlRuu["userData"])):
      #  htmlRuu["userData"]["dugaar"] = i + 1
       htmlRuu["userData"][i]["dugaar"] = str(i + 1)
    return render(request, "wallet/wallet1.html", htmlRuu)
## end guilgee hiihed ########################################################
##############################################################################

## guide #####################################################################
def guideViews(request):
    return render(request, "guide/guide.html")
##############################################################################