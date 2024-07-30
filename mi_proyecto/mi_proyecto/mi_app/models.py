# mi_app/models.py
from django.db import models

class Inicio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    cursos = models.ManyToManyField(Curso)


