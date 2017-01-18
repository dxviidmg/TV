from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *

class ListViewCanales(View):
	def get(self, request):
		template_name = 'canales/ListCanales.html'
		categorias = Categoria.objects.all()
#		canales = Canal.objects.all()

		ListaDeCanalesPorCategoria = []

		for categoria in categorias:
			ListaDeCanalesPorCategoria.append({'categoria': categoria.nombre, 'canales': Canal.objects.filter(categoria=categoria)})
			#objects.append({'user':perm.user,'edit':perm.edit})

		print(ListaDeCanalesPorCategoria)
		context = {
#		'categorias': categorias,
#		'canales': canales,
		'ListaDeCanalesPorCategoria': ListaDeCanalesPorCategoria
		}
		return render(request, template_name, context)

class DetailViewCanal(View):
	def get(self, request, pk):
		template_name = 'canales/DetailCanal.html'
		canal = get_object_or_404(Canal, pk=pk)
		context = {
		'canal': canal
		}
		return render(request, template_name, context)