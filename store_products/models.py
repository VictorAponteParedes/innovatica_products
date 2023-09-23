from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Usuario(AbstractUser):
    APROBADO_CHOICES = (
        ("aprobado", "Aprobado"),
        ("desaprobado", "Desaprobado"),
    )

    aprobado = models.CharField(
        max_length=12, choices=APROBADO_CHOICES, default="desaprobado"
    )


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
        blank=True,
    )
    estado = models.CharField(
        max_length=20,
        choices=[("nuevo", "Nuevo"), ("semi_nuevo", "Semi Nuevo"), ("usado", "Usado")],
        default="nuevo",
    )
    imagen = models.ImageField(upload_to="productos/", blank=True, null=True)

    def __str__(self):
        return self.nombre

    def image_img(self):
        if self.item_image:
            return '<img src="%s" width="50" height="50" />' % self.imagen.url
        else:
            return "(Sin imagen)"

    image_img.short_description = "Thumb"
    image_img.allow_tags = True
