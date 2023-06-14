from django.urls import path
from app import viewsForget
urlpatterns = [
    path("forget/", viewsForget.forgetView, name="forgetView"),    
    ]   
