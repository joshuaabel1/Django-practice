from django.shortcuts import render

# Create your views here.


"""

views.py:

1) Define las vistas, que son funciones o clases encargadas de procesar la lógica de negocio, interactuar con el modelo y devolver una respuesta (por lo general, renderizando un template) al usuario.

2) Puede ser basado en funciones o clases.


"""

def mi_vista(request):
    return render(request, 'mi_template.html')
