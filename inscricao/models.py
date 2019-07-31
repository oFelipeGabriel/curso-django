from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.timezone import now


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


class Curso(models.Model):
    nome = models.CharField(max_length=150)
    professor = models.CharField(max_length=150)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    
    def __str__(self):
        return self.nome


class Matricula(models.Model):
    data = models.DateField(default=now)
    aluno = models.ForeignKey(Participante, on_delete=models.SET_NULL,null=True)
    curso = models.ForeignKey(Curso, on_delete=False)

    def __str__(self):
        return self.aluno.nome+' / '+self.curso.nome