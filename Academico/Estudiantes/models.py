# Academico/Estudiantes/models.py

from django.db import models
from django.contrib.auth.hashers import make_password
from Academico.Grupos.models import Grupo  # Importa el modelo Grupo correctamente

class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    kinestesico = models.FloatField(null=True, blank=True)
    visual = models.FloatField(null=True, blank=True)
    auditivo = models.FloatField(null=True, blank=True)
    estilo_predominante = models.CharField(max_length=50, blank=True, null=True)
    usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=100)

    # Relación con el modelo Grupo
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name="Estudiantes", null=True, blank=True)



    def save(self, *args, **kwargs):
        if not self.pk:  # Solo al crear un nuevo registro
            self.contrasena = make_password(self.contrasena)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'Estudiantes'


