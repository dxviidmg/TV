from django.db import models

class Canal(models.Model):
	nombre = models.CharField(max_length=30)
	enlace = models.CharField(max_length=30)
	
	def __str__(self):
		return self.nombre
