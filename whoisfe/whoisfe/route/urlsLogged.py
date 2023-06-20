from django.urls import path
from app import *
urlpatterns = [
    path("loggedViews/", viewsLogged.loginhomelogViews, name="loggedViews"), 
    ]   
