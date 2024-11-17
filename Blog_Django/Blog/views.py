from django.shortcuts import render
from . models import Publicaciones

# Create your views here.
def home(request):
    publicacion=Publicaciones.objects.all()
    return render(request,"home.html",{"publicacion":publicacion})



