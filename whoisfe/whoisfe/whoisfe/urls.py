from django.urls import path
from app import views

urlpatterns = [    
    path("",       views.homeView,  name="homeView"),
    path("week1/", views.week1View, name="week1View"),
]
