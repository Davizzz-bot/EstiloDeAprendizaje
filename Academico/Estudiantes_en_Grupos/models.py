# Academico/Estudiantes_en_Grupos/models.py (o puedes crear un archivo separado para relaciones, por ejemplo, `Academico/Relaciones/models.py`)

from django.db import models
from Academico.Estudiantes.models import Estudiante
from Academico.Docentes.models import Docente
from Academico.Grupos.models import Grupo

class Estudiantes_en_Grupos(models.Model):
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    id_grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Estudiante {self.id_estudiante} en Grupo {self.id_grupo} con Docente {self.id_docente}"
