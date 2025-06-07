# Detector_Proyecto/settings/base.py

import environ
from pathlib import Path

# Inicializar django-environ y cargar el archivo .env
env = environ.Env()
environ.Env.read_env()

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Clave secreta (obtenida desde .env)
SECRET_KEY = env('SECRET_KEY')

# Depuración (obtenida desde .env, se espera como un valor booleano)
DEBUG = env.bool('DEBUG', default=False)

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps adicionales
    'crispy_forms',  # Para formularios estéticos
    'corsheaders',   # Para manejo de CORS si lo necesitas
    # Mis aplicaciones
    'Academico.Estudiantes',
    'Academico.Docentes',
    'Academico.Grupos',
    'Academico.Actividades',
    'Academico.Estudiantes_en_Grupos',
    #App de autenticacion
    'auth_app',
    'llm_api',
    
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Añadir middleware de CORS si lo necesitas
]

# Configuración de URLs
ROOT_URLCONF = 'Detector_Proyecto.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuración de WSGI
WSGI_APPLICATION = 'Detector_Proyecto.wsgi.application'

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='5432'),
    }
}

# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalización
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Carpeta para archivos estáticos en desarrollo
STATIC_ROOT = BASE_DIR / 'staticfiles'    # Carpeta para recopilar archivos estáticos en producción

# Archivos de medios
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'           # Carpeta para almacenar archivos de medios

# Configuración de campo de clave primaria predeterminada
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
