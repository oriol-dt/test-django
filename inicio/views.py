from django.shortcuts import render, redirect
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