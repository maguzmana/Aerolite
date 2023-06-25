from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from models import Ventilador, Recomendacion, Usuario
from forms import ContactForm




def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        # Obtener los datos ingresados por el usuario
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Realizar la autenticación del usuario (puedes usar el sistema de autenticación de Django)
        user = authenticate(username=username, password=password)

        if user is not None:
            # El usuario es válido, iniciar sesión y redirigir a la página de bienvenida
            login(request, user)
            return redirect('bienvenida')
        else:
            # El usuario no es válido, mostrar un mensaje de error
            error_message = "Nombre de usuario o contraseña incorrectos"
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def formulario(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario de contacto
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']

            # Lógica adicional (enviar correo, guardar en la base de datos, etc.)
            asunto = f"Nuevo mensaje de contacto de {nombre}"
            mensaje = f"Nombre: {nombre}\nCorreo: {correo}\nDirección: {direccion}\nTeléfono: {telefono}"
            destinatario = "tu@email.com"
            send_mail(asunto, mensaje, correo, [destinatario])

            return render(request, 'formulario_success.html')

    else:
        form = ContactForm()

    return render(request, 'formulario.html', {'form': form})

def catalogo(request):
    # Obtener todos los ventiladores de la base de datos
    ventiladores = Ventilador.objects.all()

    # Renderizar el template 'catalogo.html' con los ventiladores
    return render(request, 'catalogo.html', {'ventiladores': ventiladores})

def recomendaciones(request):
    # Obtener el usuario actual (suponiendo que tienes un sistema de autenticación implementado)
    usuario_actual = request.user

    # Obtener las recomendaciones para el usuario actual desde la base de datos
    recomendaciones = Recomendacion.objects.filter(usuario=usuario_actual)

    # Renderizar el template 'recomendaciones.html' con las recomendaciones
    return render(request, 'recomendaciones.html', {'recomendaciones': recomendaciones})

def bienvenida(request):
    return render(request, 'bienvenida.html')

def usuarios(request):
    usuarios = Usuario.objects.all()  # Obtener todos los usuarios
    context = {'usuarios': usuarios}  # Crear un diccionario con los usuarios
    return render(request, 'usuarios.html', context)  # Renderizar el template 'usuarios.html' con el contexto
