from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns=[
	path('',views.inicio,name='inicio'),
	path('catalogo/',views.home,name='home'),
	path('inicio/', views.inicio, name="inicio"),
	path('contacto/', views.contacto, name="contacto"),
	path('noticias/',views.noticias,name='noticias'),
	path('productos/',views.productos,name='productos'),
	path('respuesta/',views.respuesta,name='respuesta'),
	path('somos/',views.somos,name='somos'),
	path('coleccion/<int:pk>', views.ColeccionDetailView.as_view(), name='coleccion_detail'),
]
urlpatterns +=[path('coleccion/create',views.ColeccionCreate.as_view(),name='coleccion_create'),
	path('coleccion/<int:pk>/update/',views.ColeccionUpdate.as_view(),name='coleccion_update'),
	path('coleccion/<int:pk>/delete/',views.ColeccionDelete.as_view(),name='coleccion_delete'),
	path('accounts/',include('django.contrib.auth.urls')),
]