
from django.urls import path
from estudiantes import views


urlpatterns =[
    path("",views.index, name="index"),
 ]   


