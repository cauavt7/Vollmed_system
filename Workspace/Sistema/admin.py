from django.contrib import admin
from Sistema import models




@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','sobrenome', 'email','Criacao_data', 'telefone','crm', 'especialidade', 'ativo','mensagem')

@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','sobrenome', 'email', 'telefone','cpf', 'ativo')

@admin.register(models.Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('Paciente_id', 'medico_id', 'Horario', 'observacao', 'status')
    
    