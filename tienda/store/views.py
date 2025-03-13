from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PerfilUsuario, Producto


def index(request):
    return render(request, "store/index.html")

def categorias(request):
    return render(request, "store/categorias.html")

def mostrar_categoria(request, categoria):
    productos = {
        "blusas": [
            {"nombre": "Blusa casual", "precio": "$30", "imagen": "img/Falda.jpeg"},
            {"nombre": "Blusa elegante", "precio": "$40", "imagen": "img/Falda.jpeg"},
        ],
        "denim": [
            {"nombre": "Jean ajustado", "precio": "$80", "imagen": "img/Falda.jpeg"},
            {"nombre": "Chaqueta de mezclilla", "precio": "$120", "imagen": "img/Falda.jpeg"},
        ],
        "pantalones": [
            {"nombre": "Pantalón formal", "precio": "$70", "imagen": "img/Falda.jpeg"},
            {"nombre": "Joggers deportivos", "precio": "$60", "imagen": "img/Falda.jpeg"},
        ],
        "bodies": [
            {"nombre": "Body manga larga", "precio": "$50", "imagen": "img/Falda.jpeg"},
            {"nombre": "Body sin mangas", "precio": "$45", "imagen": "img/Falda.jpeg"},
        ],
    }

    return render(request, "store/categoria.html", {"categoria": categoria, "productos": productos.get(categoria, [])})

def registro(request):
    if request.method == "POST":
        nombre = request.POST["first_name"]
        apellido = request.POST["last_name"]
        username = request.POST["username"]
        password = request.POST["password"]

        # Crear usuario con nombre y apellido
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=nombre,
            last_name=apellido
        )

        # Asignar tipo de usuario por defecto = Cliente (2)
        PerfilUsuario.objects.create(user=user, tipo_usuario=2)

        # Iniciar sesión automáticamente
        login(request, user)

        # Mostrar modal de éxito
        return render(request, "store/registro.html", {"registro_exitoso": True})

    return render(request, "store/registro.html")

def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirigir según el tipo de usuario
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

@login_required
def perfil(request):
    return render(request, 'store/perfil.html', {'usuario': request.user})

def es_admin(user):
    perfil = getattr(user, 'perfilusuario', None)
    return perfil and perfil.tipo_usuario == 1

@user_passes_test(es_admin)
def dashboard(request):
    return render(request, "store/dashboard.html")



def comprar_producto(request, producto_nombre):
    producto = get_object_or_404(Producto, nombre=producto_nombre)
    return render(request, 'store/comprar.html', {'producto': producto})

def ver_carrito(request):
    return render(request, 'store/carrito.html')