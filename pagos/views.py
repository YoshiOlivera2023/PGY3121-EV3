from django.shortcuts import render
from carrito.models import Pedido, ProductoCarrito, Usuario, EstadoPedido
from seguimiento.models import EstadoEnvio,Envio
from datetime import datetime
from django.db.models import Q
import random
# Create your views here.

def pago(request):
    id_usuario=request.user.id
    productos = ProductoCarrito.objects.filter(Q(id_usuario=id_usuario) & Q(estado=''))
    context = {"productos": productos}
    return render(request, "pagos/pago.html", context)

def pagoRealizado(request):
    id_usuario=request.user.id
    
    productos = ProductoCarrito.objects.filter(Q(id_usuario=id_usuario) & Q(estado=''))
    ultimo_registro = productos.last()
    ProductoCarrito.objects.filter(id_usuario=id_usuario).update(estado='P')

    try:
        estado = EstadoPedido.objects.all()
        estado = estado.last()
    except (EstadoPedido.DoesNotExist):
        estado = 1

    try:
        usuario = Usuario.objects.get(id_usuario=id_usuario)
    except (Usuario.DoesNotExist):
         usuario = id_usuario 
    
    try:
        estadoEnvio = EstadoEnvio.objects.all()
        estadoEnvio = estadoEnvio.last()
    except (EstadoEnvio.DoesNotExist):
        estadoEnvio = 1           

    obj=Pedido.objects.create(
        fecha_pedido=datetime.now().date(),
        estado_pedido=estado,
        id_usuario=usuario,
        producto_carrito=ultimo_registro
    )
    obj.save()

    pedidoIngresado = Pedido.objects.all()
    ultimo_pedido_registro = pedidoIngresado.last()

    numero = random.randint(100000000000, 999999999999)
    
    obj=Envio.objects.create(
        fecha_envio=datetime.now().date(),
        codigo_seguimiento=numero,
        id_est_envio=estadoEnvio,
        id_pedido=ultimo_pedido_registro
    )
    obj.save()

    context = {"numero":numero}
    return render(request, "pagos/ok.html", context)