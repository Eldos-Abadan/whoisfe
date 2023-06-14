from django.urls import path
from app import viewsLogged
urlpatterns = [
    path("loggedViews/", viewsLogged.loginhomelogViews, name="loggedViews"), 
    ]   
