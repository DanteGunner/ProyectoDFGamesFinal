from django.shortcuts import render, redirect 
from .models import Compania, Juego
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def playstation(request):
    return render(request, 'core/playstation.html')

def xbox(request):
    return render(request, 'core/xbox.html')

def switch(request):
    return render(request, 'core/switch.html')

def comprar(request):
    return render(request, 'core/comprar.html')
@login_required
def formulario(request):

    companias = Compania.objects.all()
    variables = {
        'companias':companias
    }

    if request.POST:
        juego = Juego()
        juego.codigo = request.POST.get('txtCodigo')
        juego.nombre = request.POST.get('txtNombre')
        juego.anio_lanzamiento = request.POST.get('txtAnio')
        compania = Compania()
        compania.id = request.POST.get('cboCompania')
        juego.compania = compania

        try:
            juego.save()
            variables['mensaje'] = 'Juego guardado correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'


    return render(request, 'core/formulario.html', variables)

#CRUD de juegos
@login_required
def listar_juegos(request):

    juegos = Juego.objects.all()

    return render(request, 'core/listar_juegos.html',{
        'juegos':juegos
    })
@login_required
def eliminar_juego(request, id):
    #Buscar juego para eliminar
    juego = Juego.objects.get(id=id)

    try:
        juego.delete()
        mensaje = "Juego eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request, mensaje)

    return redirect('listado_juegos')

def modificar_juego(request, id):
    #Buscar juego
    juego = Juego.objects.get(id=id)
    companias = Compania.objects.all()
    variables = {
        'juego':juego,
        'companias':companias
    }

    if request.POST:
        juego = Juego()
        juego.id = request.POST.get('txtId')
        juego.codigo = request.POST.get('txtCodigo')
        juego.nombre = request.POST.get('txtNombre')
        juego.anio_lanzamiento = request.POST.get('txtAnio')
        compania = Compania()
        compania.id = request.POST.get('cboCompania')
        juego.compania = compania

        try:
            juego.save()
            messages.success(request, 'Juego modificado correctamente')
        except:
            messages.error(request, 'No se ha podido modificar')
        return redirect('listado_juegos')

    return render(request, 'core/modificar_juego.html', variables)

