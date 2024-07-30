# Proyecto Django - Tercera Pre-entrega

El proyecto implementa una aplicación web utilizando el patrón MVT y se sube a GitHub como parte de la entrega.

## Índice

1. [Descripción del Proyecto]()
2. [Configuración del Entorno]()
3. [Instrucciones para Ejecutar el Proyecto]()
4. [Funcionalidades]()
5. [Estructura del Proyecto]()

## Descripción del Proyecto

Este proyecto es una aplicación web desarrollada con Django que permite gestionar cursos, profesores y estudiantes. Incluye funcionalidades para agregar y buscar información en la base de datos. La aplicación sigue el patrón MVT y utiliza herencia en las plantillas HTML.

## Configuración del Entorno

1. **Clona el Repositorio:**

   git clone https://github.com/tu_usuario/Tercera-pre-entrega-Mastronardi.git
   cd Tercera-pre-entrega-Mastronardi
2. **Instala las Dependencias:**

   pip install -r requirements.txt

## Instrucciones para Ejecutar el Proyecto

1. **Realiza las Migraciones:**

   python manage.py makemigrations

   python manage.py migrate
2. **Crea un Superusuario para el Panel de Administración:**

   python manage.py createsuperuser
3. **Inicia el Servidor de Desarrollo:**

   python manage.py runserver
4. **Accede a la Aplicación:**

   http://127.0.0.1:8000/

## Funcionalidades

1. **Herencia de HTML:**
2. **Modelos:**
3. * **Inicio:** representa la página de inicio.
   * **Curso:** incluye el nombre, la descripción y la duración del curso.
   * **Profesor:** contiene el nombre y la especialidad del profesor.
   * **Estudiante:** registra el nombre, la fecha de nacimiento y los cursos en los que está inscrito.
4. **Formularios:**
   * **Agregar Curso:** permite insertar nuevos cursos en la base de datos.
   * **Agregar Profesor:** permite insertar nuevos profesores.
   * **Agregar Estudiante:** permite insertar nuevos estudiantes.
   * **Buscar Curso:** permite buscar cursos por nombre.

## Estructura del Proyecto

* **`mi_proyecto/`**
  * `settings.py`: Configuración del proyecto.
  * `urls.py`: Configuración de las URLs principales del proyecto.
  * `wsgi.py`: Configuración para despliegue en servidores WSGI.
* **`mi_app/`**
  * `models.py`: Definición de modelos de datos.
  * `views.py`: Definición de las vistas.
  * `forms.py`: Definición de formularios.
  * `urls.py`: Configuración de URLs específicas de la aplicación.
  * `templates/`: Carpeta para las plantillas HTML.
  * `static/`: Carpeta para archivos estáticos.
