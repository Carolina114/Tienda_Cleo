from django.urls import path
from . import views  # Importamos todas las vistas desde views.py

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.iniciar_sesion, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('categorias/', views.categorias, name='categorias'),
    path('categoria/<str:categoria>/', views.mostrar_categoria, name='categoria'),
    path('comprar/<str:producto_nombre>/', views.comprar_producto, name='comprar'), 
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
