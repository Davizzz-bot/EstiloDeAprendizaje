# Detector_Proyecto/settings/production.py

from .base import *

# Depuración desactivada en producción
DEBUG = env.bool('DEBUG', default=False)

# Hosts permitidos en producción
ALLOWED_HOSTS = ['tu_dominio.com', 'www.tu_dominio.com']
