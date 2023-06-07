
from django.urls import path
from app import views

urlpatterns = [
    path("", views.homeView, name="homeView"),
    path("week1/bilguun", views.bilguun, name="bilguun"),
    path("week1/", views.week1View, name="week1View"),
    path("week1/home/", views.homeView, name="homm"),
    path("week1/magnai/", views.magnai, name="magnai"),
    path("week1/tuugii/", views.tuugii, name="tuugii"),
    path("week1/odke/", views.odke, name="odke"),
    path("week1/sarnai/", views.sarnai, name="sarnai"),
    path("week1/xuslen/", views.xuslen, name="xuslen"),
    path("week1/enkhu/", views.enkhzul, name="enkhzul"),
    path("week1/zndra/", views.zndra, name="zndra"),
    path("week1/Bayrbat/", views.Bayrbat, name="Bayrbat"),
    path("week1/Odonkhuu/", views.Odonkhuu, name="Odonkhuu"),
    path("week1/Eldos/", views.eldos, name="eldos"),
    path("week1/nomin/", views.nomin, name="nomi"),
    # path("week1/Tudu/", views.Tudu, name="Tudu"),
    path("week1/Nomio1/", views.Nomio1, name="Nomio1"),
]
