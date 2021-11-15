from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from . import models

##	MODEL TEMPLATE

#class ModelForm(ModelForm):
#	class Meta:
#		model = models.model_name
#		fields = '__all__'
#		widgets = {
#			'username' : forms.TextInput(attrs = {'placeholder': 'Username'}),
#			'email' : forms.TextInput(attrs = {'placeholder': 'E-Mail'}),
#			'password': forms.PasswordInput(attrs = {'placeholder': 'Password'}), 
#			'password2': forms.PasswordInput(attrs = {'placeholder': 'Password repeat'}), 
#		}
#
#class ModelForm(ModelForm):
#	username = forms.CharField(label='Usuario', widget = forms.TextInput(attrs={'placeholder':'Usuario'}), required = True)



##	LOGIN Y REGISTER
class RegisterForm(UserCreationForm):
	username = forms.CharField(label='Usuario', widget = forms.TextInput(attrs={'placeholder':'Usuario'}), required = True)
	email = forms.CharField(label='Email', widget = forms.TextInput(attrs={'placeholder':'email@email.com'}), required = True)
	password1 = forms.CharField(label='Password 1', help_text='La contraseña debe contener mas de 8 caracteres , debe incluir tanto letras como numeros y al menos una mayuscula', widget=forms.PasswordInput(attrs={'placeholder':'Password 1'}), required = True)
	password2 = forms.CharField(label='Password 2', widget=forms.PasswordInput(attrs={'placeholder':'Password 2'}), required = True)


class LoginForm(forms.Form):
	username = forms.CharField(label='Usuario', widget = forms.TextInput(attrs={'placeholder':'Usuario'}), required = True)
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Password'}), required = True)

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

##	GESTION BANCA
class NewPersonaForm(UserCreationForm):
	dni = forms.IntegerField(label='dni', widget = forms.TextInput(attrs={'placeholder':'DNI'}), required = True)
	nombre = forms.CharField(label='Nombre', widget = forms.TextInput(attrs={'placeholder':'Nombre'}), required = True)
	apellido = forms.CharField(label='Apellido', widget = forms.TextInput(attrs={'placeholder':'Apellido'}), required = True)
	domicilio = forms.CharField(label='Domicilio', widget = forms.TextInput(attrs={'placeholder':'Domicilio'}), required = True)
	fechaNac = forms.DateField(label='FechaNac', widget = forms.TextInput(attrs={'placeholder':'Fecha de Nac'}), required = True)
	
