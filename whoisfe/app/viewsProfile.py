from django.shortcuts import render, redirect
import json
import requests
from whoisfe.settings import *
from django.http import HttpResponse
import json.decoder



def profileMain(request):
    # Check session
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")

    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"

    if request.method == "POST":
        if "userInfoUpdateSubmit" in request.POST:
            # Start userInfoUpdateSubmit
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
            if responseJson["responseCode"] == 200:
                htmlRuuDamjuulahUtguud["textColor"] = "#00ff00"
            else:
                htmlRuuDamjuulahUtguud["textColor"] = "#ff0000"
            # End userInfoUpdateSubmit

        if "changePassSubmit" in request.POST:
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

    # Get user information
    serviceHayag = "http://whoisb.mandakh.org/userInfoShow/"
    requestJSON = {
        "id": request.session['userId']
    }
    r = requests.get(serviceHayag,
                     data=json.dumps(requestJSON),
                     headers={'Content-Type': 'application/json'})
    responseJson = r.json()

    if responseJson["responseCode"] == 200:
        userData = responseJson["data"]
        htmlRuuDamjuulahUtguud["userId"] = userData["id"]
        htmlRuuDamjuulahUtguud["lastName"] = userData["lastName"]
        htmlRuuDamjuulahUtguud["firstName"] = userData["firstName"]
        htmlRuuDamjuulahUtguud["email"] = userData["email"]
        htmlRuuDamjuulahUtguud["userName"] = userData["userName"]
    else:
        htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
        htmlRuuDamjuulahUtguud["textColor"] = "#ff0000"

    return render(request, "Profile/1.html", htmlRuuDamjuulahUtguud)


