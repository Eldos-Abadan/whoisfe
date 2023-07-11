from django.shortcuts import render
import json
import requests
from whoisfe.settings import *

def forgetView(request):
    # forgotPasswordRequest, forgotPasswordRequestSubmit
    # forgotPasswordConfirm, forgotPasswordConfirmSubmit
    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["aldaaniiMedegdel"] = ""
    if(request.method=="POST"):                
        if("forgotPasswordRequestSubmit" in request.POST):
            email = request.POST.get("email")       
            pass1 = request.POST.get("pass1")
            pass2 = request.POST.get("pass2")
            if(pass1 != pass2):
                htmlRuuDamjuulahUtguud["aldaaniiMedegdel"] = "Нууц үгнүүд ялгаатай байна"
            else:
                requestJSON = {
                    "email": email,
                    "newPassword": mandakhHash(pass1)
                }
                r = requests.get("http://whoisb.mandakh.org/resetPassword/",
                                data=json.dumps(requestJSON),
                                headers={'Content-Type': 'application/json'})
                response_json = r.json()
                resultMessage = response_json.get('responseText')
                htmlRuuDamjuulahUtguud["aldaaniiMedegdel"] = resultMessage

        if("forgotPasswordConfirmSubmit" in request.POST):
            verifyCode = request.POST.get("verifyCode")
            requestJSON = {                
                "verifyCode": verifyCode
            }
            r = requests.get("http://whoisb.mandakh.org/verifyCode/",
                            data=json.dumps(requestJSON),
                            headers={'Content-Type': 'application/json'})
            response_json = r.json()
            resultMessage = response_json.get('responseText')
            htmlRuuDamjuulahUtguud["aldaaniiMedegdel"] = resultMessage            

    else:
        htmlRuuDamjuulahUtguud["aldaaniiMedegdel"] = "ene huudas shiljij orj irjee"
    return render(request, "forget/Forget.html",htmlRuuDamjuulahUtguud)