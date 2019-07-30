from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Participante(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                            on_delete=models.CASCADE, 
                            null=True, 
                            blank=True)

    def __str__(self):
        return self.nome