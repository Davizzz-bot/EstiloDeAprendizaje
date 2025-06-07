# Academico/Docentes/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Docente
from .forms import DocenteForm

# Vista para obtener un docente por su id
def detalle_docente(request, id_docente):
    docente = get_object_or_404(Docente, id_docente=id_docente)
    return render(request, 'detalle_docente.html', {'docente': docente})

def listar_docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'listar_docentes.html', {'docentes': docentes})

def crear_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_docentes')
    else:
        form = DocenteForm()
    return render(request, 'crear_docente.html', {'form': form})

def actualizar_docente(request, id_docente):
    docente = get_object_or_404(Docente, id_docente=id_docente)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('listar_docentes')
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'actualizar_docente.html', {'form': form})

def eliminar_docente(request, id_docente):
    docente = get_object_or_404(Docente, id_docente=id_docente)
    if request.method == 'POST':
        docente.delete()
        return redirect('listar_docentes')
    return render(request, 'eliminar_docente.html', {'docente': docente})
