# Academico/Grupos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Grupo
from .forms import GrupoForm

# Vista para listar todos los grupos
def listar_grupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'listar_grupos.html', {'grupos': grupos})

# Vista para ver el detalle de un grupo
def detalle_grupo(request, id_grupo):
    grupo = get_object_or_404(Grupo, id_grupo=id_grupo)
    return render(request, 'detalle_grupo.html', {'grupo': grupo})

# Vista para crear un nuevo grupo
def crear_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_grupos')
    else:
        form = GrupoForm()
    return render(request, 'crear_grupo.html', {'form': form})

# Vista para actualizar un grupo existente
def actualizar_grupo(request, id_grupo):
    grupo = get_object_or_404(Grupo, id_grupo=id_grupo)
    if request.method == 'POST':
        form = GrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('listar_grupos')
    else:
        form = GrupoForm(instance=grupo)
    return render(request, 'actualizar_grupo.html', {'form': form})

# Vista para eliminar un grupo
def eliminar_grupo(request, id_grupo):
    grupo = get_object_or_404(Grupo, id_grupo=id_grupo)
    if request.method == 'POST':
        grupo.delete()
        return redirect('listar_grupos')
    return render(request, 'eliminar_grupo.html', {'grupo': grupo})
