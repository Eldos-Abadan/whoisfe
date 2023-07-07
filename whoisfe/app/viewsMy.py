from django.shortcuts import render,redirect
from whoisfe.settings import *
import requests
import json
# from reportlab.pdfgen import canvas

def myCVViews(request):
    # Хэрэглэгч нэвтэрсэн эсэхийг шалгах
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    # Хэрэглэгчийн нэр авах start
    requestJSON = { "user_id": request.session['userId']}
    r = requests.get("http://whoisb.mandakh.org/getDashboardInfo/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
    data = r.json()
    userName = data["userName"]
    # Хэрэглэгчийн нэр авах end
    # Бүх загварийн мэдээлэл авах start
    requestJSON = {
        "user_id": request.session['userId']
    }
    r = requests.get("http://whoisb.mandakh.org/tempList/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
    data = r.json()
    # Бүх загварийн мэдээлэл авах end
    
    kholboos = []
    for ele in data:
        if(ele["tempTypeId"] != 1):
            continue
        kholboos.append({
            "name": str(ele["name"]), 
            "id": str(ele["id"])
        })
    htmlRuuDamjuulahUtguud["userName"] = userName
    htmlRuuDamjuulahUtguud["kholboos"] = kholboos
    ## pdf    
    # x = canvas.Canvas("pdf/1.pdf")
    # x.getpdfdata(render(request, "my/myCV.html", htmlRuuDamjuulahUtguud))
    # x.save()    
    ###################################


    return render(request, "my/myCV.html", htmlRuuDamjuulahUtguud)

def myNCViews(request):
        # Хэрэглэгч нэвтэрсэн эсэхийг шалгах
    checkSession(request)
    if request.session['beegii'] == 0:
        return redirect("homeView")
    htmlRuuDamjuulahUtguud = {}
    htmlRuuDamjuulahUtguud["responseText"] = ""
    # Хэрэглэгчийн нэр авах start
    requestJSON = { "user_id": request.session['userId']}
    r = requests.get("http://whoisb.mandakh.org/getDashboardInfo/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
    data = r.json()
    userName = data["userName"]
    # Хэрэглэгчийн нэр авах end
    # Бүх загварийн мэдээлэл авах start
    requestJSON = {
        "user_id": request.session['userId']
    }
    r = requests.get("http://whoisb.mandakh.org/tempList/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})
    data = r.json()
    # Бүх загварийн мэдээлэл авах end
    
    kholboos = []
    for ele in data:
        # diki = 
        if(ele["tempTypeId"] != 2):
            continue
        kholboos.append({
            "name": str(ele["name"]), 
            "id": str(ele["id"])
        })
    htmlRuuDamjuulahUtguud["userName"] = userName
    htmlRuuDamjuulahUtguud["kholboos"] = kholboos
    return render(request, "my/myNC.html", htmlRuuDamjuulahUtguud)