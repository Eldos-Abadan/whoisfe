from django.urls import path
from app import viewsMyCV, viewsCreateCV, viewsDashboard, viewsMyNC, viewsGuide, viewsProfile, viewsMain, viewsCreateNC, viewsFavorite
urlpatterns = [
   path("createNC/",    viewsCreateNC.createNCViews,     name="createNCViews"),
    path("createCV/",   viewsCreateCV.createCVViews,     name="createCVViews"),
    path("dashboard/",  viewsDashboard.dashboardViews,   name="dashboardViews"),
    path("myNC/",       viewsMyNC.myNCViews,             name="myNCViews"),
    path("guide/",      viewsGuide.guideViews,           name="guideViews"),
    path("profile/",    viewsProfile.profileViews,       name="profileViews"),
    path("home/",       viewsMain.homeLogoutView,        name="homeLogoutView"),
    path("wallet/",     viewsMain.walletView,            name="wallet"),
    path("myCV/",       viewsMyCV.myCVViews,            name="myCV"),
<<<<<<< HEAD
=======
    path("favorite/",       viewsFavorite.favoriteView,            name="favoriteView"),
    path("myCV/",       viewsMyCV.myCVViews,            name="myCVViews"),
>>>>>>> beb1caf1770f2c4c96b864348a946d8a797c8e7f
    ]   
