# Academico/Grupos/forms.py

from django import forms
from .models import Grupo

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'
