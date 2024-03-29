from django.shortcuts import render, redirect
import json
import requests
from whoisfe.settings import *
from django.http import HttpResponse
import json.decoder
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage

def profileMain(request):
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")

    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"

    if request.method == "POST":
        if "userInfoUpdateSubmit" in request.POST:
            serviceHayag = "http://whoisb.mandakh.org/userInfoUpdate/"
            userName = request.POST.get("userName")
            firstName = request.POST.get("firstName")
            lastName = request.POST.get("lastName")
            profile = request.POST.get("profile")
            requestJSON = {
                "id": request.session['userId'],
                "userName": userName,
                "firstName": firstName,
                "lastName": lastName,
                "profile": profile
            }
            if "profile" in request.FILES:
              uploaded_file = request.FILES["profile"]
              if uploaded_file:
                  file_system = FileSystemStorage(location=settings.STATICFILES_DIRS[0] + '/profile')
                  filename = file_system.save(uploaded_file.name, uploaded_file)
                  requestJSON["profile"] = f'profile/{filename}'
            r = requests.get(serviceHayag,
                             data=json.dumps(requestJSON),
                             headers={'Content-Type': 'application/json'})
            responseJson = r.json()
            htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
            if responseJson["responseCode"] == 200:
                htmlRuuDamjuulahUtguud["textColor"] = "#00ff00"
            else:
                htmlRuuDamjuulahUtguud["textColor"] = "#ff0000"

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
        htmlRuuDamjuulahUtguud["path"] = userData["profile"]
    else:
        htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
        htmlRuuDamjuulahUtguud["textColor"] = "#ff0000"

    return render(request, "Profile/1.html", htmlRuuDamjuulahUtguud)



# def profileMain(request):
#     # Check session
#     checkSession(request)
#     if request.session['beegii'] == 0:
#         return redirect("homeView")

#     htmlRuuDamjuulahUtguud = {}
#     htmlRuuDamjuulahUtguud["responseText"] = ""
#     htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"

#     if request.method == "POST":
#         if "userInfoUpdateSubmit" in request.POST:
#             # Start userInfoUpdateSubmit
#             serviceHayag = "http://whoisb.mandakh.org/userInfoUpdate/"
#             userName = request.POST.get("userName")
#             firstName = request.POST.get("firstName")
#             lastName = request.POST.get("lastName")
#             lastName = request.POST.get("lastName")
#             profile = request.POST.get("profile")
#             requestJSON = {
#                 "id": request.session['userId'],
#                 "userName": userName,
#                 "firstName": firstName,
#                 "lastName": lastName,
#                 "profile":profile
#             }
#             r = requests.get(serviceHayag,
#                              data=json.dumps(requestJSON),
#                              headers={'Content-Type': 'application/json'})
#             responseJson = r.json()
#             htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
#             if responseJson["responseCode"] == 200:
#                 htmlRuuDamjuulahUtguud["textColor"] = "#00ff00"
#             else:
#                 htmlRuuDamjuulahUtguud["textColor"] = "#ff0000"

#         if "changePassSubmit" in request.POST:
#             if request.POST.get("new") == request.POST.get("new2"):
#                 serviceHayag = "http://whoisb.mandakh.org/changePass/"
#                 requestJSON = {
#                     "id": request.session['userId'],
#                     "oldpass": mandakhHash(request.POST.get("old")),
#                     "newpass": mandakhHash(request.POST.get("new")),
#                 }
#                 r = requests.get(serviceHayag,
#                                  data=json.dumps(requestJSON),
#                                  headers={'Content-Type': 'application/json'})
#                 responseJson = r.json()
#                 htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
#             else:
#                 htmlRuuDamjuulahUtguud["responseText"] = "zailnovsho"

#     # Get user information
#     serviceHayag = "http://whoisb.mandakh.org/userInfoShow/"
#     requestJSON = {
#         "id": request.session['userId']
#     }
#     r = requests.get(serviceHayag,
#                      data=json.dumps(requestJSON),
#                      headers={'Content-Type': 'application/json'})
#     responseJson = r.json()

