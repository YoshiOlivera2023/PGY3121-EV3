#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path("nosotros", views.nosotros, name = "nosotros"),
    # path("productos", views.productos, name = "productos"),
    # path("seguimiento", views.seguimiento, name = "seguimiento"),
    path("ayuda", views.ayuda,  name = "ayuda"),
    path("registro", views.registro, name = "registro"),
<<<<<<< HEAD
    path("agregar", views.agregar, name = "agregar"),
    # path("login", views.custom_login, name="login"),
]
=======
    # path("login", views.custom_login, name="login"),
]
>>>>>>> 9a38003a42b110fe87bd9095d930a442ebae2b1c
