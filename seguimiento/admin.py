from django.contrib import admin
from .models import EstadoEnvio, Ubicacion, Envio
# Register your models here.

admin.site.register(EstadoEnvio)
admin.site.register(Ubicacion)
admin.site.register(Envio)