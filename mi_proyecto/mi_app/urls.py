# mi_app/urls.py
from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/agregar/', views.agregar_curso, name='agregar_curso'),
    path('cursos/editar/<int:id>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:id>/', views.eliminar_curso, name='eliminar_curso'),
    path('profesores/', views.listar_profesores, name='listar_profesores'),
    path('profesores/agregar/', views.agregar_profesor, name='agregar_profesor'),
    path('profesores/editar/<int:id>/', views.editar_profesor, name='editar_profesor'),
    path('profesores/eliminar/<int:id>/', views.eliminar_profesor, name='eliminar_profesor'),
    path('estudiantes/', views.listar_estudiantes, name='listar_estudiantes'),
    path('estudiantes/agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('estudiantes/editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),
=======
from .views import insertar_curso, buscar_curso

urlpatterns = [
    path('insertar_curso/', insertar_curso, name='insertar_curso'),
    path('buscar_curso/', buscar_curso, name='buscar_curso'),
>>>>>>> 623ef3c57bb2162240d92986451e5d9084e1b36d
]