from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Carrito, Comuna, EstadoPedido, Pedido, ProductoCarrito, Region, Usuario
from bicicletas.models import Bicicleta, Categoria, Marca

# Create your views here.

@login_required
def carrito_compras(request):
    carrito = ProductoCarrito.objects.select_related('bicicleta').all()
    context = {"productos": carrito}
    return render(request, "carrito/carrito_compras.html", context)

# def index(request):
#     context = {}
#     return render(request, "administrador/index.html", context)

# def login(request):
#     context = {}
#     return render(request, "administrador/login.html", context)

# def registro(request):
#     context = {}
#     return render(request, "administrador/registro.html", context)

# def nosotros(request):
#     context = {}
#     return render(request, "administrador/nosotros.html", context)

# def productos(request):
#     context = {}
#     return render(request, "bicicletas/productos.html", context)

# def seguimiento(request):
#     context = {}
#     return render(request, "administrador/seguimiento.html", context)

# def ayuda(request):
#     context = {}
#     return render(request, "administrador/ayuda.html", context)
