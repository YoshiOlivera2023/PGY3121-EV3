#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("pago", views.pago, name = "pago"),
    path("pagoRealizado", views.pagoRealizado, name = "pagoRealizado")
]
