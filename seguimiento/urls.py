#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("seguimiento", views.seguimiento, name = "seguimiento"),
<<<<<<< HEAD
    path("busqueda/<str:cod>", views.busqueda, name = "busqueda"),
    path("busquedaRealizada", views.busquedaRealizada, name = "busquedaRealizada")   

    
=======
    path("busqueda/<str:cod>", views.busqueda, name = "busqueda")
>>>>>>> 9a38003a42b110fe87bd9095d930a442ebae2b1c
]
