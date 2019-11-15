from django.contrib import admin

# Register your models here.

from . models import Articulo, Coleccion, Categoria, ArticuloInstance

admin.site.register(Articulo)
admin.site.register(Coleccion)
admin.site.register(Categoria)
admin.site.register(ArticuloInstance)
