from django.urls import path
from app import viewsLogin
urlpatterns = [
    path("login/", viewsLogin.loginViews, name="loginViews"),    
    path("logout/", viewsLogin.homeLogoutView, name="homeLogoutView"),    
    ]