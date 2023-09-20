#IMPORTANDO MODULOS DE REST FRAMEWORK
from rest_framework.routers import DefaultRouter

#IMPORTANDO MODULOS DE DJANGO
from django.urls import path, include

#IMPORTANDO MODULOS INTERNOS
from .views import UsuarioViewSet


routers = DefaultRouter()
routers.register(r"usuarios", UsuarioViewSet, basename="usuarios")

urlpatterns = [
    path("", include(routers.urls))
]





