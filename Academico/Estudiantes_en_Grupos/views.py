# Academico/Estudiantes_en_Grupos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiantes_en_Grupos
from .forms import EstudiantesEnGrupoForm

# Vista para listar todas las relaciones de estudiantes en grupos
def listar_estudiantes_en_grupos(request):
    relaciones = Estudiantes_en_Grupos.objects.all()
    return render(request, 'listar_estudiantes_en_grupos.html', {'relaciones': relaciones})

# Vista para ver el detalle de una relación estudiante-grupo
def detalle_estudiante_en_grupo(request, id):
    relacion = get_object_or_404(Estudiantes_en_Grupos, id=id)
    return render(request, 'detalle_estudiante_en_grupo.html', {'relacion': relacion})

# Vista para crear una nueva relación estudiante-grupo
def crear_estudiante_en_grupo(request):
    if request.method == 'POST':
        form = EstudiantesEnGrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes_en_grupos')
    else:
        form = EstudiantesEnGrupoForm()
    return render(request, 'crear_estudiante_en_grupo.html', {'form': form})

# Vista para actualizar una relación estudiante-grupo existente
def actualizar_estudiante_en_grupo(request, id):
    relacion = get_object_or_404(Estudiantes_en_Grupos, id=id)
    if request.method == 'POST':
        form = EstudiantesEnGrupoForm(request.POST, instance=relacion)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes_en_grupos')
    else:
        form = EstudiantesEnGrupoForm(instance=relacion)
    return render(request, 'actualizar_estudiante_en_grupo.html', {'form': form})

# Vista para eliminar una relación estudiante-grupo
def eliminar_estudiante_en_grupo(request, id):
    relacion = get_object_or_404(Estudiantes_en_Grupos, id=id)
    if request.method == 'POST':
        relacion.delete()
        return redirect('listar_estudiantes_en_grupos')
    return render(request, 'eliminar_estudiante_en_grupo.html', {'relacion': relacion})
