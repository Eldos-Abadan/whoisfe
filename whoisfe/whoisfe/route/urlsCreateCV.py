from django.urls import path
from app import viewsCreateCV
urlpatterns = [
    path("createCV/", viewsCreateCV.createCVViews, name="createCVViews"),    
    ] 