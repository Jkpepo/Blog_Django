from django.db import models
from django.utils import timezone

# Create your models here.
class Publicaciones(models.Model):
    titulo=models.CharField( max_length=50,null=False,blank=False)
    contenido=models.TextField(max_length=300,null=False,blank=False)
    autor=models.CharField(max_length=100,null=False,blank=False,default="Anonimo")
    fecha_publicacion=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.titulo}"