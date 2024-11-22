from django.shortcuts import render,redirect
from . models import Publicaciones
from . forms import PublicacionesForm 
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    lista=Publicaciones.objects.all().order_by("-id")
    paginator = Paginator(lista, 3)
    pagina=request.GET.get("page") or 1 #pido el page o en su defecto 1
    publicaciones=paginator.get_page(pagina)# obtengo el numero paginas
    pagina_actual=int(pagina)#transformo la pagina en un numero 
    paginas=range(1,publicaciones.paginator.num_pages +1)
    return render(request,"home.html",{"publicaciones":publicaciones,"paginas":paginas,"pagina_actual":pagina_actual})

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
    