def profileAdd(request):
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    nemelt = {}
    nemelt["responseText"] = ""
    nemelt["textColor"] = "#00FF00"
    if request.method == "POST":
        if ("userNemeltUpdateSubmit" in request.POST):
            # start userNemeltUpdateSubmit

            serviceHayag = "http://whoisb.mandakh.org/userNemeltUp/"
            huis = request.POST.get("gender")
            torsonOgnoo = request.POST.get("bornDate")
            regDug = request.POST.get("register")
            dugaar = request.POST.get("phoneNumber")
            irgenshil = request.POST.get("citizenship")
            ysUndes = request.POST.get("nationality")
            hayg = request.POST.get("homeAddress")
            hobby = request.POST.get("hobby")

            def debugFunciton():
                print(huis)
                print(torsonOgnoo)
                print(dugaar)
                print(irgenshil)
                print(ysUndes)
                print("sdakfjsdalhfkdsjh")
                print(hayg)
                print(hobby)
            if (len(huis) == 5):
                huis = "1"
            if (len(hobby) == 0):
                hobby = " "
            if (len(torsonOgnoo) == 0):
                torsonOgnoo = "07/01/2023"
            requestJSON = {
                "user_id": request.session['userId'],
                "regDug": regDug,
                "torsonOgnoo": torsonOgnoo,
                "dugaar": dugaar,
                "huis": huis,
                "irgenshil": irgenshil,
                "ysUndes": ysUndes,
                "hayg": hayg,
                "hobby": hobby
            }
            r = requests.post(serviceHayag,
                             data=json.dumps(requestJSON),
                             headers={'Content-Type': 'application/json'})
            responseJson = r.json()
            nemelt["responseText"] = responseJson["responseText"]
            if (responseJson["responseCode"] == 200):
                nemelt["textColor"] = "#00ff00"
            else:
                nemelt["textColor"] = "#ff0000"

    if request.method == "GET":  # Энэ хуудасруу ороход харуулах мэдээллүүдээ авч, дамжуулах хэсэг
        nemelt["userId"] = request.session['userId']
        serviceHayag = "http://whoisb.mandakh.org/userNemelt/"
        requestJSON = {
            "user_id": request.session['userId']
        }
        r = requests.get(serviceHayag,
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
        responseJson = r.json()

        if responseJson["responseCode"] == 200:
            userData = responseJson["data"]
            nemelt["userId"] = userData["user_id"]
            nemelt["gender"] = userData["huis"]
            nemelt["bornDate"] = userData["torsonOgnoo"]
            nemelt["register"] = userData["regDug"]
            nemelt["phoneNumber"] = userData["dugaar"]
            nemelt["homeAddress"] = userData["hayg"]
            nemelt["nationality"] = userData["ysUndes"]
            nemelt["hobby"] = userData["hobby"]
            nemelt["citizenship"] = userData["irgenshil"]
        else:
            nemelt["responseText"] = responseJson["responseText"]
            nemelt["textColor"] = "#ff0000"
        # #######################################################################

    return render(request, "Profile/2.html", nemelt)


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
    ajil = request.POST.get("companyNer")
    # print(ajil)
    # print(request.POST)
    if request.method == "POST":
        if ("insertButton" in request.POST):
            ajil = request.POST.get("companyNer")
            company = request.POST.get("albanTushaal")
            ehelsen = request.POST.get("date1")
            duussan = request.POST.get("date2")
            requestJSON = {
                'id': request.session['userId'],
                "ajil": ajil,
                "company": company,
                "ehelsen": ehelsen,
                "duussan": duussan
            }
            serviceHayag = "http://whoisb.mandakh.org/userTurshlagaIn/"
            r = requests.get(serviceHayag,
                            data=json.dumps(requestJSON),
                            headers={'Content-Type': 'application/json'})
            responseJson = r.json()
            print(responseJson)
            
    requestJSON = {
        'id': request.session['userId']
    }
    serviceHayag = "http://whoisb.mandakh.org/userTurshlaga/"
    
    r = requests.get(serviceHayag,
                    data=json.dumps(requestJSON),
                    headers={'Content-Type': 'application/json'})
    responseJson = r.json()
    # print(responseJson)
    print(responseJson['TurshlagaData'])
    myData = responseJson['TurshlagaData']
    htmlRuuDamjuulakh = {}
    hi = []
    hi.append(myData)
    if responseJson['responseCode'] == 200:
        htmlRuuDamjuulakh["myData"] = hi
    else:
        htmlRuuDamjuulakh["aldaaniiMedegdel"] = responseJson['responseText']
    return render(request, "Profile/5.html",htmlRuuDamjuulakh)


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
    if request.method == "POST":
        serviceHayag = "http://whoisb.mandakh.org/setSkill/"

        if ("skillInfoUpdateSubmit" in request.POST):
            requestJSON = {
                "id": request.session['userId'],
                "skill": request.POST.get("Message")
            }
            r = requests.get(serviceHayag,
                            data=json.dumps(requestJSON),
                            headers={'Content-Type': 'application/json'})
        responseJson = r.json()
        if responseJson["responseCode"] != 200:
            chadwar["aldaa"] = responseJson["responseText"]
            return render(request, "Profile/6.html", chadwar)
    # end getSkill

    # getSkill duudan ajillana.
    serviceHayag = "http://whoisb.mandakh.org/getSkill/"
    r = requests.get(serviceHayag,
                    data=json.dumps(requestJSON),
                    headers={'Content-Type': 'application/json'})
    responseJson = r.json()
    if responseJson["responseCode"] == 200:
        chadwar["medeelelel"] = responseJson["skill"]
    else:
        chadwar["aldaa"] = responseJson["responseText"]
    return render(request, "Profile/6.html", chadwar)
    # end setSkill.
#####################################


def profileSocial(request):
    # Check session
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")

    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"

    if request.method == "POST":
        serviceHayag = "http://whoisb.mandakh.org/userSocialIn/"
        app = request.POST.get("platForm")
        site = request.POST.get("userName")
        requestJSON = {
            "id": request.session['userId'],
            "app": app,
            "site": site,
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

    serviceHayag = "http://whoisb.mandakh.org/userSocial/"
    requestJSON = {
        "id": request.session['userId']
    }
    r = requests.get(serviceHayag,
                     data=json.dumps(requestJSON),
                     headers={'Content-Type': 'application/json'})
    responseJson = r.json()

    if responseJson["responseCode"] == 200:
        userData = responseJson["socialData"]
        htmlRuuDamjuulahUtguud['app'] = [data['app'] for data in userData]
        htmlRuuDamjuulahUtguud['site'] = [data['site'] for data in userData]
    else:
        htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
        htmlRuuDamjuulahUtguud["textColor"] = "#ff0000"
    # Zip the app and site lists together
    app_site_pairs = zip(htmlRuuDamjuulahUtguud['app'], htmlRuuDamjuulahUtguud['site'])
    # Pass the zipped list to the template
    return render(request, "Profile/7.html", {'app_site_pairs': app_site_pairs})
