from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('index'), name='index'),  # Redirigir directamente al login



    
    # Incluye las URLs de la aplicación auth_app
    path('auth/', include('auth_app.urls')),  # Rutas de autenticación
    
    # Incluye las URLs de las demás aplicaciones
    path('estudiantes/', include('Academico.Estudiantes.urls')),
    path('docentes/', include('Academico.Docentes.urls')),
    path('grupos/', include('Academico.Grupos.urls')),
    path('estudiantes_en_grupos/', include('Academico.Estudiantes_en_Grupos.urls')),
    path('actividades/', include('Academico.Actividades.urls')),
    path("llm_api/", include("llm_api.urls")),  # Incluye las URLs de la app llm_api
]
