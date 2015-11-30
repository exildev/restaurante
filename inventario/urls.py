from django.conf.urls import include, url
import views

urlpatterns = [
	#forms
	url(r'almacen/form/', views.AlmacenFormView.as_view(), name="almacen_form"),
	url(r'producto/form/', views.ProductoFormView.as_view(), name="producto_form"),
	url(r'proveedor/form/', views.ProveedorFormView.as_view(), name="proveedor_form"),
	url(r'presentacion/form/', views.PresentacionFormView.as_view(), name="presentacion_form"),
	url(r'entrada/form/', views.EntradaFormView.as_view(), name="entrada_form"),
	url(r'salida/form/', views.SalidaFormView.as_view(), name="salida_form"),
	url(r'requisiciondecompra/form/', views.RequisicionDeCompraFormView.as_view(), name="requisiciondecompra_form"),
	url(r'solicituddeproducto/form/', views.SolicitudDeProductoFormView.as_view(), name="solicituddeproducto_form"),

	#forms
	url(r'producto/list/', views.ProductoListView.as_view(), name="producto_list"),
]