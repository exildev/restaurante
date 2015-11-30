from django.db import models
from django.contrib.auth.models import User
from cuser.fields import CurrentUserField
from django.core import validators

class Almacen(models.Model):
	usuario = CurrentUserField(add_only=True)
	nombre = models.CharField(max_length=45)
	fecha_agregado = models.DateTimeField(auto_now_add=True)
#end class

class Producto(models.Model):
	almacen = models.ForeignKey(Almacen)
	usuario = CurrentUserField(add_only=True)
	nombre = models.CharField(max_length=45)
	fecha_agregado = models.DateTimeField(auto_now_add=True)
#end class

class Proveedor(models.Model):
	usuario = CurrentUserField(add_only=True)
	nombre = models.CharField(max_length=45)
	fecha_agregado = models.DateTimeField(auto_now_add=True)
#end class

class Presentacion(models.Model):
	usuario = CurrentUserField(add_only=True)
	producto = models.ForeignKey(Producto)
	unidades = models.DecimalField(max_digits=6, decimal_places=2, validators=[validators.MinValueValidator(0)])
	fecha_agregado = models.DateTimeField(auto_now_add=True)
#end class

class Entrada(models.Model):
	usuario = CurrentUserField(add_only=True)
	codigo = models.CharField(max_length=45)
	producto = models.ForeignKey(Producto)
	presentacion = models.ForeignKey(Presentacion)
	cantidad = models.PositiveIntegerField()
	proveedor = models.ForeignKey(Proveedor)
	valor_unitario = models.DecimalField(max_digits=6, decimal_places=2, validators=[validators.MinValueValidator(0)])
	ubicacion = models.CharField(max_length=100)
	fecha = models.DateTimeField(auto_now_add=True)

	def importe(self):
		return self.valor_unitario*self.cantidad
	#end def
#end class

class Salida(models.Model):
	usuario = CurrentUserField(add_only=True)
	entrada = models.ForeignKey(Entrada)
	cantidad = models.DecimalField(max_digits=6, decimal_places=2, validators=[validators.MinValueValidator(0)])
	fecha = models.DateTimeField(auto_now_add=True)
#end class

class RequisicionDeCompra(models.Model):
	codigo = models.CharField(max_length=45)
	usuario = CurrentUserField(add_only=True)
	fecha = models.DateTimeField(auto_now_add=True)
#end class

class SolicitudDeProducto(models.Model):
	requisiciondecompra = models.ForeignKey(RequisicionDeCompra)
	producto = models.ForeignKey(Producto)
	presentacion = models.ForeignKey(Presentacion)
	cantidad = models.PositiveIntegerField()
#end class
