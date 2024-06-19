from django import forms
from .models import Avatar
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

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

class UserEditForm(UserChangeForm):
    password = forms.CharField(help_text="",
    widget = forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña",widget=forms.PasswordInput)

    class Meta:
        
        model = User
        
        fields =["first_name","last_name","email"]

    def clean_password2(self):

         print(self.cleaned_data)

         password1 =self.cleaned_data["password1"]
         password2 =self.cleaned_data["password2"]

         if password1 != password2:
             
             raise forms.ValidationError("las contraseñas no coinciden")
         return password2


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ('imagen',)