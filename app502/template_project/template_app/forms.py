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



class CambioEstadoForm(forms.Form):
	ESTADOS = [
        ('En preparacion', 'En preparacion'),
        ('Despachado', 'Despachado'),
        ('En camino', 'En camino'),
        ('Entregado', 'Entregado'),
    ]

	codigoSeguim = forms.IntegerField(label='CodSeguim', widget = forms.TextInput(attrs={'placeholder':'Codigo de seguimiento'}), required = True)
	estado = forms.ChoiceField(widget=forms.Select,choices=ESTADOS)



class FiltroEnviosForm(forms.Form):
	FILTROS = [
        ('Codigo de seguim', 'Codigo de seguim'),
        ('Estado', 'Estado'),
        ('DNI destinatario', 'DNI destinatario'),
    ]
	
	filtro = forms.ChoiceField(widget=forms.Select,choices=FILTROS)




