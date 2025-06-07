# Academico/Actividades/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_actividades, name='listar_actividades'),
    path('crear/', views.crear_actividad, name='crear_actividad'),
    path('actualizar/<int:id_actividad>/', views.actualizar_actividad, name='actualizar_actividad'),
    path('eliminar/<int:id_actividad>/', views.eliminar_actividad, name='eliminar_actividad'),
    path('<int:id_actividad>/', views.detalle_actividad, name='detalle_actividad'),
]
