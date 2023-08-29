from django.apps import AppConfig


"""

apps.py:

1) Contiene la configuración principal de la app.

2) Es utilizado para cosas como el nombre legible de la app y configuraciones avanzadas.

"""



class FirstappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'firstApp'
