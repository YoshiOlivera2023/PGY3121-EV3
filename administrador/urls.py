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
    # path("login", views.custom_login, name="login"),
]
