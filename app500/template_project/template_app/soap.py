from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Integer, Double, String, DateTime, Date, Float, Boolean
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase
import json
from spyne import Iterable, Array
from spyne import ComplexModel
from django.forms.models import model_to_dict
#from apps.comun.always.SearchFilter import keys_add_none
from django.db import IntegrityError
from spyne.error import ResourceNotFoundError
from django.db.models.deletion import ProtectedError


#from django.shortcuts import render
from . import models

class Personas(ComplexModel):
	id = Integer
	dni = Integer
	Nombre = String
	Apellido = String
	Domicilio = String
	FechaNac = Date

class Cuentas(ComplexModel):
	id = Integer
	saldo = Float


class SoapService(ServiceBase):
	@rpc(Double(), Double(), _returns = Double)
	def sum (ctx, a, b):
		print("[MSG FROM BANCA SERVICE] " + str(a + b))
		return a + b

	@rpc(_returns = Array(Cuentas))
	def list(ctx):
		listado = models.Cuenta.objects.values('id','saldo')

		return listado

	@rpc(Integer(), Integer(), _returns = String)
	def confirmar_identidad (ctx, nroCuenta, dniPersona):
		# confirma identidad con bd del banco
		msg=""

		cuenta = models.Cuenta.objects.filter(nroCuenta= nroCuenta, dniPersona = dniPersona)
		#print(cuenta)
		if cuenta:
			msg = "[MSG FROM BANCA SERVICE] Cuenta verificada correctamente."
		else:
			msg = "[MSG FROM BANCA SERVICE] No se ha podido verificar la cuenta."

		return msg

	@rpc(Integer(), Float(), _returns = Boolean)
	def consultar_saldo (ctx, nroTarjeta, monto_compra):
		
		tarjeta = models.Tarjeta.objects.get(nroTarjeta= nroTarjeta)

		if (tarjeta.tipo_tarjeta == 'Debito'):
			cuenta = models.Cuenta.objects.get(nroCuenta= tarjeta.nroCuenta)

			if (cuenta.saldo >= monto_compra):
				msg = True
			else:
				msg = False
		
		if (tarjeta.tipo_tarjeta == 'Credito'):
			limite = float(tarjeta.limite_tarjeta)

			if (monto_compra <= limite):
				if(tarjeta.saldo <= limite):
					tarjeta.saldo = tarjeta.saldo + monto_compra
					msg = True
				else:
					msg = False
			else:
				msg = False

		return msg


	@rpc(Float(), Integer(), _returns = String)
	def transferir_saldo (ctx, monto, nroCuenta):
		
		cuenta = models.Cuenta.objects.get(nroCuenta= nroCuenta)

		msg = ""

		if cuenta:
			cuenta.saldo = cuenta.saldo + monto
			msg = "[MSG FROM BANCA SERVICE] Transferencia realizada correctamente."
			print (cuenta.saldo)
		else:
			msg = "[MSG FROM BANCA SERVICE] No se ha podido realizar la transferencia."

		return msg


soap_app = Application(
	[SoapService],
	tns = 'django.soap.example',
	in_protocol = Soap11(validator='lxml'),
	out_protocol = Soap11(),
)



def consulta():
	django_soap_app = DjangoApplication(soap_app)
	my_soap_app = csrf_exempt(django_soap_app)

	return my_soap_app

	#context = {'my_soap_app': my_soap_app}
	#return render(request, 'home.html', context)