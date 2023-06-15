from django.urls import path
from app import viewsPerInfo
urlpatterns = [
    path("perinfoform/", viewsPerInfo.perinfoViews, name="perinfoViews"),    
    ]   