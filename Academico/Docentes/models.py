# Academico/Docentes/models.py

from django.db import models
from django.contrib.auth.hashers import make_password  # Para cifrar contraseñas

class Docente(models.Model):
    id_docente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    asignatura = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=100)  # Almacenará la contraseña cifrada

    def save(self, *args, **kwargs):
        if not self.pk:  # Solo al crear un nuevo registro
            self.contrasena = make_password(self.contrasena)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'Docentes'

