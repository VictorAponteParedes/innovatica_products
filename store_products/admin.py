# IMPORTANDO MODULOS DE DJANGO
from django.contrib import admin
from django.utils.html import format_html

# IMPORTANDO MODULOS INTERNOS
from .models import Usuario, Producto, Categoria

# Register your models here.


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["username", "aprobado"]


admin.site.register(Usuario, UsuarioAdmin)


admin.site.register(Categoria)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "estado", "mostrar_imagen"]

    def mostrar_imagen(self, obj):
        """
        Este metodo me permite poder visualizar la imagen imagen en mi administrador Django
        """
        if obj.imagen:
            return format_html(
                '<img src="{}" style="border-radius: 50%; width: 40px; height: 40px;" />',
                obj.imagen.url,
            )
        else:
            return "Sin imagen"

    mostrar_imagen.short_description = "Imagen"


admin.site.register(Producto, ProductoAdmin)