#     if responseJson["responseCode"] == 200:
#         userData = responseJson["data"]
#         htmlRuuDamjuulahUtguud["userId"] = userData["id"]
#         htmlRuuDamjuulahUtguud["lastName"] = userData["lastName"]
#         htmlRuuDamjuulahUtguud["firstName"] = userData["firstName"]
#         htmlRuuDamjuulahUtguud["email"] = userData["email"]
#         htmlRuuDamjuulahUtguud["userName"] = userData["userName"]
#         htmlRuuDamjuulahUtguud["path"] = userData["profile"]
#     else:
#         htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
#         htmlRuuDamjuulahUtguud["textColor"] = "#ff0000"

#     return render(request, "Profile/1.html", htmlRuuDamjuulahUtguud)


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
            huis = request.POST.get("huis")
            torsonOgnoo = request.POST.get("bornDate")
            regDug = request.POST.get("register")
            dugaar = request.POST.get("phoneNumber")
            irgenshil = request.POST.get("citizenship")
            ysUndes = request.POST.get("nationality")
            hayg = request.POST.get("homeAddress")
            hobby = request.POST.get("hobby")

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
        nemelt["huis"] = userData["huis"]
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

    return render(request, "Profile/2.html", nemelt)


def profileFamily(request):
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"

    # Medeelel nemeh
    if request.method == "POST":
        if "userFamilyIns" in request.POST:
            henBoloh = request.POST.get("henBoloh")
            ner = request.POST.get("ner")
            dugaar = request.POST.get("dugaar")
            request_data = {
                'id': request.session['userId'],
                "henBoloh": henBoloh,
                "ner": ner,
                "dugaar": dugaar,
            }

            r = requests.post("http://whoisb.mandakh.org/userFamilyIns/",
                              data=json.dumps(request_data),
                              headers={'Content-Type': 'application/json'})
            responseJson = r.json()
            htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]            
    
    htmlRuuDamjuulahUtguud["userId"] = request.session['userId']
    # Medeelel haruulah
    requestJSON = {
        "user_id": request.session['userId']            
    }
    r = requests.get("http://whoisb.mandakh.org/userFamily/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
    try:
        responseJson = r.json()
        if responseJson['responseCode'] == 200:
            data = responseJson['data']    

            for i in range(0,len(data)):
                data[i]["dugaarS"] = i+1
            htmlRuuDamjuulahUtguud["data"] = data       
            print(data)
        else:
            htmlRuuDamjuulahUtguud["aldaaniiMedegdel"] = responseJson['responseText']
    except:
        htmlRuuDamjuulahUtguud["aldaaniiMedegdel"] = "Ямар 1 балай алдаа"
    return render(request, "Profile/4.html", htmlRuuDamjuulahUtguud)
#   profileFamily

def profileFamilyDel(request,id):
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"
    # Medeelel ustgah start
    requestJSON = {
        "familyId": id           
    }
    r = requests.get("http://whoisb.mandakh.org/userFamilyDel/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
    responseJson = r.json()
    htmlRuuDamjuulahUtguud["responseText"] = htmlRuuDamjuulahUtguud["responseText"]+"|"+responseJson['responseText']
    # Medeelel ustgah end    
    # Medeelel haruulah start
    requestJSON = {
        "user_id": request.session['userId']            
    }
    r = requests.get("http://whoisb.mandakh.org/userFamily/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
    try:
        responseJson = r.json()
        if responseJson['responseCode'] == 200:
            data = responseJson['data']    

            for i in range(0,len(data)):
                data[i]["dugaarS"] = i+1
            htmlRuuDamjuulahUtguud["data"] = data       
            print(data)
        else:
            htmlRuuDamjuulahUtguud["responseText"] = htmlRuuDamjuulahUtguud["responseText"]+"|"+responseJson['responseText']
    except:
        htmlRuuDamjuulahUtguud["responseText"] = "Ямар 1 балай алдаа"
    return render(request, "Profile/4.html", htmlRuuDamjuulahUtguud)



def profileExp(request):
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    htmlRuuDamjuulakh = {}
    htmlRuuDamjuulakh["responseText"] = ""
    # medeelel nemeh ehleh
    if request.method == "POST":
        if ("insertButton" in request.POST):
            ajil = request.POST.get("albanTushaal")
            company = request.POST.get("companyNer")
            ehelsen = request.POST.get("date1")
            duussan = request.POST.get("date2")
            if not duussan: 
                duussan = "Ажиллаж байгаа"
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
            htmlRuuDamjuulakh["responseText"] = responseJson["responseText"]
    # medeelel nemeh duusah

    requestJSON = {
        'id': request.session['userId']
    }
    serviceHayag = "http://whoisb.mandakh.org/userTurshlaga/"    
    r = requests.get(serviceHayag,
                    data=json.dumps(requestJSON),
                    headers={'Content-Type': 'application/json'})
    responseJson = r.json()    
    

    if responseJson['responseCode'] == 200:
        myData = responseJson['TurshlagaData']    

        for i in range(0,len(myData)):
            myData[i]["dugaar"] = i+1
        htmlRuuDamjuulakh["myData"] = myData        
    else:
        htmlRuuDamjuulakh["responseText"] = responseJson['responseText']
    return render(request, "Profile/5.html",htmlRuuDamjuulakh)
#   profileExp
def profileExpDel(request,id):
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"
    # Medeelel ustgah start
    requestJSON = {
        "workId": id           
    }
    r = requests.get("http://whoisb.mandakh.org/userTurshlagaDel/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
    responseJson = r.json()
    htmlRuuDamjuulahUtguud["responseText"] = htmlRuuDamjuulahUtguud["responseText"]+"|"+responseJson['responseText']
    # Medeelel ustgah end    
    # Medeelel haruulah start
    requestJSON = {
        'id': request.session['userId']
    }
    serviceHayag = "http://whoisb.mandakh.org/userTurshlaga/"    
    r = requests.get(serviceHayag,
                    data=json.dumps(requestJSON),
                    headers={'Content-Type': 'application/json'})
    responseJson = r.json()    
    

    if responseJson['responseCode'] == 200:
        myData = responseJson['TurshlagaData']    

        for i in range(0,len(myData)):
            myData[i]["dugaar"] = i+1
        htmlRuuDamjuulahUtguud["myData"] = myData        
    else:
        htmlRuuDamjuulahUtguud["aldaaniiMedegdel"] = responseJson['responseText']
    return render(request, "Profile/5.html",htmlRuuDamjuulahUtguud)


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
        'user_id': request.session['userId']
    }
    # setSkill duudan ajillana.
    if request.method == "POST":
        serviceHayag = "http://whoisb.mandakh.org/insertUserSkill/"
        requestJSON = {
            "user_id": request.session['userId'],
            "chadvariinNer": request.POST.get("chadwar"),
            "chadvariinTuvshin": request.POST.get("tuvshin")
        }
        r = requests.get(serviceHayag,
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
        responseJson = r.json()
        if responseJson["responseCode"] != 200:
            chadwar["aldaa"] = responseJson["responseText"]
            return render(request, "Profile/6.html", chadwar)
    # end getSkill
    
    requestJSON = {
        'user_id': request.session['userId']
    }
    # getSkill duudan ajillana.
    serviceHayag = "http://whoisb.mandakh.org/getUserSkill/"
    r = requests.get(serviceHayag,
                    data=json.dumps(requestJSON),
                    headers={'Content-Type': 'application/json'})
    responseJson = r.json()
    if responseJson["responseCode"] == 200:
        chadwar["medeelel"] = responseJson["skills"]
        for i in range(0, len(chadwar["medeelel"])):
            chadwar["medeelel"][i]["dugaar"] =  i + 1
    else:
        chadwar["aldaa"] = responseJson["responseText"]
    return render(request, "Profile/6.html", chadwar)

#skill ustgal heseg

def profileSkillDel(request,id):
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    chadwar = {}
    chadwar["responseText"] = ""
    chadwar["textColor"] = "#00FF00"
    requestJSON = {
        "id": id
    }
    r = requests.get("http://whoisb.mandakh.org/delUserSkill/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
    responseJson = r.json()
    chadwar["responseText"] = chadwar["responseText"]+"|"+responseJson['responseText']
    # Medeelel ustgah end    
    # Medeelel haruulah start
    requestJSON = {
        'user_id': request.session['userId']
    }
    # getSkill duudan ajillana.
    serviceHayag = "http://whoisb.mandakh.org/getUserSkill/"
    r = requests.get(serviceHayag,
                    data=json.dumps(requestJSON),
                    headers={'Content-Type': 'application/json'})
    responseJson = r.json()
    if responseJson["responseCode"] == 200:
        chadwar["medeelel"] = responseJson["skills"]
        for i in range(0,len(chadwar["medeelel"])):
            chadwar["medeelel"][i]["dugaar"] = i + 1
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

    # nemeh heseg start
    if request.method == "POST":
        if "addSave" in request.POST:
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
            return redirect('profileSocial')
        # if "editSave" in request.POST:
        #     serviceHayag = "http://whoisb.mandakh.org/userSocialUp/"
        #     app = request.POST.get("editapp")
        #     site = request.POST.get("editsite")
        #     requestJSON = {
        #         "id": request.session['userId'],
        #         "app": app,
        #         "newsite": site,
        #     }
        #     r = requests.get(serviceHayag,
        #                      data=json.dumps(requestJSON),
        #                      headers={'Content-Type': 'application/json'})
        #     responseJson = r.json()
        #     htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
        #     if responseJson["responseCode"] == 200:
        #         htmlRuuDamjuulahUtguud["textColor"] = "#00ff00"
        #     else:
        #         htmlRuuDamjuulahUtguud["textColor"] = "#ff0000"
    serviceHayag = "http://whoisb.mandakh.org/userSocial/"
    requestJSON = {
        "id": request.session['userId']
    }
    # nemeh heseg end
    r = requests.get(serviceHayag,
                     data=json.dumps(requestJSON),
                     headers={'Content-Type': 'application/json'})
    responseJson = r.json()

    if responseJson["responseCode"] == 200:        
        htmlRuuDamjuulahUtguud['socialData'] = responseJson["socialData"]
        htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
    else:
        htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
        htmlRuuDamjuulahUtguud["textColor"] = "#ff0000"
    return render(request, "Profile/7.html", htmlRuuDamjuulahUtguud)
#   profileSocial


def profileSocialDel(request,id):
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"
    requestJSON = {
        "socialId": id           
    }
    r = requests.get("http://whoisb.mandakh.org/userSocialDel/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
    responseJson = r.json()
    htmlRuuDamjuulahUtguud["responseText"] = htmlRuuDamjuulahUtguud["responseText"]+"|"+responseJson['responseText']
    # Medeelel ustgah end    
    # Medeelel haruulah start
    requestJSON = {
        "id": request.session['userId']
    }
    r = requests.get("http://whoisb.mandakh.org/userSocial/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})    
    try:
        responseJson = r.json()        
        if responseJson["responseCode"] == 200:
            htmlRuuDamjuulahUtguud['socialData'] = responseJson["socialData"]
        else:
            htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]
            htmlRuuDamjuulahUtguud["textColor"] = "#ff0000"
    except:
        htmlRuuDamjuulahUtguud["responseText"] = "Ямар 1 балай алдаа"
    return render(request, 'Profile/7.html', htmlRuuDamjuulahUtguud)

def profileEdu(request):
    checkSession(request)
    tooluur = 0
    if request.session['beegii'] == 0:
        return redirect("homeView")

    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"

    # Medeelel nemeh
    if request.method == "POST":
        if "userEduInsertSubmit" in request.POST:
            education = request.POST.get("education")
            direction = request.POST.get("direction")
            elssenOn = request.POST.get("elssenOn")
            tugssunOn = request.POST.get("tugssunOn")
            if not tugssunOn: 
                tugssunOn = "Суралцаж байгаа"
            request_data = {
                'id': request.session['userId'],
                "education": education,
                "direction": direction,
                "elssenOn": elssenOn,
                "duussanOn": tugssunOn
            }

            r = requests.post("http://whoisb.mandakh.org/userEduInsert/",
                              data=json.dumps(request_data),
                              headers={'Content-Type': 'application/json'})
            responseJson = r.json()
            htmlRuuDamjuulahUtguud["responseText"] = responseJson["responseText"]            
    
    htmlRuuDamjuulahUtguud["userId"] = request.session['userId']
    # Medeelel haruulah
    requestJSON = {
        "user_id": request.session['userId']            
    }
    r = requests.post("http://whoisb.mandakh.org/userEduGet/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
    try:
        responseJson = r.json()
        if responseJson['responseCode'] == 200:
            myData = responseJson['eduData']    

            for i in range(0,len(myData)):
                myData[i]["dugaar"] = i+1
            htmlRuuDamjuulahUtguud["myData"] = myData        
            print(myData)
        else:
            htmlRuuDamjuulahUtguud["aldaaniiMedegdel"] = responseJson['responseText']
    except:
        htmlRuuDamjuulahUtguud["aldaaniiMedegdel"] = "Ямар 1 балай алдаа"


    return render(request, "Profile/3.html", htmlRuuDamjuulahUtguud)
#   profileEdu

#del edu
def profileEduDel(request,id):
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"
    # bolowsrol ustgah start
    requestJSON = {
        "id": id           
    }
    r = requests.get("http://whoisb.mandakh.org/userEduDel/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
    responseJson = r.json()
    htmlRuuDamjuulahUtguud["responseText"] = htmlRuuDamjuulahUtguud["responseText"]+"|"+responseJson['responseText']
    # Medeelel ustgah end    
    # Medeelel haruulah start
    requestJSON = {
        "user_id": request.session['userId']            
    }
    r = requests.post("http://whoisb.mandakh.org/userEduGet/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
    try:
        responseJson = r.json()
        if responseJson['responseCode'] == 200:
            myData = responseJson['eduData']    

            for i in range(0,len(myData)):
                myData[i]["dugaar"] = i+1
            htmlRuuDamjuulahUtguud["myData"] = myData        
            print(myData)
        else:
            htmlRuuDamjuulahUtguud["aldaaniiMedegdel"] = responseJson['responseText']
    except:
        htmlRuuDamjuulahUtguud["aldaaniiMedegdel"] = "Ямар 1 балай алдаа"


    return render(request, "Profile/3.html", htmlRuuDamjuulahUtguud)



###zurag oruulah heseg#############
# def upload_file(request, id):
#     checkSession(request)
#     if request.session['beegii'] == 0:
#         return redirect("homeView")
    
#     htmlRuuDamjuulahUtguud = {}
#     htmlRuuDamjuulahUtguud["responseText"] = ""
#     htmlRuuDamjuulahUtguud["textColor"] = "#00FF00"
#     requestJSON = {
#         "user_id": request.session['userId']            
#     }
#     r = requests.post("http://whoisb.mandakh.org/insertImg/",
#                         data=json.dumps(requestJSON),
#                         headers={'Content-Type': 'application/json'})

#     if request.method == 'POST' and 'image' in request.FILES:
#         uploaded_image = request.FILES['image']
#         fs = FileSystemStorage()
#         filename = fs.save(uploaded_image.name, uploaded_image)
#         image_instance = UploadedImage(image=filename)
#         image_instance.save()

#     images = UploadedImage.objects.all()

#     return render(request, '1.html', {'htmlRuuDamjuulahUtguud': htmlRuuDamjuulahUtguud, 'images': images})