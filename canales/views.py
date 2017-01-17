from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *

class ListViewCanales(View):
	def get(self, request):
		template_name = 'canales/ListCanales.html'
		canales = Canal.objects.all()
		context = {
		'canales': canales
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