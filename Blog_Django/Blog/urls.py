from django.urls import path
from. import views

urlpatterns = [
    path('',views.home,name="home"),
    path('base/',views.base,name="base"),
    path('nosotros/',views.nosotros,name="nosotros"),
    path('descripcion<int:id>/',views.descripcion,name="descripcion"),
    path('crearpublicacion/',views.crear_publicacion,name="crear_publicacion"),
    path('crearpublicacion/<int:id>/',views.editar,name="editar"),
    
]