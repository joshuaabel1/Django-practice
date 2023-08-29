# Django-practice
Proyecto de practica para el Python study group .

### Dentro de una app (en este caso `miapp`):

1. **admin.py**:
    - Aquí defines la configuración y comportamiento de la app en el panel administrativo de Django.
    - Puedes registrar modelos para que sean administrables a través del panel de admin.

    ```python
    from django.contrib import admin
    from .models import MiModelo
    
    admin.site.register(MiModelo)
    ```

2. **apps.py**:
    - Contiene la configuración principal de la app.
    - Es utilizado para cosas como el nombre legible de la app y configuraciones avanzadas.

    ```python
    from django.apps import AppConfig
    
    class MiappConfig(AppConfig):
        name = 'miapp'
    ```

3. **__init__.py**:
    - Es un archivo vacío que indica a Python que este directorio debe ser considerado un paquete.
    - Esencial para que Python reconozca la carpeta como un módulo y pueda importar archivos desde ahí.

4. **migrations/__init__.py**:
    - Al igual que el anterior, es un archivo vacío que convierte `migrations` en un paquete.
    - En la carpeta `migrations`, Django guardará todos los archivos de migración generados cuando hagas cambios en tus modelos y ejecutes `python manage.py makemigrations`.

5. **models.py**:
    - Define los modelos de la app, que son la representación en Python de las tablas de la base de datos.
    - Cada modelo se traduce en una tabla en la base de datos.

    ```python
    from django.db import models
    
    class MiModelo(models.Model):
        nombre = models.CharField(max_length=100)
    ```

6. **tests.py**:
    - Aquí escribes las pruebas unitarias y de integración para tu app.
    - Django tiene un framework de pruebas incorporado para facilitar la escritura y ejecución de pruebas.

    ```python
    from django.test import TestCase

    class MiModeloTestCase(TestCase):
        def test_algo(self):
            ...
    ```

7. **views.py**:
    - Define las vistas, que son funciones o clases encargadas de procesar la lógica de negocio, interactuar con el modelo y devolver una respuesta (por lo general, renderizando un template) al usuario.
    - Puede ser basado en funciones o clases.

    ```python
    from django.shortcuts import render

    def mi_vista(request):
        return render(request, 'mi_template.html')
    ```

### En el nivel del proyecto:

1. **nombre_del_proyecto/__init__.py**:
    - Al igual que en la app, este archivo convierte el directorio en un paquete.

2. **nombre_del_proyecto/settings.py**:
    - Contiene todas las configuraciones de tu proyecto Django.
    - Configuraciones como base de datos, aplicaciones instaladas, middlewares, plantillas, entre otros, se definen aquí.

3. **nombre_del_proyecto/urls.py**:
    - Define las rutas URL para tu proyecto.
    - Es como una tabla de contenidos para tu aplicación web.

4. **nombre_del_proyecto/wsgi.py**:
    - Es un punto de entrada para servidores web compatibles con WSGI para servir tu proyecto.
    - Se usa en producción cuando despliegas tu aplicación en servidores.

5. **nombre_del_proyecto/asgi.py** (si está presente en versiones más recientes de Django):
    - Similar a `wsgi.py`, pero para servidores que utilizan ASGI, especialmente cuando usas características asíncronas o WebSockets en tu proyecto.

Estos archivos representan la estructura básica y estándar de un proyecto Django. A medida que tu proyecto crezca y evolucione, podrías añadir más archivos o modificar la estructura según tus necesidades.


---

**¿Qué es Django?**

Django es un framework web de alto nivel escrito en Python. Un "framework" es básicamente una colección de herramientas y bibliotecas que facilitan la creación de sitios web y aplicaciones web. Es como un kit de herramientas para construir casas; en lugar de empezar desde cero, tienes todo lo que necesitas para empezar a construir.

---

**¿Por qué usar Django?**

1. **"Baterías incluidas"**: Esto significa que Django viene con muchas características incorporadas, como un panel administrativo, una ORM (Object-Relational Mapping), y muchas más que normalmente tendrías que construir tú mismo.

2. **Seguridad**: Django ayuda a proteger tu sitio web contra vulnerabilidades comunes como ataques de inyección SQL, falsificación de solicitudes entre sitios (CSRF) y muchos más.

3. **Madurez**: Ha estado en desarrollo desde 2003 y ha sido utilizado en muchas grandes aplicaciones y sitios web, como Instagram.

4. **Reutilizable y "plugable"**: Puedes construir componentes (llamados "apps" en Django) que son reutilizables en diferentes proyectos.

