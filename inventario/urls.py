from django.conf.urls import include, url
import views

urlpatterns = [
	#forms
	url(r'almacen/form/$', views.AlmacenFormView.as_view(), name="almacen_form"),
	url(r'producto/form/$', views.ProductoFormView.as_view(), name="producto_form"),
	url(r'proveedor/form/$', views.ProveedorFormView.as_view(), name="proveedor_form"),
	url(r'presentacion/form/$', views.PresentacionFormView.as_view(), name="presentacion_form"),
	url(r'entrada/form/$', views.EntradaFormView.as_view(), name="entrada_form"),
	url(r'salida/form/$', views.SalidaFormView.as_view(), name="salida_form"),
	url(r'requisiciondecompra/form/$', views.RequisicionDeCompraFormView.as_view(), name="requisiciondecompra_form"),
	url(r'solicituddeproducto/form/$', views.SolicitudDeProductoFormView.as_view(), name="solicituddeproducto_form"),

	#lists
	url(r'producto/list/$', views.ProductoListView.as_view(), name="producto_list"),
	url(r'proveedor/list/$', views.ProveedorListView.as_view(), name="proveedor_list"),
	url(r'presentacion/list/$', views.PresentacionListView.as_view(), name="presentacion_list"),
	url(r'entrada/list/$', views.EntradaListView.as_view(), name="entrada_list"),
	url(r'salida/list/$', views.SalidaListView.as_view(), name="salida_list"),
	url(r'requisiciondecompra/list/$', views.RequisicionDeCompraListView.as_view(), name="requisiciondecompra_list"),
	url(r'solicituddeproducto/list/$', views.SolicitudDeProductoListView.as_view(), name="solicituddeproducto_list"),

	#detail
	url(r'requisiciondecompra/detail/(?P<pk>[-\w]+)/$', views.RequisiscionDeCompraDetail.as_view(), name="requisiciondecompradetail_list"),

]