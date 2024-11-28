# Blog_Django
 Blog funcional con Django -
 
DESCRIPCION:
-------------------------------
Este blog cuenta con una página principal donde se muestran todos los blogs agregados. Dispone de una barra de navegación simple, que incluye las opciones: "Inicio" (que nos lleva a la página principal), "Agregar un nuevo blog" y "Nosotros", donde se ofrece una pequeña descripción.

Los posts se listarán de tres en tres por página, ya que contamos con un paginador funcional. En cada post veremos la imagen del autor, su nombre, la fecha de creación, un fragmento del post y el título, que es un enlace que nos dirige a una vista donde se podrá ver el contenido completo de dicho post. Además, cada entrada cuenta con botones para "Actualizar" y "Eliminar".
-------------------------------
INTRUCCIONES PARA SU USO:
1) Asegurate de tener instalado Python en tu ordenador ya que este proyecto esta creado con Django
   lo puedes instalar de la pagina principal https://www.python.org/downloads/
   RECOMENDACION: asegurate de marcar la opcion de: Add python.exe to PATH ya que es indispensable para la correcta ejecucion.
      ![image](https://github.com/user-attachments/assets/cb628fde-e56c-418b-b354-965a484f8d1e)
2) Asegurate de tener instalado un editor de texto, se recomiendo Visual studio code
   lo puedes descargar:https://code.visualstudio.com/Download
3) Una vez hecho esto debemos abrir nuestro editor de texto y verificar si tenemos instalado Django,
   para verificar es muy sencillo abrimos una terminal presionando ctrl+ñ en nuestro editor y ejecutamos este comando:
   python -m django --version , esto nos debe devolver la version de Django en caso contrario significa que Django no esta instalado
   y para instalarlo ejecutamos el siguiente comando:pip install django
4) En este punto ya tendriamos lo necesario para poder ejecutar nuestro proyecto,dirigite a:https://github.com/Jkpepo/Blog_Django
5) Presiona el boton Code<>
6) Download ZIP y lo guardamos en una ubicacion en nuestro equipo
7) Extraemos el ZIP, click derecho extraer en "BLog_Django-main"
8) En nuestro editor en la parte superior izquierda presionamos "File"(Archivo)
   "Open Folder"(Abrir Carpeta) y seleccionamos la carpeta que acabamos de extraer, esto nos cargara el proyecto

9)En una terminal ejecutamos el siguiente comando cd Blog_Django-main\Blog_Django y presionamos enter
10) Ahora ejecutaremos py manage.py runserver y enter y nos debe aparecer algo asi:
    
    System check identified no issues (0 silenced).
    November 27, 2024 - 21:24:49
    Django version 5.1.3, using settings 'Blog_Django.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
12) Presionamos ctrl+click encima de la Url http://127.0.0.1:8000/ y nos abre una ventana en nuestro navegador de internet
13) ¡Ya estarás ejecutando el proyecto!
   


