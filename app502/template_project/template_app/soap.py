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

class Envios(ComplexModel):
	id = Integer
	codigoSeguim = Integer
	nroVendedor = Integer
	dniPersona = Integer
	estado = String
	domicilio_entrega = String
#	idPaquete = Integer


#class Paquete(ComplexModel):
#	id = Integer
#	descrip = Float
#	cantidad = Integer


class SoapService(ServiceBase):
	#@rpc(Double(), Double(), _returns = Double)
	#def sum (ctx, a, b):
	#	print("[MSG FROM CORREO SERVICE] " + str(a + b))
	#	return a + b

	@rpc(Integer(), Integer(), String(), _returns = Integer)
	def generarCodSeguimiento(ctx, idvendedor, dniPersona, domicilio):

		try:
			ultimo_cod = models.Envio.objects.order_by('codigoSeguim').last()
			print (ultimo_cod)
			print (type(ultimo_cod))
			if ultimo_cod == None:
				ultimo_cod = 1
				envio = models.Envio(codigoSeguim=ultimo_cod,nroVendedor=idvendedor,dniPersona=dniPersona,estado='En preparacion',domicilio_entrega=domicilio)
				envio.save()
			else:
				ultimo_cod = ultimo_cod.codigoSeguim + 1
				envio = models.Envio(codigoSeguim= ultimo_cod,nroVendedor = idvendedor,dniPersona=dniPersona,estado='En preparacion',domicilio_entrega=domicilio)
				envio.save()
		except models.Envio.DoesNotExist:
			ultimo_cod = 1

		return ultimo_cod


	@rpc(Integer(), _returns = String)
	def consultarEstadoPorCodSeguim(ctx, codigoSeguim):
		envio = models.Envio.objects.get(codigoSeguim= codigoSeguim)

		return envio.estado



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