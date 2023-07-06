from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from .models import  Comuna, EstadoPedido, Pedido, ProductoCarrito, Region, Usuario
=======
from .models import Carrito, Comuna, EstadoPedido, Pedido, ProductoCarrito, Region, Usuario
>>>>>>> 9a38003a42b110fe87bd9095d930a442ebae2b1c
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

<<<<<<< HEAD
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
=======
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
>>>>>>> 9a38003a42b110fe87bd9095d930a442ebae2b1c
