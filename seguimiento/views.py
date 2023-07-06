from django.shortcuts import render, get_object_or_404
from .models import Envio
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def seguimiento(request):
    context = {}
    return render(request, 'seguimiento/seguimiento.html', context)


def busqueda(request, cod):
    context = {}
    if request.method == 'POST':
        try:
            envio = Envio.objects.get(codigo_seguimiento=cod)
        except ObjectDoesNotExist:
            envio = None

        context = {'envio': envio}
        return render(request, 'seguimiento/seguimiento.html', context)
    else:
        return render(request, 'seguimiento/seguimiento.html', context)

def busquedaRealizada(request):
    if request.method == 'POST':
        NroSeguimiento     = request.POST["NroSeguimiento"]
        try:
            envio = Envio.objects.get(codigo_seguimiento=NroSeguimiento)
        except ObjectDoesNotExist:
            envio = None

        context = {'envio': envio,'NroSeguimiento':NroSeguimiento}
        return render(request, 'seguimiento/seguimiento.html', context)
    else:
        return render(request, 'seguimiento/seguimiento.html', context)