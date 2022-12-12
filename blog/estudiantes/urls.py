
from django.urls import path
from estudiantes import views
#from estudiantes.views import Home


urlpatterns =[
    path("",views.index, name="index"),
 ]   

#path("",views.home, name="home"),
