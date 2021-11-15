from django.shortcuts import render , redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from . import forms

from . import models


def login_index(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
	# if this is a POST request we need to process the form data
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = forms.LoginForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				
				username = request.POST['username']
				password = request.POST['password']
				
				user = authenticate(request, username=username, password=password)

				if user is not None:
						if user.is_active:				
							login(request, user)
							return redirect('home')
							messages.success(request,'Te has identificado correctamente.')
						else:
							messages.error(request,'Tu usuario no esta activo.')
				else:
					messages.error(request,'Usuario y/o contraseña incorrectas.')

				form = forms.LoginForm()
				context = {'form': form}
		else:

			form = forms.LoginForm()
			context = {'form': form}

	return render(request, 'index.html', context)


def logout_index(request):
	logout(request)
	return redirect('login')


def registrarse(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = forms.RegisterForm()
		if request.method == 'POST':
			form = forms.RegisterForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request,'Te has registrado con exito '+ user)
				return redirect('login')
			else:
				messages.error(request,'Error al registrarte')

	context = {'form':form}

	return render(request, 'register.html', context)


@login_required(login_url='login')
def template_view(request):

	item_list = []

	context = {'item_list': item_list}

	return render(request, 'home.html', context)

@login_required(login_url='login')
def banca(request):

	form_persona = forms.NewPersonaForm()
	form_persona_msg = ""

	item_list = models.Persona.objects.all()
	item_list_cuentas = models.Cuenta.objects.all()

	if request.method == 'POST':
			form_persona = forms.NewPersonaForm(request.POST)
			if form_persona.is_valid():
				dni = form_persona.cleaned_data.get('dni')
				nombre = form_persona.cleaned_data.get('nombre')
				apellido = form_persona.cleaned_data.get('apellido')
				domicilio = form_persona.cleaned_data.get('domicilio')
				fechaNac = form_persona.cleaned_data.get('fechaNac')

				persona = models.Persona(dni=dni, nombre= nombre, apellido=apellido, domicilio=domicilio, fechaNac=fechaNac)
				print(persona)
				persona.save()

				form_persona = forms.NewPersonaForm()
				form_persona_msg = "[MSG FROM CONTROLLER] Persona registrada con exito."

			else:
				form_persona_msg = "[MSG FROM CONTROLLER] Error al registrar persona."


	context = {'item_list': item_list, 'form_persona':form_persona, 'form_persona_msg': form_persona_msg, 'item_list_cuentas':item_list_cuentas }

	return render(request, 'banca.html', context)