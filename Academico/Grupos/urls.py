# Academico/Grupos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_grupos, name='listar_grupos'),
    path('crear/', views.crear_grupo, name='crear_grupo'),
    path('<int:id_grupo>/', views.detalle_grupo, name='detalle_grupo'),
    path('actualizar/<int:id_grupo>/', views.actualizar_grupo, name='actualizar_grupo'),
    path('eliminar/<int:id_grupo>/', views.eliminar_grupo, name='eliminar_grupo'),
]
