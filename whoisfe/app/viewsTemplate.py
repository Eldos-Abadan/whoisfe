from django.shortcuts import render,redirect
from whoisfe.settings import *
import requests
import json

def myCvView(request,tid,uname):    
    
    requestJSON = {
        "id": tid
    }
    r = requests.get("http://whoisb.mandakh.org/tempGet/",
                        data=json.dumps(requestJSON),
                        headers={'Content-Type': 'application/json'})    
    try:
        
        responseJson = r.json()        
        print(responseJson)
        if responseJson["responseCode"] == 200:           
           renderFile = responseJson["tempData"][0]["file"]
        else:
           print("1")
           return render(request, templateErrorRenderHTML)
    except:        
      print("2")
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
           print("3")
           return render(request, templateErrorRenderHTML)
    except:        
      print("4")
      return render(request, templateErrorRenderHTML)
    
    

    return render (request, renderFile, HTMLruuDamjuulahUtga)