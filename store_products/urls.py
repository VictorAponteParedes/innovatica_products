#IMPORTANDO LOS MODULOS INTERNOS
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    UsuarioViewSet,
    CategoriaViewSet,
    ProductoViewSet,
    registrar_usuario,
)
from django.urls import path, include

#IMPORTANDO LOS MODULOS REST FRAMEWORK
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register(r"usuarios", UsuarioViewSet, basename="usuarios")
routers.register(r"categorias", CategoriaViewSet, basename="categorias")
routers.register(r"productos", ProductoViewSet, basename="productos")

urlpatterns = [
    path("", include(routers.urls)),
    path("registrar_usuario/", registrar_usuario, name="registrar_usuario"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





