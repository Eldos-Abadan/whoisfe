from django.shortcuts import render,redirect
from whoisfe.settings import *
import requests
import json
######## cvView ######################################################
def myCvView(request,tid,uname):    
    
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
  return render(request, "templates/just.html")

def justNCViews(request): 
  return render(request, "templates/bc.html")

def odkeBcViews(request): 
  return render(request, "templates/odkeBc.html")

def odkeBcViews(request): 
  return render(request, "templates/odkeBc.html")

def mainNCViews(request): 
  return render(request, "templates/main.html")

def enkuCVViews(request): 
  return render(request, "templates/enku.html")

def enku2CVViews(request): 
  return render(request, "templates/enku2.html")

def kucvViews(request): 
  return render(request, "templates/kucv.html")