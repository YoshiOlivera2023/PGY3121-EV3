from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario          = models.AutoField(primary_key=True)
    nombre_usuario      = models.CharField(max_length=50)
    email               = models.CharField(max_length=50)
    contraseña          = models.CharField(max_length=50)
    id_region           = models.ForeignKey('carrito.Region', on_delete=models.CASCADE)
    id_comuna           = models.ForeignKey('carrito.Comuna', on_delete=models.CASCADE)

class ProductoCarrito(models.Model):
    id_prod_carr        = models.AutoField(primary_key=True)
    cantidad            = models.IntegerField()
    precio_total        = models.IntegerField()
    id_bicicleta        = models.ForeignKey('bicicletas.Bicicleta', on_delete=models.CASCADE)
    id_carrito          = models.ForeignKey('Carrito', on_delete=models.CASCADE)

class Carrito(models.Model):
    id_carrito          = models.AutoField(primary_key=True)
    usuario             = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Pedido(models.Model):
    id_pedido           = models.AutoField(primary_key=True)
    fecha_pedido        = models.DateField()
    estado_pedido       = models.ForeignKey('EstadoPedido', on_delete=models.CASCADE)
    usuario             = models.ForeignKey(Usuario, on_delete=models.CASCADE)
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

