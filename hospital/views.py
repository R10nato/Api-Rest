from rest_framework import viewsets
from hospital.models import Paciente
from hospital.serializer import PacienteSerializer


class PacientesViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


