from django.db import models

# Create your models here.


##	TEMPLATE MODEL

#class FechaNacimiento(models.Model):
#	year = models.IntegerField()
#	month = models.IntegerField()
#	day = models.IntegerField()
#
#	class Meta():
#		db_table = 'f_nacimiento'
#		
#	'''
#	def __str__(self):
#		return str(self.day) + '/' + str(self.month) + '/' + str(self.year) 
#	'''

#class FechaNacimiento(models.Model):
#	f_nac = models.DateTimeField('date published')
#
#	class Meta():
#		db_table = 'f_nacimiento'
#		
#	'''
#	def __str__(self):
#		return str(self.f_nac) 
#	'''

class Envio(models.Model):
	ESTADOS = (
        ('En preparacion', 'En preparacion'),
        ('Despachado', 'Despachado'),
        ('En camino', 'En camino'),
        ('Entregado', 'Entregado'),
    )

	codigoSeguim = models.IntegerField(unique = True)
	nroVendedor = models.IntegerField()
	dniPersona = models.IntegerField()
	estado = models.CharField(max_length=20, choices= ESTADOS)
	domicilio_entrega = models.CharField(max_length=200)

	class Meta():
		db_table = 'envio'


#class Paquete(models.Model):
#	descrip = models.FloatField()
#	cantidad = models.IntegerField()

#	class Meta():
#		db_table = 'paquete'
