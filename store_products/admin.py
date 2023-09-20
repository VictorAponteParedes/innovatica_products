from django.contrib import admin
from .models import Usuario

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["username", "aprobado"]

admin.site.register(Usuario, UsuarioAdmin)
