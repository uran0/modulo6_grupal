from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    USUARIO_TIPO_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('user', 'User'),
    )

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=5, choices=USUARIO_TIPO_CHOICES, default='user')

    def __str__(self):
        return self.usuario.username