---

**Componentes clave de Django**:

1. **Modelos**: Estos son equivalentes a las tablas en una base de datos. Permiten definir la estructura de tus datos. En lugar de escribir SQL, defines una clase en Python, y Django se encarga del resto.

2. **Vistas**: No te dejes engañar por el nombre; en Django, las vistas son donde se define la lógica de tu aplicación. Decides qué datos mostrar y cómo procesar las entradas del usuario.

3. **Templates**: Esta es la parte visual, donde defines cómo mostrar tus datos. Es como HTML, pero con superpoderes, ya que puedes insertar lógica y datos directamente en él.

4. **URLs**: Actúan como el directorio o tabla de contenido de tu aplicación. Decides qué función (vista) se debe llamar cuando se accede a una URL específica.

---

**Flujo básico en Django**:

1. El usuario ingresa una URL en su navegador.
2. Django consulta la configuración de URLs para encontrar la función (vista) correspondiente.
3. La vista procesa la solicitud, interactúa con el modelo (base de datos) si es necesario, y prepara los datos.
4. La vista utiliza un template para presentar los datos de una forma amigable.
5. Django devuelve la página renderizada al usuario.

---

**Resumen**:

Django es una herramienta poderosa y flexible para construir sitios web. Te permite concentrarte en construir tu aplicación sin preocuparte por los detalles técnicos. Como dice el lema de Django: "Hazlo de manera sencilla para los desarrolladores. Hazlo imposible equivocarse".

---


### Que es MVT:


**MVT** se refiere al patrón **Modelo-Vista-Template**. Es una variante del patrón más conocido, MVC (Modelo-Vista-Controlador), y es el patrón arquitectónico que Django utiliza para estructurar sus aplicaciones web.

Aunque MVT comparte similitudes con MVC, hay algunas diferencias clave en cómo Django lo implementa. Aquí te explico cada componente:

1. **Modelo (Model)**:
    - Representa la estructura de datos, comportamientos y reglas de negocio. Esencialmente, es una representación abstracta de la base de datos.
    - En Django, cada modelo corresponde a una tabla en la base de datos. 
    - Se encarga de las operaciones CRUD (Crear, Leer, Actualizar, Borrar) y cualquier otra lógica relacionada con los datos.

2. **Vista (View)**:
    - En Django, esto puede ser un poco confuso porque la "Vista" funciona más como un "Controlador" en MVC. No se refiere directamente a la presentación o cómo se muestran los datos.
    - La vista toma una solicitud web, procesa los datos (a menudo interactuando con un modelo) y devuelve una respuesta.
    - La respuesta puede ser la renderización de un template, una redirección, un archivo para descargar, un error, entre otros.

3. **Template (Template)**:
    - Este es el equivalente a la "Vista" en MVC. Es donde se define cómo se muestran los datos al usuario.
    - Es básicamente HTML pero con capacidad de incorporar lógica y datos dinámicos.
    - Los templates en Django permiten la inserción de datos dinámicos con una sintaxis especial, y también ofrecen características como la herencia de templates, lo que permite reutilizar partes comunes en diferentes páginas (por ejemplo, encabezados o pies de página).

**Flujo en MVT**:

1. El usuario accede a una URL específica.
2. Django consulta la configuración de las URLs y determina qué función o clase vista debe manejar la solicitud.
3. La vista procesa la solicitud. Si es necesario, interactúa con el modelo para obtener o modificar datos.
4. La vista decide qué template usar y le pasa los datos a este template.
5. El template renderiza una página HTML utilizando los datos proporcionados.
6. La vista devuelve esta página renderizada como respuesta a la solicitud del usuario.

**En resumen**, mientras que MVC y MVT comparten muchas similitudes, la principal diferencia en Django es que el componente que se encarga de la presentación se llama "Template" en lugar de "Vista", y el componente que maneja la lógica y el flujo de la aplicación se llama "Vista" en lugar de "Controlador". Es una ligera variación en la terminología, pero el concepto subyacente sigue siendo el mismo.


Un **ORM**, que proviene de las siglas en inglés "Object-Relational Mapping" (Mapeo Objeto-Relacional), es una técnica de programación que conecta las bases de datos relacionales con los conceptos de programación orientada a objetos. En esencia, permite trabajar con la base de datos utilizando objetos en lugar de escribir directamente consultas SQL.

### ORM y sus ventajas:

1. **Abstracción**: No es necesario escribir consultas SQL crudas. Puedes trabajar con la base de datos como si fueran objetos en tu lenguaje de programación.
2. **Portabilidad**: Es más fácil cambiar entre diferentes sistemas de bases de datos. El ORM suele encargarse de las especificidades de cada sistema.
3. **Seguridad**: Reduce el riesgo de vulnerabilidades como la inyección SQL, ya que las consultas se generan de forma segura.
4. **Productividad**: Puedes desarrollar más rápidamente ya que se eliminan muchas tareas repetitivas relacionadas con el acceso a datos.

### ORM de Django:

El ORM de Django es uno de sus componentes más poderosos y distintivos. Te permite definir modelos (que representan las tablas de la base de datos) como clases de Python. Una vez que esos modelos están definidos, puedes realizar operaciones CRUD sin escribir una sola consulta SQL.

**Ejemplo básico**:

1. **Definir un modelo**:
    ```python
    from django.db import models

    class Libro(models.Model):
        titulo = models.CharField(max_length=200)
        autor = models.CharField(max_length=100)
        fecha_publicacion = models.DateField()
    ```

2. **Operaciones CRUD**:

   - **Crear** un nuevo libro:
     ```python
     nuevo_libro = Libro(titulo="El Gran Gatsby", autor="F. Scott Fitzgerald", fecha_publicacion="1925-04-10")
     nuevo_libro.save()
     ```

   - **Leer** libros de la base de datos:
     ```python
     todos_los_libros = Libro.objects.all()
     libros_de_gatsby = Libro.objects.filter(titulo="El Gran Gatsby")
     ```

   - **Actualizar** un libro:
     ```python
     libro = Libro.objects.get(titulo="El Gran Gatsby")
     libro.autor = "Fitzgerald"
     libro.save()
     ```

   - **Eliminar** un libro:
     ```python
     libro = Libro.objects.get(titulo="El Gran Gatsby")
     libro.delete()
     ```

Además de estas operaciones básicas, el ORM de Django proporciona muchas otras características, como:

- **Relaciones**: Puedes definir relaciones entre modelos, como ForeignKey (clave foránea), OneToOneField (uno a uno) y ManyToManyField (muchos a muchos).
- **Migraciones**: Django tiene un sistema de migraciones que te permite realizar cambios en tus modelos (y, por lo tanto, en la estructura de tu base de datos) de una manera estructurada y controlada.
- **Consultas avanzadas**: Aunque no necesitas escribir SQL, tienes la capacidad de hacer consultas muy complejas y eficientes utilizando el ORM.
- **Administrador**: Gracias al ORM, Django proporciona una interfaz de administración automática donde puedes gestionar fácilmente tus modelos.

En resumen, el ORM de Django proporciona una capa de abstracción sobre las bases de datos relacionales que facilita y acelera el desarrollo, a la vez que mantiene la seguridad y la eficiencia.


### Jinja2 o sistema de templates de django:

¡Claro!

En Django, el sistema de templates tiene una sintaxis y funcionalidad que se asemeja mucho a Jinja2, un motor de templates popular en el ecosistema Python. De hecho, Jinja2 se inspiró en el sistema de templates de Django, pero con algunas diferencias y características adicionales.

### Uso básico del sistema de templates de Django:

Django tiene su propio lenguaje de plantillas, que es una mezcla de texto (usualmente HTML) con algunas construcciones especiales.

1. **Variables**:
    - Se usan para insertar valores dinámicos en el template.
    - Sintaxis: `{{ variable_name }}`

2. **Tags**:
    - Proporcionan lógica al sistema de templates.
    - Sintaxis: `{% tag %}`
    - Ejemplo de uso común: bucles y condicionales.

3. **Filtros**:
    - Modifican la forma en que se muestran las variables.
    - Sintaxis: `{{ variable_name|filter_name }}`

Ejemplo básico utilizando algunas de estas construcciones:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ page_title }}</title>
</head>
<body>

{% if user.is_authenticated %}
    <p>Hola, {{ user.username }}!</p>
{% else %}
    <p>Bienvenido, visitante.</p>
{% endif %}

<ul>
{% for item in item_list %}
    <li>{{ item.name|capitalize }}</li>
{% endfor %}
</ul>

