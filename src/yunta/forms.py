# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
            'placeholder': 'Usuario',
            'autocomplete': 'off',
        }
        self.fields['password1'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
            'placeholder': 'Contraseña',
            'autocomplete': 'off',
        }
        self.fields['password2'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
            'placeholder': 'Repetir contraseña',
            'autocomplete': 'off',
        }

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )


class UsuarioForm(forms.Form):
    dni = forms.CharField(max_length=8, required=True)
    email = forms.EmailField(required=True)
    nombres = forms.CharField(required=True)
    apellido_paterno = forms.CharField(required=True)
    apellido_materno = forms.CharField(required=True)
    terminos = forms.BooleanField(label='Acepto los términos y condiciones', required=True)

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['dni'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
            'placeholder': 'DNI',
            'autocomplete': 'off',
            'maxlength': '8',
            'size': '8'
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
            'placeholder': 'Correo',
            'autocomplete': 'off',
        }
        self.fields['nombres'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
            'placeholder': 'nombres',
            'autocomplete': 'off',
        }
        self.fields['apellido_paterno'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
            'placeholder': 'apellidos paterno',
            'autocomplete': 'off',
        }
        self.fields['apellido_materno'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
            'placeholder': 'apellido materno',
            'autocomplete': 'off',
        }
        self.fields['terminos'].widget.attrs = {
            'style': 'float:left'
        }