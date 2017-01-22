from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *

class ListViewCanales(View):
	def get(self, request):
		template_name = 'canales/ListCanales.html'
		categorias = Categoria.objects.all()

		ListaDeCanalesPorCategoria = []

		for categoria in categorias:
			ListaDeCanalesPorCategoria.append({'categoria': categoria.nombre, 'canales': Canal.objects.filter(categoria=categoria)})

		context = {
			'ListaDeCanalesPorCategoria': ListaDeCanalesPorCategoria
		}
		return render(request, template_name, context)

class DetailViewCanal(View):
	def get(self, request, slug):
		template_name = 'canales/DetailCanal.html'
		canal = get_object_or_404(Canal, slug=slug)
		context = {
		'canal': canal
		}
		return render(request, template_name, context)