
from django.urls import path
from app import views

urlpatterns = [
    path("", views.homeView, name="homeView"),
    path("week1/", views.week1View, name="week1View"),
    path("week1/magnai/", views.magnai, name="magnai"),
     path("week1/tuugii/", views.tuugii, name="tuugii"),
    path("week1/odke/", views.odke, name="odke"),
    path("week1/sarnai/", views.sarnai, name="sarnai"),
]
