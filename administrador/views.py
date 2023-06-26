from django.shortcuts import render
from . import views

# Create your views here.

def index(request):
    context = {}
    return render(request, "administrador/index.html", context)

def nosotros(request):
    context = {}
    return render(request, "administrador/nosotros.html", context)

def productos(request):
    context = {}
    return render(request, "administrador/productos.html", context)

def seguimiento(request):
    context = {}
    return render(request, "administrador/seguimiento.html", context)

def ayuda(request):
    context = {}
    return render(request, "administrador/ayuda.html", context)

def registro(request):
    context = {}
    return render(request, "administrador/registro.html", context)

def login(request):
    context = {}
    return render(request, "administrador/login.html", context)