from django import forms
from django.forms.models import inlineformset_factory, modelformset_factory
import models

class AlmacenForm(forms.ModelForm):
	class Meta:
		model = models.Almacen
		exclude = ()
	#end class
#end class

class ProductoForm(forms.ModelForm):
	class Meta:
		model = models.Producto
		exclude = ()
	#end class
#end class

class ProveedorForm(forms.ModelForm):
	class Meta:
		model = models.Proveedor
		exclude = ()
	#end class
#end class

class PresentacionForm(forms.ModelForm):
	class Meta:
		model = models.Presentacion
		exclude = ()
	#end class
#end class

class EntradaForm(forms.ModelForm):
	class Meta:
		model = models.Entrada
		exclude = ()
	#end class
#end class

class SalidaForm(forms.ModelForm):
	class Meta:
		model = models.Salida
		exclude = ()
	#end class
#end class

class RequisicionDeCompraForm(forms.ModelForm):
	class Meta:
		model = models.RequisicionDeCompra
		exclude = ()
	#end class
#end class

class SolicitudDeProductoForm(forms.ModelForm):
	class Meta:
		model = models.SolicitudDeProducto
		exclude = ()
	#end class
#end class
