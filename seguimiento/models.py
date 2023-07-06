from django.db import models

# Create your models here.

class EstadoEnvio(models.Model):
    id_est_envio        = models.AutoField(primary_key=True)
    nombre_estado_env   = models.CharField(max_length=100)

class Ubicacion(models.Model):
    id_ubicacion        = models.AutoField(primary_key=True)
    direccion           = models.CharField(max_length=200)
    id_region           = models.ForeignKey('carrito.Region', on_delete=models.CASCADE)
    id_comuna           = models.ForeignKey('carrito.Comuna', on_delete=models.CASCADE)

class Envio(models.Model):
    id_envio            = models.AutoField(primary_key=True)
    codigo_seguimiento  = models.CharField(max_length=20, unique=True, default='')
    fecha_envio         = models.DateField()
    id_est_envio        = models.ForeignKey('seguimiento.EstadoEnvio', on_delete=models.CASCADE)
    id_pedido           = models.ForeignKey('carrito.Pedido', on_delete=models.CASCADE)

