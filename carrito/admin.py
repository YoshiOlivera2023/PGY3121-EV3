from django.contrib import admin
from .models import Usuario, ProductoCarrito, Pedido, EstadoPedido, Region, Comuna
# Register your models here.

admin.site.register(Usuario)
admin.site.register(ProductoCarrito)
admin.site.register(Pedido)
admin.site.register(EstadoPedido)
admin.site.register(Region)
admin.site.register(Comuna)