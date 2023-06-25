from django.contrib import admin
from django.urls import path
from . import views
from . import mantenedores


urlpatterns = [
    path("", views.index, name="index"),
    path("catalogo/", views.catalogo, name="catalogo"),
    path("formulario/", views.formulario, name="formulario"),
    path("recomendaciones/", views.recomendaciones, name="recomendaciones"),
    path("login/", views.login, name="login"),
    path("admin/", admin.site.urls),
    path('usuarios/', mantenedores.usuarios, name='usuarios'),

]
