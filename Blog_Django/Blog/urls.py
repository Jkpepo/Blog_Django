from django.urls import path
from. import views

urlpatterns = [
    path('',views.home,name="home"),
    path('base/',views.base,name="base"),
    path('descripcion<int:id>/',views.descripcion,name="descripcion"),
    path('crearpublicacion/',views.crear_publicacion,name="crear_publicacion"),
    
]