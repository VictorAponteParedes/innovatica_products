from rest_framework import serializers
from .models import Usuario, Categoria, Producto


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["username", "password"]


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["nombre"]


class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()

    class Meta:
        model = Producto
        fields = ["nombre", "categoria", "estado", "imagen"]


class ProductosLimitadosSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()

    class Meta:
        model = Producto
        fields = ["nombre", "categoria"]
