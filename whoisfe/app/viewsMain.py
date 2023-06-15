from django.shortcuts import render

def homeView(request):
    myData = {}
    shineerUussen = "No"    
    if "tooluur" not in request.session:
        shineerUussen = "Yes"
        request.session['tooluur'] = 0
    else:
        request.session['tooluur'] = request.session['tooluur'] + 1
    


    myData["tooluur"] = request.session['tooluur']
    myData["shineerUussen"] = shineerUussen
    return render(request, "home/mycv.html",myData)