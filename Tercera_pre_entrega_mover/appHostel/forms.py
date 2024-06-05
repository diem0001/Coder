from django import forms

class CuartoFormulario(forms.Form):

    nombre = forms.CharField()
    numero = forms.IntegerField()
    capacidad = forms.IntegerField()

class ClienteFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    nacionalidad = forms.CharField()

class EmpleadoFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    puesto = forms.CharField()