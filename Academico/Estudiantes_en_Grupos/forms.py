# Academico/Estudiantes_en_Grupos/forms.py

from django import forms
from .models import Estudiantes_en_Grupos

class EstudiantesEnGrupoForm(forms.ModelForm):
    class Meta:
        model = Estudiantes_en_Grupos
        fields = ['id_grupo', 'id_estudiante', 'id_docente']
