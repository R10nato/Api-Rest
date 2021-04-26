from django.contrib import admin
from hospital.models import Paciente

class Pacientes(admin.ModelAdmin):
        list_display = ('id', 'nome','telefone', 'cpf', 'foto', 'email')
        list_display_links = ('id', 'nome')
        search_fields = ('nome',)


admin.site.register(Paciente, Pacientes)