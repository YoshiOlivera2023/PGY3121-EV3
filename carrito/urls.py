#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("carrito_compras", views.carrito_compras, name = "carrito_compras"),
<<<<<<< HEAD
    path("producto_del/<int:pk>", views.producto_del, name = "producto_del"),
=======
#     path("login", views.login, name = "login"),
#     path("registro", views.registro, name = "registro"),
#     path("index", views.index, name = "index"),
#     path("nosotros", views.nosotros, name = "nosotros"),
#     path("productos", views.productos, name = "productos"),
#     path("seguimiento", views.seguimiento, name = "seguimiento"),
#     path("ayuda", views.ayuda, name = "ayuda"),
>>>>>>> 9a38003a42b110fe87bd9095d930a442ebae2b1c
]




