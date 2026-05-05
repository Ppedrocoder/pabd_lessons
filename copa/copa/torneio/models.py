from django.db import models

# Create your models here.

class Grupo(models.Model):
    nome = models.CharField(max_length=1)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'Grupo {self.nome}'

class Tecnico(models.Model):
    nome = models.CharField(max_length=150)
    nacionalidade = models.CharField(max_length=100)
    data_nascimento = models.DateField()
class Selecao(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3, unique=True)
    confederacao = models.CharField(max_length=50)
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT, related_name='selecoes')
    tecnico = models.OneToOneField(Tecnico, on_delete=models.SET_NULL, null=True, blank=True, related_name='selecao')
    escudo_url = models.URLField(blank=True, null=True)
class Jogador(models.Model):
    nome = models.CharField(max_length=150)
    nome_guerra = models.CharField(max_length=50)
    selecao = models.ForeignKey(Selecao, on_delete=models.PROTECT, related_name='jogadores')
    posicao = models.CharField(max_length=50, choices='Goleiro, Zagueiro, Lateral, Volante, Meia, Atacante'.split(', '))
    numero_camisa = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    suspenso = models.BooleanField(default=False)

class Jogo(models.Model):
    pass
class EventoJogo(models.Model):
    pass