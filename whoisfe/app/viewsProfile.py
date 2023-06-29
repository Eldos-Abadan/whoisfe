from django.shortcuts import render, redirect
import json
import requests
from whoisfe.settings import *
from    django.http                  import HttpResponse


def profileMain(request):
    #  Энэ хуудасруу орохтой холбоотой заавал байх шалгалт
    checkSession(request)  
    if request.session['beegii'] == 0:        
        return redirect("homeView")    
    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"
    #######################################################

    if request.method=="POST":
        if("userInfoUpdateSubmit" in request.POST):
            # start userInfoUpdateSubmit

            serviceHayag = "http://whoisb.mandakh.org/userInfoUpdate/"
            userName = request.POST.get("userName")
            firstName = request.POST.get("firstName")
            lastName = request.POST.get("lastName")
            requestJSON = {
                "id": request.session['userId'],
                "userName": userName,
                "firstName": firstName,
                "lastName": lastName
            }
            
            r = requests.get(serviceHayag,
                            data=json.dumps(requestJSON),
                            headers={'Content-Type': 'application/json'})
            
            responseJson = r.json()                        
            htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
            if(responseJson["responseCode"] == 200):
                htmlRuuDamjuulahUtguud["textColor"] = "#00ff00"
            else:
                htmlRuuDamjuulahUtguud["textColor"] = "#ff0000"
            # end userInfoUpdateSubmit
        if("changePassSubmit" in request.POST):
            if request.POST.get("new")==request.POST.get("new2"):
                serviceHayag = "http://whoisb.mandakh.org/changePass/"
                requestJSON = {
                    "id": request.session['userId'],
                    "oldpass": mandakhHash(request.POST.get("old")),
                    "newpass": mandakhHash(request.POST.get("new")),
                }
                r = requests.get(serviceHayag,
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
                responseJson = r.json()
                htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
            else:
                htmlRuuDamjuulahUtguud["responseText"] = "zailnovsho"

    #  Энэ хуудасруу ороход харуулах мэдээллүүдээ авч, дамжуулах хэсэг
    htmlRuuDamjuulahUtguud["userId"] = request.session['userId']
    serviceHayag = "http://whoisb.mandakh.org/userInfoShow/"
    requestJSON = {
        "id": request.session['userId']
    }
    r = requests.get(serviceHayag,
                    data=json.dumps(requestJSON),
                    headers={'Content-Type': 'application/json'})
    response_json = r.json()

    response_json = response_json[0]
    htmlRuuDamjuulahUtguud["lastName"] = response_json["lastName"]
    htmlRuuDamjuulahUtguud["firstName"] = response_json["firstName"]
    htmlRuuDamjuulahUtguud["email"] = response_json["email"]
    htmlRuuDamjuulahUtguud["userName"] = response_json["userName"]
    #######################################################################

    return render(request, "Profile/1.html",htmlRuuDamjuulahUtguud)

def profileAdd(request):
    checkSession(request)  
    if request.session['beegii'] == 0:        
        return redirect("homeView")    
    return render(request, "Profile/2.html",)

def profileFamily(request):
    checkSession(request)  
    if request.session['beegii'] == 0:        
        return redirect("homeView")    
    return render(request, "Profile/4.html",)

def profileEdu(request):
    checkSession(request)  
    if request.session['beegii'] == 0:        
        return redirect("homeView")    
    return render(request, "Profile/3.html",)

def profileExp(request):
    checkSession(request)  
    if request.session['beegii'] == 0:        
        return redirect("homeView")    
    return render(request, "Profile/5.html",)

def profileSkill(request):
    checkSession(request)  
    if request.session['beegii'] == 0:        
        return redirect("homeView")    
    return render(request, "Profile/6.html",)

def profileSocial(request):
    checkSession(request)  
    if request.session['beegii'] == 0:        
        return redirect("homeView")    
    
    if request.method == "POST":
        name = request.POST.get("name")
        site = request.POST.get("site")

        request_data = {
            "ner": name,
            "site": site,
            }
    requestJSON = {
        "id": request.session['userId']
    }
    r = requests.get("http://whoisb.mandakh.org/userSocialIn/",
                    data=json.dumps(requestJSON),
                    headers={'Content-Type': 'application/json'})
    
    return render(request, "Profile/7.html",)