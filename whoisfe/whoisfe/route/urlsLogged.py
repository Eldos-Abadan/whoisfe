from django.urls import path
from app import viewsMyCV, viewsCreateCV, viewsDashboard, viewsMyNC, viewsGuide, viewsProfile, viewsMain, viewsCreateNC, viewsFamInfo
urlpatterns = [
    path("createNC/" ,   viewsCreateNC.createNCViews,     name="createNCViews" ) ,
    path("createCV/" ,   viewsCreateCV.createCVViews,     name="createCVViews" ) ,
    path("dashboard/",   viewsDashboard.dashboardViews,   name="dashboardViews") ,
    path("myNC/"     ,   viewsMyNC.myNCViews,             name="myNCViews"     ) ,
    path("guide/"    ,   viewsGuide.guideViews,           name="guideViews"    ) ,    
    ##############################################################################
    path("profile/main/"  ,   viewsProfile.profileMain,      name="profileMain"  ) ,
    path("profile/add/"   ,   viewsProfile.profileAdd,       name="profileAdd"   ) ,
    path("profile/family/",   viewsProfile.profileFamily,    name="profileFamily") ,
    path("profile/family/del/<int:id>/",   viewsProfile.profileFamilyDel,    name="profileFamilyDel") ,
    path("profile/edu/"   ,   viewsProfile.profileEdu,       name="profileEdu"   ) ,
    path("profile/exp/"   ,   viewsProfile.profileExp,       name="profileExp"   ) ,
     path("profile/exp/del/<int:id>/"   ,   viewsProfile.profileExpDel,       name="profileExpDel"   ) ,
    path("profile/skill/" ,   viewsProfile.profileSkill,     name="profileSkill" ) ,
    path("profile/social/",   viewsProfile.profileSocial,    name="profileSocial") ,
    ##############################################################################
    path("home/"     ,   viewsMain.homeLogoutView,        name="homeLogoutView") ,
    path("wallet/"   ,   viewsMain.walletView,            name="wallet"        ) ,
    path("wallet/1/"   ,   viewsMain.wallet1View,            name="wallet1"        ) ,
    path("myCV/"     ,   viewsMyCV.myCVViews,             name="myCV"          ) ,
    path("famInfo/" ,   viewsFamInfo.FamInfoView,      name="FamInfoView"  ) ,
    ]   
