from django.urls import path
from app import viewsMain
urlpatterns = [
    path("", viewsMain.homeView, name="homeView"),    
    path("logout/", viewsMain.homeLogoutView, name="homeLogoutView"),    
    ]