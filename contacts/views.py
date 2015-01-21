# Django
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader, RequestContext
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.core import serializers

# Aplicacion
from contacts.models import Contact, ContactForm, ContactEditForm

# Vistas
def index(request):
	contacts = serializers.serialize("json", Contact.objects.all())
	t = loader.get_template('contacts/index.html')
	c = RequestContext(request, {'contacts':contacts})
	return HttpResponse(t.render(c))

# Entradas:	request
# Proceso:	El metodo se encarga de generar el template que permite mostrar un formulario al usuario
# Salidas:	Se retorna el template al usuario
def add(request):
	formC = ContactForm(request.POST, request.FILES)
	t = loader.get_template('contacts/add.html')
	c = RequestContext(request, {'formC':formC})
	return HttpResponse(t.render(c))

# Entradas:	Se recibe un request
# Proceso:	El metodo valida los datos y se encarga de guardar los datos en la base de datos
# Salidas:	Se retorna el template para agregar contactos
def create(request):
	formC = ContactForm(request.POST)
	t = loader.get_template('contacts/add.html')
	c = RequestContext(request, {'formC':formC})
	if request.method == 'POST' and formC.is_valid():
		formC.save()
		return HttpResponseRedirect(reverse('contacts.views.add'))
	else:
		formC = ContactForm()
	return render_to_response('contacts/add.html', {'formC':formC}, context_instance=RequestContext(request))

# Entradas:	Se recibe un request y el id del contacto que se quiere modificar
# Proceso:	El metodo pregunta si el "request" que se quiere realizar es un POST, si es asi, se toman los datos del
#			form y se almacenan en la base de datos
# Salidas:	No retorna ningun valor en concreto.
def edit(request, contact_id):
	if request.method == 'POST':
		contact = Contact.objects.get(pk=contact_id)
		formC = ContactEditForm(request.POST, instance=contact)
		if formC.is_valid():
			formC.save()
		contacts = Contact.objects.all()
		t = loader.get_template('contacts/view.html')
		c = RequestContext(request, {'contacts':contacts})
		return HttpResponseRedirect(reverse('contacts.views.view'))
	else:
		contact = Contact.objects.get(pk=contact_id)
		formC = ContactEditForm(instance=contact)
		return render_to_response('contacts/edit.html', {'formC':formC}, context_instance=RequestContext(request))

# Entradas:	Se recibe un request
# Proceso:	El metodo envia a la vista la lista de todos los contactos del usuario
# Salidas:	Una variable que se pasa a la vista y que contiene todos los contactos
def view(request):
	contacts = Contact.objects.all()
	t = loader.get_template('contacts/view.html')
	c = RequestContext(request, {'contacts':contacts})
	return HttpResponse(t.render(c))

# Entradas:	Se recibe un request y el id del contacto que se quiere consultar
# Proceso:	El metodo busca el contacto consultado por medio del id
# Salidas:	Una variable que se pasa a la vista y que contiene todos los datos del contacto consultado
def viewContact(request, contact_id,):
	contact = Contact.objects.get(pk=contact_id)
	t = loader.get_template('contacts/viewContact.html')
	c = RequestContext(request, {'contact':contact})
	return HttpResponse(t.render(c))

# Entradas:	Se recibe un request y un id del contacto a eliminar
# Proceso:	El metodo busca el contacto consultado por medio del id y lo elimina
# Salidas:	Se retorna a la vista una lista con los contactos restantes. 
def delete(request, contact_id):
    Contact.objects.get(pk=contact_id).delete()
    contacts = Contact.objects.all()
    t = loader.get_template('contacts/view.html')
    c = RequestContext(request, {'contacts':contacts})
    return HttpResponse(t.render(c))

def login(request):
	return render_to_response('contacts/login.html', context_instance=RequestContext(request))

def disconnect(request):
	return render_to_response('contacts/login.html', context_instance=RequestContext(request))



