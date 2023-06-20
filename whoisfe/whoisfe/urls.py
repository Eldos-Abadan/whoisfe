
from django.urls import path,  include

urlpatterns = [

    # newtersen hereglegchiin huudasnuud #
    path("", include('whoisfe.route.urlsLogged')),
  
    # week1 huudasnuud #
    path("", include('whoisfe.route.urlsWeek1')),

      # notlogin #
     path("", include('whoisfe.route.urlsNotLogin')),

]
