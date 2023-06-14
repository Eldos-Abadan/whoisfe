from django.urls import path
from app import viewsWeek1
urlpatterns = [
    path("week1/",                  viewsWeek1.week1Views,              name="week1Views"),
    path("week1/home/",             viewsWeek1.week1HomeViews,          name="week1Home"),
    path("week1/week1Bilguun",      viewsWeek1.week1BilguunViews,       name="week1Bilguun"),
    path("week1/week1Magnai/",      viewsWeek1.week1MagnaiViews,        name="week1Magnai"),
    path("week1/week1Odke/",        viewsWeek1.week1OdkeViews,          name="week1Odke"),
    path("week1/week1Sarnai/",      viewsWeek1.week1SarnaiViews,        name="week1Sarnai"),
    path("week1/week1Xuslen/",      viewsWeek1.week1XuslenViews,        name="week1Xuslen"),
    path("week1/week1Enkzul/",      viewsWeek1.week1EnkhzulViews,       name="week1Enkhzul"),
    path("week1/week1Zndra/",       viewsWeek1.week1ZndraViews,         name="week1Zndra"),
    path("week1/week1Bayrbat/",     viewsWeek1.week1BayrbatViews,       name="week1Bayrbat"),
    path("week1/week1Odonkhuu/",    viewsWeek1.week1OdonkhuuViews,      name="week1Odonkhuu"),
    path("week1/week1Eldos/",       viewsWeek1.week1EldosViews,         name="week1Eldos"),
    path("week1/week1Nomin/",       viewsWeek1.week1NominViews,         name="week1Nomin"),
    path("week1/week1Tudu/",        viewsWeek1.week1TuduViews,          name="week1Tudu"),
    path("week1/week1Nomio1/",      viewsWeek1.week1Nomio1Views,        name="week1Nomio1"),
    path("week1/week1Tserenbaatar/",viewsWeek1.week1TserenbaatarViews,  name="week1Tserenbaatar"),
    path("week1/week1Bumaa/",       viewsWeek1.week1BumaaViews,         name="week1Bumaa"),
    path("week1/week1Olzii/",       viewsWeek1.week1OlziiViews,         name="week1Olzii"),
    path("week1/week1HaTuguldur/",  viewsWeek1.week1HaTuguldurViews,    name="week1HaTuguldur"),
    path("week1/week1Ebe/",         viewsWeek1.week1EbeViews,           name="week1Ebe"),
    ]  
