from django.contrib import admin
from Sistema import models




@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'ativo')

@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'ativo')

@admin.register(models.Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'ativo')
    
    