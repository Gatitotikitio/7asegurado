from django.shortcuts import render , redirect , get_object_or_404
from .forms import contactoForm ,  item , ProductoForm 

# Create your views here.

def home (request):
    return render (request, 'app/home.html')

def contacto(request):
    data = {
        'form': contactoForm()
    }
    if request.method == 'POST':
        formulario = contactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "contacto guardado"
        else:
            data["form"]= formulario 

    return render(request, 'app/contacto.html', data)

def repuesto (request):
    return render (request, 'app/repuesto.html')

def tuning (request):
    return render (request, 'app/tuning.html')

def pago (request):
    return render (request, 'app/pago.html')

def inicio(request):
    return render(request, 'app/inicio.html')

def registro(request):
    return render(request, 'app/registro.html')

def not404(request):
    return render (request, 'app/404.html')


def agregarProducto(request):

    data = {
        'form': ProductoForm()

    }
    if request.method ==  'POST':
        formulario = ProductoForm(data=request.POST, files=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/item/agregar.html',data)

def listarProductos(request):

    productos = item.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'app/item/listar.html',data)


def modificarProdutos(request,id):
        
        producto = get_object_or_404(item, id=id)

        data = {
            'form': ProductoForm(instance=producto)
        }

        if request.method == 'POST':
            formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect (to="listarProductos")
            data["form"]=formulario
        
        return render(request, 'app/item/modificar.html',data)


def eliminarProductos(request, id):
    producto = get_object_or_404(item, id=id)
    producto.delete()
    return redirect(to="listarProductos")

