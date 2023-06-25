from django.shortcuts import render
from django.contrib.auth.models import usuarios


def usuarios(request):
    # Lógica para obtener y mostrar los usuarios
    return render(request, 'usuarios.html')
