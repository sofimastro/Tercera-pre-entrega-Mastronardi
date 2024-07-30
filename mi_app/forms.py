# mi_app/forms.py
from django import forms
from .models import Curso, Profesor, Estudiante

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'duracion']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'especialidad']

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'fecha_nacimiento', 'cursos']


# mi_app/forms.py
class BuscarCursoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
