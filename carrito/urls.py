#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name = "index"),
    path("carrito_compras", views.carrito_compras, name = "carrito_compras"),
]
