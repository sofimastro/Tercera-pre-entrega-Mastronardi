# mi_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URLs para Cursos
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/agregar/', views.agregar_curso, name='agregar_curso'),
    path('cursos/editar/<int:id>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:id>/', views.eliminar_curso, name='eliminar_curso'),

    # URLs para Profesores
    path('profesores/', views.listar_profesores, name='listar_profesores'),
    path('profesores/agregar/', views.agregar_profesor, name='agregar_profesor'),
    path('profesores/editar/<int:id>/', views.editar_profesor, name='editar_profesor'),
    path('profesores/eliminar/<int:id>/', views.eliminar_profesor, name='eliminar_profesor'),

    # URLs para Estudiantes
    path('estudiantes/', views.listar_estudiantes, name='listar_estudiantes'),
    path('estudiantes/agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('estudiantes/editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    # URLs para Acciones Básicas (si son necesarias)
    path('insertar_curso/', views.insertar_curso, name='insertar_curso'),
    path('buscar_curso/', views.buscar_curso, name='buscar_curso'),
]
