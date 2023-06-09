from django.urls import path
from app import viewsMain
urlpatterns = [
    path("", viewsMain.homeView, name="homeView"),    
    ]   
