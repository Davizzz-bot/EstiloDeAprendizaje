# Detector_Proyecto/settings/development.py

from .base import *

# Depuración activada para desarrollo
DEBUG = env.bool('DEBUG', default=True)

# Hosts permitidos en desarrollo
ALLOWED_HOSTS = []
