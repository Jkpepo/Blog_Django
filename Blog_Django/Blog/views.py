from django.shortcuts import render,redirect
from . models import Publicaciones
from . forms import PublicacionesForm

# Create your views here.
def home(request):
    publicaciones=Publicaciones.objects.all()
    return render(request,"home.html",{"publicaciones":publicaciones})

def base(request):
    return render(request,"base.html")

def descripcion(request,id):
    publicacion=Publicaciones.objects.get(id=id)
    return render(request,"descripcion.html",{"publicacion":publicacion})

def crear_publicacion(request):
    if request.method == 'POST':
        formulario=PublicacionesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
        else:
            return render(request,"crearpublicacion.html",{"formulario":formulario})
    formulario=PublicacionesForm()
    return render (request,"crearpublicacion.html",{'formulario':formulario})
    



