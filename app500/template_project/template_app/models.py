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

class Persona(models.Model):
	dni = models.IntegerField()
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	domicilio = models.CharField(max_length=200)
	fechaNac = models.DateField()

	class Meta():
		db_table = 'persona'



class Propietario(models.Model):
	dniPersona = models.IntegerField()
	idCuenta = models.IntegerField()
	
	class Meta():
		db_table = 'propietario'



class Cuenta(models.Model):
	nroCuenta = models.IntegerField()
	dniPersona = models.IntegerField()
	saldo = models.FloatField()

	class Meta():
		db_table = 'cuenta'

class Tarjeta(models.Model):
	TIPOS = (
		('Credito', 'Credito'),
		('Debito', 'Debito'),
	)
	
	LIMITES = (
		('100000', '100000'),
		('70000', '70000'),
		('50000', '50000'),
		('30000', '30000'),
	)
	nroCuenta = models.IntegerField()
	nroTarjeta = models.IntegerField()
	tipo_tarjeta = models.CharField(max_length=12, choices=TIPOS)
	limite_tarjeta = models.CharField(max_length=12, choices=LIMITES, null=True, blank=True)
	saldo = models.FloatField()

	class Meta():
		db_table = 'tarjeta'