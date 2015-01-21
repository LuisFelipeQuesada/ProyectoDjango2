# Librerias de Django
from django.db import models
from django.forms import ModelForm
from django import forms
from django.core.validators import *
from django.contrib.auth.models import User

# Librerias Externas
import oauth2 as oauth

# Se define la clase Contact, la cual representa los contactos que se ingresaran a la base de datos
class Contact(models.Model):
	name = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	business = models.CharField(max_length=200)
	age = models.IntegerField()
	phone = models.IntegerField()
	email = models.EmailField(max_length=200)
	longitud = models.FloatField(null=True)
	latitud = models.FloatField(null=True)

	# Este metodo se encarga de mostrar todos los campos como strings 
	def __unicode__(self):
		return self.name, self.lastName, self.business, self.age, self.phone, self.email, self.longitud, self.latitud

# Clase en la que se crea un Form para el modelo Contact
# Se define el modelo que utiliza asi como los campos que se mostran y algunas propiedades para los widgets
class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ('id', 'name', 'lastName', 'business', 'age', 'phone', 'email', 'longitud', 'latitud')
		widgets = {
            'name': forms.TextInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
            'lastName': forms.TextInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
            'age': forms.TextInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
            'business': forms.TextInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
            'email': forms.TextInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
            'phone': forms.TextInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
            'longitud': forms.HiddenInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
            'latitud': forms.HiddenInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
        }

# Clase en la que se crea un Form para el modelo Contact
# Se define el modelo que utiliza asi como los campos que se mostran y algunas propiedades para los widgets
class ContactEditForm(ModelForm):
	class Meta:
		model = Contact
		fields = ('id', 'name', 'lastName', 'business', 'age', 'phone', 'email', 'longitud', 'latitud')
		widgets = {
            'name': forms.TextInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
            'lastName': forms.TextInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
            'age': forms.TextInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
            'business': forms.TextInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
            'email': forms.TextInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
            'phone': forms.TextInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
            'longitud': forms.HiddenInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
            'latitud': forms.HiddenInput(attrs={'cols': 80, 'rows': 20, 'class':"text"}),
        }

