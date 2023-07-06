from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from . import views
from bicicletas.models import Bicicleta, Categoria, Marca
from carrito.models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
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
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            nombre_usuario        = user_creation_form.cleaned_data['username']
            email    = user_creation_form.cleaned_data['email']
            contraseña         = user_creation_form.cleaned_data['password1']

            obj = Usuario.objects.create(
            nombre_usuario=nombre_usuario,
            email=email,
            contraseña=contraseña
            )
            obj.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            #return redirect('home')
            context = {}
            return render(request, "administrador/index.html", context)
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/registro.html', data)

def agregar(request):
    bicicletas = Bicicleta.objects.all()
    context = {"bicicletas": bicicletas}
    return render(request, "bicicletas/listBici.html", context)
