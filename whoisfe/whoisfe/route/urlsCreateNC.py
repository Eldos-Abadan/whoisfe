from django.urls import path
from app import viewsCreateNC
urlpatterns = [
    path("createNC/", viewsCreateNC.createNCViews, name="createNCViews"),    
    ] 