from django.shortcuts import render
from rest_framework import viewsets
from hospital.serializer import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


