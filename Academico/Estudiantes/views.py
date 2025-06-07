# Academico/Estudiantes/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante
from .forms import EstudianteForm

# Vista para obtener un estudiante por su id
def detalle_estudiante(request, id_estudiante):
    estudiante = get_object_or_404(Estudiante, id_estudiante=id_estudiante)
    return render(request, 'detalle_estudiante.html', {'estudiante': estudiante})

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'listar_estudiantes.html', {'estudiantes': estudiantes})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'crear_estudiante.html', {'form': form})

def actualizar_estudiante(request, id_estudiante):
    estudiante = get_object_or_404(Estudiante, id_estudiante=id_estudiante)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'actualizar_estudiante.html', {'form': form})

def eliminar_estudiante(request, id_estudiante):
    estudiante = get_object_or_404(Estudiante, id_estudiante=id_estudiante)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('listar_estudiantes')
    return render(request, 'eliminar_estudiante.html', {'estudiante': estudiante})


