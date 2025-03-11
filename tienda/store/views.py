from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PerfilUsuario

def index(request):
    categorias = ["Todos", "Vestidos", "Blusas", "Pantalones", "Zapatos"]

    productos = [
        {"nombre": "Vestido elegante", "precio": "$50", "imagen": "/static/img/Falda.jpeg", "categoria": "Vestidos"},
        {"nombre": "Blusa casual", "precio": "$30", "imagen": "/static/img/Falda.jpeg", "categoria": "Blusas"},
        {"nombre": "Pantalón de moda", "precio": "$40", "imagen": "/static/img/Falda.jpeg", "categoria": "Pantalones"},
        {"nombre": "Zapatos de tacón", "precio": "$60", "imagen": "/static/img/Falda.jpeg", "categoria": "Zapatos"},
    ]
    
    return render(request, "store/index.html", {"productos": productos, "categorias": categorias})

def registro(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username, password=password)
        PerfilUsuario.objects.create(user=user, tipo_usuario=2)  # Siempre cliente

        return render(request, "store/registro.html", {"registro_exitoso": True})  # Enviar variable
    
    return render(request, "store/registro.html")

def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('redirigir_usuario')  # Redirigir según el tipo de usuario
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('lista_productos')

@login_required
def redirigir_usuario(request):
    perfil = getattr(request.user, 'perfilusuario', None)
    if perfil and perfil.tipo_usuario == 1:  # Administrador
        return redirect('dashboard')
    else:  # Cliente
        return redirect('lista_productos')

def es_admin(user):
    perfil = getattr(user, 'perfilusuario', None)
    return perfil and perfil.tipo_usuario == 1

@user_passes_test(es_admin)
def dashboard(request):
    return render(request, "store/dashboard.html")
