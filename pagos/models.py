from django.db import models

# Create your models here.

class MetodoPago(models.Model):
    id_met_pago         = models.AutoField(primary_key=True)
    nombre_metodo_pago  = models.CharField(max_length=50)

class Pago(models.Model):
    id_pago             = models.AutoField(primary_key=True)
    monto_total         = models.IntegerField()
    fecha_pago          = models.DateField()
    id_pedido           = models.ForeignKey('carrito.Pedido', on_delete=models.CASCADE)
    id_met_pago         = models.ForeignKey('pagos.MetodoPago', on_delete=models.CASCADE)
