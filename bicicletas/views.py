from django.shortcuts import render
from .models import Bicicleta, Categoria, Marca
from carrito.models import Pedido, ProductoCarrito, Usuario
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import os
from django.db.models import Sum, Q

# Create your views here.

def productos(request):
    bicicletas = Bicicleta.objects.all()
    context = {"bicicletas": bicicletas}
    return render(request, "bicicletas/productos.html", context)

def formBici(request):
    if request.method != "POST":
        categorias = Categoria.objects.all()
        marcas = Marca.objects.all()
        context = {"categorias": categorias, "marcas": marcas}
        return render(request, "bicicletas/formBici.html", context)
    else:
        id_bicicleta        = request.POST.get("id_bicicleta")
        nombre_bicicleta    = request.POST.get("nombre")
        descripcion         = request.POST.get("descripcion")
        precio              = request.POST.get("precio")
        imagen               = request.FILES.get('imagen')
        categoria_id        = request.POST.get("categoria")
        marca_id            = request.POST.get("marca")

        try:
            objCategoria = Categoria.objects.get(id_categoria=categoria_id)
            objMarca = Marca.objects.get(id_marca=marca_id)

            # Guardar la imagen en el directorio de almacenamiento estático
            if 'imagen' in request.FILES:
                with open(os.path.join(settings.STATIC_ROOT, 'img/productos', imagen.name), 'wb') as destination:
                    for chunk in imagen.chunks():
                        destination.write(chunk)
            else:
                error_message = "SIN IMG."            


            obj = Bicicleta.objects.create(
                id_bicicleta=id_bicicleta,
                nombre_bicicleta=nombre_bicicleta,
                descripcion=descripcion,
                precio=precio,
                imagen=imagen.name,
                id_categoria=objCategoria,
                id_marca=objMarca
            )
            obj.save()
            bicicletas = Bicicleta.objects.all()
            context = {"bicicletas": bicicletas}
            return render(request, "bicicletas/listBici.html", context)
        except ObjectDoesNotExist:
            error_message = "La categoría o marca seleccionada no existe."
            categorias = Categoria.objects.all()
            marcas = Marca.objects.all()
            context = {"categorias": categorias, "marcas": marcas, "error_message": error_message}
            return render(request, "bicicletas/formBici.html", context)


def crudBici(request):
    bicicletas = Bicicleta.objects.all()
    context = {"bicicletas": bicicletas}
    return render(request, "bicicletas/listBici.html", context)

def delBici(request,pk):
    context={}
    try:
        bicicleta = Bicicleta.objects.get(id_bicicleta = pk)   
        bicicleta.delete()
        mensaje = "Bien, datos eliminados..."
        bicicletas = Bicicleta.objects.all()
        context = {"bicicletas": bicicletas, "mensaje": mensaje}
        return render(request, "bicicletas/listBici.html", context)
    except:
        mensaje = "Error, id no existe..."
        bicicletas = Bicicleta.objects.all()
        context = {"bicicletas": bicicletas, "mensaje": mensaje}
        return render(request, "bicicletas/listBici.html", context)

def editBici(request, pk):
    if pk != 0:
        bicicleta = Bicicleta.objects.get(id_bicicleta = pk)
        categorias = Categoria.objects.all()
        marcas = Marca.objects.all()

        context = {"bicicleta": bicicleta, "categorias": categorias, "marcas": marcas}
        if bicicleta:
            return render(request, "bicicletas/editBici.html", context)
        else:
            context = {"mensaje":"Error, rut no existe..."}
            return render(request, "bicicletas/listBici.html", context)
        
def updateBici(request):
    if request.method == "POST":
        #Es un POST, por lo tanto se recuperan los datos del formulario
        #y se graban en la tabla
    
        id_bicicleta     = request.POST["id_bicicleta"]
        nombre_bicicleta = request.POST["nombre"]
        descripcion      = request.POST["descripcion"]   
        precio           = request.POST["precio"]   
        imagen           = request.FILES.get('imagen') 
        categoria        = request.POST["categoria"]    
        marca            = request.POST["marca"]
        
        objCategoria = Categoria.objects.get(id_categoria = categoria)
        objMarca     = Marca.objects.get(id_marca = marca)
        if 'imagen' in request.FILES:
             with open(os.path.join(settings.STATIC_ROOT, 'img/productos', imagen.name), 'wb') as destination:
                for chunk in imagen.chunks():
                    destination.write(chunk)

        bicicleta = Bicicleta()
        bicicleta.id_bicicleta = id_bicicleta
        bicicleta.nombre_bicicleta = nombre_bicicleta
        bicicleta.descripcion = descripcion
        bicicleta.precio = precio
        bicicleta.imagen = imagen.name
        bicicleta.id_categoria = objCategoria
        bicicleta.id_marca = objMarca
        bicicleta.save()
        
     
        bicicletas = Bicicleta.objects.all()
        context = {"mensaje": "Ok, los datos actualizados...","bicicletas": bicicletas}
        return render(request, "bicicletas/listBici.html", context)
    else:
        #no es un POST, por lo tanto se muestra el formulario para agregar.
        bicicletas = Bicicleta.objects.all()
        context = {"bicicletas": bicicletas}
        return render(request, "bicicletas/listBici.html", context)
    
def insertarCarrito(request):
    if request.method == "POST":
        bicicleta_id = request.POST.get("bicicleta_id")
        precio = request.POST.get("precio")
        usuario_id = request.user.id
        
        try:
            usuario = Usuario.objects.get(id_usuario=usuario_id)

        except (Usuario.DoesNotExist):
            usuario = usuario_id
        
        obj = ProductoCarrito.objects.create(
            cantidad=1,
            precio_total=precio,
            id_bicicleta_id=bicicleta_id,
            id_usuario=usuario
        )
        obj.save()
        id_usuario=request.user.id
        productos = ProductoCarrito.objects.filter(Q(id_usuario=id_usuario) & Q(estado=''))
        suma_total = productos.aggregate(total=Sum('precio_total'))['total']
        context = {"productos": productos, 'suma_total': suma_total}
        return render(request, "carrito/carrito_compras.html", context)

    