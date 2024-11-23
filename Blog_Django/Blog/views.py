from django.shortcuts import render,redirect
from . models import Publicaciones
from . forms import PublicacionesForm 
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    lista=Publicaciones.objects.all().order_by("-id")
    paginator = Paginator(lista, 3)
    pagina=request.GET.get("page") or 1 #pido el page o en su defecto 1
    publicaciones=paginator.get_page(pagina)# obtengo la pagina
    pagina_actual=int(pagina)#transformo la pagina en un numero 
    rango_inicio = (pagina_actual - 1) // 5 * 5 + 1  # Inicio del rango de páginas (páginas 1-5, 6-10, etc.)
    rango_fin = min(rango_inicio + 4, paginator.num_pages)  # Fin del rango de páginas (no superar el número total de páginas)
    paginas = range(rango_inicio, rango_fin + 1)#aqui le paso el rango inicio y fin 
    # paginas=range(1,publicaciones.paginator.num_pages +1)# esto es para que funcione normal a medida que hay mas elementos crea mas paginas
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
    



