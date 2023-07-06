#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("productos", views.productos, name="productos"),

    path("formBici", views.formBici, name="formBici"),
    path("crudBici", views.crudBici, name="crudBici"),
    path("delBici/<int:pk>", views.delBici, name="delBici"),
    path("editBici/<int:pk>", views.editBici, name="editBici"),
    path("updateBici", views.updateBici, name="updateBici"),
<<<<<<< HEAD
    path("updateBici", views.updateBici, name="updateBici"),
    path("insertarCarrito", views.insertarCarrito, name="insertarCarrito"),
=======
>>>>>>> 9a38003a42b110fe87bd9095d930a442ebae2b1c
]

