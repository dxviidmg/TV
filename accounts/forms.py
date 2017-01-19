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

#	def clean_email(self):
#		cd = self.cleaned_data
#		if User.objects.filter(email=cd['email']).exists():		
#			raise forms.ValidationError("This email already used")
#		return cd['email']

class PerfilCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('fecha_de_nacimiento', 'fotografia')