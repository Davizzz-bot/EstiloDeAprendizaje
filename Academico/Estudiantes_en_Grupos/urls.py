# Academico/Estudiantes_en_Grupos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_estudiantes_en_grupos, name='listar_estudiantes_en_grupos'),
    path('crear/', views.crear_estudiante_en_grupo, name='crear_estudiante_en_grupo'),
    path('<int:id>/', views.detalle_estudiante_en_grupo, name='detalle_estudiante_en_grupo'),
    path('actualizar/<int:id>/', views.actualizar_estudiante_en_grupo, name='actualizar_estudiante_en_grupo'),
    path('eliminar/<int:id>/', views.eliminar_estudiante_en_grupo, name='eliminar_estudiante_en_grupo'),
]
