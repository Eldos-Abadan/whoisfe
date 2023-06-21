# from    django.shortcuts    import render,redirect
# from    django.contrib      import messages
# from    whoisfe.settings    import *
# import  requests 
# import  hashlib
# import  json


# def mandakhHash(password):
#     return hashlib.md5(password.encode('utf-8')).hexdigest()


# # nuuts vg sergeeh hesgiin
# def forgetView(request):
#     if request.method == "POST":
#         jsons = request.POST.dict()
#         message={}
#         email = json["myName"]
#         newPass1 = mandakhHash(json["myPass1"])
#         newPass2 = mandakhHash(json["myPass2"])
#         requestJSON = {
#             "email": email,
#             "newPass1": newPass1,
#             "newPass2": newPass2
#         }
#         r = requests.get("http://whoisb.mandakh.org/userLogin/",
#                             data=json.dumps(requestJSON),
#                             headers={'Content-Type': 'application/json'})
# ####################################
