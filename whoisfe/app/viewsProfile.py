from django.shortcuts import render, redirect
import json
import requests
from whoisfe.settings import *
from django.http import HttpResponse


def profileMain(request):
    #  Энэ хуудасруу орохтой холбоотой заавал байх шалгалт
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"
    #######################################################

    if request.method == "POST":
        if ("userInfoUpdateSubmit" in request.POST):
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
            if (responseJson["responseCode"] == 200):
                htmlRuuDamjuulahUtguud["textColor"] = "#00ff00"
            else:
                htmlRuuDamjuulahUtguud["textColor"] = "#ff0000"
            # end userInfoUpdateSubmit
        if ("changePassSubmit" in request.POST):
            if request.POST.get("new") == request.POST.get("new2"):
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

    return render(request, "Profile/1.html", htmlRuuDamjuulahUtguud)

def profileAdd (request):
    checkSession(request)  
    if request.session['beegii'] == 0:        
        return redirect("homeView")    
    
def profileAdd(request):
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    return render(request, "Profile/2.html",)


def profileFamily(request):
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"
    if request.method == "POST":
        henBoloh = request.POST.get("henBoloh")
        ner = request.POST.get("ner")
        dugaar = request.POST.get("dugaar")

        request_data = {
            "henBoloh": henBoloh,
            "ner": ner,
            "dugaar": dugaar
        }
    requestJSON = {
        "id": request.session['userId']
    }
    r = requests.get("http://whoisb.mandakh.org/userFamilyIns/",
                     data=json.dumps(requestJSON),
                     headers={'Content-Type': 'application/json'})
    responseJson = r.json()
    htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
    if responseJson["responseCode"] == 200:
            htmlRuuDamjuulahUtguud["textColor"] = "#00ff00"
    else:
            htmlRuuDamjuulahUtguud["textColor"] = "#ff0000"

    htmlRuuDamjuulahUtguud["userId"] = request.session['userId']
    requestJSON = {
        "user_id": request.session['userId']
    }
    r = requests.get("http://whoisb.mandakh.org/userFamilyIns/",
                     data=json.dumps(requestJSON),
                     headers={'Content-Type': 'application/json'},)
    response_json = r.json()
    htmlRuuDamjuulahUtguud['henBoloh'] = response_json.get('henBoloh')
    htmlRuuDamjuulahUtguud['ner'] = response_json.get('ner')
    htmlRuuDamjuulahUtguud['dugaar'] = response_json.get('dugaar')

    
    return render(request, "Profile/4.html", htmlRuuDamjuulahUtguud)


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


# Chadvar uurchluh bolon hadgalah hrauulah function
def profileSkill(request):
    checkSession(request)  
    if request.session['beegii'] == 0:        
        return redirect("homeView")
    chadwar = {}
    chadwar["responseText"] = ""
    chadwar["textColor"] = "#00FF00"
    chadwar["userId"] = request.session['userId']
    requestJSON = {
        'id': request.session['userId']
    }
    # setSkill duudan ajillana.
    if request.method=="POST":
        serviceHayag ="http://whoisb.mandakh.org/setSkill/"

        if("skillInfoUpdateSubmit" in request.POST):
            requestJSON = {
                "id" : request.session['userId'],
                "skill": request.POST.get("Message")
            }
            r = requests.get(serviceHayag,
                            data=json.dumps(requestJSON),
                            headers={'Content-Type': 'application/json'})
        responseJson = r.json()
        if responseJson["responseCode"] != 200:
            chadwar["aldaa"] =  responseJson["responseText"]
            return render(request, "Profile/6.html", chadwar)
    # end getSkill
    
    # getSkill duudan ajillana.
    serviceHayag ="http://whoisb.mandakh.org/getSkill/"
    r = requests.get(serviceHayag,
                    data=json.dumps(requestJSON),
                    headers={'Content-Type': 'application/json'})
    responseJson = r.json()
    if responseJson["responseCode"] == 200:
        chadwar["medeelelel"] = responseJson["skill"] 
    else:    
        chadwar["aldaa"] =  responseJson["responseText"]
    return render(request, "Profile/6.html", chadwar)
    # end setSkill.
#####################################



def profileSocial(request):
    #  Энэ хуудасруу орохтой холбоотой заавал байх шалгалт
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"
    #######################################################
    if request.method == "POST":
        serviceHayag = "http://whoisb.mandakh.org/userSocialIn/"
        app = request.POST.get("app")
        site = request.POST.get("name")
        requestJSON = {
            'id': request.session['userId'],
            'app': app,
            'site': site
        }
        r = requests.get(serviceHayag,
                         data=json.dumps(requestJSON),
                         headers={'Content-Type': 'application/json'})
        responseJson = r.json()
        htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
        if responseJson["responseCode"] == 200:
            htmlRuuDamjuulahUtguud["textColor"] = "#00ff00"
        else:
            htmlRuuDamjuulahUtguud["textColor"] = "#ff0000"

    htmlRuuDamjuulahUtguud["userId"] = request.session['userId']
    requestJSON = {
        "user_id": request.session['userId']
    }
    r = requests.get("http://whoisb.mandakh.org/userSocial/",
                     data=json.dumps(requestJSON),
                     headers={'Content-Type': 'application/json'},)
    response_json = r.json()
    htmlRuuDamjuulahUtguud['app'] = response_json.get('app')
    htmlRuuDamjuulahUtguud['name'] = response_json.get('ner')


    return render(request, "Profile/7.html", htmlRuuDamjuulahUtguud)  
    #######################################################################