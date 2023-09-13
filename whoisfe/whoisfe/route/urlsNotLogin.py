from django.urls import path
from app import viewsMain, viewsLogin, viewsRegister
from app import viewsTemplate
urlpatterns = [  
    path("",                            viewsMain.homeView,                 name="homeView"),
    path("login/",                      viewsLogin.loginViews,              name="loginViews"),
    path("register/",                   viewsRegister.registerViews,        name="registerViews"), 
    path("forget/",                     viewsLogin.forgetView,              name="forgetView"),
    path("guide/",                      viewsMain.guideViews,               name="guideViews"),
    path("signUpWarn/",                 viewsRegister.signUpWarnViews,      name="viewsSignUpWarning"),
    path("register/email_activation",   viewsRegister.EmailVerView,         name="EmailVerView"), 
    # CV bolon NC template-uud ##########################################################################
    path("mycv/<int:tid>/<str:uname>/",                     viewsTemplate.myCvView,                 name="myCv"),
    path("myNC/<int:tid>/<str:uname>/",                     viewsTemplate.myNcView,                 name="myNc"),
    path("justCV/",                                         viewsTemplate.justCVViews,              name="justcv"),
    path("justNC/",                                         viewsTemplate.justNCViews,              name="justnc"),
    path("BC/",                                             viewsTemplate.odkeBcViews,              name="BC"),
    path("mainNC/",                                         viewsTemplate.mainNCViews,              name="mainnc"),
    path("enkuCV/",                                         viewsTemplate.enkuCVViews,              name="enkucv"),
    path("enku2CV/",                                        viewsTemplate.enku2CVViews,             name="enku2cv"),
    path("kucv/",                                           viewsTemplate.kucvViews,                name="kucv"),
    path("bw/",                                             viewsTemplate.bwViews,                  name="bw"),
    #####################################################################################################
    ]   