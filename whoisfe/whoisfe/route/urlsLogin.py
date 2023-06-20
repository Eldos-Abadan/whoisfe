from django.urls import path
from app import viewsLogin
urlpatterns = [
    path("Login/", viewsLogin.loginViews, name="loginViews"),    
    ]   