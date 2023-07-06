#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("pago", views.pago, name = "pago"),
    path("pagoRealizado", views.pagoRealizado, name = "pagoRealizado")
=======
    path("pago", views.pago, name = "pago")
>>>>>>> 9a38003a42b110fe87bd9095d930a442ebae2b1c
]
