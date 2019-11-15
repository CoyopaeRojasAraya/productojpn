from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    #Model representing a book genre."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name

class Articulo(models.Model):
    
	title = models.CharField(max_length=200)
	coleccion = models.ForeignKey('Coleccion', on_delete=models.SET_NULL, null=True)
	resumen = models.TextField(max_length=1000, help_text='Resumen del producto')
	codigo = models.CharField('codigo', max_length=13, help_text='13 Character">Codigo numerico</a>')
	
    
	def __str__(self):
		return self.title
    
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('articulo_detail', args=[str(self.id)])


class ArticuloInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identificador del articulo')
	articulo = models.ForeignKey('Articulo', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)

	LOAN_STATUS = (
		('m', 'Proximamente'),
		('a', 'Disponible'),
		('r', 'Reservado'),
	)

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='m',
		help_text='Disponible',
	)

	class Meta:
		ordering = ['due_back']

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.id} ({self.articulo.title})'


class Coleccion(models.Model):
	"""Model representing an author."""
	nombre = models.CharField(max_length=100)
	date_of_launch = models.DateField(null=True, blank=True)
	
	class Meta:
		ordering = ['nombre']

	def get_absolute_url(self):
		return reverse('coleccion_detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.nombre}'	

