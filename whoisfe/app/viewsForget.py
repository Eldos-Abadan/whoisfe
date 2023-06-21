from    django.shortcuts    import render,redirect
from    django.contrib      import messages
from    whoisfe.settings    import *
from    whoisfe.whoisfe.settings    import *
import  requests 
import  hashlib
import  json

def mandakhHash(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()


# nuuts vg sergeeh hesgiin
def forgetView(request):

    gg={}
    aldaaniiMedeelel = 'Нууц үгээ зөв давтан оруулна уу.'
    if request.method == "POST":
        
        # aldaa ilgeeh
        def aldaaIlgeeh(aldaaniiNer):
            aldaaniiMedeelel = aldaaniiNer
            gg["aldaaniiMedeelel"] = aldaaniiMedeelel
            return render(request, "forget/Forget.html", gg)
        #######################################
        def emailExists(email):
            myCon = connectDB()
            userCursor = myCon.cursor()
            userCursor.execute('SELECT COUNT(*) FROM "f_user" WHERE "email" = %s', (email,))
            result = userCursor.fetchone()
            userCursor.close()
            disconnectDB(myCon)
            return result[0] > 0
        #######################################
        # email bolon verify khiisen esekh
        def verify(email):
            myCon = connectDB()
            userCursor = myCon.cursor()
            userCursor.execute('SELECT "id", "email" FROM "f_user" WHERE "email" = %s AND "isVerified" = true', (email,))
            result = userCursor.fetchone()
            userCursor.close()
            disconnectDB(myCon)
            return result[0] > 0
        #######################################
        jsons = request.POST.dict()
        print(type(jsons))
        email = jsons["email"]
        newPass1 = mandakhHash(jsons["newPass1"])
        newPass2 = mandakhHash(jsons["newPass2"])
        # print(newPass1)
        requestJSON = {
            "email": email,
            "newPass1": newPass1,
            "newPass2": newPass2
        }
        # Pass нь тэнцүү биш бол
        if(newPass1 != newPass2):
            aldaaIlgeeh('Нууц үгээ зөв давтан оруулна уу.')
        # Email байхгүй үед
        elif(not emailExists(email)):
            return redirect('registerViews')
        # Email нь verify хийгдээгүй үед
        elif(not verify(email)):
            return redirect('homeViews')
            aldaaIlgeeh('Та мэйлээ баталгаажуулаагүй байна.')
        # Email нь verify байгаа үед
        else:
            return redirect('loginViews')
            aldaaIlgeeh('Амжилттай шинэчлэлээ.')
            
        r=requests.get("http://whoisb.mandakh.org/forget/",
                            data=json.dumps(requestJSON),
                            headers={'Content-Type': 'application/json'})
        
    # gg["aldaaniiMedeelel"] = aldaaniiMedeelel
    return render(request, "forget/Forget.html")
###########################################################