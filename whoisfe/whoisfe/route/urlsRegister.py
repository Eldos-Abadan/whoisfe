from django.urls import path
from app import viewsRegister
urlpatterns = [
    path("register/", viewsRegister.registerViews, name="registerViews"),    
    ]   