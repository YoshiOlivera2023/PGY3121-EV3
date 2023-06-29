from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, "bicicletas/index.html", context)

def formBici(request):
    context = {}
    return render(request, "bicicletas/formBici.html", context)