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
  return render(request, "templates/homeTemp/just.html")

def bwViews(request): 
  return render(request, "templates/homeTemp/Magnai.html")

def justNCViews(request): 
  return render(request, "templates/homeTemp/bc.html")

def odkeBcViews(request): 
  return render(request, "templates/homeTemp/odkeBc.html")

# def odkeBcViews(request): 
#   return render(request, "templates/ncTemp/odkeBc.html")

def mainNCViews(request): 
  return render(request, "templates/homeTemp/main.html")

def enkuCVViews(request): 
  return render(request, "templates/homeTemp/enku.html")

def enku2CVViews(request): 
  return render(request, "templates/homeTemp/enku2.html")

def kucvViews(request): 
  return render(request, "templates/kucv.html")