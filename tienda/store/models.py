from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    stock = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class PerfilUsuario(models.Model):
    TIPO_USUARIO = [
        (1, 'Administrador'),
        (2, 'Cliente'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación con User
    tipo_usuario = models.IntegerField(choices=TIPO_USUARIO, default=2)  # 1 = Admin, 2 = Cliente

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.username})"