from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario          = models.AutoField(primary_key=True)
    nombre_usuario      = models.CharField(max_length=50)
    email               = models.CharField(max_length=50)
    contraseña          = models.CharField(max_length=50)


class ProductoCarrito(models.Model):
    id_prod_carr        = models.AutoField(primary_key=True)
    cantidad            = models.IntegerField()
    precio_total        = models.IntegerField()
    estado              = models.CharField(max_length=50,blank=True)
    id_bicicleta        = models.ForeignKey('bicicletas.Bicicleta', on_delete=models.CASCADE)
    id_usuario          = models.ForeignKey('Usuario', on_delete=models.CASCADE)


class Pedido(models.Model):
    id_pedido           = models.AutoField(primary_key=True)
    fecha_pedido        = models.DateField()
    estado_pedido       = models.ForeignKey('EstadoPedido', on_delete=models.CASCADE)
    id_usuario          = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto_carrito    = models.ForeignKey(ProductoCarrito, on_delete=models.CASCADE)

class EstadoPedido(models.Model):
    id_estado           = models.AutoField(primary_key=True)
    nombre_estado_ped   = models.CharField(max_length=50)

class Region(models.Model):
    id_region           = models.AutoField(primary_key=True)
    nombre_region       = models.CharField(max_length=80)

class Comuna(models.Model):
    id_comuna           = models.AutoField(primary_key=True)
    nombre_comuna       = models.CharField(max_length=70)

