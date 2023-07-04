from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from . import views

# Create your views here.

def index(request):
    context = {}
    return render(request, "administrador/index.html", context)

def nosotros(request):
    context = {}
    return render(request, "administrador/nosotros.html", context)

# def productos(request):
#     context = {}
#     return render(request, "bicicletas/productos.html", context)

# def seguimiento(request):
#     context = {}
#     return render(request, "seguimiento/seguimiento.html", context)

def ayuda(request):
    context = {}
    return render(request, "administrador/ayuda.html", context)

def registro(request):
    context = {}
    return render(request, "administrador/registro.html", context)

# @login_required
# def custom_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect(reverse('administrador:index'))  # Redirige a la vista 'index' dentro de la aplicación 'administrador'
#         else:
#             return render(request, 'administrador/login.html', {'error': 'Usuario o contraseña incorrectos'})
#     else:
#         return render(request, 'administrador/login.html')