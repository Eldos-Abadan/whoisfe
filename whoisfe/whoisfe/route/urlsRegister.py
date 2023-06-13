from django.urls import path
from app import viewsRegister
urlpatterns = [
    path("registerViews/", viewsRegister.registerViews, name="registerViews"),    
    ]   