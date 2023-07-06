#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("seguimiento", views.seguimiento, name = "seguimiento"),
    path("busqueda/<str:cod>", views.busqueda, name = "busqueda"),
    path("busquedaRealizada", views.busquedaRealizada, name = "busquedaRealizada")   

    
]
