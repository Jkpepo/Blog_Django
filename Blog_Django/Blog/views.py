from django.shortcuts import render,redirect,get_object_or_404
from . models import Publicaciones
from . forms import PublicacionesForm 
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def home(request):
    
    lista=Publicaciones.objects.all().order_by("-fecha_publicacion")
    paginator = Paginator(lista, 3)
    pagina=request.GET.get("page") or 1 #pido el page o en su defecto 1
    publicaciones=paginator.get_page(pagina)# obtengo la pagina
    pagina_actual=int(pagina)#transformo la pagina en un numero 
    rango_inicio = (pagina_actual - 1) // 5 * 5 + 1  # Inicio del rango de páginas (páginas 1-5, 6-10, etc.)
    rango_fin = min(rango_inicio + 4, paginator.num_pages)  # Fin del rango de páginas (no superar el número total de páginas)
    paginas = range(rango_inicio, rango_fin + 1)#aqui le paso el rango inicio y fin 
    # paginas=range(1,publicaciones.paginator.num_pages +1)# esto es para que funcione normal a medida que hay mas elementos crea mas paginas
    return render(request,"home.html",{"publicaciones":publicaciones,"paginas":paginas,"pagina_actual":pagina_actual})

################### BASE DEL PROYECTO #################
def base(request):
    return render(request,"base.html")

######################## VISTA PARA MOSTRAR TO.DO EL CONTENIDO ###############
def descripcion(request,id):
    publicacion=Publicaciones.objects.get(id=id)
    return render(request,"descripcion.html",{"publicacion":publicacion})

##################### CREAR UN BLOG NUEVO########################
def crear_publicacion(request):
    if request.method == 'POST':
        formulario=PublicacionesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request," Blog se agregó correctamente")
            return redirect('home')
        else:
            return render(request,"crearpublicacion.html",{"formulario":formulario})
    formulario=PublicacionesForm()
    return render (request,"crearpublicacion.html",{'formulario':formulario})

#################################### EDITAR EL BLOG MEDIANTE SU ID ################

def editar(request,id):
    formulario = get_object_or_404(Publicaciones,pk=id)
    if request.method == 'POST':
        formulario = PublicacionesForm(request.POST, instance=formulario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f"Has editado el blog:  {formulario.cleaned_data['titulo']}")
            return redirect('home')
    else:
        formulario = PublicacionesForm(instance=formulario)
    return render(request,'editar_publicacion.html',{'formulario':formulario})

############################### ELIMINAR EL BLOG MEDIANTE EL ID  ################################

def eliminar(request,id):
    formulario=Publicaciones.objects.get(id=id)
    messages.success(request,f"Has eliminado el blog:  {formulario.titulo}")
    formulario.delete()
    return redirect("home")
    
########################### VISTA PAGINA NOSOTROS 

def nosotros(request):
    return render(request,"nosotros.html")
