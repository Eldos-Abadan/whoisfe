from django.urls import path
from app import viewsGuide
urlpatterns = [
    path("guide/", viewsGuide.guideViews, name="guideViews")
]
