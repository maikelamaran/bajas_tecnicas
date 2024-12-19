import os
import sys

# Asegúrate de que la ruta al directorio del proyecto esté en sys.path
sys.path.append('/home/mikerosy/bajas_tecnicas')  # Cambia esta ruta si es necesario

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bajastecnicas.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
