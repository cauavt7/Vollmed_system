from django.db import models
from django.utils import timezone

class Medico(models.Model):
    nome = models.CharField( max_length=50)
    sobrenome =models.CharField(max_length=40)
    email = models.EmailField()
    Criacao_data = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length=15)
    crm = models.CharField(max_length=6)
    especialidade = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    mensagem = models.TextField(blank=True)


    def __str__(self):
        return F' {self.nome} {self.Sobrenome}'


class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=40)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    especialidade = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return F' {self.nome} {self.Sobrenome}'
    

class Consulta(models.Model):
    Paciente_id =models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico_id =models.ForeignKey(Medico, on_delete=models.CASCADE)

    Horario = models.DateTimeField
    observacao =models.TextField(blank=True) 

    status = models.CharField(
        default='A',
        max_length=1,
        choices=(
                ('A','Agendada'),
                ('X','Cancelada'),
                ('C','Confirmada'),
                ('R','Realizada'),

        )
    ) 

    def __str__(self):
        return f'Consulta {self.get_status_display()} — {self.paciente_id}' 


    

