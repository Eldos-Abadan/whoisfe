from django.urls import path
from app import viewsLogged
urlpatterns = [
    path("logged/", viewsLogged.loginHomeLogViews, name="loggedViews"), 
    ]   
