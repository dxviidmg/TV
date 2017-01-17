from django.views.generic import View
from django.shortcuts import render

class Home(View):
	def get(self, request):
		template_name = 'home.html'
		return render(request, template_name)
