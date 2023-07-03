from django.shortcuts import render, redirect
import json
import requests
from whoisfe.settings import *
from django.http import HttpResponse
import json.decoder

# Хэрэглэгчийн мэдээллээ бөглөсөн эсэхийг мэдэгдэх
def dashboardViews(request): 
    # Хэрэглэгч нэвтэрсэн эсэхийг шалгах
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    htmlData = {}
    htmlData["aldaaniiMedeelel"] = {}
    try:
        serviceHayag = [
            "/userNemelt/",
            "/userFamily/",
            "/userEduGet/",
            "/userTurshlaga/",
            "/getSkill/",
            "/userSocial/"
        ]
        # legth list нь тухайн сервис дуудаж хэр олон мэдээлэл авч байгааг мэдэх зорилготой
        length = [1, 1, 1, 1, 1, 1]
        htmlData = {}
        htmlData["userData1"] = []
        for i in range(0, len(serviceHayag)):
            # Зарим нь хэрэглэгчийн id-ийг "user_id", "id" гэж хүсэлт илгээж байгаа
            if(i < 3 ): requestJSON = { "user_id": request.session['userId']}
            else: requestJSON = { "id": str(request.session['userId'])}
            r = requests.get("http://whoisb.mandakh.org" + serviceHayag[i],
                                data=json.dumps(requestJSON),
                                headers={'Content-Type': 'application/json'} )
            jsonsData = r.json()
            print(jsonsData)
            # responseCode шалгах
            # if(jsonsData["responseCode"]) != 555:
            if(jsonsData["responseCode"]) != 200:
                htmlData["aldaaniiMedeelel"] = jsonsData["responseText"]
                jsonsData = {'responseCode': 200, 'responseText': 'Амжилттай', 'data': [{'id': 68, 'user_id': 214, 'henBoloh': None, 'ner': None, 'dugaar': None}]}
                # htmlData["userData1"] = ""
                # return render(request, "dashboard/dashboard.html", htmlData)
            # data гэх хувьсагчид мэдээллээ авч байна.
            data = jsonsData[str(list(jsonsData)[2])]
            array = []
            # Хэрэв dict, болон list хэлбэрээр ирвэл нэг list болгон салгаж байна.
            if(type(data) != list):
                array.append(data)
                if(len(array) > 1):
                    data = list(jsonsData[str(list(jsonsData)[2])])
                    # Хэрэв list урт олон байвал хэрэглэгч мэдээллээ оруулсан байна.
                    length[i] = len(data)
            else:
                data = data[0]
            htmlData["userData"] = {}
            bvrenEsekh = 1
            if(length[i] == 1):
                for element in data:
                    if not ((str(element) == "id") or (str(element) == "user_id")):
                        element = str(element)
                        if ((data[element] is None) or (data[element] == "None")):
                            bvrenEsekh = 0
                            htmlData["userData"][element] = " дутуу байна."
                        else:
                            htmlData["userData"][element] = data[element]
                            continue
            if i == 0: 
                htmlData["userData"]["garchig"] = "Нэмэлт мэдээлэл"
                if htmlData["userData"]["huis"] == 1:
                    htmlData["userData"]["huis"] = "Эрэгтэй"
                elif htmlData["userData"]["huis"] == 2:
                    htmlData["userData"]["huis"] = "Эмэгтэй"
                else:
                    htmlData["userData"]["huis"] = "Бусад"
            if i == 1: htmlData["userData"]["garchig"] = "Гэр бүлийн мэдээлэл"
            if i == 2: htmlData["userData"]["garchig"] = "Боловсрол"
            if i == 3: htmlData["userData"]["garchig"] = "Туршлага"
            if i == 4: htmlData["userData"]["garchig"] = "Чадвар"
            if i == 5: htmlData["userData"]["garchig"] = "Сошиал"
            htmlData["userData"]["bvrenEsekh"] = bvrenEsekh
            htmlData["userData1"].append(htmlData["userData"])
    except Exception as e:
        htmlData["aldaaniiMedeelel"] = "Уучлаарай, одоогоор энэ хуудсан дээрх мэдээллийг харуулах боломжгүй байна."
        # htmlData["userData1"] = ""
        return render(request, "dashboard/dashboard.html", htmlData)
    return render(request, "dashboard/dashboard.html", htmlData)
##############################################################################