from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import  Cliente, Endereco, FormaPagamento, Item, ItemPedido, Pedido, Vendedor
from .serializers import  ClienteSerializer, EnderecoSerializer, FormaPagamentoSerializer, ItemPedidoSerializer, ItemSerializer, PedidoSerializer, VendedorSerializer

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