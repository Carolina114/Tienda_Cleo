from django.urls import path
from . import views  # Importamos todas las vistas desde views.py

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.iniciar_sesion, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('redirigir/', views.redirigir_usuario, name='redirigir_usuario'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
