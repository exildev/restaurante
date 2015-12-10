from django.shortcuts import render

def render_to_pdf(template_src, context_dict):
	template = get_template(template_src)
	context  = Context(context_dict)
	html   = template.render(context)
	result = StringIO.StringIO()

	pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
#end def

def requisicion_pdf(request):
	return render_to_pdf('')