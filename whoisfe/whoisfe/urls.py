
from django.urls import path,  include

urlpatterns = [
    # undsen huudasnuud #
    path("", include('whoisfe.route.urlsMain')),

    # newtersen hereglegchiin huudasnuud #
    path("", include('whoisfe.route.urlsLogged')),
  
    # week1 huudasnuud #
    path("", include('whoisfe.route.urlsWeek1')),
   
    # Forget #
    path("", include('whoisfe.route.urlsForget')),
 
    # Register #
    path("", include('whoisfe.route.urlsRegister')),
    
    # Personal Information Form #
    path("", include('whoisfe.route.urlsPerInfo')),
 
    # login huudas #
    path("", include('whoisfe.route.urlsLogin')),
    
    # my name card  #
    path("", include('whoisfe.route.urlsMyNC')),
    
    # CreateCV #
     path("", include('whoisfe.route.urlsCreateCV')),


]
