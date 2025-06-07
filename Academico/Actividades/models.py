# Academico/Actividades/models.py

from django.db import models

class Actividad(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    descripcion_actividad = models.CharField(max_length=255)  # Descripción de la actividad
    estilo_kinestesico = models.FloatField(null=True, blank=True)   # Campo opcional
    estilo_auditivo = models.FloatField(null=True, blank=True)      # Campo opcional
    estilo_visual = models.FloatField(null=True, blank=True)         # Campo opcional
    tipo_actividad = models.CharField(max_length=50)       # Tipo de actividad (e.g., práctica, teórica)
    nivel_dificultad = models.CharField(max_length=50)     # Nivel de dificultad de la actividad
    observaciones = models.CharField(max_length=255, blank=True, null=True)  # Observaciones adicionales

    def __str__(self):
        return self.descripcion_actividad

    class Meta:
        db_table = 'Actividades'  # Nombre de la tabla en la base de datos, si deseas personalizarlo
