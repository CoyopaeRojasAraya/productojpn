from django.shortcuts import render, HttpResponse
from .models import ArticuloInstance, Articulo, Coleccion, Categoria
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views import generic

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html',{})
def contacto(request):
    return render(request, 'contacto.html',{})
def noticias(request):
    return render(request, 'noticias.html',{})
def productos(request):
    Articulo1=Articulo.objects.all()
    no_Articulo=ArticuloInstance.objects.all()
    return render(request,'productos.html',context={'Articulo1':Articulo1,'no_Articulo':no_Articulo})
def respuesta(request):
    return render(request, 'respuesta.html',{})
def somos(request):
    return render(request, 'somos.html',{})
def home(request):
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    """
    Función vista para la página inicio del sitio.
    """
	

    # Genera contadores de algunos de los objetos principales
    num_articulo=Articulo.objects.all().count()
    num_instances=ArticuloInstance.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_disponible=ArticuloInstance.objects.filter(status__exact='a').count()
    num_coleccion=Coleccion.objects.count()  # El 'all()' esta implícito por defecto.
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto


    return render(
        request,
        'index.html',
        context={'num_articulo':num_articulo,'num_instances':num_instances,'num_instances_disponible':num_instances_disponible,'num_coleccion':num_coleccion,'num_visits':num_visits},
    )

class ColeccionCreate(CreateView):
	model=Coleccion
	fields='__all__'
	initial={'date_of_launch':'05/01/2018',}

class ColeccionUpdate(UpdateView):
	model=Coleccion
	fields=['nombre','date_of_launch']

class ColeccionDelete(DeleteView):
	model=Coleccion
	success_url=reverse_lazy('coleccion')

class ColeccionDetailView(generic.DetailView):
    model=Coleccion

class ArticuloDetailView(generic.DetailView):
    model = Articulo

class ArticuloListView(generic.ListView):                 
    model=Articulo
    paginate_by=10
	
class ColeccionListView(generic.ListView):                 
    model=Coleccion
    paginate_by=10
	