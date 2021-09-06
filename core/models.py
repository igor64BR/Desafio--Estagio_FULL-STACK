from django.contrib.auth.models import User
from django.db import models
from django.forms import DateInput
from organizadores.models import Organizadore


# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=100)
    organizadores = models.ManyToManyField(Organizadore)
    # organizadores = models.ForeignKey(User, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
