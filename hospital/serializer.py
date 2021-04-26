from rest_framework import serializers
from hospital.models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nome','telefone', 'cpf', 'foto', 'email']