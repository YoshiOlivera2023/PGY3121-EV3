from django.shortcuts import render

# Create your views here.

def pago(request):
    context = {}
    return render(request, "pagos/pago.html", context)
