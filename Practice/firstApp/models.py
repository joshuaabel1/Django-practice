from django.db import models

# Create your models here.


"""

models.py:

1) Define los modelos de la app, que son la representación en Python de las tablas de la base de datos.

2) Cada modelo se traduce en una tabla en la base de datos.


"""

class MyModel(models.Model):
    nombre = models.CharField(max_length=100)


from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
