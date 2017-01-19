from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from django.contrib import messages
from .models import *

class CreateViewAccount(View):
	def get(self, request):
		template_name = "accounts/createAccount.html"
		UserForm = UserCreateForm()
		PerfilForm = PerfilCreateForm()
		context = {
		'UserForm':UserForm,
		'PerfilForm': PerfilForm
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name = "accounts/createAccount.html"
		NuevoUserForm = UserCreateForm(request.POST)
		NuevoPerfilForm = PerfilCreateForm(request.POST, request.FILES)
		if NuevoUserForm.is_valid():
			NuevoUser = NuevoUserForm.save(commit=False)	
			NuevoUser.set_password(NuevoUserForm.cleaned_data['password'])
			NuevoUser.save()

		if NuevoPerfilForm.is_valid():
			NuevoPerfil = NuevoPerfilForm.save(commit=False)
			NuevoPerfil.user = NuevoUser
			NuevoPerfil.save()
			return redirect('accounts:login')
		else:
			context = {
			'UserForm': NuevoUserForm,
			'PerfilForm': NuevoPerfilForm
			}
			return render(request,template_name,context)

class ViewProfile(View):
#	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/viewProfile.html"
		perfil = Perfil.objects.get(user=request.user)
		print(perfil)
		context = {
			'perfil': perfil
		}
		return render(request,template_name, context)