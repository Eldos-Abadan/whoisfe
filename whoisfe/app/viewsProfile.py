from django.shortcuts import render, redirect
import datetime
import json
import requests
from django.contrib import messages
from whoisfe.settings import *
from    django.http                  import HttpResponse


def profileViews(request):
    checkSession(request)  
    if request.session['beegii'] ==0:        
        return redirect("homeView")    
    baas = {}
    baas["userId"] = request.session['userId']

    requestJSON = {
        "id": request.session['userId']
    }

    r = requests.get("http://whoisb.mandakh.org/userInfoShow/",
                    data=json.dumps(requestJSON),
                    headers={'Content-Type': 'application/json'})
    response_json = r.json()
    response_json = response_json[0]
    baas["userName"] = response_json.get('userName')
    baas["firstName"] = response_json.get('firstName')
    baas["lastName"] = response_json.get('lastName')
    baas["email"] = response_json.get('email')
    
    return render(request, "Profile/1.html",baas)



def profileMain(request):
    return render(request, "Profile/1.html",)

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
    return render(request, "Profile/7.html",)