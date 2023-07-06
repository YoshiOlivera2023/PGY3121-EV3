#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("carrito_compras", views.carrito_compras, name = "carrito_compras"),
    path("producto_del/<int:pk>", views.producto_del, name = "producto_del"),
]




