from django.db import models
from django.core.urlresolvers import reverse

class Categoria(models.Model):
	nombre = models.CharField(max_length=30) 

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['nombre']

class Canal(models.Model):
	categoria = models.ForeignKey(Categoria)
	nombre = models.CharField(max_length=30)
	enlace = models.CharField(max_length=30)
	logo = models.ImageField(upload_to='canales/%Y/%m/%d/', null=True, blank=True)
	slug = models.SlugField(max_length=200, unique=True, null=True)

	def get_absolute_url(self):
		return reverse('canales:DetailViewCanal', args=[self.slug])
	
	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['nombre']