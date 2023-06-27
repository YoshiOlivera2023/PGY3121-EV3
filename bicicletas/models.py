from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria        = models.AutoField(primary_key=True)
    nombre_categoria    = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

class Marca(models.Model):
    id_marca        = models.AutoField(primary_key=True)
    nombre_marca    = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_marca

class Bicicleta(models.Model):
    id_bicicleta        = models.AutoField(primary_key=True)
    nombre_bicicleta    = models.CharField(max_length=100)
    descripcion         = models.TextField()
    precio              = models.IntegerField()
    imagen              = models.ImageField(upload_to='img/')
    id_categoria        = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_marca            = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_bicicleta