from django import forms
from django.forms import ModelForm, PasswordInput, Select
from app.models import *
import sys, inspect

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        CHOICES = (('', 'Seleccionar'), ('A', 'Activo'), ('I', 'Inactivo'))
        widgets = {
            'clave': PasswordInput(attrs = {'type': 'password'}),
            'estado': Select( choices=CHOICES)
        }
        exclude = ['id_usuario']


def getForms():
    var = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            var.append({
                'name': name,
                'form': obj
            })

    return var
