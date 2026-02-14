from django.shortcuts import render
from .models import Tarea

def home(request):
    tareas = Tarea.objects.all()

    return render(request, 'inicio/lista_tareas.html', {'tareas': tareas})