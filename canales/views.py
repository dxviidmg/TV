from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ListViewCanales(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = 'canales/ListCanales.html'
		categorias = Categoria.objects.all()

		ListaDeCanalesPorCategoria = []

		for categoria in categorias:
			ListaDeCanalesPorCategoria.append({'categoria': categoria.nombre, 'canales': Canal.objects.filter(categoria=categoria)})


		context = {
			'ListaDeCanalesPorCategoria': ListaDeCanalesPorCategoria,
		}
		return render(request, template_name, context)

class DetailViewCanal(View):
	@method_decorator(login_required)
	def get(self, request, slug):
		template_name = 'canales/DetailCanal.html'
		canal = get_object_or_404(Canal, slug=slug)
		categoria = Categoria.objects.get(canal=canal)
		canalesRelacionados = Canal.objects.filter(categoria=categoria).exclude(pk=canal.pk)
		context = {
			'canal': canal,
			'categoria': categoria,
			'canalesRelacionados': canalesRelacionados,
		}
		return render(request, template_name, context)