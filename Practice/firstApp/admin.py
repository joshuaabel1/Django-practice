from django.contrib import admin
from .models import MyModel


"""
admin.py:

1) Aquí defines la configuración y comportamiento de la app en el panel administrativo de Django.

2) Puedes registrar modelos para que sean administrables a través del panel de admin.

"""


admin.site.register(MyModel)