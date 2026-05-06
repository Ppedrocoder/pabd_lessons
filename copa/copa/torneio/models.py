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
    CONFEDERACOES = {
        'CONMEBOL': 'CONMEBOL',
        'UEFA': 'UEFA',
        'CAF': 'CAF',
        'AFC': 'AFC',
        'CONCACAF': 'CONCACAF',
        'OFC': 'OFC'
    }
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3, unique=True)
    confederacao = models.CharField(max_length=50, choices=CONFEDERACOES.items())
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
    selecao_mandante = models.ForeignKey(Selecao, on_delete=models.PROTECT, related_name='jogos_mandante')
    selecao_visitante = models.ForeignKey(Selecao, on_delete=models.PROTECT, related_name='jogos_visitante')
    fase = models.CharField(max_length=50, choices='Grupos, 32 Avos de Final, Oitavas de Final, Quartas de Final, Semifinal, Final'.split(', '))
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT, null=True, blank=True)
    data_hora = models.DateTimeField()
    estadio = models.CharField(max_length=150, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    gols_mandante = models.PositiveIntegerField(default=0)
    gols_visitante = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices='Agendado, Em Andamento, Encerrado, Cancelado'.split(', '), default='Agendado')
class EventoJogo(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name='eventos')
    jogador = models.ForeignKey(Jogador, on_delete=models.PROTECT, related_name='eventos')
    tipo = models.CharField(max_length=50, choices='Gol, Cartão Amarelo, Cartão Vermelho, Gol Contra'.split(', '))
    minuto = models.PositiveIntegerField()
    acrescimo = models.BooleanField(default=False)