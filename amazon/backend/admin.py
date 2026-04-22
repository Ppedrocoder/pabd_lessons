from django.contrib import admin
from .models import Cliente, Endereco, FormaPagamento, Item, ItemPedido, Pedido, Vendedor
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_cadastro')
    search_fields = ('nome', 'email')
    ordering = ('nome',)
@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cliente_id', 'rua', 'cidade', 'estado', 'cep')
    search_fields = ('rua', 'cidade', 'estado')
    ordering = ('cidade',)
@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf_cnpj', 'telefone', 'avaliacao', 'ativo', 'data_cadastro')
    search_fields = ('nome', 'email', 'cpf_cnpj')
    ordering = ('nome', 'data_cadastro')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'categoria', 'disponivel', 'criado_em', 'atualizado_em')
    search_fields = ('nome',)
    ordering = ('nome',)
@admin.register(FormaPagamento)
class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
    search_fields = ('tipo',)
    ordering = ('tipo',)
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente_id', 'endereco_id', 'forma_pagamento_id', 'data', 'valor_total', 'status')
    search_fields = ('status',)
    ordering = ('data',)
@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido_id', 'item_id', 'quantidade')
    search_fields = ('pedido_id__cliente_id__nome', 'item_id__nome')
    ordering = ('pedido_id',)
