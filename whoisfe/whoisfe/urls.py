
from django.urls import path
from app import views

urlpatterns = [
    path("", views.homeView, name="homeView"),
    path("week1/", views.week1View, name="week1View"),
    path("week1/magnai/", views.magnai, name="magnai"),
    path("week1/Eldos/", views.Eldos, name="Eldos"),
    path("week1/HaTuguldur/", views.HaTuguldur, name="HaTuguldur"),
]
