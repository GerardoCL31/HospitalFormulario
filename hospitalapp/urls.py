from django.urls import path
from . import views

urlpatterns =[
    path("registro/", views.registro_cita, name="registro_cita"),
    
]