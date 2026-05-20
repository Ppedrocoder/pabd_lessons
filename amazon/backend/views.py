from contextvars import Token

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import  Cliente, Endereco, FormaPagamento, Item, ItemPedido, Pedido, Vendedor, Usuario
from .serializers import  ClienteSerializer, EnderecoSerializer, FormaPagamentoSerializer, ItemPedidoSerializer, ItemSerializer, PedidoSerializer, UsuarioSerializer, VendedorSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

class ClienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Cliente.
    Fornece automaticamente os endpoints list, create, retrieve,
    update, partial_update e destroy.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # Habilita filtros, busca textual e ordenação via query params
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['nome', 'email'] # ?nome=Maria
    search_fields = ['nome', 'email'] # ?search=Maria
    ordering_fields = ['nome', 'data_cadastro'] # ?ordering=-data_cadastro
class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['cidade', 'estado']
    search_fields = ['rua', 'cidade', 'estado']
    ordering_fields = ['cidade', 'estado']
class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer   
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['nome']
    search_fields = ['nome']
    ordering_fields = ['nome']
  
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(disponivel=True)
    serializer_class = ItemSerializer   
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['nome', 'preco']
    search_fields = ['nome', 'descricao']
    ordering_fields = ['nome', 'preco']
class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer   
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['tipo']
    search_fields = ['tipo']
    ordering_fields = ['tipo']
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer   
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'data']
    search_fields = ['status']
    ordering_fields = ['data', 'valor_total']
class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer   
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['pedido_id', 'item_id']
    search_fields = ['pedido_id__cliente_id__nome', 'item_id__nome']
    ordering_fields = ['pedido_id', 'item_id']

@api_view(['POST'])
@permission_classes([AllowAny]) # registro é público
def signup(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        usuario = serializer.save() # chama o create() do serializer
        token = Token.objects.create(user=usuario)
        return Response({'token': token.key, 'usuario': serializer.data},
    status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny]) # login é público
def login(request):
    usuario = get_object_or_404(Usuario, username=request.data.get('username'))
    if not usuario.check_password(request.data.get('password')):
        return Response({'detail': 'Credenciais inválidas.'},
    status=status.HTTP_400_BAD_REQUEST)
    token, _ = Token.objects.get_or_create(user=usuario)
    return Response({'token': token.key,
    'usuario': UsuarioSerializer(usuario).data})
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated]) # exige token válido
def perfil(request):
    return Response({
        'username': request.user.username,
        'tipo': request.user.tipo,
        'mensagem': f'Olá, {request.user.username}! Você é {request.user.get_tipo_display()}.'
    })