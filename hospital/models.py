from django.db import models

# Create your models here.
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)
    foto = models.ImageField(upload_to='API-REST/hospital/templates/fotos', null=True, blank=True)
    email = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome