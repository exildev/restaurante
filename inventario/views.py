from django.shortcuts import render
from supra import views as supra
import models
import forms

"""
	FORMS

"""

class AlmacenFormView(supra.SupraFormView):
	model = models.Almacen
	form_class = forms.AlmacenForm
#end class

class ProductoFormView(supra.SupraFormView):
	model = models.Producto
	form_class = forms.ProductoForm
#end class

class ProveedorFormView(supra.SupraFormView):
	model = models.Proveedor
	form_class = forms.ProveedorForm
#end class

class PresentacionFormView(supra.SupraFormView):
	model = models.Presentacion
	form_class = forms.PresentacionForm
#end class

class EntradaFormView(supra.SupraFormView):
	model = models.Entrada
	form_class = forms.EntradaForm
#end class

class SalidaFormView(supra.SupraFormView):
	model = models.Salida
	form_class = forms.SalidaForm
#end class


class SolicitudDeProductoFormView(supra.SupraInlineFormView):
	base_model = models.RequisicionDeCompra
	inline_model = models.SolicitudDeProducto
	form_class = forms.SolicitudDeProductoForm
#end class

class RequisicionDeCompraFormView(supra.SupraFormView):
	model = models.RequisicionDeCompra
	form_class = forms.RequisicionDeCompraForm
	inlines = [SolicitudDeProductoFormView]
#end class

"""
	LISTS

"""

class AlmacenListView(supra.SupraListView):
	model = models.Almacen
#end class

class ProductoListView(supra.SupraListView):
	model = models.Producto
	list_display = ['id', 'almacen', 'almacenado_en', 'username', 'nombre', 'fecha_agregado']
	class Renderer:
		almacenado_en = 'almacen__nombre'
		username = 'usuario__username'
	#end class
#end class

class ProveedorListView(supra.SupraListView):
	model = models.Proveedor
	class Renderer:
		username = 'usuario__username'
	#end class
#end class

class PresentacionListView(supra.SupraListView):
	model = models.Presentacion
	class Renderer:
		username = 'usuario__username'
	#end class
#end class

class EntradaListView(supra.SupraListView):
	model = models.Entrada
	class Renderer:
		username = 'usuario__username'
	#end class
#end class

class SalidaListView(supra.SupraListView):
	model = models.Salida
	class Renderer:
		username = 'usuario__username'
	#end class
#end class

class RequisicionDeCompraListView(supra.SupraListView):
	model = models.RequisicionDeCompra
	class Renderer:
		username = 'usuario__username'
	#end class
#end class

class SolicitudDeProductoListView(supra.SupraListView):
	model = models.SolicitudDeProducto
	search_fields = ['producto_id']
	class Renderer:
		username = 'usuario__username'
	#end class
#end class

class RequisiscionDeCompraDetail(supra.SupraDetailView):
	model = models.RequisicionDeCompra
	class Renderer:
		productos = SolicitudDeProductoListView
	#end class
#end class