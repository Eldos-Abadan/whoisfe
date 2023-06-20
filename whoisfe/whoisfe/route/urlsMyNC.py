from django.urls import path
from app import viewsMyNC
urlpatterns = [
    path("myNC/", viewsMyNC.myNCViews, name="myNCViews"),    
    ] 