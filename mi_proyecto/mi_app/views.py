# mi_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Profesor, Estudiante
from .forms import CursoForm, ProfesorForm, EstudianteForm

# Vista para listar todos los cursos
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_app/listar_cursos.html', {'cursos': cursos})

# Vista para agregar un nuevo curso
def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')  # Redirige a la vista que muestra todos los cursos
    else:
        form = CursoForm()
    return render(request, 'mi_app/agregar_curso.html', {'form': form})

# Vista para editar un curso existente
def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'mi_app/editar_curso.html', {'form': form})

# Vista para eliminar un curso
def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('listar_cursos')
    return render(request, 'mi_app/eliminar_curso.html', {'curso': curso})

# Vista para listar todos los profesores
def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'mi_app/listar_profesores.html', {'profesores': profesores})

# Vista para agregar un nuevo profesor
def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')
    else:
        form = ProfesorForm()
    return render(request, 'mi_app/agregar_profesor.html', {'form': form})

# Vista para editar un profesor existente
def editar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'mi_app/editar_profesor.html', {'form': form})

# Vista para eliminar un profesor
def eliminar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    if request.method == 'POST':
        profesor.delete()
        return redirect('listar_profesores')
    return render(request, 'mi_app/eliminar_profesor.html', {'profesor': profesor})

# Vista para listar todos los estudiantes
def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'mi_app/listar_estudiantes.html', {'estudiantes': estudiantes})

# Vista para agregar un nuevo estudiante
def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'mi_app/agregar_estudiante.html', {'form': form})

# Vista para editar un estudiante existente
def editar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'mi_app/editar_estudiante.html', {'form': form})

# Vista para eliminar un estudiante
def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('listar_estudiantes')
        return render(request, 'mi_app/eliminar_estudiante.html', {'estudiante': estudiante})
