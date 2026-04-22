from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True) # UNIQUE no banco
    telefone = models.CharField(max_length=20, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True) # Preenchido automaticamente
    class Meta:
      db_table = 'clientes' # Nome explícito da tabela no banco
      ordering = ['nome'] # Ordenação padrão nas consultas

    def __str__(self):
      # Retorna a representação legível do objeto
      return f'{self.nome} <{self.email}>'

class Endereco(models.Model):
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    rua = models.CharField(max_length=200, null=False)
    cidade = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=50, null=False)
    cep = models.CharField(max_length=20, null=False)
    class Meta:
      db_table = 'enderecos' # Nome explícito da tabela no banco
      ordering = ['estado'] # Ordenação padrão nas consultas

    def __str__(self):
      # Retorna a representação legível do objeto
      return f'{self.rua}, {self.cidade} - {self.estado}, CEP: {self.cep}'
class Vendedor(models.Model):
    nome = models.CharField(max_length=100, null=False)
    endereco_id = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=False)
    telefone = models.CharField(max_length=20, blank=True)
    class Meta:
      db_table = 'vendedores' # Nome explícito da tabela no banco
      ordering = ['nome'] # Ordenação padrão nas consultas

    def __str__(self):
      # Retorna a representação legível do objeto
      return f'{self.nome} <{self.email}>'

class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False)
    class Meta:
      db_table = 'categorias' # Nome explícito da tabela no banco
      ordering = ['nome'] # Ordenação padrão nas consultas

    def __str__(self):
      # Retorna a representação legível do objeto
      return f'{self.nome}'

class Item(models.Model):
    vendedor_id = models.ForeignKey(Vendedor, on_delete=models.CASCADE, null=False)
    nome = models.CharField(max_length=100, null=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    descricao = models.TextField(blank=True)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    qtd_estoque = models.IntegerField(default=0)
    class Meta:
      db_table = 'itens' # Nome explícito da tabela no banco
      ordering = ['nome'] # Ordenação padrão nas consultas

    def __str__(self):
      # Retorna a representação legível do objeto
      return f'{self.nome} <{self.preco}> - {self.categoria_id.nome} - Vendedor: {self.vendedor_id.nome} - Estoque: {self.qtd_estoque} unidades'
class FormaPagamento(models.Model):
    tipo = models.CharField(max_length=50, null=False)
    class Meta:
      db_table = 'formas_pagamento' # Nome explícito da tabela no banco
      ordering = ['tipo'] # Ordenação padrão nas consultas

    def __str__(self):
      # Retorna a representação legível do objeto
      return f'{self.tipo}'


class Pedido(models.Model):
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    endereco_id = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=False)
    forma_pagamento_id  = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE, null=False)
    data = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.CharField(max_length=20, default="Pendente")
    class Meta:
      db_table = 'pedidos' # Nome explícito da tabela no banco
      ordering = ['data'] # Ordenação padrão nas consultas

    def __str__(self):
      # Retorna a representação legível do objeto
      return f'Pedido {self.id} - Cliente: {self.cliente_id.nome} - Valor: {self.valor_total} - Status: {self.status} - Data: {self.data.strftime("%Y-%m-%d %H:%M:%S")} - Forma de Pagamento: {self.forma_pagamento_id.tipo} - Entrega: {self.endereco_id.rua}, {self.endereco_id.cidade} - {self.endereco_id.estado}'
    

class ItemPedido(models.Model):
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=False) 
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, null=False)
    quantidade = models.IntegerField(null=False)
    class Meta:
      db_table = 'itens_pedido' # Nome explícito da tabela no banco
      ordering = ['pedido_id'] # Ordenação padrão nas consultas

    def __str__(self):
      # Retorna a representação legível do objeto
      return f'Item do Pedido {self.pedido_id.id} - Item: {self.item_id.nome} - Quantidade: {self.quantidade}'


