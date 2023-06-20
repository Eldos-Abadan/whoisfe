from django.urls import path
from app import *
urlpatterns = [
    path("logginViews/", viewsNotLogin.notLoginViews, name="loginViews"), 
    path("Login/", viewsLogin.loginViews, name="loginViews"),  
    ]   