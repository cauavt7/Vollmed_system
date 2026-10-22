from django.db import models
from django.utils import timezone

class Medico(models.Model):
    nome = models.CharField( max_length=50)
    Sobrenome =models.CharField(max_length=40)
    email = models.EmailField()
    Criacao_data = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length=15)
    crm = models.CharField(max_length=6)
    especialidade = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    mensagem = models.TextField(blank=True)


    def __str__(self):
        return F' {self.nome} {self.Sobrenome}'
