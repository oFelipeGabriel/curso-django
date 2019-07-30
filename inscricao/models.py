from django.db import models

# Create your models here.
class Participante(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=150)