"""
URL configuration for amazon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from backend import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from backend.views import UsuarioViewSet

    
schema_view = get_schema_view(
   openapi.Info(
      title="Amazon API",
      default_version='v1',
      description="API para gerenciamento de clientes",
   ),
   public=True,
   permission_classes=(AllowAny,),
)

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet, basename='cliente')
router.register(r'enderecos', views.EnderecoViewSet, basename='endereco')
router.register(r'vendedores', views.VendedorViewSet, basename='vendedor')
router.register(r'itens', views.ItemViewSet, basename='item')
router.register(r'formas-pagamento', views.FormaPagamentoViewSet, basename='forma-pagamento')
router.register(r'pedidos', views.PedidoViewSet, basename='pedido')
router.register(r'itens-pedido', views.ItemPedidoViewSet, basename='item-pedido')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('amazon_api/', include(router.urls)), # Todos os endpoints da API
    path('amazon_api/signup/', UsuarioViewSet.signup, name='signup'), # Endpoint para cadastro de usuários
    path('amazon_api/login/', UsuarioViewSet.login, name='login'), # Endpoint para login de usuários
    path('amazon_api/perfil/', UsuarioViewSet.perfil, name='perfil'), # Endpoint para visualizar o perfil do usuário
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
