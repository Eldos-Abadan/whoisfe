from django.urls import path
from app import viewsMain, viewsLogin, viewsRegister, viewsForget, viewsGuide
urlpatterns = [  
    path("",            viewsMain.homeView,          name="homeView"),
    path("login/",      viewsLogin.loginViews,       name="loginViews"),
    path("register/",   viewsRegister.registerViews, name="registerViews"), 
    path("forget/",     viewsForget.forgetView,      name="forgetView"),
    path("guide/",      viewsGuide.guideViews,       name="guideViews"),
    ]   