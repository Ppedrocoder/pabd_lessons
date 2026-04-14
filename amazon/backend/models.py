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
