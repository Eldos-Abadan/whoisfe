from django.urls import path
from app import viewsLogin
urlpatterns = [
    path("loginView/", viewsLogin.loginView, name="loginView"),    
    ]   
