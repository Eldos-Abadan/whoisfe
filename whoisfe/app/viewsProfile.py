from django.shortcuts import render, redirect
import datetime
import json
import requests
from django.contrib import messages
from whoisfe.settings import *
from    django.http                  import HttpResponse


def profileViews(request):
    # checkSession(request)  
    # if request.session['beegii'] ==0:        
    #     return redirect("homeView")    
    # htmlRuuDataDamjuulah = {}
    # htmlRuuDataDamjuulah = request.session['userData']
    return render(request, "Profile/1.html") #htmlRuuDataDamjuulah

def userInfoShows(request, user_id):
    if not user_id:
        response = {
            "responseCode": 550,
            "responseText": "User ID is missing"
        }
        return render(request, "Profile/1.html", context=response)

    url = f"http://whoisb.mandakh.org/userInfoShow/?id={user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        user_info = response.json()
        context = {
            "user_info": user_info
        }
        return render(request, "Profile/1.html", context)
    else: 
        response = {
            "responseCode": response.status_code,
            "responseText": "Request failed"
        }
        return render(request, "Profile/1.html", context=response)


