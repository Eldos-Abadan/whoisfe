from django.shortcuts import render, redirect
import json
import requests
from whoisfe.settings import *
from    django.http                  import HttpResponse


def profileMain(request):
    checkSession(request)  
    if request.session['beegii'] == 0:        
        return redirect("homeView")    
    
    htmlRuuDamjuulahUtguud = {}
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
    

    return render(request, "Profile/1.html",htmlRuuDamjuulahUtguud)

def profileAdd(request):
    return render(request, "Profile/2.html",)

def profileFamily(request):
    return render(request, "Profile/4.html",)

def profileEdu(request):
    return render(request, "Profile/3.html",)

def profileExp(request):
    return render(request, "Profile/5.html",)

def profileSkill(request):
    return render(request, "Profile/6.html",)

def profileSocial(request):
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