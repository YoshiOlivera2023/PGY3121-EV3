from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import  Comuna, EstadoPedido, Pedido, ProductoCarrito, Region, Usuario
from bicicletas.models import Bicicleta, Categoria, Marca
from django.db.models import Sum, Q

# Create your views here.

@login_required
def carrito_compras(request):
    id_usuario=request.user.id
    productos = ProductoCarrito.objects.filter(Q(id_usuario=id_usuario) & Q(estado=''))
    suma_total = productos.aggregate(total=Sum('precio_total'))['total']
    context = {"productos": productos, 'suma_total': suma_total}
    return render(request, "carrito/carrito_compras.html", context)

def producto_del(request,pk):
    context={}
    try:
        producto = ProductoCarrito.objects.get(id_prod_carr = pk)   
        producto.delete()
        mensaje = "Bien, datos eliminados..."
        id_usuario=request.user.id
        productos = ProductoCarrito.objects.filter(Q(id_usuario=id_usuario) & Q(estado=''))
        suma_total = productos.aggregate(total=Sum('precio_total'))['total']
        context = {"productos": productos, "mensaje": mensaje, 'suma_total': suma_total}
        return render(request, "carrito/carrito_compras.html", context)
    except:
        mensaje = "Error, id no existe..."
        id_usuario=request.user.id
        productos = ProductoCarrito.objects.filter(Q(id_usuario=id_usuario) & Q(estado=''))
        context = {"productos": productos, "mensaje": mensaje}
        return render(request, "carrito/carrito_compras.html", context)
