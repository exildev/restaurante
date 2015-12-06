from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
	    url(r'^dashboard.html$', TemplateView.as_view(template_name="angularinv/dashboard.html")),
	    url(r'^bodegas.html$', TemplateView.as_view(template_name="angularinv/inventario.html")),
	    url(r'^recetas.html$', TemplateView.as_view(template_name="angularinv/recetas.html")),
	    url(r'^requisicion.html$', TemplateView.as_view(template_name="angularinv/requisicion.html")),
	    url(r'^ventas.html$', TemplateView.as_view(template_name="angularinv/ventas.html")),
	    url(r'^form/requisicion.html$', TemplateView.as_view(template_name="angularinv/formRequisicion.html")),
	    url(r'^dirPagination.tpl.html$', TemplateView.as_view(template_name="angularinv/dirPagination.tpl.html")),
	    url(r'^singleRequisicion.html$', TemplateView.as_view(template_name="angularinv/singleRequisicion.html")),

]