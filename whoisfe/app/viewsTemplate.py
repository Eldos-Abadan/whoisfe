from django.shortcuts import render,redirect
from whoisfe.settings import *
import requests
import json
from django.conf import settings
from django.core.files.storage import FileSystemStorage
######## cvView ######################################################
from django.http import HttpResponse
import os


def myCvView(request, tid, uname):
    requestJSON = {"id": tid}
    r = requests.get("http://whoisb.mandakh.org/tempGet/", data=json.dumps(requestJSON),
                     headers={'Content-Type': 'application/json'})
    try:
        responseJson = r.json()
        if responseJson["responseCode"] == 200:
            renderFile = responseJson["tempData"][0]["file"]
        else:
            return render(request, "templateErrorRenderHTML.html")
    except:
        return render(request, "templateErrorRenderHTML.html")

    requestJSON = {"userName": uname}
    if request.method == "POST" and "tempSubmit" in request.POST:
        serviceHayag = "http://whoisb.mandakh.org/uploadTemplate/"
        name = request.POST.get("name")
        tempTypeId = int(request.POST.get("tempTypeId"))
        catId = int(request.POST.get("catId"))
        file = request.POST.get("file")
        requestJSON = {
            "name": name,
            "tempTypeId": tempTypeId,
            "catId": catId,
            "file": file
        }
        if "file" in request.FILES:
            uploaded_file = request.FILES["file"]
            if uploaded_file:
                file_system = FileSystemStorage(location=settings.templateVar+'/newTemplates')
                filename = file_system.save(uploaded_file.name, uploaded_file)
                requestJSON["file"] = f'templates/newTemplates/{filename}'
                print(requestJSON["file"])

        r = requests.get(serviceHayag, data=json.dumps(requestJSON), headers={'Content-Type': 'application/json'})
        responseJson = r.json()
        HTMLruuDamjuulahUtga = {"responseText": responseJson["responseText"]}
        if responseJson["responseCode"] == 200:
            HTMLruuDamjuulahUtga["textColor"] = "#00ff00"
        else:
            HTMLruuDamjuulahUtga["textColor"] = "#ff0000"

    r = requests.get("http://whoisb.mandakh.org/userAllInfo/", data=json.dumps(requestJSON),
                     headers={'Content-Type': 'application/json'})
    try:
        responseJson = r.json()

        if responseJson["responseCode"] == 200:
            HTMLruuDamjuulahUtga = responseJson
        else:
            return render(request, "myCV")
    except:
        return render(request, "myCV")

    return render(request, renderFile, HTMLruuDamjuulahUtga)

###########################################################################

########### ncView ######################################################



def myNcView(request,tid,uname):    
    
    requestJSON = {
        "id": tid
    }
    r = requests.get("http://whoisb.mandakh.org/tempGet/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})    
    try:
        
        responseJson = r.json()        
        if responseJson["responseCode"] == 200:           
           renderFile = responseJson["tempData"][0]["file"]
        else:
           return render(request, templateErrorRenderHTML)
    except:        
      return render(request, templateErrorRenderHTML)
    requestJSON = {
        "userName": uname
    }
    r = requests.get("http://whoisb.mandakh.org/userAllInfo/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})    
    try:
        responseJson = r.json()
        
        if responseJson["responseCode"] == 200:
           HTMLruuDamjuulahUtga = responseJson
        else:
           return render(request, templateErrorRenderHTML)
    except:        
      return render(request, templateErrorRenderHTML)    

    return render (request, renderFile, HTMLruuDamjuulahUtga)
######################################################################
def justCVViews(request): 
  return render(request, "templates/homeTemp/just.html")

def bwViews(request): 
  return render(request, "templates/homeTemp/Magnai.html")

def justNCViews(request): 
  return render(request, "templates/homeTemp/bc.html")

def odkeBcViews(request): 
  return render(request, "templates/homeTemp/odkeBc.html")

def mainNCViews(request): 
  return render(request, "templates/homeTemp/main.html")

def enkuCVViews(request): 
  return render(request, "templates/homeTemp/enku.html")

def enku2CVViews(request): 
  return render(request, "templates/homeTemp/enku2.html")

def kucvViews(request): 
  return render(request, "templates/kucv.html")