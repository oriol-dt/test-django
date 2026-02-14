from django.shortcuts import render, redirect, get_object_or_404
from .forms import TareaForm
from .models import Tarea

def home(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()

    tareas = Tarea.objects.all()

    return render(request, 'inicio/lista_tareas.html', {
        'tareas': tareas,
        'form': form
    })

def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect('home')

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    return redirect('home')
