from django.db import models

from django.db import models

class Ventilador(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='ventiladores/')
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

class Venta(models.Model):
    ventilador = models.ForeignKey(Ventilador, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)

