from django.shortcuts import render,redirect
from whoisfe.settings import *

def dashboardViews(request):
    return render(request, "dashboard/dashboard.html")