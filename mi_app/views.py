# mi_app/views.py
from django.shortcuts import render, redirect
from .forms import CursoForm, ProfesorForm, EstudianteForm, BuscarCursoForm
from .models import Curso, Profesor, Estudiante

def insertar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'insertar_curso.html', {'form': form})

def buscar_curso(request):
    form = BuscarCursoForm(request.GET)
    cursos = Curso.objects.all()
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        if nombre:
            cursos = cursos.filter(nombre__icontains=nombre)
    return render(request, 'buscar_curso.html', {'form': form, 'cursos': cursos})

