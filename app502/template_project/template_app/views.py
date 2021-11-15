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
def envios(request):

	item_list = models.Envio.objects.all()
	form_cambio_estado_msg = ""
	form_cambio_estado = forms.CambioEstadoForm()
	form_filtrar_envios = forms.FiltroEnviosForm()

	if request.method == 'POST':
		form_cambio_estado = forms.CambioEstadoForm(request.POST)
		
		if form_cambio_estado.is_valid():
			codigoSeguim = form_cambio_estado.cleaned_data.get('codigoSeguim')
			estado = form_cambio_estado.cleaned_data.get('estado')
			#envio = models.Envio.objects.get(codigoSeguim= codigoSeguim)
			try:
				envio = models.Envio.objects.get(codigoSeguim= codigoSeguim)
			except models.Envio.DoesNotExist:
				envio = None


			if envio:
				envio.estado = estado
				envio.save()
				form_cambio_estado_msg = "Se cambio el estado correctamente."
				form_cambio_estado = forms.CambioEstadoForm()
			else:
				form_cambio_estado_msg = "Error al cambiar el estado"
				
		else:
			form_filtrar_envios = forms.FiltroEnviosForm(request.POST)
			
			if form_filtrar_envios.is_valid():
				filtro = form_filtrar_envios.cleaned_data.get('filtro')

				if (filtro == 'Codigo de seguim'):
					item_list = models.Envio.objects.all().order_by('codigoSeguim')

				if (filtro == 'Estado'):
					item_list = models.Envio.objects.all().order_by('estado')

				if (filtro == 'DNI destinatario'):
					item_list = models.Envio.objects.all().order_by('dniPersona')

	context = {'item_list': item_list, 'form_filtrar_envios': form_filtrar_envios,'form_cambio_estado': form_cambio_estado, 'form_cambio_estado_msg': form_cambio_estado_msg}

	return render(request, 'envios.html', context)

