from django.urls import path
from app import viewsMain, viewsLogin, viewsRegister, viewsForget, viewsGuide, viewsSignUpWarn, viewsEmailVer
from app import viewsTemplate
urlpatterns = [  
    path("",                            viewsMain.homeView,                 name="homeView"),
    path("login/",                      viewsLogin.loginViews,              name="loginViews"),
    path("register/",                   viewsRegister.registerViews,        name="registerViews"), 
    path("forget/",                     viewsForget.forgetView,             name="forgetView"),
    path("guide/",                      viewsGuide.guideViews,              name="guideViews"),
    path("signUpWarn/",                 viewsSignUpWarn.signUpWarnViews,    name="viewsSignUpWarning"),
    path("register/email_activation",   viewsEmailVer.EmailVerView,         name="EmailVerView"), 
    # CV bolon NC template-uud ##########################################################################
    path("mycv/<int:tid>/<str:uname>/",                     viewsTemplate.myCvView,              name="myCvView"),
    path("justCV/",                     viewsMain.justCVViews,              name="justcv"),
    path("justNC/",                     viewsMain.justNCViews,              name="justnc"),
    path("BC/",                         viewsMain.odkeBcViews,              name="BC"),
    path("mainNC/",                     viewsMain.mainNCViews,              name="mainnc"),
    path("enkuCV/",                     viewsMain.enkuCVViews,              name="enkucv"),
    path("enku2CV/",                     viewsMain.enku2CVViews,              name="enku2cv"),
    #####################################################################################################
    ]   