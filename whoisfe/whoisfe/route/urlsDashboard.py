from django.urls import path
from app import viewsDashboard
urlpatterns = [
    path("dashboard/", viewsDashboard.dashboardViews, name="dashboardViews"),    
    ]   