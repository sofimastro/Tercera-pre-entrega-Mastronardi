# mi_app/urls.py
from django.urls import path
from .views import insertar_curso, buscar_curso

urlpatterns = [
    path('insertar_curso/', insertar_curso, name='insertar_curso'),
    path('buscar_curso/', buscar_curso, name='buscar_curso'),
]
