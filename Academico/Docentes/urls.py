# Academico/Docentes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_docentes, name='listar_docentes'),
    path('crear/', views.crear_docente, name='crear_docente'),
    path('actualizar/<int:id_docente>/', views.actualizar_docente, name='actualizar_docente'),
    path('eliminar/<int:id_docente>/', views.eliminar_docente, name='eliminar_docente'),
    path('<int:id_docente>/', views.detalle_docente, name='detalle_docente'),  # URL de detalle
]
