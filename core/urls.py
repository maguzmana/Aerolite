from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('formulario/', views.formulario, name='formulario'),
    path('recomendaciones/', views.recomendaciones, name='recomendaciones'),
    path('login/',views.login, name='login'),
]

