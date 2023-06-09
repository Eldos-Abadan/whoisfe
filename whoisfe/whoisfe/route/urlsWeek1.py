from django.urls import path
from app import viewsWeek1
urlpatterns = [
    path("week1/bilguun", viewsWeek1.bilguun, name="bilguun"),
    path("week1/", viewsWeek1.week1View, name="week1View"),
    path("week1/home/", viewsWeek1.week1HomeView, name="week1Home"),
    path("week1/magnai/", viewsWeek1.magnai, name="magnai"),
    # path("week1/tuugii/", viewsWeek1.tuugii, name=""),
    path("week1/odke/", viewsWeek1.odke, name="odke"),
    path("week1/sarnai/", viewsWeek1.sarnai, name="sarnai"),
    path("week1/xuslen/", viewsWeek1.xuslen, name="xuslen"),
    path("week1/enkhu/", viewsWeek1.enkhzul, name="enkhzul"),
    path("week1/zndra/", viewsWeek1.zndra, name="zndra"),
    path("week1/Bayrbat/", viewsWeek1.Bayrbat, name="Bayrbat"),
    path("week1/Odonkhuu/", viewsWeek1.Odonkhuu, name="Odonkhuu"),
    path("week1/Eldos/", viewsWeek1.eldos, name="eldos"),
    path("week1/nomin/", viewsWeek1.nomin, name="nomi"),
    path("week1/Tudu/", viewsWeek1.Tudu, name="Tudu"),
    path("week1/Nomio1/", viewsWeek1.Nomio1, name="Nomio1"),
    path("week1/Tserenbaatar/", viewsWeek1.Tserenbaatar, name="Tserenbaatar"),
    path("week1/bumaa/", viewsWeek1.bumaa, name="bumaa"),
    path("week1/olzii/", viewsWeek1.olzii, name="olzii"),
    path("week1/HaTuguldur/", viewsWeek1.HaTuguldur, name="HaTuguldur"),
    ]  
