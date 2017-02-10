from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
		if NuevoUserForm.is_valid() and NuevoPerfilForm.is_valid():
			NuevoUser = NuevoUserForm.save(commit=False)
			NuevoUser.username = str(NuevoUserForm.cleaned_data['username'])
			NuevoUser.first_name = str(NuevoUserForm.cleaned_data['first_name'])
			NuevoUser.last_name = str(NuevoUserForm.cleaned_data['last_name'])
			NuevoUser.email = str(NuevoUserForm.cleaned_data['email'])	
			NuevoUser.set_password(NuevoUserForm.cleaned_data['password'])
			NuevoUser.save()

			NuevoPerfil = NuevoPerfilForm.save(commit=False)
			NuevoPerfil.user = NuevoUser
			NuevoPerfil.save()
			return redirect('accounts:login')
		else:
			context = {
			'UserForm': NuevoUserForm,
			'PerfilForm': NuevoPerfilForm
			}
			return redirect('accounts:ViewProfile')

class ViewProfile(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/viewProfile.html"
		perfil = Perfil.objects.get(user=request.user)
		UserForm = UserEditForm(instance=request.user)
		PerfilForm = PerfilCreateForm(instance=perfil)
		
		context = {
			'perfil': perfil,
			'UserForm': UserForm,
			'PerfilForm': PerfilForm,
		}
		return render(request,template_name, context)
	def post(self, request):
		template_name = "accounts/viewProfile.html"
		perfil = Perfil.objects.get(user=request.user)
		EdicionUserForm = UserEditForm(instance=request.user, data=request.POST)
		EdicionPerfilForm = PerfilCreateForm(instance=perfil, data=request.POST, files=request.FILES)

		if EdicionUserForm.is_valid:
			EdicionUserForm.save()
		if EdicionPerfilForm.is_valid:
			EdicionPerfilForm.save()
		return redirect('accounts:ViewProfile')

class ViewChangePassword(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/change_password.html"
		form = PasswordChangeForm(user=request.user)
		context = {
		'form': form,
		}
		return render(request,template_name, context)
	def post(self,request):
		template_name = "accounts/change_password.html"
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('accounts:ViewProfile')
		else:
			context = {
			'form': form,
			}
			return render(request,template_name,context)
