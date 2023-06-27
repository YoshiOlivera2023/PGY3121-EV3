from django.shortcuts import render
from .models import Carrito, Comuna, EstadoPedido, Pedido, ProductoCarrito, Region, Usuario
from bicicletas.models import Bicicleta, Categoria, Marca

# Create your views here.

def index(request):
    context = {}
    return render(request, "carrito/index.html", context)

def carrito_compras(request):
    carrito = ProductoCarrito.objects.select_related('bicicleta').all()
    context = {"productos": carrito}
    return render(request, "carrito/carrito_compras.html", context)