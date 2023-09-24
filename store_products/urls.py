# IMPORTANDO LOS MODULOS INTERNOS
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    UsuarioViewSet,
    CategoriaViewSet,
    ProductoViewSet,
    registrar_usuario,
)
from django.urls import path, include

# IMPORTANDO LOS MODULOS REST FRAMEWORK
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

routers = DefaultRouter()
routers.register(r"usuarios", UsuarioViewSet, basename="usuarios")
routers.register(r"categorias", CategoriaViewSet, basename="categorias")
routers.register(r"productos", ProductoViewSet, basename="productos")

urlpatterns = [
    path("", include(routers.urls)),
    path("registrar_usuario/", registrar_usuario, name="registrar_usuario"),
    # Al poner el username y password en esta (url )nos generara un token para los usuario
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="obtain_token"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