</body>
</html>
```

### Jinja2:

Si bien el sistema de templates de Django es poderoso, algunas personas prefieren usar Jinja2 debido a su mayor flexibilidad y características adicionales. Afortunadamente, es posible usar Jinja2 con Django si así lo prefieres.

Las similitudes entre el sistema de templates de Django y Jinja2 son muchas, y si conoces uno, es fácil adaptarse al otro. Sin embargo, hay diferencias en cuanto a algunas construcciones avanzadas y la extensibilidad.

### ¿Por qué alguien querría usar Jinja2 en Django?

1. **Rendimiento**: Jinja2 es, en general, más rápido en la renderización que el sistema de templates predeterminado de Django.
2. **Flexibilidad**: Jinja2 permite la creación de macros (funciones reutilizables en los templates) y tiene una extensión más sencilla.
3. **Similitud con otros proyectos**: Si ya estás trabajando con otros proyectos que utilizan Jinja2 (como Flask), puede tener sentido utilizar la misma herramienta para la consistencia.

### Integración de Jinja2 con Django:

Si decides usar Jinja2 en tu proyecto Django, hay pasos específicos que debes seguir para integrarlo. Básicamente, implica instalar Jinja2, configurar Django para usarlo y luego adaptar tus templates y vistas según sea necesario.

En resumen, tanto el sistema de templates de Django como Jinja2 son herramientas poderosas para renderizar vistas en aplicaciones web. La elección entre uno y otro suele basarse en preferencias personales, necesidades del proyecto y experiencia previa.



En Django, las vistas son simplemente funciones de Python (o métodos, en el caso de vistas basadas en clases) que toman una solicitud web y devuelven una respuesta web. Pueden ser implementadas como funciones simples, conocidas como **"vistas basadas en funciones" (FBV, por sus siglas en inglés: Function-Based Views)** o como clases, conocidas como **"vistas basadas en clases" (CBV, por sus siglas en inglés: Class-Based Views)**.

### Vistas Basadas en Funciones (FBV):

Las FBV son simplemente funciones que toman un objeto `request` y devuelven un objeto `response`. Son simples, directas y fáciles de escribir.

**Ejemplo**:

```python
from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse('¡Hola, mundo!')
```

### Ventajas de FBV:

1. **Simplicidad**: Son directas y fáciles de leer, especialmente para tareas simples.
2. **Control directo**: Puedes ver claramente qué sucede en cada línea de la función.
3. **Familiaridad**: Para quienes son nuevos en Django o en la programación orientada a objetos, las FBV pueden ser más accesibles.

### Vistas Basadas en Clases (CBV):

Las CBV aprovechan la orientación a objetos de Python para definir vistas como clases. Estas clases pueden heredar comportamientos de otras vistas y se basan en la reutilización y la extensibilidad.

**Ejemplo**:

```python
from django.http import HttpResponse
from django.views import View

class MiVista(View):
    def get(self, request):
        return HttpResponse('¡Hola, mundo!')
```

### Ventajas de CBV:

1. **Reutilización**: Puedes reutilizar comportamientos comunes a través de la herencia.
2. **Extensibilidad**: Es fácil añadir más métodos HTTP (como POST, PUT) simplemente añadiendo métodos a la clase.
3. **Organización**: Las CBV pueden ser más organizadas y claras para vistas complejas con múltiples puntos de entrada.
4. **Decoradores como Mixins**: En lugar de decoradores, puedes utilizar mixins para proporcionar funcionalidades adicionales.

### Diferencias clave:

1. **Sintaxis y estructura**: Las FBV utilizan una sintaxis funcional, mientras que las CBV utilizan clases y métodos para definir comportamientos.
2. **Reutilización**: Mientras que puedes reutilizar partes de FBV con funciones y decoradores, las CBV aprovechan la herencia de clases y los mixins para reutilizar comportamientos.
3. **Claridad**: Las FBV suelen ser más claras para comportamientos simples, pero las CBV pueden ser más claras cuando hay múltiples comportamientos o métodos HTTP en una sola vista.

### Conclusión:

La elección entre FBV y CBV a menudo se reduce a una cuestión de preferencia personal y a las necesidades del proyecto. Las FBV son sencillas y directas, ideales para vistas más simples. Las CBV ofrecen una estructura organizada y son poderosas para vistas más complejas, especialmente cuando hay mucha reutilización y extensibilidad involucrada. Ambas son herramientas válidas en el arsenal de un desarrollador de Django.


### Base de datos:

Una base de datos es un sistema estructurado para almacenar, organizar y recuperar información. Tradicionalmente, esta información se organiza en tablas que contienen filas y columnas, especialmente en el contexto de bases de datos relacionales como PostgreSQL, MySQL, SQLite, etc. Las bases de datos permiten realizar operaciones CRUD (crear, leer, actualizar y eliminar) en sus datos.