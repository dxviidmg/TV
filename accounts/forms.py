from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class UserCreateForm(forms.ModelForm):
	password = forms.CharField(label='Password',widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repite tu password',widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ('username','first_name', 'last_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Los passwords no coicinden')
		return cd['password2']

	def clean_username(self):
		cd = self.cleaned_data['username']
		if User.objects.filter(username=cd).exists():
			raise forms.ValidationError("Este usuario ya ha sido registrado")
		return cd

	def clean_email(self):
		cd = self.cleaned_data['email']
		if User.objects.filter(email=cd).exists():
			raise forms.ValidationError("Este correo electrónico ya ha sido registrado")
		return cd

class PerfilCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('fotografia',)

class UserEditForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = ('first_name', 'last_name',)
#class PasswordResetRequestForm(forms.Form):
#	email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)