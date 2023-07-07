from django.urls import path
from app import viewsPerInfo
urlpatterns = [
    path("profile/", viewsPerInfo.perinfoViews, name="perinfoViews"),    
    ]   