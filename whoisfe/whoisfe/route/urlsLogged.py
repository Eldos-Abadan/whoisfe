from django.urls import path
from app import viewsLogged
urlpatterns = [
    path("logged/", viewsLogged.loggedViews, name="loggedViews"),
    path("createNC/", viewsLogged.createNCViews, name="createNCViews"),
    path("createCV/", viewsLogged.createCVViews, name="createCVViews"),
    path("dashboard/", viewsLogged.dashboardViews, name="dashboardViews"),
    path("myNC/", viewsLogged.myNCViews, name="myNCViews"),
    # path("myCVViews/", viewsLogged.myCVViews, name="myCVViews"),
    # path("walletViews/", viewsLogged.walletViews, name="walletViews"),
    path("guide/", viewsLogged.guideViews, name="guideViews"),
    path("profile/", viewsLogged.profileViews, name="profileViews"),
    ]   
