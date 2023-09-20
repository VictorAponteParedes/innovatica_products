from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Usuario(AbstractUser):
    APROBADO_CHOICES = (
        ('aprobado', 'Aprobado'),
        ('desaprobado', 'Desaprobado'),
    )

    aprobado = models.CharField(max_length=12, choices=APROBADO_CHOICES, default='desaprobado')