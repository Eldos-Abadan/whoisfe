from django.urls import path
from app import viewsNotLogin
urlpatterns = [  
    path("home/", viewsNotLogin.homeViews, name="homeViews"),
    path("login/", viewsNotLogin.loginViews, name="loginViews"),
    path("register/", viewsNotLogin.registerViews, name="registerViews"), 
    path("forget/", viewsNotLogin.forgetViews, name="forgetViews"),
    path("guide/", viewsNotLogin.guideViews, name="guideViews"),
    ]   