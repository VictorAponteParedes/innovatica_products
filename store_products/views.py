# IMPORTANDO LOS MODULOS REST FRAMEWORK
from rest_framework.decorators import (
    api_view,
    action,
    authentication_classes,
    permission_classes,
)

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework_simplejwt.tokens import AccessToken

# IMPORTANDO LOS MODULOS INTERNOS
from .models import Usuario, Categoria, Producto
from .serializers import (
    UsuarioSerializer,
    CategoriaSerializer,
    ProductoSerializer,
    ProductosLimitadosSerializer,
)

# Create your views here.


@api_view(["POST"])
def registrar_usuario(request):
    if request.method == "POST":
        # Obtener los datos del formulario JSON enviado desde un cliente servidor
        data = request.data
        username = data.get("username")
        password = data.get("password")

        # VALIDA CASO EL USUARIO NO COMPLETE LOS CAMPOS NECESARIOS
        if not username or not password:
            return Response(
                {"error": "Se requieren campos username y password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Crear un nuevo usuario personalizado
        usuario = Usuario.objects.create_superuser(username=username, password=password)

        usuario.save()

        # Generar tokens JWT
        refresh = RefreshToken.for_user(usuario)
        access_token = str(refresh.access_token)

        return Response(
            {
                "message": "Usuario registrado exitosamente",
                "access_token": access_token,
            },
            status=status.HTTP_201_CREATED,
        )


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()


class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

    def get_queryset(self):
        """
        Puedo filtrar por nombre, categoria, estado, atra vez de la url
        ejemplo: http://localhost:8000/api/v1/nombre?
        """
        queryset = super().get_queryset()

        nombre = self.request.query_params.get("nombre", None)
        categoria = self.request.query_params.get("categoria", None)
        estado = self.request.query_params.get("estado", None)

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if categoria:
            queryset = queryset.filter(categoria__nombre=categoria)
        if estado:
            queryset = queryset.filter(estado=estado)

        return queryset

    def get_serializer_class(self):
        # Valido si el usuario tiene token y si esta aprobado
        if (
            self.request.user.is_authenticated
            and self.request.user.aprobado == "aprobado"
        ):
            return ProductoSerializer
        else:
            return ProductosLimitadosSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Verificar si el usuario está autenticado y aprobado
        if (
            self.request.user.is_authenticated
            and self.request.user.aprobado == "aprobado"
        ):
            instance.delete()
            return Response(
                {"success": "Producto eliminado correctamente."},
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response(
                {"error": "No tienes permiso para eliminar este producto."},
                status=status.HTTP_403_FORBIDDEN,
            )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=kwargs.pop("partial", False)
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
