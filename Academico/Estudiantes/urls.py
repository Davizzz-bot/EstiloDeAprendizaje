# Academico/Estudiantes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_estudiantes, name='listar_estudiantes'),
    path('crear/', views.crear_estudiante, name='crear_estudiante'),
    path('actualizar/<int:id_estudiante>/', views.actualizar_estudiante, name='actualizar_estudiante'),
    path('eliminar/<int:id_estudiante>/', views.eliminar_estudiante, name='eliminar_estudiante'),
    path('<int:id_estudiante>/', views.detalle_estudiante, name='detalle_estudiante'),  # Nueva URL de detalle
]
