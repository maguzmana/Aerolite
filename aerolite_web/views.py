from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def formulario(request):
    return render(request, 'formulario.html')

def recomendaciones(request):
    return render(request, 'recomendaciones.html')

def login(request):
    return render(request, 'login.html')