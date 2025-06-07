# Academico/Grupos/models.py

from django.db import models

class Grupo(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=100)  # Nombre del grupo, como "Grupo A", "Grupo B", etc.
    kinestesico = models.FloatField(null=True, blank=True)  # Porcentaje promedio de estilo kinestésico
    auditivo = models.FloatField(null=True, blank=True)     # Porcentaje promedio de estilo auditivo
    visual = models.FloatField(null=True, blank=True)       # Porcentaje promedio de estilo visual

    def __str__(self):
        return self.nombre_grupo

    class Meta:
        db_table = 'Grupos'  # Nombre de la tabla en la base de datos
