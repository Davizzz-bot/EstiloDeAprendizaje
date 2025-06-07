# Academico/Actividades/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Actividad
from .forms import ActividadForm

# Vista para listar todas las actividades
def listar_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, 'listar_actividades.html', {'actividades': actividades})

# Vista para ver el detalle de una actividad específica
def detalle_actividad(request, id_actividad):
    actividad = get_object_or_404(Actividad, id_actividad=id_actividad)
    return render(request, 'detalle_actividad.html', {'actividad': actividad})

# Vista para crear una nueva actividad
def crear_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_actividades')
    else:
        form = ActividadForm()
    return render(request, 'crear_actividad.html', {'form': form})

# Vista para actualizar una actividad existente
def actualizar_actividad(request, id_actividad):
    actividad = get_object_or_404(Actividad, id_actividad=id_actividad)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('listar_actividades')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'actualizar_actividad.html', {'form': form})

# Vista para eliminar una actividad
def eliminar_actividad(request, id_actividad):
    actividad = get_object_or_404(Actividad, id_actividad=id_actividad)
    if request.method == 'POST':
        actividad.delete()
        return redirect('listar_actividades')
    return render(request, 'eliminar_actividad.html', {'actividad': actividad})
